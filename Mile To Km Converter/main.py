from tkinter import *


def converter():
    input = float(mile_input.get()) * 1.6
    km_label.config(text=input)


window = Tk()
window.title("Mile To Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

mile_input = Entry(width=20)
mile_input.grid(row=0, column=1)

mile_label = Label(width=20)
mile_label.grid(row=0, column=2)
mile_label["text"] = "Miles"

label = Label(width=20)
label.grid(row=1, column=0)
label["text"] = "is equal to"

km_label = Label(width=20)
km_label.grid(row=1, column=1)
km_label["text"] = 0

km_label1 = Label(width=20)
km_label1.grid(row=1, column=2)
km_label1["text"] = "Km"

button = Button(width=20, text="Calculate", command=converter)
button.grid(row=2, column=1)

window.mainloop()