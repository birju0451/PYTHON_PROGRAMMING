from tkinter import*
root=Tk()
root.geometry("430x300")
def hello():
    print("birju kumar")

frame=Frame(root,borderwidth=6,bg='blue',relief=SUNKEN)
frame.pack(side=LEFT,anchor=NW)

b1=Button(frame,fg='blue',text='stop',command=hello)
b1.pack(side=LEFT)
root.mainloop()