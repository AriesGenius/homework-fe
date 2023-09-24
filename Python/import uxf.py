import uxf
import xml.etree.ElementTree as ET

def convert_uxf_to_txt(filename):
    """Converts a UXF file to TXT format."""
    #file = uxf.load(filename)
    tree = ET.parse(filename)
    root = tree.getroot()
    #tree class use 

    txt = ""
    for child in root:
        txt += child.tag + ":" + child.text + "\n"

    return txt


def extract_data_from_uxf(uxf_file):
  """Extracts data from a .uxf file using ElementTree.

  Args:
    uxf_file: The path to the .uxf file.

  Returns:
    A list of dictionaries, where each dictionary contains the extracted data for a
    single element in the .uxf file.
  """

  tree = ET.parse(uxf_file)
  root = tree.getroot()

  data = []
  for element in root.findall('element'):
    data.append({
      'name': element.get('name'),
      'type': element.get('type'),
      'value': element.get('value'),
      'Staff':element.get('Staff')
    })

  return data

def sort_data_into_groups(data, group_by_key):
  """Sorts data into groups based on a given key.

  Args:
    data: A list of dictionaries, where each dictionary contains the data for a
      single object.
    group_by_key: The key to use for grouping the data.

  Returns:
    A dictionary, where the keys are the unique values of the group_by_key and the
    values are lists of dictionaries containing the data for all objects in that
    group.
  """

  groups = {}
  for item in data:
    group_key = item[group_by_key]
    if group_key not in groups:
      groups[group_key] = []
    groups[group_key].append(item)

  return groups

def main():
  uxf_file = 'bonj007_domain1.uxf'
  group_by_key = 'type'

  data = extract_data_from_uxf(uxf_file)
  groups = sort_data_into_groups(data, group_by_key)
 

  # Print the sorted data to the console.
  for group_key, items in groups.items():
    print(group_key)
    for item in items:
      print('  ', item)

if __name__ == '__main__':
  main()



