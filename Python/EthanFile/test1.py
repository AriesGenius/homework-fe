import re

class_example_file = "classFormat.txt"
class Conteact:
    
    def __init__(self,name):
        self.name=name

    
with open(class_example_file, "r") as file:
        Clean_list_CC=[]
        count_CC=0
        count_CC_good=0
        problem_CC=[]
        
        count_RC=0
        count_RC_good=0
        problem_RC=[]
        
        for line in file:
          
            if 'ClassComponent' in line:
                
                # Extracting information within brackets
                start_bracket = line.find('(')
                end_bracket = line.find(')')
                content_inside_brackets = line[start_bracket + 1 : end_bracket]
                # Splitting the string by spaces to get individual words
                words = line.split()
                # Splitting the content inside brackets into an array
                array_name_CC = words[0]
                array_elements_CC = [elem.strip() for elem in content_inside_brackets.split(',')]
                
               #print(array_elements_CC       
                
                
                Clean_list = [re.sub(r'\[|\]', ' ', item) for item in array_elements_CC]

                for x in Clean_list:
                    count_CC+=1
                    if x[0].isupper() and x[-1].islower():
                        print(f"{array_name_CC} {x} good")
                        # Append x to Clean_list_CC
                        Clean_list_CC.append(x)
                        count_CC_good+=1
                    else:
                        print(f"{array_name_CC} {x} wrong or null")
                        problem_CC.append(f"{array_name_CC} {x} wrong or null")

                        Clean_list_CC.append(x)

                print('_________________________________')         
               
            elif 'RelationshipComponent' in line:

                # Extracting information within brackets
                start_bracket = line.find('(')
                end_bracket = line.find(')')
                content_inside_brackets = line[start_bracket + 1 : end_bracket]
                # Splitting the string by spaces to get individual words
                words = line.split()
                # Splitting the content inside brackets into an array
                array_name_RC = words[0]
                array_elements_RC = [elem.strip() for elem in content_inside_brackets.split(',')]

                #clear list
                Clean_list = [re.sub(r'\[|\]', ' ', item) for item in array_elements_RC]
                print('--------------------')
                
 
                #check connection
                if Clean_list[0] =='Inhertance':
                    
                    if len(Clean_list)==3:
                        print('Good length for inhertance')
                        # Check if both elements exist in array_elements_CC
                                       
                        if Clean_list[1] and Clean_list[2] not in Clean_list_CC:
                            print(f"Not exsiting class name{Clean_list[1]} or {Clean_list[2]}")
                        else:
                            print('Exsiting class name')
                                    

                    elif len(Clean_list)!=3:
                        print('Wrong length for inhertance')
                elif  Clean_list[0] == "Aggregation" or Clean_list[0] == "Dependency"or Clean_list[0] == "Composition":
                    if len(Clean_list)==6:
                        print('Good length ')
                        # Check if both elements exist in array_elements_CC
                                       
                        if Clean_list[1] and Clean_list[2] not in Clean_list_CC:
                            print(f"Not exsiting class name{Clean_list[1]} or {Clean_list[2]}")
                        else:
                            print('Exsiting class name')
                                    
                        #  null check
                        if  Clean_list[3] is not None:
                            print(f"{Clean_list[3]} is not null")
                            
                            # Check if direction are present in Clean_list[3]
                            if any(c in Clean_list[3] for c in "<>vV^"):
                                print("Cleane_list[3] contains symbols '<>v^'")
                            else:
                                print("Cleane_list[3] does not contain any of the symbols '<>v^'")

                        else:
                            print(f"{Clean_list[3]} is null")
                            #check last
                        if Clean_list[4] and Clean_list[5] is not None:
                            
                         
                            if all(c.isdigit() or c in "* ." for c in Clean_list[4]):
                                print(f"Clean_list[4] contains only numbers, *, and .")
                            else:
                                print(f"Clean_list[4] contains other characters")
                            if all(c.isdigit() or c in "* ." for c in Clean_list[5]):
                                print(f"Clean_list[5] contains only numbers, *, and .")
                            else:
                                print(f"Clean_list[5] contains other characters")
                            
                        
                        else:
                            print('Null check fail')
                    elif len(Clean_list)!=6:
                        print('wrong length')
                else:
                    print('undefined connection')

            elif 'AttributeComponent' in line:
                # Extracting information within brackets
                start_bracket = line.find('(')
                end_bracket = line.find(')')
                content_inside_brackets = line[start_bracket + 1 : end_bracket]
                # Splitting the string by spaces to get individual words
                words = line.split()
                # Splitting the content inside brackets into an array
                array_name_AC = words[0]
                array_elements_AC = [elem.strip() for elem in content_inside_brackets.split(',')]
                
                print('--------------------------')
                Clean_list_CC = [elem.strip() for elem in Clean_list_CC]
                #check attribute name existed in class
                if array_elements_AC[0] is not None:
                    if array_elements_AC[0]  in Clean_list_CC:
                        print('good')
                        print(f"{array_elements_AC[0]}")
                        
                    else:
                        print('not good')
                        print(f"{array_elements_AC[0]}")
                else:
                    print(f"{array_elements_AC[0] } are empty")
                #check properits
                properits=['date','int','str','bool']
                if array_elements_AC[1]  in properits:
                    print('properits existd')
                else:
                    print('properites not existed')
                #check public or private
                if array_elements_AC[2] == "+" or array_elements_AC[2] == "-"or array_elements_AC[2] == "#":
                    print('Good symbol')
                else:
                    print('bad symbol')
                
            elif 'MethodComponent' in line:
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
             
              
                if array_elements_MC[1] =='void' or array_elements_MC[1]== 'Void':
                    print('Good content void')
                elif ':' in array_elements_MC[1]:
                    content_after_colon = array_elements_MC[1].split(':')[1].strip()
                    if content_after_colon =='str'or content_after_colon=='int' or content_after_colon== 'date'or content_after_colon== 'DateTime'or content_after_colon== 'bool':
                        print('Good input class name')
                else:
                    print(f"{array_name_MC} Check input")
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
     

print(count_CC)
print(count_CC_good)
print(problem_CC)
print('-----------------')
print(count_RC)
print(count_RC_good)
print(problem_RC)
