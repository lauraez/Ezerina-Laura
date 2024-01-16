from tkinter import *
from random import *
window = Tk()
window.title('It is them cats')
size = 900
c = Canvas(window,width=size,height=size)
c.pack()
while True:
    color = choice(['#ed9bae','#791644','#d5a6bd'])
    x0 = randint(0,size)
    y0 = randint(0,size)
    randomsize = randint(0,size/5)
    
    #c.create_oval((x0,y0,x0+randomsize,y0+randomsize),fill = color)
    #c.create_text((x0+randomsize,y0+randomsize),text = '|ᐠ-ꞈ-ᐟ|')
    window.update()

mainloop()