from tkinter import *

window = Tk()
window.title("Tkinter GUI Intro")
window.minsize(500,300)


label = Label(text="New Label")
label.pack()

input = Entry()
input.pack()

def hit_me():
    new_label = input.get()
    label.config(text=new_label)

button = Button(text="Click Me",command=hit_me)
button.pack()




window.mainloop()