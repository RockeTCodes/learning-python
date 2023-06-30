from tkinter import *
from passwordgen import passwordgen
from tkinter import messagebox
import pyperclip

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas = Canvas(height=200,width=200,highlightthickness=0)
image = PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

def addpass():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if not website or not email or not password:
        messagebox.showerror(title="Error",message="Please fill all the details.")
    else:    
        is_ok = messagebox.askokcancel(title=website,message=f"You have entered following details.\nEmail: {email}\nPassword:{password}.\nDo you want to save this?")
        if is_ok:
            with open("data.txt","a") as file:
                file.write(f"{website} | {email} | {password}\n")
        website_input.delete(0,END)
        password_input.delete(0,END)
    
def generate_pass():
    password = passwordgen()
    password_input.delete(0,END)
    password_input.insert(0,password)
    pyperclip.copy(password)



#labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


#inputs
website_input = Entry(width=58)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()

email_input = Entry(width=58)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"kaushalbhardwaj1125@gmail.com")

password_input = Entry(width=33)
password_input.grid(row=3,column=1)


#buttons
genpass_button = Button(text="Generate Password",highlightthickness=0,width=20,command=generate_pass)
genpass_button.grid(row=3,column=2)

addpass_button = Button(text="Add",highlightthickness=0,width=49,command=addpass)
addpass_button.grid(row=4,column=1,columnspan=2)

window.mainloop()