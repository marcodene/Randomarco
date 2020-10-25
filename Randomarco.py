import random
import tkinter as tk

#list of all the students
students = ['Abbotto', 'Anglieri', 'Briola', 'Budeanu', 'Cattai', 'Celant', 'De Negri', 'Du', 'Dubini', 'Gandolfi', 'Grimaldi', 'Licciardi', 'Maggiore', 'Mazzotti', 'Micara', 'Mihindukulasuria', 'Monteduro', 'Orlando', 'Piana', 'Ruiz', 'Stella', 'Tettamanti', 'Zola']

#length of the students list
length = len(students)

#Function to pick a random student and remove it from the student list
def random_picker():
    global length
    
    if length != 0 :
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
        lbl_result["text"] = 'There are no more students'
    



window = tk.Tk()

# btn widget => when clicked it gets a random student
btn_picker = tk.Button(text="Random", command=random_picker)

# lbl to display the random student picked
lbl_result = tk.Label()

# Display the btn and the lbl
btn_picker.pack()
lbl_result.pack()

#Display the window
window.mainloop()