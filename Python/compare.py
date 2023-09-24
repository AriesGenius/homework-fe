import xml.etree.ElementTree as ET

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
    })

  return data

def compare_uxf_files(correct_uxf_file, wrong_uxf_file):
  """Compares two .uxf files and prints the differences to the console.

  Args:
    correct_uxf_file: The path to the correct .uxf file.
    wrong_uxf_file: The path to the wrong .uxf file.
  """

  correct_data = extract_data_from_uxf(correct_uxf_file)
  wrong_data = extract_data_from_uxf(wrong_uxf_file)

  # Create a dictionary to store the differences between the two files.
  differences = {}

  # Iterate over the correct data and compare it to the wrong data.
  for correct_item in correct_data:
    wrong_item = None
    for wrong_item in wrong_data:
      if correct_item['name'] == wrong_item['name'] and correct_item['type'] == wrong_item['type']:
        break

    # If the wrong item is None, then it means that the corresponding correct item
    # does not exist in the wrong file.
    if wrong_item is None:
      differences[correct_item['name']] = {
        'correct': correct_item,
        'wrong': None,
      }

    # If the two items are not equal, then add the difference to the differences dictionary.
    elif correct_item != wrong_item:
      differences[correct_item['name']] = {
        'correct': correct_item,
        'wrong': wrong_item,
      }

  # Print the differences to the console.
  for name, difference in differences.items():
    print('Differences for element "{}":'.format(name))
    print('  Correct: {}'.format(difference['correct']))
    print('  Wrong: {}'.format(difference['wrong']))

if __name__ == '__main__':
  correct_uxf_file = 'correct_uxf_file.uxf'
  wrong_uxf_file = 'wrong_uxf_file.uxf'

  compare_uxf_files(correct_uxf_file, wrong_uxf_file)
