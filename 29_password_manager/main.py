from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','?','#','$','%','&','(',')','*','+','=','-']

    number_letters = random.randint(8,10)
    number_numbers = random.randint(2,4)
    number_symbols = random.randint(2,4)

    password_numbers = [random.choice(letters) for _ in range(number_letters)]
    password_letters = [random.choice(numbers) for _ in range(number_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(number_symbols)]
    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password_word =''.join(password_list)
    password_input.delete(0,END)
    password_input.insert(string=password_word,index=0)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def adicionar():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    data = website + ' | ' + username + ' | ' + password + '\n'
    if website == '' or username == '' or password == '':
        messagebox.showerror(title='Alert',message="Don't leave blank fields")
    else:
        confirmation = messagebox.askokcancel(title=website, message=f"These are the detais entered: \nEmail: {username}\nPassword: {password}\n Is it ok to save?")

        if confirmation:
            with open('data.txt', 'a') as file:
                file.write(data)
            website_input.delete(0,END)
            password_input.delete(0,END)
            pyperclip.copy(password)
            
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

# CANVAS
canvas = Canvas(height=200,width=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1,row= 0)

# 3 ENTRY
# miles_input = Entry(width=10)

website_input = Entry()
website_input.grid(column=1,row=1,columnspan=2,sticky="EW")
website_input.focus()

username_input = Entry()
username_input.grid(column=1,row=2,columnspan=2,sticky="EW")
username_input.insert(0,'your_email@email.com')

password_input = Entry()
password_input.grid(column=1,row=3,sticky="EW")

# 3 LABELS
website_label = Label(text='Website:')
website_label.grid(column=0,row=1)

username_label = Label(text='Email/Username:')
username_label.grid(column=0,row=2)

password_label = Label(text='Password:')
password_label.grid(column=0,row=3)

# 2 BUTTONS
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2,row=3,sticky="EW")

add_button = Button(text='Add', command = adicionar,width=35)
add_button.grid(column=1,row=4,columnspan=2,sticky="EW")















window.mainloop()