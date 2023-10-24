import re

def main():
    correct_filelocation = input("Please input the location of the correct file to open: ")
    wrong_filelocation = input("wrong file")
    Correct_array =[]
    wrong_array = []

    
    

    try:
        with open(correct_filelocation, "r") as correct_fileOpen:
            
            # existing code here ...
            # read the file
            correct_fileOpen = open(correct_filelocation, "r")

            correct_file_list = []
            

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

            labels = []

            # additional attribuutes
            relationshipLocation = "<additional_attributes>"
            directionList = []

            for line in correct_fileOpen:

                correct_file_list.append(line)

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
            while indexCount < len(correct_file_list):
                if attributes in correct_file_list[indexCount] and methods not in correct_file_list[indexCount + 1]:
                    attributesIndex = 1
                    attributeCount = 0
                    while attributes not in correct_file_list[(indexCount + attributesIndex)] and "</panel_attributes>" not in correct_file_list[(indexCount + attributesIndex)]:
                        attributesList.append(correct_file_list[(indexCount + attributesIndex)])
                        newAttributesList.append(correct_file_list[(indexCount + attributesIndex)])
                        attributeType.append(correct_file_list[(indexCount + attributesIndex)])
                        attributesIndex += 1
                        attributeCount += 1
                    attributeCountList.append(attributeCount)
                elif attributes in correct_file_list[indexCount] and methods in correct_file_list[indexCount + 1]:
                    methodsIndex = 1
                    methodCount = 0
                    while methods in correct_file_list[indexCount + methodsIndex]:
                        methodsList.append(correct_file_list[(indexCount + methodsIndex)])
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
            date = "date"
            dateTime = "DateTime"
            string = "str"
            bool = "bool"
            twoDots = ":"
            leftArrow = "&lt;"
            rightArrow = "&gt;"

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

            Correct_array.append("The relationships are " + str(relationships))
            Correct_array.append("The x coordinates are: " + str(xCoordinate))
            Correct_array.append("The y coordinates are: " + str(yCoordinate))
            Correct_array.append("The w coordinates are: " + str(wCoordinate))
            Correct_array.append("The h coordinates are: " + str(hCoordinate))
            Correct_array.append("The classes are: " + str(newClasses))
            Correct_array.append("The m1's are: " + str(m1))
            Correct_array.append("The m2's are: " + str(m2))
            Correct_array.append("The attributes are: " + str(attributesList))
            Correct_array.append("The attributes are: " + str(newAttributesList))
            Correct_array.append("The methods are: " + str(methodsList))
            Correct_array.append("attribute count list: " + str(attributeCountList))
            Correct_array.append("method count list: " + str(methodCountList))
            Correct_array.append("the attribute visibilities are: " + str(attributeVis))
            Correct_array.append("the attribute types are: " + str(attributeTypes))
            Correct_array.append("the labels are: " + str(labels))
            Correct_array.append("relationship labels level: " + str(relationLevel))


            f = open("classFormat.txt", "w")

            writeCount = 0
            c = 0
            classIndex = 0
            attributesTotal = 0
            for x in newClasses:
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
            for r in relationships:
                f.write("RelationshipComponent(")
                f.write(r)
                f.write(", ")
                f.write("SourceClass")
                f.write(", ")
                f.write("TargetClass")
                f.write(", ")
                if relationships.index(r) in relationLevel:
                    f.write(labels[labelCount])
                    labelCount += 1
                else:
                    f.write("no label")
                #f.write("label")
                f.write(", [")
                f.write(m1[multiplicityCount])
                f.write(", ")
                f.write(m2[multiplicityCount])
                f.write("])")
                f.write("\n")
                multiplicityCount += 1
                indCount += 1

            f.write("\n")

            c1 = 0
            c2 = 0
            lengthValue = 0

            for a in newAttributesList:
                f.write("AttributeComponent(")
                f.write(a)
                f.write(", ")
                if len(attributeTypes) > lengthValue:
                    f.write(attributeTypes[c2])
                else:
                    f.write("noAttributeType")
                f.write(", ")
                if len(attributeVis) > lengthValue:
                    f.write(attributeVis[c1])
                else:
                    f.write("noAttributeVis")
                f.write(")")
                f.write("\n")
                c1 += 1
                c2 += 1
                lengthValue += 1

            
    
        with open(wrong_filelocation, "r") as wrong_fileOpen:
            
            # read the file
            wrong_fileOpen = open(wrong_filelocation, "r")

            wrong_file_list = []
            

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

            labels = []

            # additional attribuutes
            relationshipLocation = "<additional_attributes>"
            directionList = []

            for line in wrong_fileOpen:

                wrong_file_list.append(line)

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
            while indexCount < len(wrong_file_list):
                if attributes in wrong_file_list[indexCount] and methods not in wrong_file_list[indexCount + 1]:
                    attributesIndex = 1
                    attributeCount = 0
                    while attributes not in wrong_file_list[(indexCount + attributesIndex)] and "</panel_attributes>" not in wrong_file_list[(indexCount + attributesIndex)]:
                        attributesList.append(wrong_file_list[(indexCount + attributesIndex)])
                        newAttributesList.append(wrong_file_list[(indexCount + attributesIndex)])
                        attributeType.append(wrong_file_list[(indexCount + attributesIndex)])
                        attributesIndex += 1
                        attributeCount += 1
                    attributeCountList.append(attributeCount)
                elif attributes in wrong_file_list[indexCount] and methods in wrong_file_list[indexCount + 1]:
                    methodsIndex = 1
                    methodCount = 0
                    while methods in wrong_file_list[indexCount + methodsIndex]:
                        methodsList.append(wrong_file_list[(indexCount + methodsIndex)])
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
            date = "date"
            dateTime = "DateTime"
            string = "str"
            bool = "bool"
            twoDots = ":"
            leftArrow = "&lt;"
            rightArrow = "&gt;"

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

            # printing everything
         
            wrong_array.append("The relationships are " + str(relationships))
            wrong_array.append("The x coordinates are: " + str(xCoordinate))
            wrong_array.append("The y coordinates are: " + str(yCoordinate))
            wrong_array.append("The w coordinates are: " + str(wCoordinate))
            wrong_array.append("The h coordinates are: " + str(hCoordinate))
            wrong_array.append("The classes are: " + str(newClasses))
            wrong_array.append("The m1's are: " + str(m1))
            wrong_array.append("The m2's are: " + str(m2))
            wrong_array.append("The attributes are: " + str(attributesList))
            wrong_array.append("The attributes are: " + str(newAttributesList))
            wrong_array.append("The methods are: " + str(methodsList))
            wrong_array.append("attribute count list: " + str(attributeCountList))
            wrong_array.append("method count list: " + str(methodCountList))
            wrong_array.append("the attribute visibilities are: " + str(attributeVis))
            wrong_array.append("the attribute types are: " + str(attributeTypes))
            wrong_array.append("the labels are: " + str(labels))
            wrong_array.append("relationship labels level: " + str(relationLevel))
            f = open("classFormat.txt", "w")

            writeCount = 0
            c = 0
            classIndex = 0
            attributesTotal = 0
            for x in newClasses:
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
            for r in relationships:
                f.write("RelationshipComponent(")
                f.write(r)
                f.write(", ")
                f.write("SourceClass")
                f.write(", ")
                f.write("TargetClass")
                f.write(", ")
                if relationships.index(r) in relationLevel:
                    f.write(labels[labelCount])
                    labelCount += 1
                else:
                    f.write("no label")
                #f.write("label")
                f.write(", [")
                f.write(m1[multiplicityCount])
                f.write(", ")
                f.write(m2[multiplicityCount])
                f.write("])")
                f.write("\n")
                multiplicityCount += 1
                indCount += 1

            f.write("\n")

            c1 = 0
            c2 = 0
            lengthValue = 0

            for a in newAttributesList:
                f.write("AttributeComponent(")
                f.write(a)
                f.write(", ")
                if len(attributeTypes) > lengthValue:
                    f.write(attributeTypes[c2])
                else:
                    f.write("noAttributeType")
                f.write(", ")
                if len(attributeVis) > lengthValue:
                    f.write(attributeVis[c1])
                else:
                    f.write("noAttributeVis")
                f.write(")")
                f.write("\n")
                c1 += 1
                c2 += 1
                lengthValue += 1
                
            for item in Correct_array:
                print(item)
            print("______________________________________Answer file reading")
            for item in wrong_array:
                print(item)

            print("_______________________________________________-user file reading")

            # Compare the two arrays
            if Correct_array == wrong_array:
                print("Correct and wrong arrays are equal.")
            else:
                print("Correct and wrong arrays are different.")

           


    except FileNotFoundError:
        print("File not found. Please check the file location.")

    

    
        

if __name__ == "__main__":
    main()
