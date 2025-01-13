from tkinter import*
root=Tk()
root.geometry("800x400")
root.title("canvas")
canvas_widget=Canvas(root,width=700,height=400)
canvas_widget.pack()
#from here you can draw diagram what ever you want to draw 

canvas_widget.create_line(0,0,800,200)
canvas_widget.create_rectangle(5,5,700,300,fill='silver')
canvas_widget.create_text(200,200,text="rectangle")
canvas_widget.create_oval(5,5,700,300,fill='gold')

root.mainloop()