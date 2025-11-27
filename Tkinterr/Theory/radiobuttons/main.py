from tkinter import *

food = ['pizza', 'hamburger', 'hotdog']

def order():
    if x.get() == 0:
        print('You ordered a pizza!')
    elif x.get() == 1:
        print('You ordered a hamburger!')
    elif x.get() == 2:
        print('You ordered a hotdog!')
    else:
        print('huh?')


window = Tk()
window.geometry('400x200')

pizzaImage = PhotoImage(file='Tkinterr/Theory/radiobuttons/pizza.png')
hamburgerImage = PhotoImage(file='Tkinterr/Theory/radiobuttons/hamburger.png')
hotdogImage = PhotoImage(file='Tkinterr/Theory/radiobuttons/hotdog.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window, text=food[index], variable=x, value=index, 
                              padx=20, font=('Impact', 35), image=foodImages[index],
                              compound='left', # indicatoron=0 # eliminate circle indicators
                              command=order)
    radiobutton.pack(anchor=W)

window.mainloop()