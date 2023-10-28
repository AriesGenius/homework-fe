import re

class_example_file = "database.txt"

attribute_array = []
realtion_array = []
good=[]
problem=[]

# Function to clean attribute names
def clean_attribute(attribute):
    return attribute.strip("[]'()")

def remove_all_brackets_and_quotes(attribute_array):
  """Removes all brackets and quotes from a text."""
  return re.sub('[\[\]\'()]', '', attribute_array)





def deletebreacket (Att_array):
    for item in Att_array:
        # Remove all parentheses from the item.
        item = item.replace("(", "").replace(")", "")

  # Return the updated array.
    return Att_array
    
def remove_unwanted_chars(input_string):
    cleaned_string = input_string.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace('"', '')
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
    if not any(valid_type in split_row[0] for valid_type in valid_relationship_types):
        problem.append("Relationship error: " + split_row[0])

    else:
        good.append("Good Relationship type")
   

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
    new_item4= remove_unwanted_chars(split_row[4])
    new_item5= remove_unwanted_chars(split_row[5])
    
    print('not sure how this ListMultiplicity is correctd. my idea is only accept numbers and *')
    print(new_item4,new_item5)



                
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
    cleaned_list= []
    for words in Att_array:
        cleaned_words= words.replace("(", "").replace(")", "")
        cleaned_list.append(cleaned_words)
    for item in cleaned_list:
        if not item[0].isupper() or not item[-1].islower():
            problem.append("check format " + item)
        else:
             good.append("good format " + item)       
          
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
            attribute_name_array.append(''+ att_name+'')
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
for row in attribute_array:
  for i in range(len(row)):
    row[i] = remove_symbols(row[i])

for row2 in realtion_name_array:
    for i in range(len(row2)):
        row2 = remove_symbols(row2[i])
     

#check every thing in attribute array
for x in attribute_array:
    Att_array = x[0].split(",")
    checkdata(Att_array)

check_relationship_format(realtion_name_array)
#Those printed statment could be third time feedback
print('_________________________')
print('problem having in this database language model')
print(problem)
print('Good stuff in this datbase language model')
print(good)


