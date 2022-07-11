from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)


    password = "".join(password_list)
    

    pass_entry.insert(0, password)
    pyperclip.copy(password)





# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = web_entry.get()
    password = pass_entry.get()
    email_username = email_entry.get()
    new_data = { 
        website:{
            "email": email_username, 
            "password": password, 

        }
    }


    if len(website) == 0 or len(password) ==0:
        empty_field = messagebox.showerror(title="ERROR", message="Please fill out all fields")
    else:
        try:
            with open("password_log.json", "r") as password_file:
                data = json.load(password_file)
        except:
            with open("password_log.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            data.update(new_data)

            with open("password_log.json", "w") as password_file:
                json.dump(data, password_file, indent=4)

        finally:
            web_entry.delete(0 ,"end")
            pass_entry.delete(0,"end")


# --------------------------Search function --------------------------- #

def find_password():
    website = web_entry.get()
    try:
        with open("password_log.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


# Label for Website input
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
# Website Entry 
web_entry = Entry(width=21)
web_entry.grid(column=1, row=1)


# Label for email/username input
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
# email Entry 
email_entry = Entry(width=35)
email_entry.insert(END, "exampleEmail@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)


# Password Label 
pass_label = Label(text=("Password:"))
pass_label.grid(column=0, row=3)
# Password entry
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)


#generate Password Button 
gen_pass = Button(text=("Generate Password"), command=generate_password)
gen_pass.grid(column=2, row=3)


#Search Button 
search_button = Button(text=("Search"), width=13, command=find_password)
search_button.grid(column=2, row=1)


# Add button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)







window.mainloop()

