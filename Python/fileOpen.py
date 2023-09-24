file=load(C:\Users\make1\OneDrive\Desktop\Ituor\Test.uxf)
fileOpen = open(file, "r")    
relationshipArrow = "lt"
arrowCount = []

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
    elif index == 4:
        relationships.append("Aggregation")
    elif index == 5:
        relationships.append("Composition")

#print(relationships)
##with open('testR.txt','w') as f:
#    f.writelines(arrowCount)
#    f.writelines(relationships);

