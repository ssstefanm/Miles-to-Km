from tkinter import *


def button_clicked():
    # replaces the text from the label with whatever u write in the entry
    kilometers = int(miles.get()) * 1.609344
    print(kilometers)
    km.config(text=kilometers)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=100, pady=200)
# Label
my_label1 = Label(text="is equal to", font=("Arial", 15, "normal"))
my_label1.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Arial", 15, "normal"))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 15, "normal"))
km_label.grid(column=2, row=1)
# my_label["text"] = "New Text"
# my_label.config(text="Newer Text")
km = Label(text="0", font=("Arial", 10, "normal"))
km.grid(column=1, row=1)
# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=10,)


# entry
miles = Entry(width=10)
miles.grid(column=1, row=0)


window.mainloop()
