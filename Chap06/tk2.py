from tkinter import *

root = Tk()
root.option_add("*Font", "consolas 20")
Label(root, text="apple").pack(anchor=E)
Label(root, text="apple", fg="red").pack()
Label(root, text="apple", bg="green").pack(anchor=W)
Label(root, text="apple", fg="green").pack(pady=10)
Label(root, text="banana", bg="yellow", width=15).pack()
Label(root, text="coconut", bg="green").pack(fill=X)
root.mainloop()

