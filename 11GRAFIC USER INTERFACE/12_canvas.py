from tkinter import*
root=Tk()

canvas_width=300
canvas_height=300
root.geometry(f"{canvas_width}x{canvas_height}")
root.title('BIRJU KUMAR JALVANSHI')
#create canvas:-
canvas_widget=Canvas(width=canvas_width,height=canvas_height)
canvas_widget.pack()

canvas_widget.create_line(0,0,300,300)
canvas_widget.create_rectangle(2,5,300,300,fill='blue')


canvas_widget.create_oval(2,5,300,300)

root.mainloop()