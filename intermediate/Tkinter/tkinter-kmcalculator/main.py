from tkinter import *


window = Tk()
window.title("Tkinter GUI Intro")
window.minsize(300,100)

label1 = Label(text="Equals to: ")
label1.grid(column=0,row=1)

input = Entry()
input.grid(column=1,row=0)

label2 = Label(text="Miles")
label2.grid(column=2,row=0)


label3 = Label(text="0")
label3.grid(column=1,row=1)


label4 = Label(text="Km")
label4.grid(column=2,row=1)

def calculate():
    
    if input.get():
        result = int(input.get())*1.6
        print(result)
        label3.config(text=result)
    else:
        label3.config(text="Please provide a valid input.")

 

button = Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)

window.mainloop()