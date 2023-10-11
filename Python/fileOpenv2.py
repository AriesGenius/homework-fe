# file must first be converted to a text file.
file = input("Please input the location of the file to open: ")

# read the file
fileOpen = open(file, "r")

# list of file lines for reading attributes and methods
file_list = []

# the string which represents the types of relationships
relationshipArrow = "lt"
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

# *..* 1..* etc
m1_numbers = "m1"
m2_numbers = "m2"

# list for m1_numbers and m2_numbers
m1 = []
m2 = []

# attributes
attributes = "--"
attributesList = []

methods = "("
methodsList = []

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
    elif className in line:
        classes.append(line)

    # appending the lines that m1 and m2 are in to the lists.
    elif m1_numbers in line:
        m1.append(line)
    elif m2_numbers in line:
        m2.append(line)

    # appending attributes to list.
    #elif attributes in line:
    #    attributesList.append(line)

indexCount = 0
while indexCount < len(file_list):
    if attributes in file_list[indexCount] and methods not in file_list[indexCount + 1]:
        attributesList.append(file_list[(indexCount + 1)])
    elif attributes in file_list[indexCount] and methods in file_list[indexCount + 1]:
        methodsList.append(file_list[(indexCount + 1)])
        if attributes in file_list[indexCount] and methods in file_list[indexCount + 2]:
            methodsList.append(file_list[(indexCount + 2)])
    indexCount += 1

newClasses = [name.replace("<panel_attributes>", "") for name in classes]

print(arrowCount)

# listing the names of the relationships
relationships = []

# The different numbers represent what type of relationship
for index in arrowCount:
    if index == 2:
        relationships.append("Inheritance")
    elif index == 0:
        relationships.append("Association")
    elif index == 2.1:
        relationships.append("Realisation")
    elif index == 1.1:
        relationships.append("Dependency")
    elif index == 3:
        relationships.append("Directed Association")
    elif index == 4:
        relationships.append("Aggregation")
    elif index == 5:
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

# printing everything
print("The relationships are", relationships)

print("The x coordinates are:", xCoordinate)
print("The y coordinates are:", yCoordinate)
print("The w coordinates are:", wCoordinate)
print("The h coordinates are:", hCoordinate)

print("The classes are:", newClasses)

print("The m1's are:", m1)
print("The m2's are:", m2)

print("The attributes are:", attributesList)
print("The methods are:", methodsList)