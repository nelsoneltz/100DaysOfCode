from tkinter import *

def miles_to_km():
    miles= float(miles_input.get())
    km = round(miles * 1.609,2)
    kilometer_result_label.config(text=f'{km}')


#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=300)
window.config(padx=20,pady=20)

# 1 entry

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# 4 labels
miles_label = Label(text= 'Miles')
miles_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text='0')
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text='Km')
kilometer_label.grid(column=2, row=1)

# 1 button

calculate = Button(text='Calculate',command=miles_to_km)
calculate.grid(column=1, row=2)








window.mainloop()