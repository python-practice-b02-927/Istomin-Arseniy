from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')

canv.pack(fill=BOTH, expand=1)

colors = ['orange', 'yellow', 'green', 'blue']

score_label = Label(root, bg='black', fg='white', width=20)
start_button = Button(canv, text="Start", height=3, width=10)
restart_button = Button(canv, text="Restart", bg='black', height=3, width=10)
leaderboard_button = Button(root, text="Leaderboard", bg='black', height=3, width=10)
ball = []
leaders = []
score = 0
game = True
time = 1000
bonus = []
dt = 50
def new_ball():
    global score, time, ball, game, bonus
    del_bonus(bonus)
    cur_ball = {}
    cur_ball['x'] = rnd(100, 700)
    cur_ball['y'] = rnd(100, 500)
    cur_ball['r'] = rnd(30, 50)
    cur_ball['flag'] = False
    cur_ball['vx'] = rnd(-3, 3)
    cur_ball['vy'] = rnd(-3, 3)
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


def new_hard_ball():
    global score, time, ball, game, bonus
    del_bonus(bonus)
    cur_ball = {}
    cur_ball['x'] = rnd(100, 700)
    cur_ball['y'] = rnd(100, 500)
    cur_ball['r'] = rnd(30, 50)
    cur_ball['flag'] = False
    if rnd(0, 1) > 0.5:
        cur_ball['vx'] = rnd(10, 15)
    else:
        cur_ball['vx'] = rnd(-15, -10)
    if rnd(0, 1) > 0.5:
        cur_ball['vy'] = rnd(10, 15)
    else:
        cur_ball['vy'] = rnd(-15, -10)
    # flag is False when ball hasn't been clicked and True when ball has been clicked
    x = cur_ball['x']
    y = cur_ball['y']
    r = cur_ball['r']
    ball_id = canv.create_oval(x - r, y - r, x + r, y + r, fill='red', width=0)
    cur_ball['id'] = ball_id
    cur_ball['bonus'] = 0
    ball.append(cur_ball)
    hard_time = rnd(4000, 10000)
    if game:
        root.after(hard_time, new_hard_ball)
    else:
        canv.delete(ALL)

def del_bonus(bonus):
    while len(bonus) > 0:
        canv.delete(bonus[len(bonus) - 1])
        bonus.pop(len(bonus) - 1)


def collision(i):
    if ball[i]['x'] < ball[i]['r'] or ball[i]['x'] > 800-ball[i]['r']:
        ball[i]['vx'] = -ball[i]['vx']
    if ball[i]['y'] < ball[i]['r'] or ball[i]['y'] > 600-ball[i]['r']:
        ball[i]['vy'] = -ball[i]['vy']


def move_ball():
    global ball, game
    for i in range(len(ball)):
        collision(i)
        ball[i]['x'] += ball[i]['vx']
        ball[i]['y'] += ball[i]['vy']
        canv.move(ball[i]['id'], ball[i]['vx'], ball[i]['vy'])
    if game:
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
            score_label['text'] = str(score)+' '
            ball[i]['flag'] = True
            canv.delete(ball[i]['id'])
            ball.pop(i)
    if not catch:
        end_game()


def end_game():
    global game, leaders
    score_label['text'] = 'Failed with score:' + str(score)
    canv.delete(ALL)
    game = False
    leader_file = open('leaderboard.txt', 'w')
    leader_file.write(' '+str(score))
    leader_file.close()
    leader_file = open('leaderboard.txt', 'r')
    leaders = (leader_file.read()).split()
    leaders.sort(reverse=True)
    leaders = leaders[:10]
    leaders_str = ''
    for i in leaders:
        leaders_str = i + " "
    leader_file.close()
    leader_file = open('leaderboard.txt', 'w')
    leader_file.write(leaders_str)
    leader_file.close()



def start_game(event):
    global game, ball, score
    game = True
    score = 0
    ball.clear()
    canv.delete(ALL)
    score_label['text'] = ''
    start_button.destroy()
    score_label.pack()
    new_ball()
    new_hard_ball()
    move_ball()
    canv.bind('<Button-1>', click)


def leaderboard(event):
    print(leaders)


start_button.bind('<Button-1>', start_game)
restart_button.pack(anchor=CENTER)
restart_button.bind('<Button-1>', start_game)
start_button.pack(anchor=CENTER)
leaderboard_button.bind('<Button-1>', leaderboard)
leaderboard_button.pack(anchor=SW)


mainloop()
