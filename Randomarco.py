import random
import tkinter as tk

students = ['Abbotto', 'Anglieri', 'Briola', 'Budeanu', 'Cattai', 'Celant', 'De Negri', 'Du', 'Dubini', 'Gandolfi', 'Grimaldi', 'Licciardi', 'Maggiore', 'Mazzotti', 'Micara', 'Mihindukulasuria', 'Monteduro', 'Orlando', 'Piana', 'Ruiz', 'Stella', 'Tettamanti', 'Zola']


def random_picker():
    num = random.randint(0, len(students)-1)
    lbl_result["text"] = str(students[num])

window = tk.Tk()


btn_picker = tk.Button(text="Random", command=random_picker)
lbl_result = tk.Label()

btn_picker.pack()
lbl_result.pack()

window.mainloop()