from tkinter import *


root = Tk()             
root.geometry('400x650')

canvas = Canvas(root, width=480, height=600) 
 

def draw_lines():
    canvas.create_line(300, 35, 300, 200, dash=(4, 2))
    

def drag(event):
    event.widget.place(x=event.x_root, y=event.y_root,anchor=CENTER)



canvas.bind("<B1-Motion>", drag)

btn1 = Button(root, text='line',  command=draw_lines)
btn2 = Button(root, text= 'Close', command=root.destroy)

btn1.pack(side=TOP)   
btn2.pack(side=TOP)


canvas.pack()
canvas.mainloop()