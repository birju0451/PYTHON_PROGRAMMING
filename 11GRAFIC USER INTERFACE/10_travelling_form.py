from tkinter import*
def getvals():
  print('its work')
root=Tk()
root.geometry("400x250")
#heading for gui:-
l1=Label(root,text="WELCOME TO BIRJU TRAVELS",fg="black",font="comiccsansms,14,bold",pady=20)
l1.grid(row=0,column=3)
#text for our form
name=Label(root,text='name')
phone=Label(root,text='phone')
gender=Label(root,text='gender')
emergency=Label(root,text='emergency')
paymentmode=Label(root,text='paymentmode')
#pack text for our form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

#tkinter variable for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

#entry for our form
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)
#packing the entry
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

#cheakbox
foodservice=Checkbutton(text='want to prebook your meals')
foodservice.grid(row=6,column=3)

#button & packing it and assining it a command 
Button(text='submit your form to birju travels',command=getvals).grid(row=7,column=3)

root.mainloop()
