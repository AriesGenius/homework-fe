# Initialize empty arrays for class and relationship data
classArray = []
relationshipArray = []


# Function to check if a line starts with "class" or "Relationship"
def is_class_line(line):
    return line.strip().startswith("class")

def is_relationship_line(line):
    return line.strip().startswith("Relationship")


    

        
# Open the text file for reading
with open('database.txt', 'r') as file:
    # Read the lines one by one
    lines = file.readlines()
    for line in lines:
        if is_class_line(line):
            # Extract class data from the line and clean the attributes
            class_data = [clean_attribute(attr) for attr in line.strip()[16:-1].split(',')]
            classArray.append(class_data)
        elif is_relationship_line(line):
            # Extract relationship data from the line and clean the attributes
            relationship_data = [clean_attribute(attr) for attr in line.strip()[20:-1].split(',')]
            relationshipArray.append(relationship_data)

# Print the cleaned data
check_class_data_format(class_data)
check_relationship_format(relationship_data)
"""
print("Class Data:")
for class_data in classArray:
    print(class_data)

print("\nRelationship Data:")
for relationship_data in relationshipArray:
    print(relationship_data)
"""
