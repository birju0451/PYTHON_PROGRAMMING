from tkinter import *

root = Tk()

# Here you can write your logic
root.title("birju")

root.geometry("300x200")
root.minsize(200, 100)  # Corrected method to set minimum size
root.maxsize(1200,500)  #first is width and second is height

label1=Label(text='my first program')
label1.pack()
root.mainloop()
