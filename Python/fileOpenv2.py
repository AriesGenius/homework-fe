# file must first be converted to a text file.
file = input("Please input the location of the file to open: ")

fileOpen = open(file, "r")

relationshipArrow = "lt"
arrowCount = []

className = "<panel_attributes>_"
classes = []

xCoordinateStart = "<x>"
yCoordinateStart = "<y>"
wCoordinateStart = "<w>"
hCoordinateStart = "<h>"
xCoordinateEnd = "</x>"
yCoordinateEnd = "</y>"
wCoordinateEnd = "</w>"
hCoordinateEnd = "</h>"

xCoordinate = []
yCoordinate = []
wCoordinate = []
hCoordinate = []

for line in fileOpen:
    count = 0
    letterCount = 0
    if relationshipArrow in line:
        for letter in line:
            if letter == "&":
                count = count + 1
            if letter == ".":
                count = count + 0.1
        arrowCount.append(count)

    elif xCoordinateStart in line:
        xCoordinate.append(line)
        print(xCoordinate)
    elif yCoordinateStart in line:
        yCoordinate.append(line)
        print(yCoordinate)
    elif wCoordinateStart in line:
        wCoordinate.append(line)
        print(wCoordinate)
    elif hCoordinateStart in line:
        hCoordinate.append(line)
        print(hCoordinate)

    elif className in line:
        classes.append(line)

print(arrowCount)

relationships = []
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

print(relationships)

print("The x coordinate is:", xCoordinate)
print("The y coordinate is:", yCoordinate)
print("The w coordinate is:", wCoordinate)
print("The h coordinate is:", hCoordinate)

print(classes)