from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def func():
    print('HOOOORRRAY')
# ---------------------------- SAVE PASSWORD ------------------------------- #
def adicionar():
    print('added')
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

username_input = Entry()
username_input.grid(column=1,row=2,columnspan=2,sticky="EW")

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
generate_password_button = Button(text='Generate Password', command=func)
generate_password_button.grid(column=2,row=3,sticky="EW")

add_button = Button(text='Add', command = adicionar,width=35)
add_button.grid(column=1,row=4,columnspan=2,sticky="EW")















window.mainloop()