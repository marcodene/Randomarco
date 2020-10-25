import random
import tkinter as tk

students = ['Abbotto', 'Anglieri', 'Briola', 'Budeanu', 'Cattai', 'Celant', 'De Negri', 'Du', 'Dubini', 'Gandolfi', 'Grimaldi', 'Licciardi', 'Maggiore', 'Mazzotti', 'Micara', 'Mihindukulasuria', 'Monteduro', 'Orlando', 'Piana', 'Ruiz', 'Stella', 'Tettamanti', 'Zola']


def random_picker():
    # pick a random number from 0 to the length of the student list
    num = random.randint(0, len(students)-1)
    # set the lbl_result text to the random student picked
    lbl_result["text"] = str(students[num])



window = tk.Tk()


btn_picker = tk.Button(text="Random", command=random_picker)
lbl_result = tk.Label()

btn_picker.pack()
lbl_result.pack()

window.mainloop()