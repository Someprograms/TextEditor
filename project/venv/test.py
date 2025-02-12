import tkinter as tk
import tkinterDnD as tkinterDnD

root = tkinterDnD.Tk()

# Create a frame that will hold other widgets

# Configure the column and row of the root window to expand
root.grid_columnconfigure(0, weight=1)  # Allow the frame to expand horizontally
root.grid_rowconfigure(0, weight=1)     # Allow the frame to expand vertically

# Add a label inside the frame
label = tk.Canvas(root, background='black')
label.grid(row=0, column=0, sticky="nsew")  # sticky="nsew" makes the label expand in all directions

# Allow the root window to be resized
root.resizable(True, True)

root.mainloop()
