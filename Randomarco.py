import random
import tkinter as tk

#list of all the students
students = ['Abbotto', 'Anglieri', 'Briola', 'Budeanu', 'Cattai', 'Celant', 'De Negri', 'Du', 'Dubini', 'Gandolfi', 'Grimaldi', 'Licciardi', 'Maggiore', 'Mazzotti', 'Micara', 'Mihindukulasuria', 'Monteduro', 'Orlando', 'Piana', 'Ruiz', 'Stella', 'Tettamanti', 'Zola']

#length of the students list
length = len(students)

#Function to pick a random student and remove it from the student list
def random_picker():
    global length
    global input_field

    if length != 0 :
        #it gets from the input_field how many student to pick up
        n_to_repeat = input_field.get()

        # if the string of the input is blank than ask to enter a number
        if n_to_repeat == '':
            lbl_result["text"] = "You have entered nothing.\nPlease enter a number."

        # if the string of the input is a non-digit than ask to enter a number
        elif n_to_repeat.isdigit() == False:
            lbl_result["text"] = "You haven't entered a number.\nPlease enter a number."

        else:
            # pick a random number from 0 to the length of the student list
            num = random.randint(0, length-1)

            print('num: ' + str(num))

            # set the lbl_result text to the random student picked
            lbl_result["text"] = str(students[num])

            #remove the index of the student picked from the list
            students.pop(num)
            #refresh the students length
            length = len(students)
            
            print('students left: ' + str(length))
        
    else:
        #if the students are finished then display that there are no more students available
        lbl_result["text"] = 'There are no more students'
    



window = tk.Tk()
#lbl ask how many student must be picked
lbl_num_to_pick = tk.Label(text = 'How many students do you wanna pick?')

#input field where you can set how many students you want to be picked
input_field = tk.Entry()

# btn widget => when clicked it gets a random student
btn_picker = tk.Button(text="Pick", command=random_picker)

# lbl to display the random student picked
lbl_result = tk.Label()

# Display the btn and the lbl
lbl_num_to_pick.pack()
input_field.pack()
btn_picker.pack()
lbl_result.pack()

#Display the window
window.mainloop()