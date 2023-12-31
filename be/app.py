import os
import re
from flask import Flask, request, render_template, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# The host name where MySQL is located
HOSTNAME = "8.134.18.116"
# The port number MySQL listens to, default is 3306
PORT = 3306
# Username to connect to MYSOL
USERNAME = "Class"
# Password to connect to MYSQL
PASSWORD = "ClassAdmin"
# Database name created on MySQL
DATABASE = "class"

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

db = SQLAlchemy(app)



# User table
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    useremail = db.Column(db.String(100), nullable=False)
   # User type (teacher/student)
    type = db.Column(db.String(100), nullable=False)


# Course table
class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Course name
    course_name = db.Column(db.String(100), nullable=False)
    # Course teacher
    course_teacher = db.Column(db.String(100), nullable=False)


# Course Homework table
class CourseHomework(db.Model):
    __tablename__ = "course_homework"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Course name
    course_name = db.Column(db.String(100), nullable=False)
    # Course homework
    course_homework = db.Column(db.String(100), nullable=False)


# Homework table
class Homework(db.Model):
    __tablename__ = "homework"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Homework content, in file format
    homework_content = db.Column(db.String(100), nullable=False)
    # Homework name
    homework_name = db.Column(db.String(100), nullable=False)
    # Course homework
    homework_course = db.Column(db.String(100), nullable=False)
    # Homework submission time
    homework_time = db.Column(db.String(100), nullable=False)
    # Homework score
    homework_score = db.Column(db.String(100), nullable=False)
    #user who submitted the homework
    homework_user = db.Column(db.String(100), nullable=False)

# Student course selection table
class CourseMsg(db.Model):
    __tablename__ = "course_msg"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Student name
    student_name = db.Column(db.String(100), nullable=False)
    # Course name
    course_name = db.Column(db.String(100), nullable=False)


# Create all tables
with app.app_context():
    db.create_all()


# I. User operations
# Add (Register)
@app.route('/user/register', methods=['POST'])
def register():
    try:
        # Get JSON data from POST request
        request_data = request.get_json()

        # Extract user information from JSON data
        username = request_data.get('username')
        password = request_data.get('password')
        useremail = request_data.get('useremail')
        user_type = request_data.get('type')

        ## Extract user information from JSON data
        sql = text("select * from user where username = :username")
        result = db.session.execute(sql, {"username": username})
        usr_exist = result.fetchone()

        if usr_exist is not None:
            response_data = {
                "code": 200,
                "message": "Username already exists",
                "data": {}  #  Return the ID of the new user
            }
            return jsonify(response_data)

        # Create new user
        user = User(username=username, password=password, useremail=useremail, type=user_type)

        # Add new user to the database
        db.session.add(user)
        db.session.commit()

        # Return a successful JSON response
        response_data = {
            "code": 200,
            "message": "User created successfully",
            "data": {"user_id": user.id, "username": user.username, "type": user.type}  # 返回新用户的ID
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # If an error occurs, return an error JSON response
        response_data = {
            "code": 500,
            "message": "Internal server error",
            "data": {}
        }
        return jsonify(response_data), 500


@app.route('/user/login', methods=['POST'])
def login():
    try:
        # Get JSON data from POST request
        request_data = request.get_json()

        # Extract user information from JSON data
        username = request_data.get('username')
        password = request_data.get('password')
        usertype = request_data.get('usertype')
        # Check if username and password are correct
        sql = text("select * from user where username = :username and password = :password and type = :usertype")
        result = db.session.execute(sql, {"username": username, "password": password, "usertype": usertype})
        usr_exist = result.fetchone()

        # If the account and password are correct
        if usr_exist is not None:
            # Retrieve all courses
            response_data = {
                "code": 200,
                "message": "Login successful",
                "data": {"username": username, "type": usertype}   # Return the new user's ID
            }
            return jsonify(response_data)
        else:
            response_data = {
                "code": 500,
                "message": "Login failed, incorrect account or password",
                "data": {}
            }
            return jsonify(response_data), 500

    except Exception as e:
        print(e)
        # If an error occurs, return an error JSON response
        response_data = {
            "code": 500,
            "message": "Internal server error",
            "data": {}
        }
        return jsonify(response_data), 500


# Create course homework
@app.route('/user/create_course_homework', methods=['POST'])
def create_course_homework():
    try:
        # Get JSON data from POST request
        request_data = request.get_json()

        # Extract course information from JSON data
        course_name = request_data.get('course_name')
        course_homework = request_data.get('course_homework')

        # Check if the course exists
        sql = text("select * from course where course_name = :course_name")
        result = db.session.execute(sql, {"course_name": course_name})
        course = result.fetchone()
        # If the course does not exist
        if course is None:
            response_data = {
                "code": 500,
                "message": "Creation failed, the course does not exist",
                "data": {}
            }
            return jsonify(response_data), 500
        # Check if the course homework already exists
        sql = text("select * from course_homework where course_homework = :course_homework")
        result = db.session.execute(sql, {"course_homework": course_homework})
        course_homeworks = result.fetchone()
        # If the course homework already exists
        if course_homeworks is not None:
            response_data = {
                "code": 500,
                "message": "Creation failed, the course homework already exists",
                "data": {}
            }
            return jsonify(response_data), 500

        # Create new course homework
        course_homework = CourseHomework(course_name=course_name, course_homework=course_homework)
        # Add new course homework to the database
        db.session.add(course_homework)
        db.session.commit()

        # Return a successful JSON response
        response_data = {
            "code": 200,
            "message": "Course homework created successfully",
            "data": {"course_homework_id": course_homework.id}  # Return the ID of the new course homework
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # If an error occurs, return an error JSON response
        response_data = {
            "code": 500,
            "message": "Internal server error",
            "data": {}
        }
        return jsonify(response_data), 500


# Submit homework
@app.route('/user/submit_homework', methods=['POST'])
def submit_homework():
    try:
        # Get JSON data from POST request
        file = request.files['file']
        # Homework name
        homework_name = request.form['homework_name']
        # Course homework
        homework_course = request.form['homework_course']
        homework_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        homework_user = request.form['homework_user']

        # Check if the course homework exists
        sql = text("select * from course_homework where course_homework = :course_homework")
        result = db.session.execute(sql, {"course_homework": homework_name})
        course_homeworks = result.fetchone()
        # If the course homework does not exist
        if course_homeworks is None:
            response_data = {
                "code": 500,
                "message": "Submission failed, the course homework does not exist",
                "data": {}
            }
            return jsonify(response_data), 500

        # Check if the student is registered for the course
        sql = text("select * from course_msg where student_name = :student_name and course_name = :course_name")

        result = db.session.execute(sql, {"student_name": homework_user, "course_name": homework_course})

        course_msg = result.fetchone()
        # If the course is not registered
        if course_msg is None:
            response_data = {
                "code": 500,
                "message": "Submission failed, the course is not registered",
                "data": {}
            }
            return jsonify(response_data), 500

        # Save the file
        path = r'E:\homework-fe\be'
        file.save(os.path.join(path, file.filename))

        outfile = getgrade(os.path.join(path, file.filename))

        # Create new homework
        homework = Homework(homework_content=r'E:\homework-fe\be' + file.filename, homework_name=homework_name,
                            homework_course=homework_course, homework_time=homework_time,
                            homework_user=homework_user, homework_score=outfile)


        # Add new homework to the database    
        db.session.add(homework)
        db.session.commit()

        # Return a successful JSON response
        response_data = {
            "code": 200,
            "message": "Homework submitted successfully",
            "data": {"homework_id": homework.id}  # Return the ID of the new homework
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # If an error occurs, return an error JSON response
        response_data = {
            "code": 500,
            "message": "Internal server error",
            "data": {}
        }
        return jsonify(response_data), 500

# Query all courses by teacher name
@app.route('/user/query_course_by_teacher', methods=['POST'])
def query_course_by_teacher():
    try:
        # Get JSON data from POST request
        request_data = request.get_json()

        # Extract course information from JSON data
        course_teacher = request_data.get('course_teacher')

        # Check if the student course exists
        sql = text("select * from course where course_teacher = :course_teacher")
        result = db.session.execute(sql, {"course_teacher": course_teacher})
        courses = result.fetchall()
        # If the student course does not exist
        if courses is None:
            response_data = {
                "code": 500,
                "message": "Query failed, the teacher's courses do not exist",
                "data": {}
            }
            return jsonify(response_data), 500
        else:
            # Convert the result into a serializable data type
            courses_list = []

            for row in courses:
                course_dict = {
                    "id": row[0],
                    "course_name": row[1],
                    "course_teacher": row[2]
                }
                courses_list.append(course_dict)

        # Return a successful JSON response
        response_data = {
            "code": 200,
            "message": "Teacher course query successful",
            "data": {"courses": courses_list}  # Return the ID of the new homework
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # If an error occurs, return an error JSON response
        response_data = {
            "code": 500,
            "message": "Internal server error",
            "data": {}
        }
        return jsonify(response_data), 500


# Query all homework by course name, from the course_homework table
@app.route('/user/query_homework_by_course', methods=['POST'])
def query_homework_by_course():
    host_with_port = request.host
    try:
        # Get JSON data from POST request
        request_data = request.get_json()

        # Extract course information from JSON data
        course_name = request_data.get('course_name')
        username = request_data.get('username')

        # Check if the student course exists
        sql = text("select * from course_homework where course_name = :course_name")
        result = db.session.execute(sql, {"course_name": course_name})
        courses = result.fetchall()
        # If the student course does not exist
        if courses is None:
            response_data = {
                "code": 500,
                "message": "Query failed, the course homework does not exist",
                "data": {}
            }
            return jsonify(response_data), 500
        else:
            # Convert the result into a serializable data type
            courses_list = []

            for row in courses:
                course_dict = {
                    "id": row[0],
                    "course_name": row[1],
                    "course_homework": row[2],
                }
                # Check if the student has already submitted the homework
                sql = text(
                    "select * from homework where homework_course = :homework_course and homework_user = :homework_user and homework_name = :homework_name")
                result = db.session.execute(sql, {"homework_course": course_name, "homework_user": username,
                                                  "homework_name": row[2]})
                homeworks = result.fetchone()
                if homeworks is None:
                    course_dict["submit"] = False
                else:
                    course_dict["submit"] = True
                    # If the student has submitted, then return the homework score
                    course_dict["homework_score"] =f'http://{host_with_port}/{homeworks[5]}'
                courses_list.append(course_dict)

        # Return a successful JSON response
        response_data = {
            "code": 200,
            "message": "Course homework query successful",
            "data": {"courses": courses_list}  # Return the ID of the new homework
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # If an error occurs, return an error JSON response
        response_data = {
            "code": 200,
            "message": "Internal server error",
            "data": {}
        }
        return jsonify(response_data), 200




def getgrade(upfile):
    # is the diagram for programming or database courses?
    umlChoice = 1

    # file must first be converted to a text file.
    file = upfile

    # read the file
    fileOpen = open(file, "r")

    # list of file lines for reading attributes and methods
    file_list = []

    # the string which represents the types of relationships
    relationshipArrow = "lt"

    # the string which represents relationships
    relationship = "<id>Relation</id>"
    relationCount = -1
    relationLevel = []

    # arrows for relationship labels
    labelArrow1 = "&lt; "
    labelArrow2 = " &gt"

    # a list for counting how many times the relationshipArrow string is seen
    arrowCount = []

    # the string which represents the class names in the file
    className = "    <panel_attributes>"
    # a list for all the class names
    classes = []

    # the strings representing where the coordinates of classes and arrows are in the file
    xCoordinateStart = "<x>"
    yCoordinateStart = "<y>"
    wCoordinateStart = "<w>"
    hCoordinateStart = "<h>"
    xCoordinateEnd = "</x>"
    yCoordinateEnd = "</y>"
    wCoordinateEnd = "</w>"
    hCoordinateEnd = "</h>"

    # listing the coordinates
    xCoordinate = []
    yCoordinate = []
    wCoordinate = []
    hCoordinate = []

    # attribute and method count lists.
    attributeCountList = []
    methodCountList = []

    # *..* 1..* etc
    m1_numbers = "m1"
    m2_numbers = "m2"

    # list for m1_numbers and m2_numbers
    m1 = []
    m2 = []

    # attributes
    attributes = "--"
    attributesList = []
    newAttributesList = []
    attributeType = []

    # methods
    methods = "("
    methodsList = []
    newMethodsList = []

    labels = []

    # additional attribuutes
    relationshipLocation = "<additional_attributes>"
    directionList = []

    for line in fileOpen:

        file_list.append(line)

        # counting the number of times the reationshipArrow string is seen per line in the file
        count = 0

        if relationshipArrow in line:
            for letter in line:
                # '&' represents the arrows
                if letter == "&":
                    count = count + 1
                # '.' represents a dotted line
                if letter == ".":
                    count = count + 0.1
            arrowCount.append(count)

        # counting the number of relationships
        if relationship in line:
            relationCount += 1

        # appending the labels to a list
        if labelArrow1 in line or labelArrow2 in line:
            labels.append(line)
            print(relationCount)
            relationLevel.append(relationCount)

        # appending the coordinates if they are found in the line of the file.
        elif xCoordinateStart in line:
            xCoordinate.append(line)
        elif yCoordinateStart in line:
            yCoordinate.append(line)
        elif wCoordinateStart in line:
            wCoordinate.append(line)
        elif hCoordinateStart in line:
            hCoordinate.append(line)

        # appending the class name it is found in the line of the file
        elif className in line and relationshipArrow not in line:
            classes.append(line)

        # appending the lines that m1 and m2 are in to the lists.
        elif m1_numbers in line:
            m1.append(line)
        elif m2_numbers in line:
            m2.append(line)

        # appending the start and finish locations of relationships to list
        elif relationshipLocation in line:
            directionList.append(line)

        # appending attributes and methods to lists
    indexCount = 0
    while indexCount < len(file_list):
        if attributes in file_list[indexCount] and methods not in file_list[indexCount + 1]:
            attributesIndex = 1
            attributeCount = 0
            while attributes not in file_list[(indexCount + attributesIndex)] and "</panel_attributes>" not in \
                    file_list[(indexCount + attributesIndex)]:
                attributesList.append(file_list[(indexCount + attributesIndex)])
                newAttributesList.append(file_list[(indexCount + attributesIndex)])
                attributeType.append(file_list[(indexCount + attributesIndex)])
                attributesIndex += 1
                attributeCount += 1
            attributeCountList.append(attributeCount)
        elif attributes in file_list[indexCount] and methods in file_list[indexCount + 1]:
            methodsIndex = 1
            methodCount = 0
            while methods in file_list[indexCount + methodsIndex]:
                methodsList.append(file_list[(indexCount + methodsIndex)])
                newMethodsList.append(file_list[(indexCount + methodsIndex)])
                methodsIndex += 1
                methodCount += 1
            methodCountList.append(methodCount)
        indexCount += 1

    newClasses = [name.replace("<panel_attributes>", "") for name in classes]

    print(arrowCount)

    # listing the names of the relationships
    relationships = []

    # The different numbers represent what type of relationship
    for ind in arrowCount:
        if ind == 2:
            relationships.append("Inheritance")
        elif ind == 0:
            relationships.append("Association")
        elif ind == 2.1:
            relationships.append("Realisation")
        elif ind == 1.1:
            relationships.append("Dependency")
        elif ind == 3:
            relationships.append("Directed Association")
        elif ind == 4:
            relationships.append("Aggregation")
        elif ind == 5:
            relationships.append("Composition")

    # characters to be removed from the lists.
    spaces = " "
    letter1 = "x"
    letter2 = "\n"
    letter3 = "y"
    letter4 = "w"
    letter5 = "h"
    arrow1 = "<"
    arrow2 = ">"
    slash1 = "/"
    underscore = "_"
    star = "*"
    m1Code = "m1="
    m2Code = "m2="
    panelAttributes = "</panel_attributes>"
    additionalAttributes1 = "    <additional_attributes>"
    additionalAttributes2 = "</additional_attributes>"
    minus = "-"
    plus = "+"
    hashtag = "#"
    date = "date"
    dateTime = "DateTime"
    string = "str"
    bool = "bool"
    twoDots = ":"
    leftArrow = "&lt;"
    rightArrow = "&gt;"
    bracket1 = "("
    bracket2 = ")"

    # for loops using replace statements to remove the
    # previously stated characters.
    for idx, ele in enumerate(xCoordinate):
        xCoordinate[idx] = ele.replace(letter1, '')
    for idx, ele in enumerate(xCoordinate):
        xCoordinate[idx] = ele.replace(spaces, '')
    for idx, ele in enumerate(xCoordinate):
        xCoordinate[idx] = ele.replace(letter2, '')
    for idx, ele in enumerate(xCoordinate):
        xCoordinate[idx] = ele.replace(arrow1, '')
    for idx, ele in enumerate(xCoordinate):
        xCoordinate[idx] = ele.replace(arrow2, '')
    for idx, ele in enumerate(xCoordinate):
        xCoordinate[idx] = ele.replace(slash1, '')

    for idx, ele in enumerate(yCoordinate):
        yCoordinate[idx] = ele.replace(letter3, '')
    for idx, ele in enumerate(yCoordinate):
        yCoordinate[idx] = ele.replace(spaces, '')
    for idx, ele in enumerate(yCoordinate):
        yCoordinate[idx] = ele.replace(letter2, '')
    for idx, ele in enumerate(yCoordinate):
        yCoordinate[idx] = ele.replace(arrow1, '')
    for idx, ele in enumerate(yCoordinate):
        yCoordinate[idx] = ele.replace(arrow2, '')
    for idx, ele in enumerate(yCoordinate):
        yCoordinate[idx] = ele.replace(slash1, '')

    for idx, ele in enumerate(wCoordinate):
        wCoordinate[idx] = ele.replace(letter4, '')
    for idx, ele in enumerate(wCoordinate):
        wCoordinate[idx] = ele.replace(spaces, '')
    for idx, ele in enumerate(wCoordinate):
        wCoordinate[idx] = ele.replace(letter2, '')
    for idx, ele in enumerate(wCoordinate):
        wCoordinate[idx] = ele.replace(arrow1, '')
    for idx, ele in enumerate(wCoordinate):
        wCoordinate[idx] = ele.replace(arrow2, '')
    for idx, ele in enumerate(wCoordinate):
        wCoordinate[idx] = ele.replace(slash1, '')

    for idx, ele in enumerate(hCoordinate):
        hCoordinate[idx] = ele.replace(letter5, '')
    for idx, ele in enumerate(hCoordinate):
        hCoordinate[idx] = ele.replace(spaces, '')
    for idx, ele in enumerate(hCoordinate):
        hCoordinate[idx] = ele.replace(letter2, '')
    for idx, ele in enumerate(hCoordinate):
        hCoordinate[idx] = ele.replace(arrow1, '')
    for idx, ele in enumerate(hCoordinate):
        hCoordinate[idx] = ele.replace(arrow2, '')
    for idx, ele in enumerate(hCoordinate):
        hCoordinate[idx] = ele.replace(slash1, '')

    for idx, ele in enumerate(newClasses):
        newClasses[idx] = ele.replace(letter2, '')
    for idx, ele in enumerate(newClasses):
        newClasses[idx] = ele.replace(spaces, '')
    for idx, ele in enumerate(newClasses):
        newClasses[idx] = ele.replace(underscore, '')
    for idx, ele in enumerate(newClasses):
        newClasses[idx] = ele.replace(star, '')
    for idx, ele in enumerate(newClasses):
        newClasses[idx] = ele.replace(slash1, '')

    for idx, ele in enumerate(m1):
        m1[idx] = ele.replace(letter2, '')
    for idx, ele in enumerate(m1):
        m1[idx] = ele.replace(m1Code, '')

    for idx, ele in enumerate(m2):
        m2[idx] = ele.replace(letter2, '')
    for idx, ele in enumerate(m2):
        m2[idx] = ele.replace(m2Code, '')
    for idx, ele in enumerate(m2):
        m2[idx] = ele.replace(panelAttributes, '')

    for idx, ele in enumerate(attributesList):
        attributesList[idx] = ele.replace(letter2, '')

    for idx, ele in enumerate(methodsList):
        methodsList[idx] = ele.replace(panelAttributes, '')
    for idx, ele in enumerate(methodsList):
        methodsList[idx] = ele.replace(letter2, '')

    for idx, ele in enumerate(newMethodsList):
        newMethodsList[idx] = ele.split(bracket1, 1)[0]
        print(idx)
    for idx, ele in enumerate(newMethodsList):
        newMethodsList[idx] = ele.replace(panelAttributes, '')
    for idx, ele in enumerate(newMethodsList):
        newMethodsList[idx] = ele.replace(letter2, '')
    for idx, ele in enumerate(newMethodsList):
        newMethodsList[idx] = ele.replace(twoDots, '')
    for idx, ele in enumerate(newMethodsList):
        newMethodsList[idx] = ele.replace(bracket1, '')
    for idx, ele in enumerate(newMethodsList):
        newMethodsList[idx] = ele.replace(bracket2, '')
    for idx, ele in enumerate(newMethodsList):
        newMethodsList[idx] = ele.replace(plus, '')
    for idx, ele in enumerate(newMethodsList):
        newMethodsList[idx] = ele.replace(minus, '')
    for idx, ele in enumerate(newMethodsList):
        newMethodsList[idx] = ele.replace(hashtag, '')
    for idx, ele in enumerate(newMethodsList):
        newMethodsList[idx] = ele.replace(bool, '')
    for idx, ele in enumerate(newMethodsList):
        newMethodsList[idx] = ele.replace(string, '')

    for idx, ele in enumerate(directionList):
        directionList[idx] = ele.replace(additionalAttributes1, '')
    for idx, ele in enumerate(directionList):
        directionList[idx] = ele.replace(additionalAttributes2, '')
    for idx, ele in enumerate(directionList):
        directionList[idx] = ele.replace(letter2, '')

    for idx, ele in enumerate(newAttributesList):
        newAttributesList[idx] = ele.replace(minus, '')
    for idx, ele in enumerate(newAttributesList):
        newAttributesList[idx] = ele.replace(plus, '')
    for idx, ele in enumerate(newAttributesList):
        newAttributesList[idx] = ele.replace(date, '')
    for idx, ele in enumerate(newAttributesList):
        newAttributesList[idx] = ele.replace(dateTime, '')
    for idx, ele in enumerate(newAttributesList):
        newAttributesList[idx] = ele.replace(string, '')
    for idx, ele in enumerate(newAttributesList):
        newAttributesList[idx] = ele.replace(bool, '')
    for idx, ele in enumerate(newAttributesList):
        newAttributesList[idx] = ele.replace(twoDots, '')
    for idx, ele in enumerate(newAttributesList):
        newAttributesList[idx] = ele.replace(letter2, '')
    for idx, ele in enumerate(newAttributesList):
        newAttributesList[idx] = ele.replace(hashtag, '')

    attributeVis = []

    for t in attributesList:
        if "+" in t:
            attributeVis.append("+")
        elif "-" in t:
            attributeVis.append("-")
        elif "#" in t:
            attributeVis.append("#")

    attributeTypes = []

    for k in attributeType:
        ch = ":"
        if ch in k:
            listOfChars = k.split(ch, 1)
            if len(listOfChars) > 0:
                k = listOfChars[1]
                attributeTypes.append(k)

    for idx, ele in enumerate(attributeTypes):
        attributeTypes[idx] = ele.replace(letter2, '')

    for idx, ele in enumerate(labels):
        labels[idx] = ele.replace(letter2, '')
    for idx, ele in enumerate(labels):
        labels[idx] = ele.replace(panelAttributes, '')
    for idx, ele in enumerate(labels):
        labels[idx] = ele.replace(leftArrow, '<')
    for idx, ele in enumerate(labels):
        labels[idx] = ele.replace(rightArrow, '>')

    splitDirectionList = []
    for locate in directionList:
        splitDirection = locate.split(';')
        splitDirectionList.append(splitDirection)

    methodVis = []
    for method in methodsList:
        if "+" in method:
            methodVis.append("+")
        elif "-" in method:
            methodVis.append("-")
        elif "#" in method:
            methodVis.append("#")

    methodVoid1 = []
    methodVoid2 = []
    for method in methodsList:
        void1 = method.split('(')[1]
        void1 = void1.split(')')[0]
        methodVoid1.append(void1)
        void2 = method.split(')')[1]
        methodVoid2.append(void2)

    for idx, ele in enumerate(methodVoid2):
        methodVoid2[idx] = ele.replace(twoDots, '')

    # printing everything
    print("The relationships are", relationships)

    print("The x coordinates are:", xCoordinate)
    print("The y coordinates are:", yCoordinate)
    print("The w coordinates are:", wCoordinate)
    print("The h coordinates are:", hCoordinate)

    print(directionList)
    print(splitDirectionList)

    print("The classes are:", newClasses)

    print("The m1's are:", m1)
    print("The m2's are:", m2)

    print("The attributes are:", attributesList)
    print("The attributes are:", newAttributesList)
    print("The methods are:", methodsList)
    print("The methods are:", newMethodsList)

    print("attribute count list:", attributeCountList)
    print("method count list:", methodCountList)

    print("the attribute visibilities are:", attributeVis)
    print("the method visibilities are:", methodVis)
    print("the attribute types are:", attributeTypes)

    print("the labels are:", labels)
    print("relationship labels level:", relationLevel)

    print(methodVoid1)
    print(methodVoid2)

    f = open("classFormat.txt", "w")

    writeCount = 0
    c = 0
    classIndex = 0
    classCount = 0
    attributesTotal = 0
    for x in newClasses:
        classCount += 1
        classCountStr = str(classCount)
        f.write('class')
        f.write(classCountStr)
        f.write(' = ')
        f.write("ClassComponent(")
        f.write(x)
        f.write(",[")
        while newClasses.index(x) == classIndex:
            if classIndex == 0:
                while c < attributeCountList[writeCount]:
                    f.write(newAttributesList[c])
                    if c != (attributeCountList[writeCount] - 1):
                        f.write(", ")
                    c += 1
                classIndex += 1
            else:
                while c >= attributesTotal and c < (attributesTotal + attributeCountList[writeCount]):
                    f.write(newAttributesList[c])
                    if c != (attributesTotal + attributeCountList[writeCount] - 1):
                        f.write(", ")
                    c += 1
                classIndex += 1
            attributesTotal += attributeCountList[writeCount]
        f.write("])")
        f.write("\n")
        writeCount += 1

    f.write("\n")

    indCount = 0
    multiplicityCount = 0
    labelCount = 0
    relationshipNum = 0
    classNumber = 0
    for r in relationships:
        relationshipNum += 1
        rNumStr = str(relationshipNum)
        f.write('relationship')
        f.write(rNumStr)
        f.write(' = ')
        f.write("RelationshipComponent(")
        f.write(r)
        f.write(", ")
        f.write(newClasses[classNumber])
        f.write(", ")
        f.write(newClasses[(classNumber + 1)])
        f.write(", ")
        if relationships.index(r) in relationLevel:
            f.write(labels[labelCount])
            labelCount += 1
        else:
            f.write(" ")
        f.write(", [")
        f.write(m1[multiplicityCount])
        f.write(", ")
        f.write(m2[multiplicityCount])
        f.write("])")
        f.write("\n")
        multiplicityCount += 1
        indCount += 1
        classNumber += 1

    f.write("\n")

    if umlChoice == '1':
        c1 = 0
        c2 = 0
        mV = 0
        mLengthV = 0
        lengthValue = 0
        attributeNum = 0
        methodNum = 0
        for a in newAttributesList:
            attributeNum += 1
            aNumStr = str(attributeNum)
            f.write('attribute')
            f.write(aNumStr)
            f.write(' = ')
            f.write("AttributeComponent(")
            f.write(a)
            f.write(", ")
            if len(attributeTypes) > lengthValue:
                f.write(attributeTypes[c2])
            else:
                f.write(" ")
            f.write(", ")
            if len(attributeVis) > lengthValue:
                f.write(attributeVis[c1])
            else:
                f.write(" ")
            f.write(")")
            f.write("\n")
            c1 += 1
            c2 += 1
            lengthValue += 1

        f.write("\n")

        for m in newMethodsList:
            methodNum += 1
            mNumStr = str(methodNum)
            f.write("method")
            f.write(mNumStr)
            f.write(" = ")
            f.write("MethodComponent(")
            f.write(m)
            f.write("()")
            f.write(", ")
            if len(methodVoid1) > mLengthV and len(methodVoid1[mV]) > 0:
                f.write(methodVoid1[mV])
            else:
                f.write("void")
            f.write(", ")
            if len(methodVoid2) > mLengthV and len(methodVoid2[mV]) > 0:
                f.write(methodVoid2[mV])
            else:
                f.write("void")
            f.write(", ")
            if len(methodVis) > mLengthV:
                f.write(methodVis[mV])
            else:
                f.write(" ")
            f.write(")")
            f.write("\n")
            mV += 1
            mLengthV += 1
    
    print("_________________________________")
    class_example_file = r"E:\homework-fe\be\database.txt"

    attribute_array = []
    realtion_array = []
    good = []
    problem = []

    # Function to clean attribute names
    def clean_attribute(attribute):
        return attribute.strip("[]'()")

    def remove_all_brackets_and_quotes(attribute_array):
        """Removes all brackets and quotes from a text."""
        return re.sub('[\[\]\'()]','', attribute_array)

    def deletebreacket(Att_array):
        for item in Att_array:
            # Remove all parentheses from the item.
            item = item.replace("(", "").replace(")", "")

        # Return the updated array.
        return Att_array

    def remove_unwanted_chars(input_string):
        cleaned_string = input_string.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace('"',
                                                                                                                  '')
        return cleaned_string

    def check_relationship_format(realtion_name_array):

        valid_relationship_types = ["Association", "Inheritance", "Aggregation", "Composition"]
        problems = []

        for row in realtion_name_array:
            row = str(row)

            # Split the row on commas.
            split_row = row.split(",")

            # Strip any leading or trailing whitespace from each element of the split row.
            split_row = [element.strip() for element in split_row]

            # Return the split row.

            valid_relationship_types = ["Association", "Inheritance", "Aggregation", "Composition"]
            # Check if every index is not null, except when split_row[0] is inheritance, and split_row[3] and [4] must be null.
            if split_row[0] != "Inheritance" and any(element is None for element in split_row):
                problems.append(
                    "All fields must be not null, except split_row[3] and [4] when split_row[0] is Inheritance")
            elif split_row[0] == "Inheritance" and (split_row[3] is not None or split_row[4] is not None):
                problems.append("split_row[3] and [4] must be null when split_row[0] is Inheritance")

            # Check if the relationship type is valid.
            if split_row[0] not in valid_relationship_types:
                problems.append("Relationship error: " + split_row[0])

            # Check if the source and target classes exist in the attribute_name_array.
            if split_row[1] not in attribute_name_array or split_row[2] not in attribute_name_array:
                problems.append("Class name not in existing class names: ", split_row[1], split_row[2])
                # Check if the source and target classes exist in the attribute_name_array.
            if split_row[1] not in attribute_name_array or split_row[2] not in attribute_name_array:
                problem.append("Class name not in existing class names: ", split_row[1], split_row[2])

            else:
                good.append("good class name")

            # Check if the last letter of the label is one of "^v<>"
            valid_symbols = "^v<>"
            if split_row[3][-2] in valid_symbols:
                good.append("direction exist")
            else:
                problem.append("direction not exist")
            new_item4 = remove_unwanted_chars(split_row[4])
            new_item5 = remove_unwanted_chars(split_row[5])

            # print(new_item4,new_item5)

    def remove_symbols(attribute_array):
        """Removes all symbols except for commas and parentheses from a list of strings.

        Args:
            attribute_array: A list of strings.

        Returns:
            A list of strings with all symbols except for commas and parentheses removed.
        """

        # Create a regular expression to match all symbols except for commas and parentheses.
        regex = re.compile(r"[^\w\s,()]")
        result = []

        # Remove all spaces from the strings in the attribute array.
        for string in attribute_array:
            result.append(string.replace(" ", ""))

        # Substitute all matches with an empty string.
        return regex.sub("", result)

    def remove_symbols(realtion_array):

        # Create a regular expression to match all symbols except for commas and parentheses.
        regex = re.compile(r"[^\w\s,()]")
        result = []
        for string in realtion_array:
            result.append(string.replace(" ", ""))
        # Substitute all matches with an empty string.
        return regex.sub("", realtion_array)

    def checkdata(Att_array):
        cleaned_list = []
        for words in Att_array:
            cleaned_words = words.replace("(", "").replace(")", "")
            cleaned_list.append(cleaned_words)
        for item in cleaned_list:
            if not item[0].isupper() or not item[-1].islower():
                problem.append("check format " + item)
            else:
                good.append("good format " + item)

    with open(class_example_file, "r") as file:
        attribute_name_array = []
        realtion_name_array = []
        for line in file.readlines():
            # Check if the line contains an AttributeComponent
            if re.search(r"ClassComponet", line):
                divid = line.split('=')

                att_name = divid[0].strip()
                res = re.findall(r'\(.*?\)', line)

                # Add the attribute to the attribute array
                attribute_name_array.append('' + att_name + '')
                attribute_array.append(res)



            # Check if the line contains a RelationshipComponent
            elif re.search(r"RelationshipComponet", line):
                # Extract the relationship name, source attribute, and destination attribute from the line
                divid = line.split('=')
                res = re.findall(r'\(.*?\)', line)
                att_name = divid[0].strip()

                # Add the relationship to the attribute array
                realtion_array.append('[' + att_name + ']')
                realtion_name_array.append(res)
    for row in attribute_array:
        for i in range(len(row)):
            row[i] = remove_symbols(row[i])

    for row2 in realtion_name_array:
        for i in range(len(row2)):
            row2 = remove_symbols(row2[i])

    # check every thing in attribute array
    for x in attribute_array:
        Att_array = x[0].split(",")
        checkdata(Att_array)

    check_relationship_format(realtion_name_array)

    print('_________________________________')
    # Count the total number of problems and good things in the array
    count_problem = len(problem)
    count_good = len(good)
    total_count = count_problem + count_good

    # Calculate the percentage of problems and good things in the array
    percent_problem = count_problem / total_count * 100
    percent_good = count_good / total_count * 100

    # Print the total count and percentage of problems and good things in the array
    print("Total count of problems:", count_problem)
    print("Total count of good things:", count_good)
    print("Percentage of problems:", percent_problem)
    print("Percentage of good things:", percent_good)
   
    import time
    import datetime

    # Get the current time
    now_time = datetime.datetime.now()
    # Convert to a specified format:
    otherStyleTime = now_time.strftime("%Y-%m-%d%H%M%S")
    print(otherStyleTime)
    # Write these into a new txt file, named with the current timestamp
    # Get the path under the current directory to the 'static' folder
    path = os.getcwd() + '\\be\\static'
    print('1111111'+path + '\\' + otherStyleTime + ".txt")
    # The filename is the current time, the path is 'path'
    f = open(path + '\\' + otherStyleTime + ".txt", "w")
    f.write("Total count of problems:" + str(count_problem) + "\n")
    f.write("Total count of good things:" + str(count_good) + "\n")
    f.write("Percentage of problems:" + str(percent_problem) + "\n")
    f.write("Percentage of good things:" + str(percent_good) + "\n")

    print('------------------------------')
    f.write('------------------------------' + "\n")
    print('First time and second time feedback ')
    f.write('First time and second time feedback' + "\n")

    # Check each index of the problem array and print the appropriate message.
    if percent_good > percent_problem:
        print('You did good job,but there are something you can improve with')
        f.write('You did good job,but there are something you can improve with' + "\n")
    elif percent_good < percent_problem:
        print("Keep it up, don't give up")
        f.write("Keep it up, don't give up" + "\n")
    for index, problems in enumerate(problem):
        if index == 0:
            print("Please check Relationship ")
            f.write("Please check Relationship " + "\n")
        elif index == 1:
            print("Please check your attribute name.")
            f.write("Please check your attribute name." + "\n")
        elif index == 2:
            print("Please check your label.")
            f.write("Please check your label." + "\n")
        elif index == 3:
            print("Class name is not included in existing classes,please check")
            f.write("Class name is not included in existing classes,please check" + "\n")

    print('-----------------------------------')
    f.write('-----------------------------------' + "\n")
    print('Third Time feedback')
    f.write('Third Time feedback' + "\n")
    # If the percentage of good things is more than the percentage of problems, print a message encouraging the user to keep up the good work, but also print the problem array
    if percent_good > percent_problem:
        print("Good effort, keep it up, but there are some problems in this array:")
        f.write("Good effort, keep it up, but there are some problems in this array:" + "\n")
        print(problem)
        f.write(str(problem) + "\n")
    else:
        print("There are more problems than good things in this array:")
        f.write("There are more problems than good things in this array:" + "\n")
        print(problem)
        f.write(str(problem) + "\n")
    f.close()
    # Return the filename
    return '/static/' + otherStyleTime + ".txt"


if __name__ == '__main__':
    # Start Flask in debug mode
    app.run(debug=True)
