import re

class ClassComponent:
  def __init__(self, name, components):
    self.name = name
    self.components = components

class RelationshipComponent:
  def __init__(self, type, source, target, label, multiplicity):
    self.type = type
    self.source = source
    self.target = target
    self.label = label
    self.multiplicity = multiplicity

def check_line_type(line):
  """Checks if a line of database UML code contains "classComponent" or "RelationshipCompoent".

  Args:
    line: A line of database UML code.

  Returns:
    True if the line contains "classComponent" or "RelationshipCompoent", False otherwise.
  """

  if "classComponent" in line or "RelationshipCompoent" in line:
    return True
  else:
    return False

def check_class_component(class_component):
  """Checks if a class component is valid.

  Args:
    class_component: A ClassComponent object.

  Returns:
    True if the class component is valid, False otherwise.
  """

  # Check if the class component name is valid.
  if not class_component.name[0].isupper() or not class_component.name[-1].islower():
    print("Class component name is not valid: {}".format(class_component.name))
    return False

  # Check if the class component components are valid.
  for component in class_component.components:
    if not check_component_name(component):
      return False

  return True

def check_relationship_component(relationship_component):
  """Checks if a relationship component is valid.

  Args:
    relationship_component: A RelationshipComponent object.

  Returns:
    True if the relationship component is valid, False otherwise.
  """

  # Check if the relationship component type is valid.
  if relationship_component.type not in ["Association", "Inheritance", "Aggregation", "Composition"]:
    print("Relationship type is not valid: {}".format(relationship_component.type))
    return False

  # Check if the relationship component source and target classes are valid.
  if not check_component_name(relationship_component.source):
    return False
  if not check_component_name(relationship_component.target):
    return False

  # Check if the relationship component label is valid.
  if not relationship_component.label[0].isupper() or not relationship_component.label[-1].islower():
    print("Relationship label name is not valid: {}".format(relationship_component.label))
    return False

  # Check if the relationship component multiplicity is valid.
  for multiplicity in relationship_component.multiplicity:
    if not multiplicity.isdigit() and multiplicity != "*" and multiplicity != "..":
      print("Relationship multiplicity is not valid: {}".format(multiplicity))
      return False

  return True

def check_component_name(component_name):
  """Checks if a component name is valid.

  Args:
    component_name: A string representing the component name.

  Returns:
    True if the component name is valid, False otherwise.
  """

  return component_name[0].isupper() and component_name[-1].islower()

def main():
  # Read the database UML code from a file.
  with open("classexample.txt", "r") as f:
    lines = f.readlines()

  # Create a list of class components and relationship components.
  class_components = []
  relationship_components = []
  for line in lines:
    line = line.strip()
    if check_line_type(line):
  

      # Split the line into components.
      components = line.split(",")

      # If the line is a class component, create a ClassComponent object.
      if components[0] == "classComponent":
        class_component = ClassComponent(components[1], components[2:])
        class_components.append(class_component)

      # If the line is a relationship component, create a RelationshipComponent object.
      elif components[0] == "RelationshipCompoent":
        relationship_component = RelationshipComponent(components[1], components[2], components[3], components[4], components[5:])
        relationship_components.append(relationship_component)

      # Otherwise, print an error message.
      else:
        print("Invalid line: {}".format(line))

  # Check if all of the class components are valid.
  for class_component in class_components:
    check_class_component(class_component)

  # Check if all of the relationship components are valid.
  for relationship_component in relationship_components:
    check_relationship_component(relationship_component)

if __name__ == "__main__":
  main()
