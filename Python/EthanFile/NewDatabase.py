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
                                problem_RC.append(f"{Clean_list[4]} contains other characters")
                            if all(c.isdigit() or c in "* ." for c in Clean_list[5]):
                                print(f"Clean_list[5] contains only numbers, *, and .")
                            else:
                                print(f"Clean_list[5] contains other characters")
                                problem_RC.append(f"{Clean_list[4]} contains other characters")
                                
                            
                        
                        else:
                            print('Null check fail')
                            problem_RC.append(f"{array_name_RC} have null value")
                    elif len(Clean_list)!=6:
                        print('wrong length')
                        problem_RC.append(f"{array_name_RC} please check value")
                else:
                    print('undefined connection')
                    problem_RC.append(f"{array_name_RC} have undefined Relationshiptype")

print('-----------------')
print(count_CC)
print(count_CC_good)
print(problem_CC)
Total_CC= count_CC_good+len(problem_CC)
print(Total_CC)
precentage_CC= count_CC_good/Total_CC*100
print(precentage_CC)

print('-----------------')
print(count_RC)
print(count_RC_good)
print(problem_RC)
Total_RC= count_RC_good+len(problem_RC)
print(Total_RC)
precentage_RC= count_RC_good/Total_RC*100
print(precentage_RC)
for item in problem_RC:
    print (item)
    if str(item) == "does not contain any of the symbols '<>v^'":
        print('good symbol')
    '''
    if str(item) == 'Not exsiting class name':
        print('Please check Realtionship target or source class ')
    elif str(item) == 'Wrong length for inhertance':
        print('Please check Your inhertance Realtionship compents')
    elif str(item) =='does not contain any of the symbols':
        print('Please check your label')
    elif str(item) =='is null':
        print('your label is empty')
    elif str(item) == 'undefined realtionshiptype':
        print('Please check your relationshiptype')
'''



