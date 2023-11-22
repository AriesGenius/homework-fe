import re

class_example_file = "classFormat.txt"
class Conteact:
    
    def __init__(self,name):
        self.name=name

    
with open(class_example_file, "r") as file:
    for line in file:
            if 'MethodComponent' in line:
                print('______________________')
                # Extracting information within brackets
                start_bracket = line.find('(')
                end_bracket = line.rfind(')')
                content_inside_brackets = line[start_bracket + 1 : end_bracket]
                # Splitting the string by spaces to get individual words
                words = line.split()
                # Splitting the content inside brackets into an array
                array_name_MC = words[0]
                array_elements_MC = [elem.strip() for elem in content_inside_brackets.split(',')]
                
                Clean_list = [re.sub(r'\[|\] ', ' ', item) for item in array_elements_MC]
                
                #check for ()
                if re.search(r"\(\)", array_elements_MC[0]):
                    print(f"() found {array_elements_MC[0]}")
                else:
                    print(f" please check {array_name_MC} method")
                #check input file
                array_elements_MC[1] = array_elements_MC[1].strip()
                print(array_elements_MC[1])
             
              
                if array_elements_MC[1] =='void' or array_elements_MC[1]== 'Void':
                    print('Good content void')
                elif ':' in array_elements_MC[1]:
                    content_after_colon = array_elements_MC[1].split(':')[1].strip()
                    if content_after_colon =='str'or content_after_colon=='int' or content_after_colon== 'date'or content_after_colon== 'DateTime'or content_after_colon== 'bool':
                        print('Good input class name')
                    else:
                        print('not good')
                else:
                    print(f"{array_name_MC} Check input")

                    '''
                # check output  file
                array_elements_MC[2] = array_elements_MC[2].strip()
      
                if array_elements_MC[2]=='str' or array_elements_MC[2]=='bool'or array_elements_MC[2]=='DateTime':
                    print('Good output')
                else:
                    print(f"{array_name_MC} Check output")

                #check public or private
                array_elements_MC[3] = array_elements_MC[3].strip()
                if array_elements_MC[3] == "+" or array_elements_MC[3] == "-" or array_elements_MC[3] =="#":
                    print('Good visibility')
                else:
                    print(f"{array_name_MC} Check visibility")
                 '''
