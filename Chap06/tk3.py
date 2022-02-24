# Label widget
from tkinter import *

root = Tk()
root.option_add("*Font", "consolas 20")
Label(root, text="coconut", bg="green").pack(fill=X)
Label(root, text="แผ่นดินของเรา", bg="deep sky blue").pack(fill=X)
Label(root, text="green\ntea", bg="green").pack(fill=X)
Label(root,
      text="Happiness is when what you think, what you say, and what you do are in harmony.",
      bg="gold").pack(fill=X)
Label(root,
      text="Happiness is when what you think, what you say, and what you do are in harmony.",
      bg="orange", wraplength=400, justify=RIGHT).pack(fill=X)
Label(root,
      text="Happiness is when what you think, what you say, and what you do are in harmony.",
      bg="deep sky blue", wraplength=700, justify=LEFT).pack(fill=X)
Label(root,
      text="Happiness is when what you think, what you say, and what you do are in harmony.\n\nMahatma Gandhi",
      bg="hot pink", wraplength=700).pack(fill=X)
root.mainloop()

