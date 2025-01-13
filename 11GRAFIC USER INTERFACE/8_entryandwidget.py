from tkinter import*

def get_val():
    print(uservalue.get())
    print(passvalue.get())

root=Tk()
root.geometry("600x300")

user=Label(root,text='username')
password=Label(root,text='password')
user.grid()
password.grid(row=1)

# Variable class in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar
uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

button=Button(root,text="submit",command=get_val)
button.grid(row=3)

root.mainloop()