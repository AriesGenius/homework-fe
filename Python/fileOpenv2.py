# file must first be converted to a text file.
file = input("Please input the location of the file to open: ")

# read the file
fileOpen = open(file, "r")

# the string which represents the types of relationships
relationshipArrow = "lt"
# a list for counting how many times the relationshipArrow string is seen
arrowCount = []

# the string which represents the class names in the file
className = "<panel_attributes>_"
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

for line in fileOpen:
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

# printing everything
print("The relationships are", relationships)

print("The x coordinates are:", xCoordinate)
print("The y coordinates are:", yCoordinate)
print("The w coordinates are:", wCoordinate)
print("The h coordinates are:", hCoordinate)

print("The classes are:", newClasses)