import os

from flask import Flask, request, render_template, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# MySQL所在的主机名
HOSTNAME = "8.134.18.116"
# MySQL监听的端口号，默认3306
PORT = 3306
# 连接MYSOL的用户名
USERNAME = "Class"
# 连接MYSQL的密码
PASSWORD = "ClassAdmin"
# MySQL上创建的数据库名称
DATABASE = "class"

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

db = SQLAlchemy(app)


# 用户表
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    useremail = db.Column(db.String(100), nullable=False)
    # 用户类型（老师/学生)
    type = db.Column(db.String(100), nullable=False)


# 课程表
class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 课程名称
    course_name = db.Column(db.String(100), nullable=False)
    # 课程教师
    course_teacher = db.Column(db.String(100), nullable=False)


# 课程作业表
class CourseHomework(db.Model):
    __tablename__ = "course_homework"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 课程名称
    course_name = db.Column(db.String(100), nullable=False)
    # 课程作业
    course_homework = db.Column(db.String(100), nullable=False)


# 作业表
class Homework(db.Model):
    __tablename__ = "homework"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 作业内容，file的格式
    homework_content = db.Column(db.String(100), nullable=False)
    # 课程名称
    homework_name = db.Column(db.String(100), nullable=False)
    # 课程作业
    homework_course = db.Column(db.String(100), nullable=False)
    # 作业提交时间
    homework_time = db.Column(db.String(100), nullable=False)
    # 作业分数
    homework_score = db.Column(db.String(100), nullable=False)
    # 作业提交人
    homework_user = db.Column(db.String(100), nullable=False)


# 学生选课表
class CourseMsg(db.Model):
    __tablename__ = "course_msg"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 学生姓名
    student_name = db.Column(db.String(100), nullable=False)
    # 课程名称
    course_name = db.Column(db.String(100), nullable=False)


# 创建所有表
with app.app_context():
    db.create_all()


# 一、用户操作
# 增（注册
@app.route('/user/register', methods=['POST'])
def register():
    try:
        # 从POST请求中获取JSON数据
        request_data = request.get_json()

        # 从JSON数据中提取用户信息
        username = request_data.get('username')
        password = request_data.get('password')
        useremail = request_data.get('useremail')
        user_type = request_data.get('type')

        # 查找是否有相同的用户名存在
        sql = text("select * from user where username = :username")
        result = db.session.execute(sql, {"username": username})
        usr_exist = result.fetchone()

        if usr_exist is not None:
            response_data = {
                "code": 200,
                "message": "用户名已经存在",
                "data": {}  # 返回新用户的ID
            }
            return jsonify(response_data)

        # 创建新用户
        user = User(username=username, password=password, useremail=useremail, type=user_type)

        # 将新用户添加到数据库中
        db.session.add(user)
        db.session.commit()

        # 返回成功的JSON响应
        response_data = {
            "code": 200,
            "message": "用户创建成功",
            "data": {"user_id": user.id,"username":user.username,"type":user.type}  # 返回新用户的ID
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 500,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 500


@app.route('/user/login', methods=['POST'])
def login():
    try:
        # 从POST请求中获取JSON数据
        request_data = request.get_json()

        # 从JSON数据中提取用户信息
        username = request_data.get('username')
        password = request_data.get('password')
        usertype = request_data.get('usertype')
        # 查询用户名密码是否正确
        sql = text("select * from user where username = :username and password = :password and type = :usertype")
        result = db.session.execute(sql, {"username": username, "password": password, "usertype": usertype})
        usr_exist = result.fetchone()

        # 如果账号密码正确
        if usr_exist is not None:
            # 查找所有课程
            response_data = {
                "code": 200,
                "message": "登录成功",
                "data": {"username": username,"type":usertype}  # 返回新用户的ID
            }
            return jsonify(response_data)
        else:
            response_data = {
                "code": 500,
                "message": "登录失败，账号或密码错误",
                "data": {}
            }
            return jsonify(response_data), 500

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 500,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 500


# 创建课程
@app.route('/user/create_course', methods=['POST'])
def create_course():
    try:
        # 从POST请求中获取JSON数据
        request_data = request.get_json()

        # 从JSON数据中提取课程信息
        course_name = request_data.get('course_name')
        course_teacher = request_data.get('course_teacher')

        # 查询course_teacher的角色
        sql = text("select type from user where username = :course_teacher")
        result = db.session.execute(sql, {"course_teacher": course_teacher})
        type = result.scalar()

        if type != "教师":
            response_data = {
                "code": 500,
                "message": "创建失败，该用户不是老师",
                "data": {}
            }
            return jsonify(response_data), 500
        else:
            # 创建新课程
            course = Course(course_name=course_name, course_teacher=course_teacher)
            # 将新课程添加到数据库中
            db.session.add(course)
            db.session.commit()

            # 返回成功的JSON响应
            response_data = {
                "code": 200,
                "message": "课程创建成功",
                "data": {"course_id": course.id}  # 返回新课程的ID
            }
            return jsonify(response_data)

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 500,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 500


# 创建课程作业
@app.route('/user/create_course_homework', methods=['POST'])
def create_course_homework():
    try:
        # 从POST请求中获取JSON数据
        request_data = request.get_json()

        # 从JSON数据中提取课程信息
        course_name = request_data.get('course_name')
        course_homework = request_data.get('course_homework')

        # 查询课程是否存在
        sql = text("select * from course where course_name = :course_name")
        result = db.session.execute(sql, {"course_name": course_name})
        course = result.fetchone()
        # 如果课程不存在
        if course is None:
            response_data = {
                "code": 500,
                "message": "创建失败，该课程不存在",
                "data": {}
            }
            return jsonify(response_data), 500
        # 查询课程作业是否存在
        sql = text("select * from course_homework where course_homework = :course_homework")
        result = db.session.execute(sql, {"course_homework": course_homework})
        course_homeworks = result.fetchone()
        # 如果课程作业已存在
        if course_homeworks is not None:
            response_data = {
                "code": 500,
                "message": "创建失败，该课程作业已存在",
                "data": {}
            }
            return jsonify(response_data), 500

        # 创建新课程作业
        course_homework = CourseHomework(course_name=course_name, course_homework=course_homework)
        # 将新课程作业添加到数据库中
        db.session.add(course_homework)
        db.session.commit()

        # 返回成功的JSON响应
        response_data = {
            "code": 200,
            "message": "课程作业创建成功",
            "data": {"course_homework_id": course_homework.id}  # 返回新课程作业的ID
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 500,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 500


# 提交作业
@app.route('/user/submit_homework', methods=['POST'])
def submit_homework():
    try:
        # 从POST请求中获取JSON数据
        file = request.files['file']
        # 课程名称
        homework_name = request.form['homework_name']
        # 课程作业
        homework_course = request.form['homework_course']
        homework_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        homework_user = request.form['homework_user']



        # 查询课程作业是否存在
        sql = text("select * from course_homework where course_homework = :course_homework")
        result = db.session.execute(sql, {"course_homework": homework_name})
        course_homeworks = result.fetchone()
        # 如果课程作业不存在
        if course_homeworks is None:
            response_data = {
                "code": 500,
                "message": "提交失败，该课程作业不存在",
                "data": {}
            }
            return jsonify(response_data), 500

        # 查询学生是否注册该课程
        sql = text("select * from course_msg where student_name = :student_name and course_name = :course_name")

        result = db.session.execute(sql, {"student_name": homework_user, "course_name": homework_course})

        course_msg = result.fetchone()
        # 如果课程已经注册
        if course_msg is None:
            response_data = {
                "code": 500,
                "message": "提交失败，该课程未注册",
                "data": {}
            }
            return jsonify(response_data), 500

        # 创建新作业
        homework = Homework(homework_content='/www/wwwroot/api/' + file.filename, homework_name=homework_name,
                            homework_course=homework_course, homework_time=homework_time,
                            homework_user=homework_user, homework_score="未批改")
        # 保存文件
        path = '/www/wwwroot/api/'
        file.save(os.path.join(path, file.filename))
        # 将新作业添加到数据库中
        db.session.add(homework)
        db.session.commit()

        # 返回成功的JSON响应
        response_data = {
            "code": 200,
            "message": "作业提交成功",
            "data": {"homework_id": homework.id}  # 返回新作业的ID
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 500,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 500


# 查询作业
@app.route('/user/query_homework', methods=['POST'])
def query_homework():
    try:
        # 从POST请求中获取JSON数据
        request_data = request.get_json()

        # 从JSON数据中提取课程信息
        homework_course = request_data.get('homework_course')
        # 课程作业
        homework_user = request_data.get('homework_user')
        # 通过课程名称或用户查询作业
        if homework_course is not None:
            sql = text("select * from homework where homework_course = :homework_course")
            result = db.session.execute(sql, {"homework_course": homework_course})
            homeworks = result.fetchall()
        elif homework_user is not None:
            sql = text("select * from homework where homework_user = :homework_user")
            result = db.session.execute(sql, {"homework_user": homework_user})
            homeworks = result.fetchall()
        elif homework_user is not None and homework_course is not None:
            # 同时满足课程名称和用户
            sql = text(
                "select * from homework where homework_course = :homework_course and homework_user = :homework_user")
            result = db.session.execute(sql, {"homework_course": homework_course, "homework_user": homework_user})
            homeworks = result.fetchall()
        else:
            response_data = {
                "code": 500,
                "message": "查询失败，参数错误",
                "data": {}
            }
            return jsonify(response_data), 500

        # 如果课程作业不存在
        if homeworks is None:
            response_data = {
                "code": 500,
                "message": "查询失败，该课程作业不存在",
                "data": {}
            }
            return jsonify(response_data), 500
        else:
            # 将结果转换为一个可以被序列化的数据类型
            homeworks_list = []

            for row in homeworks:
                homework_dict = {
                    "id": row[0],
                    "homework_content": row[1],
                    "homework_name": row[2],
                    "homework_course": row[3],
                    "homework_time": row[4],
                    "homework_score": row[5],
                    "homework_user": row[6]
                }
                homeworks_list.append(homework_dict)

        # 返回成功的JSON响应
        response_data = {
            "code": 200,
            "message": "作业查询成功",
            "data": {"homeworks": homeworks_list}  # 返回新作业的ID
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 500,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 500


# 删除作业
@app.route('/user/delete_homework', methods=['POST'])
def delete_homework():
    try:
        # 从POST请求中获取JSON数据
        request_data = request.get_json()

        # 从JSON数据中提取课程信息
        homework_id = request_data.get('homework_id')

        # 查询作业是否存在
        sql = text("select * from homework where id = :homework_id")
        result = db.session.execute(sql, {"homework_id": homework_id})
        homeworks = result.fetchone()
        # 如果作业不存在
        if homeworks is None:
            response_data = {
                "code": 500,
                "message": "删除失败，该作业不存在",
                "data": {}
            }
            return jsonify(response_data), 500

        # 删除作业
        sql = text("delete from homework where id = :homework_id")
        db.session.execute(sql, {"homework_id": homework_id})
        db.session.commit()

        # 返回成功的JSON响应
        response_data = {
            "code": 200,
            "message": "作业删除成功",
            "data": {}  # 返回新作业的ID
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 500,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 500


# 通过用户名查询学生课程
@app.route('/user/query_course', methods=['POST'])
def query_course():
    try:
        # 从POST请求中获取JSON数据
        request_data = request.get_json()

        # 从JSON数据中提取课程信息
        student_name = request_data.get('student_name')

        # 查询学生课程是否存在
        sql = text("select * from course_msg where student_name = :student_name")
        result = db.session.execute(sql, {"student_name": student_name})
        courses = result.fetchall()
        # 如果学生课程不存在
        if courses is None:
            response_data = {
                "code": 500,
                "message": "查询失败，该学生课程不存在",
                "data": {}
            }
            return jsonify(response_data), 500
        else:
            # 将结果转换为一个可以被序列化的数据类型
            courses_list = []

            for row in courses:
                course_dict = {
                    "id": row[0],
                    "student_name": row[1],
                    "course_name": row[2]
                }
                courses_list.append(course_dict)

        # 返回成功的JSON响应
        response_data = {
            "code": 200,
            "message": "学生课程查询成功",
            "data": {"courses": courses_list}  # 返回新作业的ID
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 500,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 500


# 通过用户名查询学生作业
@app.route('/user/query_homework_by_user', methods=['POST'])
def query_homework_by_user():
    try:
        # 从POST请求中获取JSON数据
        request_data = request.get_json()

        # 从JSON数据中提取课程信息
        homework_user = request_data.get('homework_user')

        # 查询学生课程是否存在
        sql = text("select * from homework where homework_user = :homework_user")
        result = db.session.execute(sql, {"homework_user": homework_user})
        courses = result.fetchall()
        # 如果学生课程不存在
        if courses is None:
            response_data = {
                "code": 500,
                "message": "查询失败，该学生作业不存在",
                "data": {}
            }
            return jsonify(response_data), 500
        else:
            # 将结果转换为一个可以被序列化的数据类型
            courses_list = []

            for row in courses:
                course_dict = {
                    "id": row[0],
                    "homework_content": row[1],
                    "homework_name": row[2],
                    "homework_course": row[3],
                    "homework_time": row[4],
                    "homework_score": row[5],
                    "homework_user": row[6]
                }
                courses_list.append(course_dict)

        # 返回成功的JSON响应
        response_data = {
            "code": 200,
            "message": "学生作业查询成功",
            "data": {"courses": courses_list}  # 返回新作业的ID
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 500,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 500


# 通过教师名称查询所有课程
@app.route('/user/query_course_by_teacher', methods=['POST'])
def query_course_by_teacher():
    try:
        # 从POST请求中获取JSON数据
        request_data = request.get_json()

        # 从JSON数据中提取课程信息
        course_teacher = request_data.get('course_teacher')

        # 查询学生课程是否存在
        sql = text("select * from course where course_teacher = :course_teacher")
        result = db.session.execute(sql, {"course_teacher": course_teacher})
        courses = result.fetchall()
        # 如果学生课程不存在
        if courses is None:
            response_data = {
                "code": 500,
                "message": "查询失败，该教师课程不存在",
                "data": {}
            }
            return jsonify(response_data), 500
        else:
            # 将结果转换为一个可以被序列化的数据类型
            courses_list = []

            for row in courses:
                course_dict = {
                    "id": row[0],
                    "course_name": row[1],
                    "course_teacher": row[2]
                }
                courses_list.append(course_dict)

        # 返回成功的JSON响应
        response_data = {
            "code": 200,
            "message": "教师课程查询成功",
            "data": {"courses": courses_list}  # 返回新作业的ID
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 500,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 500


# 通过课程名称查询所有作业,course_homework这张表
@app.route('/user/query_homework_by_course', methods=['POST'])
def query_homework_by_course():
    try:
        # 从POST请求中获取JSON数据
        request_data = request.get_json()

        # 从JSON数据中提取课程信息
        course_name = request_data.get('course_name')

        # 查询学生课程是否存在
        sql = text("select * from course_homework where course_name = :course_name")
        result = db.session.execute(sql, {"course_name": course_name})
        courses = result.fetchall()
        # 如果学生课程不存在
        if courses is None:
            response_data = {
                "code": 500,
                "message": "查询失败，该课程作业不存在",
                "data": {}
            }
            return jsonify(response_data), 500
        else:
            # 将结果转换为一个可以被序列化的数据类型
            courses_list = []

            for row in courses:
                course_dict = {
                    "id": row[0],
                    "course_name": row[1],
                    "course_homework": row[2]
                }
                courses_list.append(course_dict)

        # 返回成功的JSON响应
        response_data = {
            "code": 200,
            "message": "课程作业查询成功",
            "data": {"courses": courses_list}  # 返回新作业的ID
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 200,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 200


# 学生注册课程
@app.route('/user/register_course', methods=['POST'])
def register_course():
    try:
        # 从POST请求中获取JSON数据
        request_data = request.get_json()

        # 从JSON数据中提取课程信息
        student_name = request_data.get('student_name')
        course_name = request_data.get('course_name')

        # 查询课程是否存在
        sql = text("select * from course where course_name = :course_name")
        result = db.session.execute(sql, {"course_name": course_name})
        course = result.fetchone()
        # 如果课程不存在
        if course is None:
            response_data = {
                "code": 500,
                "message": "注册失败，该课程不存在",
                "data": {}
            }
            return jsonify(response_data), 500

        # 查询学生是否已经注册该课程
        sql = text("select * from course_msg where student_name = :student_name and course_name = :course_name")
        result = db.session.execute(sql, {"student_name": student_name, "course_name": course_name})
        course_msg = result.fetchone()
        # 如果课程已经注册
        if course_msg is not None:
            response_data = {
                "code": 500,
                "message": "注册失败，该课程已经注册",
                "data": {}
            }
            return jsonify(response_data), 500

        # 创建新课程
        course_msg = CourseMsg(student_name=student_name, course_name=course_name)
        # 将新课程添加到数据库中
        db.session.add(course_msg)
        db.session.commit()

        # 返回成功的JSON响应
        response_data = {
            "code": 200,
            "message": "课程注册成功",
            "data": {"course_msg_id": course_msg.id}  # 返回新课程的ID
        }
        return jsonify(response_data)

    except Exception as e:
        print(e)
        # 如果发生错误，返回错误的JSON响应
        response_data = {
            "code": 200,
            "message": "服务器内部错误",
            "data": {}
        }
        return jsonify(response_data), 200



if __name__ == '__main__':
    # 开启Flask的调试模式
    app.run(debug=True)
