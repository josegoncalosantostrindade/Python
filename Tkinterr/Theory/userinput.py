from tkinter import *

window = Tk()

def submit():
    username = entry.get()
    print('Hello ' + username)

def delete():
    entry.delete(0, END) # this deletes the line of text

def backspace():
    entry.delete(len(entry.get()) - 1, END) # delete last character


submit = Button(window, text='Submint', command=submit)
submit.pack(side='right')

delete = Button(window, text='Delete', command=delete)
delete.pack(side='right')

backspace = Button(window, text='Backspace', command=backspace)
backspace.pack(side='right')

entry = Entry()
entry.config(font=('Times', 50))
entry.config(bg='#111111')
entry.config(fg='#00ff00')
# entry.insert(0, 'Spongebob')
# entry.config(state='disabled')
entry.config(width=10)
# entry.config(show='*') # hidden input (ex: password)
entry.pack()

window.mainloop()