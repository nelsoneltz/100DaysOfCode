import tkinter

#Create window
window = tkinter.Tk()
# Change Title
window.title('First GUI')
# Set min size
window.minsize(width=500,height = 300)

# Label
my_label = tkinter.Label(text='writing some text',font=('Aria',24,'bold'))
my_label.pack()

# Button
def button_click():
    my_label.config(text=f'{input.get()}')

button = tkinter.Button(text='Click HERE!',command=button_click)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()




















# Keep window Open and running
window.mainloop()