
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = []
password = ""
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_list=[random.choice(letters) for char in range(nr_letters)]
    password_list+=[random.choice(symbols) for _ in range(nr_symbols)]
    password_list+=[random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)



    password = [char for char in password_list]
    passkey = "".join(password)
    password_entry.delete(0, END)
    password_entry.insert(0,passkey)
    pyperclip.copy(passkey)


    def button_pressed():
        window.after(2000, copy_label.destroy)

    copy_label = Label(text="Password Copied", font=("Arial", 8))
    copy_label.grid(row=5, column=1)
    button_pressed()
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web_name=web_entry.get()
    email=email_entry.get()
    password_name=password_entry.get()
    new_data={
        web_name:{"email":email,"password":password_name}
    }
    if web_name=="" or email=="" or password_name=="":
        messagebox.showerror("Oops","Please enter all the details ")
    else:
        is_ok = messagebox.askokcancel(web_name, f"These are the details entered \n"
                                                 f"email:{email}\n"
                                                 f"password:{password_name}\n"
                                                 f"is it ok save?")
        if is_ok:
            try:
                with open('Data.json', 'r') as f:
                    data = json.load(f)
                    data.update(new_data)
                with open('Data.json', 'w') as f:
                    json.dump(data, f, indent=4)
            except FileNotFoundError:
                with open("Data.json","w") as file:
                    json.dump(new_data, file, indent=4)
            finally:
                web_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

def search():
    web_name=web_entry.get()
    try:
        with open('Data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Oops","file not found ,first add a data file")
    else:
        if web_name in data:
            web_data=data[web_name]
            messagebox.showinfo(web_name,f"email:{web_data["email"]}\npassword:{web_data["password"]}\nPassword Copied to the Clipboard")
            pyperclip.copy(web_data["password"])
        else:
            messagebox.showerror("Oops","User details not found ")
    finally:
        web_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(500, 425)
window.config(padx=50, pady=50)
logo = PhotoImage(file = "logo.png")
canvas = Canvas(window, width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
web_label = Label(window, text="Website:",font=("Arial", 12))
web_label.grid(row=1, column=0)
email_label=Label(window, text="Email/Username:",font=("Arial", 12))
email_label.grid(row=2, column=0)
password_label=Label(window, text="Password:",font=("Arial", 12))
password_label.grid(row=3, column=0)
web_entry=Entry(width=35,bg="white")
web_entry.grid(row=1, column=1)
email_entry=Entry(width=56,bg="white")
email_entry.grid(row=2, column=1,columnspan=2)
password_entry=Entry(width=35,bg="white")
password_entry.grid(row=3, column=1)
password_button=Button(text="Generate Password",bg="white",relief="ridge",width=16,command=generate_password)
password_button.grid(row=3, column=2)
add_button=Button(text="Add",width=48,bg="white",relief="ridge",command=add)
add_button.grid(row=4, column=1,columnspan=2)
websearch_button=Button(text="Search",bg="white",relief="ridge",width=16,command=search)
websearch_button.grid(row=1, column=2)















window.mainloop()