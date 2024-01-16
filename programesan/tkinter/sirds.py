from tkinter import *
tests = Tk()
tests.geometry("200x200")
tests.title('<3')
c = Canvas(tests,bg = "#ed9bae",height = "200") 
oval = c.create_oval((85,10,165,90), outline = "pink",fill = "pink")
oval = c.create_oval((30,10,110,90), outline = "pink",fill = "pink")
points = [34, 69, 100, 142, 161, 69]
poly = c.create_polygon(points, outline = "pink",fill='pink')
text = c.create_text((100,160),text='sirds',fill='white',font=( 14))
c.pack()
tests.mainloop()