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

        count_AC =0
        count_AC_good=0
        problem_AC=[]

        count_MC=0
        count_MC_good=0
        problem_MC=[]

        for line in file:
        #Check Class Componet
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
                count_CC+=1
                for x in Clean_list:
                    
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
          #Check Relationship Components     
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
                count_RC+=1
                
 
                #check connection
                if Clean_list[0] =='Inhertance':
                    
                    if len(Clean_list)==3:
                        print('Good length for inhertance')
                        count_RC_good+=1
                        # Check if both elements exist in array_elements_CC
                                       
                        if Clean_list[1] and Clean_list[2] not in Clean_list_CC:
                            print(f"Not exsiting class name{Clean_list[1]} or {Clean_list[2]}")
                            problem_RC.append(f"Not exsiting class name{Clean_list[1]} or {Clean_list[2]}")
                        else:
                            count_RC_good+=1
                            print('Exsiting class name')
                            
                                    

                    elif len(Clean_list)!=3:
                        print('Wrong length for inhertance')
                        problem_RC.append('Wrong length for inhertance')
                elif  Clean_list[0] == "Aggregation" or Clean_list[0] == "Dependency"or Clean_list[0] == "Composition":
                    if len(Clean_list)==6:
                        count_RC_good+=1
                        print('Good length ')
                        # Check if both elements exist in array_elements_CC
                                       
                        if Clean_list[1] and Clean_list[2] not in Clean_list_CC:
                            print(f"Not exsiting class name{Clean_list[1]} or {Clean_list[2]}")
                            problem_RC.append(f"Not exsiting class name{Clean_list[1]} or {Clean_list[2]}")
                        else:
                            count_RC_good+=1
                            print('Exsiting class name')
                                    
                        #  null check
                        if  Clean_list[3] is not None:
                            print(f"{Clean_list[3]} is not null")
                            
                            # Check if direction are present in Clean_list[3]
                            if any(c in Clean_list[3] for c in "<>vV^"):
                                print("Clean_list[3] contains symbols '<>v^'")
                            else:
                                print("Clean_list[3] does not contain any of the symbols '<>v^'")
                                problem_RC.append(f"{Clean_list[3]} does not contain any of the symbols '<>v^'")
                        else:
                            print(f"{Clean_list[3]} is null")
                            #check ListMultiplicity
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
                            problem_RC.append(f"{array_name_RC} have null value")
                    elif len(Clean_list)!=6:
                        print('wrong length')
                        problem_RC.append(f"{array_name_RC} please check value")
                else:
                    print('undefined connection')
                    problem_RC.append(f"{array_name_RC} have undefined Relationshiptype")
            #Check AttributeComponets
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
                
                
                Clean_list_CC = [elem.strip() for elem in Clean_list_CC]
                count_AC+=1
                #check attribute name existed in class
                if array_elements_AC[0] is not None:
                    if array_elements_AC[0]  in Clean_list_CC:
                        print('good')
                        print(f"{array_elements_AC[0]}")
                        count_AC_good+=1
                        
                    else:
                        print('not good')
                        print(f"{array_elements_AC[0]}")
                        problem_AC.append(f"{array_name_AC} Attribute name are not exsiting in class name")
                else:
                    print(f"{array_elements_AC[0] } are empty")
                    problem_AC.append(f"{array_name_AC} missing Attribute name")
                #check properits
                properits=['date','int','str','bool']
                if array_elements_AC[1]  in properits:
                    print('properits existd')
                    count_AC_good+=1
                else:
                    print('properites not existed')
                    problem_AC.append(f"in { array_name_AC} AttributeType wrong")
                    
                #check public or private
                if array_elements_AC[2] == "+" or array_elements_AC[2] == "-"or array_elements_AC[2] == "#":
                    print('Good symbol')
                    count_AC_good+=1
                    
                else:
                    print('bad symbol')
                    problem_AC.append(f"{array_name_AC} have undefined visibility marker")
            #Check MethodComonent
            elif 'MethodComponent' in line:
           
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
                count_MC +=1
                #check for ()
                if re.search(r"\(\)", array_elements_MC[0]):
                    print(f"() found {array_elements_MC[0]}")
                    count_MC_good+=1
                else:
                    print(f" please check {array_name_MC} method")
                    problem_AC.append(f"{array_name_MC} Check method name")
                #check input file
                array_elements_MC[1] = array_elements_MC[1].strip()
              
                if array_elements_MC[1] =='void' or array_elements_MC[1]== 'Void':
                    print('Good content void')
                    count_MC_good+=1
                elif ':' in array_elements_MC[1]:
                    content_after_colon = array_elements_MC[1].split(':')[1].strip()
                    if content_after_colon =='str'or content_after_colon=='int' or content_after_colon== 'date' or content_after_colon== 'DateTime'or content_after_colon== 'bool':
                        print('Good input class name')
                        count_MC_good+=1
                    else:
                        problem_MC.append(f"{array_name_MC} Check intput class name")
                else:
                    print(f"{array_name_MC} Check input attribute")
                    problem_MC.append(f"{array_name_MC} Check intput class name")
                # check output  file
                array_elements_MC[2] = array_elements_MC[2].strip()
      
                if array_elements_MC[2]=='str' or array_elements_MC[2]=='bool'or array_elements_MC[2]=='DateTime':
                    print('Good output')
                    count_MC_good+=1
                else:
                    print(f"{array_name_MC} Check output attribute")
                    problem_MC.append(f"{array_name_MC} Check output class name")

                #check public or private
                array_elements_MC[3] = array_elements_MC[3].strip()
                if array_elements_MC[3] == "+" or array_elements_MC[3] == "-" or array_elements_MC[3] =="#":
                    print('Good visibility')
                    count_MC_good+=1
                else:
                    print(f"{array_name_MC} Check visibility")
                    problem_MC.append(f"{array_name_MC} have undefined visibility marker")
            
print(count_CC)
print(count_CC_good)
print(problem_CC)
print('-----------------')
print(count_RC)
print(count_RC_good)
print(problem_RC)
print('-----------------')
print(count_AC)
print(count_AC_good)
print(problem_AC)
print('-----------------')
print(count_MC)
print(count_MC_good)
print(problem_MC)


