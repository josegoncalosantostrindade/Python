from tkinter import *

def display():
    if x.get() == 1 and y.get() == 0:
        print('I like pyhton!')
    elif x.get() == 0 and y.get() == 1:
        print('I like linux!')
    elif x.get() == 1 and y.get() == 1:
        print('I like both pyhton and linux!')
    else:
        print('I do not like either')


window = Tk()
x = IntVar()
y = IntVar()

checkbox1 = Checkbutton(window, text='Python', variable=x, onvalue=1, offvalue=0, command=display)
checkbox1.pack()
checkbox1.config(font=('Arial', 20)) # this changes the font
checkbox1.config(fg='#0000ff') # foreground color
checkbox1.config(bg='#000000') # background color
checkbox1.config(activeforeground='#0000ff')
checkbox1.config(activebackground='#000000')
photo1 = PhotoImage(file='Tkinterr/Theory/checkboxes/python_icon.png')
checkbox1.config(image=photo1, compound='left') # sets image to photo image
checkbox1.config(padx=25, pady=10)
checkbox1.config(anchor='w') # this anchors widget to relative cardinal direction

checkbox2 = Checkbutton(window, text='Linux', variable=y, onvalue=1, offvalue=0, command=display)
checkbox2.pack()
checkbox2.config(font=('Arial', 20)) # this changes the font
checkbox2.config(fg='#0000ff') # foreground color
checkbox2.config(bg='#000000') # background color
checkbox2.config(activeforeground='#0000ff')
checkbox2.config(activebackground='#000000')
photo2 = PhotoImage(file='Tkinterr/Theory/checkboxes/linux_icon.png')
checkbox2.config(image=photo2, compound='left') # sets image to photo image
checkbox2.config(padx=25, pady=10)
checkbox2.config(anchor='w')

window.mainloop()