from tkinter import*
root=Tk()
#create a canvas as child to root  window 
c=Canvas(root,bg='pink',height=400,width=300,cursor='pencil')

#create a lne in canvas
#id=c.create_line(50,50,200,50,150,width=4,fill='black')
c.pack()

root.mainloop()
