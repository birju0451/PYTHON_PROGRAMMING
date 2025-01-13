import tkinter as tk
def submit():
    text = entry.get()  # Get the text entered in the entry widget
    label.config(text=text)  # Update the label text with the text from the entry
    print(text)

# Create a function to be called when the button is clicked
# Create the main application window
root = tk.Tk()
root.title("Entry and Label Example")

# Create an entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a label widget
label = tk.Label(root, text="Label")
label.pack(pady=10)

# Create a button widget
def submit():
    text = entry.get()  # Get the text entered in the entry widget
    label.config(text=text)  # Update the label text with the text from the entry
    print(text)

button = tk.Button(root, text="Submit", command=submit)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
