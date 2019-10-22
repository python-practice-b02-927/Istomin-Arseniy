from tkinter import *
import random as r

root = Tk()

root.geometry('800x700')
root.resizable(width=False, height=False)

c = Canvas(root, bg='azure')
c.pack(fill=BOTH, expand=1)

color = ('indian red', 'orange', 'yellow', 'pale green', 'RoyalBlue1', 'MediumPurple')
rainbow_list = [[0 for _ in range(6)] for _ in range(10)]
cat = [0 for _ in range(11)]
body_parts = ('head', 'ear1', 'ear2', 'eye1', 'eye2', 'mouth1', 'mouth2', 'nose', 'body', 'leg1', 'leg2')

xs = 170
ys = 190
dx = 0.05
djump = [-19, -17, -15, -13, -11, -9, -7, -5, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
step = 0
flag_step = False
flag_jump = 1
flag_jrainbow = 1


def cat_creation(xh, yh):
    # legs
    cat[body_parts.index('leg1')] = c.create_oval(60 + xh, 108 + yh, 85 + xh, 153 + yh, fill='grey', outline='grey')
    cat[body_parts.index('leg2')] = c.create_oval(115 + xh, 108 + yh, 140 + xh, 153 + yh, fill='grey', outline='grey')

    # body
    cat[body_parts.index('body')] = c.create_rectangle(50 + xh, 50 + yh, 150 + xh, 125 + yh, fill='hot pink',
                                                       outline='burlywood1', width=8)
    # head
    cat[body_parts.index('head')] = c.create_rectangle(120 + xh, 60 + yh, 180 + xh, 110 + yh, fill='grey',
                                                       outline='grey')

    # ears and eyes
    cat[body_parts.index('ear1')] = c.create_polygon(120 + xh, 60 + yh, 130 + xh, 40 + yh, 140 + xh, 60 + yh,
                                                     fill='grey', outline='grey')
    cat[body_parts.index('ear2')] = c.create_polygon(160 + xh, 60 + yh, 170 + xh, 40 + yh, 180 + xh, 60 + yh,
                                                     fill='grey', outline='grey')
    cat[body_parts.index('eye1')] = c.create_oval(130 + xh, 75 + yh, 140 + xh, 85 + yh, fill='black')
    cat[body_parts.index('eye2')] = c.create_oval(170 + xh, 75 + yh, 160 + xh, 85 + yh, fill='black')

    # mouth and nose
    cat[body_parts.index('mouth1')] = c.create_line(140 + xh, 105 + yh, 160 + xh, 105 + yh, fill='black')
    cat[body_parts.index('mouth2')] = c.create_line(150 + xh, 95 + yh, 150 + xh, 105 + yh, fill='black')
    cat[body_parts.index('nose')] = c.create_rectangle(147 + xh, 89 + yh, 153 + xh, 95 + yh, fill='hot pink')


def rainbow():
    global color, rainbow_list
    for j in range(10):
        for i in range(6):
            rainbow_list[j][i] = c.create_rectangle(22 * j, 245 + 10 * i, 22 + 22 * j, 255 + 10 * i,
                                                    fill=color[i], outline=color[i])


def head_moving(xh, yh):
    c.move(cat[body_parts.index('head')], xh, yh)
    c.move(cat[body_parts.index('eye1')], xh, yh)
    c.move(cat[body_parts.index('eye2')], xh, yh)
    c.move(cat[body_parts.index('ear1')], xh, yh)
    c.move(cat[body_parts.index('ear2')], xh, yh)
    c.move(cat[body_parts.index('mouth1')], xh, yh)
    c.move(cat[body_parts.index('mouth2')], xh, yh)
    c.move(cat[body_parts.index('nose')], xh, yh)


def return_body_move(xh, yh):
    def body_move():
        xx = xh
        yy = yh
        c.move(cat[body_parts.index('body')], xx, yy)
        head_moving(xx, yy)

    return body_move


def return_full_body_move(xh, yh):
    def full_body_move():
        xx = xh
        yy = yh
        c.move(cat[body_parts.index('leg1')], xx, yy)
        c.move(cat[body_parts.index('leg2')], xx, yy)
        c.move(cat[body_parts.index('body')], xx, yy)
        head_moving(xh, yh)

    return full_body_move


def running_cat():
    global xs, ys, dx, step, flag_step, flag_jump

    if flag_jump == 1:

        if (step < 0) and (step % 3 == 0):
            for j in range(10):
                if j % 2 == 0:
                    for i in range(6):
                        c.move(rainbow_list[j][i], 0, 10 * dx)

                        head_moving(0, dx)

            for j in range(10):
                if j % 2 == 1:
                    for i in range(6):
                        c.move(rainbow_list[j][i], 0, -10 * dx)

        if (step > 0) and (step % 3 == 0):
            for j in range(10):
                if j % 2 == 0:
                    for i in range(6):
                        c.move(rainbow_list[j][i], 0, - 10 * dx)

                        head_moving(0, -dx)

            for j in range(10):
                if j % 2 == 1:
                    for i in range(6):
                        c.move(rainbow_list[j][i], 0, 10 * dx)

        if flag_step is False:
            c.move(cat[body_parts.index('leg1')], -1, 0)
            c.move(cat[body_parts.index('leg2')], 1, 0)
        else:
            c.move(cat[body_parts.index('leg1')], 1, 0)
            c.move(cat[body_parts.index('leg2')], -1, 0)

        if step > 10:
            flag_step = True
        elif step < -10:
            flag_step = False
        if flag_step is False:
            step += 1
        else:
            step -= 1
    root.after(30, running_cat)


def return_flag_jump():
    global flag_jump
    flag_jump = 1


def jumping_cat(event):
    global flag_jump, djump
    print(flag_jump)
    flag_jump += 1
    if flag_jump == 2:
        flag_jump += 1
        for i in range(10):
            root.after(10 * i, return_body_move(0, 10 * dx))
        for i in range(10):
            root.after(100 + 10 * i, return_body_move(0, -10 * dx))
        for i in range(40):
            if i < 21:
                root.after(200 + 60 * i, return_full_body_move(0, djump[i]))
            root.after(200 + 60 * i, return_jumping_rainbow(0, i))
        root.after(1500, return_flag_jump)


def return_jumping_rainbow(xh, a):
    def jumping_rainbow():
        counter = a
        xx = xh
        for j in range(9, -1, -1):
            counter -= 1
            if (counter >= 0) and (counter < 21):
                for i in range(6):
                    c.move(rainbow_list[j][i], xx, djump[counter])

    return jumping_rainbow

cloud_number = None
cloud_list = []  # list of clouds characteristics
cloud_color = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace', 'linen', 'antique white',
               'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 'mint cream',
               'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'dark slate gray', 'dim gray',
               'slate gray', 'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue',
               'dark slate blue', 'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',
               'blue', 'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
               'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
               'cyan', 'light cyan', 'cadet blue', 'medium aquamarine']


def fog_generation():  # func generate cloud_number fog clouds
    global cloud_number
    for i in range(cloud_number):
        # generation of cloud characteristics
        cloud_speed = r.randint(-5, -1)
        cloud_length = r.randint(50, 200)
        cloud_x = r.randint(0, 800)
        cloud_y = r.randint(360, 600)

        # cloud drawing
        cloud = c.create_line(cloud_x, cloud_y, cloud_x + cloud_length, cloud_y, fill=r.choice(cloud_color),
                              width=20)
        cloud_list.append([cloud, cloud_speed, cloud_length, cloud_y])


def fog_animation():  # func animate fog
    for i in range(cloud_number):
        c.move(cloud_list[i][0], cloud_list[i][1], 0)
        if c.coords(cloud_list[i][0])[2] < 0:
            cloud_y = r.randint(360, 600)
            c.move(cloud_list[i][0], 800 + cloud_list[i][2], 0)

    root.after(60, fog_animation)


cloud_number = 15
fog_generation()
root.after(60, fog_animation)


rainbow()
cat_creation(170, 190)
running_cat()

root.bind('<space>', jumping_cat)

root.mainloop()