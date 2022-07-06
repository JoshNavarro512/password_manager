from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip



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


    if len(website) == 0 or len(password) ==0:
        empty_field = messagebox.showerror(title="ERROR", message="Please fill out all fields")
    else:
        validate_data = messagebox.askokcancel(title=website, message=f"These are the deatails entered: \n"
                                            f" Email: {email_username}\n Password: {password}\n"
                                            f"Is it ok to save.")
        if validate_data:
            with open("password_log.txt", "a+") as password_file:
                password_file.write(f"Website: {website} Email/Username:  {email_username} Password:  {password} \n")
                web_entry.delete(0 ,"end")
                pass_entry.delete(0,"end")


    

   



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


# Label for Website input
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
# Website Entry 
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)


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


# Add button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)







window.mainloop()

