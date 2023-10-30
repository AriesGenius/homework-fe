import re

class_example_file = "Classexample.txt"

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
    # Check if every index is not null, except when split_row[0] is inheritance, and split_row[3] and [4] must be null.
    if split_row[0] != "Inheritance" and any(element is None for element in split_row):
        problems.append("All fields must be not null, except split_row[3] and [4] when split_row[0] is Inheritance")
    elif split_row[0] == "Inheritance" and (split_row[3] is not None or split_row[4] is not None):
        problems.append("split_row[3] and [4] must be null when split_row[0] is Inheritance")

    # Check if the relationship type is valid.
    if split_row[0] not in valid_relationship_types:
        problems.append("Relationship error: " + split_row[0])

    # Check if the source and target classes exist in the attribute_name_array.
    if split_row[1] not in attribute_name_array or split_row[2] not in attribute_name_array:
        problems.append("Class name not in existing class names: ", split_row[1], split_row[2])    
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
    
    
    #print(new_item4,new_item5)



                
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


print('_________________________________')

# Count the total number of problems and good things in the array
count_problem = len(problem)
count_good = len(good)
total_count = count_problem + count_good

# If there are no problems, print a message saying that the design is perfect
if count_problem == 0:
    print('your design is prefect')

# Otherwise, calculate the percentage of problems and good things in the array
else:
    percent_problem = count_problem / total_count * 100
    percent_good = count_good / total_count * 100

print("Total count of problems:", count_problem)
print("Total count of good things:", count_good)

# Print the percentage of problems and good things in the array
print("Percentage of problems:", percent_problem)
print("Percentage of good things:", percent_good)


print('------------------------------')
print('First time and second time feedback ')

# Check each index of the problem array and print the appropriate message.
if percent_good > percent_problem:
    print('You did good job,but there are something you can improve with')
elif percent_good < percent_problem:
    print("Keep it up, don't give up")
for index, problems in enumerate(problem):
    if index == 0:
        print("Please check Relationship ")
    elif index == 1:
        print("Please check your attribute name.")
    elif index == 2:
        print("Please check your label.")
    elif index == 3:
        print("Class name is not included in existing classes,please check")

print('-----------------------------------')
print('Third Time feedback')
# If the percentage of good things is more than the percentage of problems, print a message encouraging the user to keep up the good work, but also print the problem array
if percent_good > percent_problem:
  print("Good effort, keep it up, but there are some problems in this array:")
  print(problem)
else:
  print("There are more problems than good things in this array:")
  print(problem)


