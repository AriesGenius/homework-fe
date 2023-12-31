import re

class_example_file = "database.txt"

attribute_array = []
realtion_array = []

# Function to clean attribute names
def clean_attribute(attribute):
    return attribute.strip("[]'()")


def check_class_data_format(class_data):
    for index, attribute in enumerate(class_data):
        result = check_attribute_format(attribute)
        print(f"{index}: {attribute}: {result}")

def check_attribute_format(attribute):
    # Check if the first letter is capital and the last letter is lowercase
    if attribute[0].isupper() and attribute[-1].islower():
        return "Good format"
    else:
        return "Format problem"

def check_relationship_format(relationship_data):
    valid_relationship_types = ["Association", "Inheritance", "Aggregation", "Composition"]
    problem= []
    

    for attribute in relationship_data:
        data_pieces = attribute.split(',')
        if len(data_pieces) != 6:
            print(f"Format problem: {attribute}")
        else:
            relationship_type, source_class, target_class, label, direction, multiplicity = map(str.strip, data_pieces)
            
              

            if relationship_type not in valid_relationship_types:
                problem.append(f"Relationship type wrong: ")
                
                
     
            if not (label[0].isupper() and label[-2].islower()):
                problem.append(f"Label name format problem: ")
            elif label[-1] not in "^v<>":
                problem.append(f"Direction error: ")
           
            if not multiplicity.replace(".", "").replace("*", "").isdigit():
                problem.append(f"Multiplicity format problem: ")
            else:
                print(f"Good format: ")

with open(class_example_file, "r") as file:
    attribute_name_array = []
    realtion_name_array=[]
    for line in file.readlines():
        # Check if the line contains an AttributeComponent
        if re.search(r"ClassComponet", line):
            divid= line.split('=')
            
            att_name= divid[0].strip()
            res = re.findall(r'\(.*?\)', line)
            

            # Add the attribute to the attribute array
            attribute_name_array.append('['+ att_name+']')
            attribute_array.append(res)
        
                

        # Check if the line contains a RelationshipComponent
        elif re.search(r"RelationshipComponet", line):
            # Extract the relationship name, source attribute, and destination attribute from the line
            divid=line.split('=')
            res = re.findall(r'\(.*?\)', line)
            att_name= divid[0].strip()
            
            
            # Add the relationship to the attribute array
            realtion_array.append('['+ att_name+']')
            realtion_name_array.append(res)


# Print the attribute array
print(attribute_name_array)
print(attribute_array)
print(realtion_name_array)
print(realtion_array)
print('--------------------------')
check_relationship_format(realtion_array)
check_class_data_format(attribute_array)

