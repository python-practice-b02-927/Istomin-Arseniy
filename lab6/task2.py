from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')

canv.pack(fill=BOTH, expand=1)

colors = ['orange', 'yellow', 'green', 'blue']

l = Label(root, bg='black', fg='white', width=20)
ball = []
score = 0

flag = True
time = 2000
def new_ball():
    global flag, score, time, x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    if flag:
        time = 500 + int(1500 / (0.1 * score + 1))
        root.after(time, new_ball)
    else:
        l['text'] = 'Failed with score:' + str(score)
        canv.delete(ALL)
    flag = False


def click(event):
    global score, flag
    mouse_x = event.x
    mouse_y = event.y
    if ((x - mouse_x)**2 + (y - mouse_y)**2 <= r**2) and flag == False:
        if (x - mouse_x)**2 + (y - mouse_y)**2 <= (0.1 * r)**2:
            score += 5
            canv.create_text(x, y, text="x5", justify=CENTER, font="Verdana 30", fill='red')
        elif (x - mouse_x)**2 + (y - mouse_y)**2 <= (0.2 * r)**2:
            score += 2
            canv.create_text(x, y, text="x2", justify=CENTER, font="Verdana 30", fill='red')
        else:
            score += 1
        l['text'] = str(score)
        flag = True


l.pack()
new_ball()


canv.bind('<Button-1>', click)
mainloop()
