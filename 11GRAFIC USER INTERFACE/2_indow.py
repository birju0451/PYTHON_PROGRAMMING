from tkinter import*
#create a top level window
root=Tk()
#set window tittle:-
root.title('my window')

#set window size
root.geometry("400x300")#breadth*length

#set window icon
root.wm_iconbitmap('image.png')

#display window and weigt for an event 
root.mainloop()