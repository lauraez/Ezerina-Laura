from tkinter import *
tests = Tk()
tests.geometry("200x200")
tests.title('<3')
c = Canvas(tests,bg = "black",height = "200",width='200') 
arc = c.create_oval((85,10,165,90), outline = "pink",fill = "pink")
#                    x1 y1 x2  y2
arc = c.create_oval((30,10,110,90), outline = "pink",fill = "pink")
#                    x1 y1 x2  y2
points = [34, 69, 100, 142, 161, 69]
#         x1  y1  x2   y2   x3   y3
poly = c.create_polygon(points, outline = "pink",fill='pink')
text = c.create_text((100,160),text='Sirsniņa',fill='white',font=(15))
c.pack()
tests.mainloop()