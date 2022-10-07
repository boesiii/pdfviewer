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
    
def measure(event):
# def printcoords(self, event):
    # btn1.bind("<Button-1>", measure)
    print ('measure button')
    # x, y = event.x, event.y
    print("Mouse position: (%s %s)" % (event.x, event.y))
    # pass
    

                                                  
Button(root,text="open",command=browseFiles,width=40,
        font="arial 20",bd=4).pack()
        
btn1 = Button(root,text="Measure",width=40, font="arial 20",bd=4)
btn1.bind("<Button-1>", measure)
btn1.pack()

        
# Button(root,text="Measure",command=measure,width=40,
        # font="arial 20",bd=4).pack()
        
root.mainloop()
