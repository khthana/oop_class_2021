from tkinter import *

def on_click():

    lst = [interests[i] for i, chk in enumerate(chks) if chk.get()]
    # print(lst)
    print(",".join(lst))

interests = ['Music', 'Book', 'Movie', 'Photography', 'Game', 'Travel']
root = Tk()
root.option_add("*Font", "impact 30")
chks = [BooleanVar() for i in interests]

Label(root, text="Your interests", bg="gold").pack()
for i, s in enumerate(interests):
    Checkbutton(root, text=s, variable=chks[i]).pack(anchor=W)  # W = West

Button(root, text="submit", command=on_click).pack()
root.mainloop()

