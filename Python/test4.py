import re

class_example_file = "database.txt"
with open(class_example_file, "r") as f:
  attribute_name_array = []
  relation_name_array = []

  for line in f:
    # Check if the line contains an AttributeComponent
    if re.search(r"AttributeComponent", line):
      # Split the line on the '=' character
      divid = line.split('=')

      # Get the attribute name
      att_name = divid[0].strip()

      # Find all occurrences of the pattern in the line
      res = re.findall(r'\(.*?\)', line)

      # Add the attribute to the attribute array
      attribute_name_array.append(att_name)
      attribute_array.append(res)

print(attribute_array)
