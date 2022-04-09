import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

menubar = tk.Menu(root)
root.config(menu=menubar)

menu = tk.Menu(menubar, tearoff=0)
var1 = tk.StringVar()
for color in ("blue", "red", "yellow"):
    menu.add_radiobutton(label=color, variable=var1, value=color)
menubar.add_cascade(label="Color", menu=menu)

tk.Label(root, textvariable=var1, font="Arial 32 bold", width=10).pack()

root.mainloop()