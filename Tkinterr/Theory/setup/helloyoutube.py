from tkinter import *

window = Tk() # instantiate an instance of window
window.geometry('420x420')
window.title('Gonçalo first GUI program')

icon = PhotoImage(file='Tkinterr/Theory/setup/obsidian.png')
window.iconphoto(True, icon)
window.config(background='black')

window.mainloop() # place window on computer screen, listen for events