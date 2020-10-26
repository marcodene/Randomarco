import random
import tkinter as tk

default = ['Abbotto', 'Anglieri', 'Briola', 'Budeanu', 'Cattai', 'Celant', 'De Negri', 'Du', 'Dubini', 'Gandolfi', 'Grimaldi', 'Licciardi', 'Maggiore', 'Mazzotti', 'Micara', 'Mihindukulasuria', 'Monteduro', 'Orlando', 'Piana', 'Ruiz', 'Stella', 'Tettamanti', 'Zola']

#list of all the students
students = ['Abbotto', 'Anglieri', 'Briola', 'Budeanu', 'Cattai', 'Celant', 'De Negri', 'Du', 'Dubini', 'Gandolfi', 'Grimaldi', 'Licciardi', 'Maggiore', 'Mazzotti', 'Micara', 'Mihindukulasuria', 'Monteduro', 'Orlando', 'Piana', 'Ruiz', 'Stella', 'Tettamanti', 'Zola']
#length of the students list
length = len(students)

prev_stud = []
prev_stud_picked = ''

proced = False

first_time = True

undo_one_time = False

prev_txt = ''

curr_studs = ''

#Function to pick a random student and remove it from the student list
def random_picker():
    global length
    global input_field
    global prev_txt
    global proced
    global prev_stud_picked
    global first_time
    global undo_one_time
    global curr_studs

    #You can't undo two times in a row
    undo_one_time = False

    #save the students picked in a var
    prev_stud_picked = lbl_result["text"]
    print('stud_picked: ' + prev_stud_picked)

    #Clean the lbl_result
    lbl_result["text"] = ''
    prev_txt = ''

    if length != 0 :
        #it gets from the input_field how many student to pick up
        n_to_repeat = input_field.get()

        # if the string of the input is blank than ask to enter a number
        if n_to_repeat == '':
            lbl_result["text"] = "You have entered nothing.\nPlease enter a number."

        # if the string of the input is a non-digit than ask to enter a number
        elif n_to_repeat.isdigit() == False:
            lbl_result["text"] = "You haven't entered a number.\nPlease enter a number."

        # if the string of the input is a too high than ask to enter a minor number. This runs only if the user hasn't already insert an available number
        elif int(n_to_repeat) > length - 1 and proced == False:
            lbl_result["text"] = "There aren't enough students in the class.\nPlease enter a minor number."
           

        else:
            proced = True

            #This runs if the user has already insert an available number, but it is higher than the students left
            if int(n_to_repeat) > length - 1:
                #it display just the students left
                for i in range (length):
                    if prev_txt == '':
                        txt = students[i]
                    else:
                        txt = f'{prev_txt}, {students[i]}'

                    prev_txt = txt

                lbl_result["text"] = f"There is not another group of {n_to_repeat} people.\nThere is a group of {length} people\n{txt}"

            else:
                for i in range(int(n_to_repeat)):
                    # pick a random number from 0 to the length of the student list
                    num = random.randint(0, length-1)

                    '''print('num: ' + str(num))'''
                    
                    # set the lbl_result text to the random student picked
                    if prev_txt == '':
                        lbl_result["text"] = str(students[num])
                    else:
                        lbl_result["text"] = f'{prev_txt}, {str(students[num])}'

                    prev_txt = lbl_result["text"]
                    

                    #remove the index of the student picked from the list
                    students.pop(num)
                    #refresh the students length
                    length = len(students)
                    
                    '''print('students left: ' + str(length))'''

                curr_studs = lbl_result["text"]
                print(curr_studs)

            lbl_stud_left["text"] = f'There are {length} students left.'

            if first_time == True:
                prev_stud_picked = lbl_result["text"]
                print('stud_picked: ' + prev_stud_picked)

                first_time = False

        
    else:
        #if the students are finished then display that there are no more students available
        lbl_result["text"] = 'There are no more students'
    

def undo():
    global prev_stud
    global prev_stud_picked
    global length
    global students
    global undo_one_time
    global curr_studs

    print('curr_studs: ' + curr_studs)

    if undo_one_time:
        lbl_result["text"] = "You can't undo anymore."
    else:
        stud_to_add = curr_studs.split(", ")
        print(stud_to_add)

        for i in stud_to_add:
            #Check if the stud_to_add is inside the default array. This is made to prevent that you add "You can't undo anymore." or whatever is diplayed in the lbl_result
            if i in default:
                students.append(i)
                print(i)
            else:
                print('testa di cazzo')
            
            
        print(students)
        length = len(students)
        
        
        print('length: ' + str(length))

        lbl_stud_left["text"] = f'There are {length} students left.'
        lbl_result["text"] = prev_stud_picked

    #You can't undo two times in a row
    undo_one_time = True



def reset():
    global default
    global students
    global length

    students = default
    
    length = len(students)

    lbl_stud_left["text"] = f'There are {length} students left.'
    lbl_result["text"] = ""


window = tk.Tk()
window.title('RANDOMARCO')
window.minsize(300, 100)

#lbl ask how many student must be picked
lbl_num_to_pick = tk.Label(text = 'How many students do you wanna pick?')

#input field where you can set how many students you want to be picked
input_field = tk.Entry()
input_field.insert(0, 'Insert a number:')

#lbl say the num of students left
lbl_stud_left = tk.Label(text = f'There are {length} students left.')

# btn widget => when clicked it gets a random student
btn_picker = tk.Button(text="Pick", command=random_picker)

# lbl to display the random student picked
lbl_result = tk.Label()

#Undo btn
btn_undo = tk.Button(text="Undo", command=undo)

#Reset btn
btn_reset = tk.Button(text="Reset", command=reset)

# Display the btn and the lbl
lbl_num_to_pick.pack()
input_field.pack()
lbl_stud_left.pack()
btn_picker.pack()
lbl_result.pack()
btn_undo.pack(side=tk.LEFT, padx= 10, pady = 5)
btn_reset.pack(side=tk.RIGHT, padx= 10, pady = 5)

#Display the window
window.mainloop()
