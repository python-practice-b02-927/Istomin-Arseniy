from tkinter import *


def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)


root = Tk()
root.geometry('800x800')
e = Entry(root, width=20)
b = Button(root, text="Преобразовать")
l = Label(root, bg='black', fg='white', width=20)
e.pack()
b.pack()
l.pack()
b.bind('<Button-1>', strToSortlist)
mainloop()