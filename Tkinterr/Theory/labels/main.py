from tkinter import *

window = Tk()

photo = PhotoImage(file='Tkinterr/Theory/labels/image.png')

label = Label(window, text='bro, do you even code?', font=('Arial', 40, 'bold'), 
              fg='green', bg='black', relief='raised', 
              bd='10', padx='20', pady='20', 
              image=photo, compound='bottom')
label.pack()
# label.place(x=100, y=100)

window.mainloop()