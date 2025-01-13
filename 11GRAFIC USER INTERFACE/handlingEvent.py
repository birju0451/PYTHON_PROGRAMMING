from tkinter import*

def harry(event):
    print(f"you click on the button at {event.x},{event.y}")


root=Tk()
root.title("event in tkinter")
root.geometry("600x300")
widget=Button(root,text='click me please')
widget.pack()

widget.bind('<Button-1>',harry)
widget.bind('<Double-1>',quit)

root.mainloop()