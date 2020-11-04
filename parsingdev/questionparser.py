import os.path
import re
    
    
def separate_by_number(lines):
    full_list = []
    question_block = []

    print("hell")
    for line in lines:
        if len(line) > 0:

            current_string = line.lstrip()
#             print(current_string)
#             print(full_list)

            if current_string.startswith(tuple('0123456789')):
                q_index = re.search( r'^(\d+)s{0,}[\)|\.]{1}\s{0,}', current_string)

#                 print(q_index.group(0)) # full match, numbering and delimeters
#                 print(q_index.group(1)) # just the number

                # If match is found then check if its a new question.
                # Else treat it as content for the current question.
                if q_index != None:

                    # extra Check to make sure the question is incremental relative to the previous question.
                    # It assumes that the questions in the doc are numbered correctly
#                     if int(q_index.group(1)) == track_question + 1:
#                         print(q_index)
#                         print(current_string)
#                         print(current_string.replace(q_index.group(0),""))

                    if len(question_block) != 0:
                        full_list.append(question_block)

                    question_block = []
                    question_block.append(
                        current_string.replace(q_index.group(0), ""))
#                     else:
#                         print(current_string)
#                         question_block.append(current_string)
                else:
                    question_block.append(current_string)
                    print(current_string)

            else:
                question_block.append(current_string)
                print(current_string)

    full_list.append(question_block) 
    print(full_list)
    print(len(full_list))
    
# ================================================   
    
def separate_by_newline(lines):
    full_list = [] # Questions list
    question_block = [] # temp question holder
    separator_found = False #detect newline

    for index, line in enumerate(lines):
        #print(line)
        current_line = line.lstrip()

        # If newline detected, set flag to true
        # else set it to false
        if len(current_line) == 0:
          separator_found = True
        else:
          separator_found = False

        # Add question block to the list when current line is new line
        # If not new line, add line to the question block
        # this will result in False: separator_found == True & len(question_block) > 0
        if separator_found == True:
          if len(question_block) > 0:
            full_list.append(question_block)
            question_block = []
          # print("_______________________________________________")
        elif separator_found == False:
          question_block.append(current_line)
          # print(current_line)
        
        # Add the last question block to the question list if the last line is not a new line
        if index == len(lines)-1 :
          if len(question_block) > 0:
            full_list.append(question_block)
        
    print(" ")
    print(full_list)
    print(len(full_list))
    
    
    
# ================================================    

my_path = os.path.abspath('')
path = os.path.join(my_path, "test.txt")

with open(path, newline='') as f:
#     test = f.readlines() 
    lines = f.read().splitlines()
    full_list = []  # string         
    question_block = []
        
    
    # separate_by_number(lines)
    
    # print("++++++++++++++++++++++")
    
    separate_by_newline(lines)    