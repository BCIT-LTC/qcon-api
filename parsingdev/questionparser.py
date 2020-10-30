my_path = os.path.abspath('')
path = os.path.join(my_path, "test.txt")


with open(path, newline='') as f:
#     test = f.readlines() 
    test = f.read().splitlines()
    full_list = []  # string    
    track_question = 0 # to track number of questions detected    
   
    question_block = []
    
    for line in test:        
              
        if len(line) > 0:
            
            current_string = line.lstrip()                      
#             print(current_string)  
#             print(full_list)
            
            if current_string.startswith(tuple('0123456789')):
                print("current Question: " + str(track_question+1))                
                q_index = re.search(r'^(\d+)s{0,}[\)|\.]{1}\s{0,}', current_string)

#                 print(q_index.group(0)) # full match, numbering and delimeters    
#                 print(q_index.group(1)) # just the number
    
                # If match is found then check if its a new question.
                # Else treat it as content for the current question.
                if q_index != None:               
                    
                    #extra Check to make sure the question is incremental relative to the previous question. 
                    #It assumes that the questions in the doc are numbered correctly
#                     if int(q_index.group(1)) == track_question + 1:
#                         print(q_index)
#                         print(current_string)
#                         print(current_string.replace(q_index.group(0),""))
                        
                    if track_question != 0:                
                        full_list.append(question_block)    
                    question_block = []    
                    track_question += 1 
                    question_block.append(current_string.replace(q_index.group(0),""))                                           
#                     else: 
#                         print(current_string) 
#                         question_block.append(current_string)
                else:
                    question_block.append(current_string)
                    print(current_string)

            else:
                question_block.append(current_string)
                print(current_string)

    func.my_function()
    full_list.append(question_block) 
    print(full_list)
    print(track_question)