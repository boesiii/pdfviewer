from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os

# init
root = Tk()
root.geometry("630x700+400+100")
root.title("PDF viewer")
root.configure(bg="white")

# main
def browseFiles():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="select pdf file",
                                        filetype=(("PDF File",".pdf"),
                                                  ("PDF File",".PDF"),
                                                  ("All file",".txt")
                                                  ))
    v1=pdf.ShowPdf()
    v2=v1.pdf_view(root,pdf_location=open(filename,"r"),width=77,height=100)
    v2.pack(pady=(0,0))
    
def line(event):
    # w.create_line(0, 0, event.x, event.y)
    # print (event.x,event.y)
    
    label['text'] = (str(event.x),str(event.y))
    
def bind_line():
    root.bind("<Button-1>", line)
    
btn_open = Button(root,text="open",command=browseFiles,width=40,
        font="arial 20",bd=4)
btn_open.pack()
        
btn_measure = Button(root,text="Measure",command=bind_line,width=40,
                 font="arial 20",bd=4)
btn_measure.pack()

label = Label( root, text="Text", width=40,font="arial 20",bd=4)
label.pack()
 
root.mainloop()
