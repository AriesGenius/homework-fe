# Initialize empty arrays for class and relationship data
classArray = []
relationshipArray = []

# Function to check if a line starts with "class" or "Relationship"
def is_class_line(line):
    return line.strip().startswith("class")

def is_relationship_line(line):
    return line.strip().startswith("Relationship")
def check_attribute_format(attribute):
    # Check if the first letter is capital and the last letter is lowercase
    if attribute[0].isupper() and attribute[-1].islower():
        return "Good format"
    else:
        return "Format problem"
        print(attribute[0]+"first"+attribute[-1])
def check_class_data_format(class_data):
    for attribute in class_data:
        result = check_attribute_format(attribute)
        print(f"{attribute}: {result}")

# Open the text file for reading
with open('Classexample.txt', 'r') as file:
    # Read the lines one by one
    lines = file.readlines()
    for line in lines:
        if is_class_line(line):
            # Extract class data from the line
            class_data = line.strip()[16:-1].split(',')
            classArray.append(class_data)
        elif is_relationship_line(line):
            # Extract relationship data from the line
            relationship_data = line.strip()[20:-1].split(',')
            relationshipArray.append(relationship_data)

# Print the extracted data
check_class_data_format(class_data)
print("Class Data:")
for class_data in classArray:
    print(class_data)

print("\nRelationship Data:")
for relationship_data in relationshipArray:
    print(relationship_data)
