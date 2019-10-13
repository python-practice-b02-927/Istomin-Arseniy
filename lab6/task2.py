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
game = True
time = 1000
bonus = []
dt = 100

def new_ball():
    global score, time, ball, game, bonus
    del_bonus(bonus)
    cur_ball = {}
    cur_ball['x'] = rnd(100, 700)
    cur_ball['y'] = rnd(100, 500)
    cur_ball['r'] = rnd(30, 50)
    cur_ball['flag'] = False
    cur_ball['vx'] = rnd(-5, 5)
    cur_ball['vy'] = rnd(-5, 5)
    # flag is False when ball hasn't been clicked and True when ball has been clicked
    x = cur_ball['x']
    y = cur_ball['y']
    r = cur_ball['r']
    ball_id = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    cur_ball['id'] = ball_id
    cur_ball['bonus'] = 0
    ball.append(cur_ball)
    if game:
        root.after(time, new_ball)
    else:
        canv.delete(ALL)


def del_bonus(bonus):
    while len(bonus) > 0:
        canv.delete(bonus[len(bonus) - 1])
        bonus.pop(len(bonus) - 1)


def collision():
    pass


def move_ball():
    global ball
    for i in range(len(ball)):
        collision()
        ball[i]['x'] += ball[i]['vx']
        ball[i]['y'] += ball[i]['vy']
        canv.move(ball[i]['id'], ball[i]['vx'], ball[i]['vy'])
    root.after(dt, move_ball)

def click(event):
    global score, game, ball, bonus
    mouse_x = event.x
    mouse_y = event.y
    length = len(ball)
    catch = False
    for i in range(length - 1, -1, -1):
        x = ball[i]['x']
        y = ball[i]['y']
        r = ball[i]['r']
        if ((x - mouse_x) ** 2 + (y - mouse_y) ** 2 <= r ** 2) and not ball[i]['flag']:
            catch = True
            if (x - mouse_x) ** 2 + (y - mouse_y) ** 2 <= (0.1 * r) ** 2:
                score += 5
                bonus_id = canv.create_text(x, y, text="x5", justify=CENTER, font="Verdana 30", fill='red')
                bonus.append(bonus_id)
            elif (x - mouse_x) ** 2 + (y - mouse_y) ** 2 <= (0.2 * r) ** 2:
                score += 2
                bonus_id = canv.create_text(x, y, text="x2", justify=CENTER, font="Verdana 30", fill='red')
                bonus.append(bonus_id)
            else:
                score += 1
            l['text'] = str(score)
            ball[i]['flag'] = True
            canv.delete(ball[i]['id'])
            ball.pop(i)
    if not catch:
        end_game()




def end_game():
    global game
    l['text'] = 'Failed with score:' + str(score)
    canv.delete(ALL)
    game = False


l.pack()
new_ball()
move_ball()
canv.bind('<Button-1>', click)
mainloop()
