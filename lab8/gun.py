from random import randrange as rnd, choice, uniform
import tkinter as tk
import math
import time
import const

# print (dir(math))
g = const.g
u = const.u
k = const.k
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
target_number = 2

# k, u - коэффициенты трения

class Ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 20
        self.in_air = True

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.vy < 7 and self.y >= 600 - self.r:
            self.in_air = False
        self.collision()
        self.x += self.vx
        if self.in_air:
            self.y += self.vy
            self.vy += g
        else:
            self.vx *= u
            self.live -= 1
        self.set_coords()

    def collision(self):
        if self.x > 800 - self.r:
            self.vx = -self.vx * k
            self.vy *= u
            self.x = 800 - self.r
            self.live -= 1
        if self.x < self.r:
            self.vx = -self.vx * k
            self.vy *= u
            self.x = self.r
            self.live -= 1
        if self.y > 600 - self.r:
            self.vy = -self.vy * k
            self.vx *= u
            self.y = 600 - self.r
            self.live -= 1
        if self.y < self.r:
            self.vy = -self.vy * k
            self.vx *= u
            self.y = self.r
            self.live -= 1

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.angle = 1
        self.x = 20
        self.y = 450
        self.id = canv.create_line(self.x, self.y, self.x+30, self.y-30, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.x, self.y)
        self.angle = math.atan2((event.y - new_ball.y), (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.angle)
        new_ball.vy = self.f2_power * math.sin(self.angle)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targeting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.angle = math.atan2((event.y - self.y), (event.x - self.x))

    def extension(self):
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.angle),
                    self.y + max(self.f2_power, 20) * math.sin(self.angle)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def move_up(self, event):
        if self.y > 10:
            self.y -= 3

    def move_down(self, event):
        if self.y < 570:
            self.y += 3

    def move_right(self, event):
        if self.x < 600:
            self.x += 3

    def move_left(self, event):
        if self.x > 10:
            self.x -= 3

class Target:
    def __init__(self):
        self.points = 0
        self.vx = 0
        self.vy = rnd(-1, 1)
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        y = self.y = rnd(350, 500)
        x = self.x = rnd(600, 780)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def move(self):
        self.y += self.vy
        canv.move(self.id, self.vx, self.vy)
        if self.y < 50 + self.r:
            self.y = 51 + self.r
            self.vy = -self.vy
        elif self.y > 550 - self.r:
            self.y = 549 + self.r
            self.vy = -self.vy

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.id_points = canv.create_text(30, 30, text=self.score, font='28')

    def update_score(self, point=1):
        self.score += point
        canv.itemconfig(self.id_points, text=self.score)


screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []
targets = []

scoreboard = Scoreboard()


def new_game():
    global screen1, balls, bullet
    canv.itemconfig(screen1, text='')
    g1.x = 20
    g1.y = 450
    bullet = 0
    balls = []
    targets = []
    targets_lives = 0
    for i in range(target_number):
        new_target = Target()
        targets.append(new_target)
        targets_lives += targets[i].live

    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targeting)
    root.bind('<Up>', g1.move_up)
    root.bind('<Down>', g1.move_down)
    root.bind('<Left>', g1.move_left)
    root.bind('<Right>', g1.move_right)
    while targets_lives or balls:
        to_del = []
        for j in range(target_number):
            targets[j].move()
        for i, b in enumerate(balls):
            b.move()
            for j in range(target_number):
                if b.hittest(targets[j]) and targets[j].live:
                    targets_lives -= targets[j].live
                    targets[j].live = 0
                    targets[j].hit()
            if b.live < 0:
                to_del.append(i)
                canv.delete(b.id)
        for i in range(len(to_del) - 1, -1, -1):
            del balls[to_del[i]]
        canv.update()
        time.sleep(0.03)
        g1.extension()
        g1.power_up()
    scoreboard.update_score(target_number)
    canv.bind('<Button-1>', '')
    canv.bind('<ButtonRelease-1>', '')
    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
    canv.delete(g1)
    root.after(1500, new_game)


new_game()

tk.mainloop()
