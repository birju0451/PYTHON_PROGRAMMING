from tkinter import *

root = Tk()
root.geometry('1200x900')  # width x height

# Load the image
photo = PhotoImage(file='vv.png')

# Create a label and display the image
label1 = Label(image=photo)
label1.pack()

root.mainloop()
