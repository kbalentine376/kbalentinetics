# I decided to make a retro pong instead of what other game I had in idea as it was quicker and easier. 
# The shapes, and general movement (the paddels ; Up and Down) was coded by me, as well as the out of bounds / collision
# I used AI for the enemy paddle, I did not understand how to make it follow the ball and I used it for the key bindings as well

#The controls are W and S, you're on the left.


import tkinter as tk

WIDTH = 800
HEIGHT = 500

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100

BALL_SIZE = 15


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Retro Pong")

        self.canvas = tk.Canvas(self.root, width = WIDTH, height = HEIGHT, bg = "black")
        self.canvas.pack()

        self.canvas.create_line(WIDTH // 2, 0, WIDTH // 2, HEIGHT, fill = "white", dash = (10, 10))

        self.player = self.canvas.create_rectangle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, 30 + PADDLE_WIDTH, HEIGHT // 2 + PADDLE_HEIGHT // 2, fill = "white")

        self.enemy = self.canvas.create_rectangle(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, WIDTH - 30, HEIGHT // 2 + PADDLE_HEIGHT // 2, fill = "white")

        self.ball = self.canvas.create_oval(WIDTH // 2 - BALL_SIZE, HEIGHT // 2 - BALL_SIZE, WIDTH // 2 + BALL_SIZE, HEIGHT // 2 + BALL_SIZE, fill = "white")

        self.paddle_speed = 4
        self.ai_speed = 6

        self.dx = 4
        self.dy = 3

        self.w_pressed = False
        self.s_pressed = False

        self.root.bind("<KeyPress-w>", self.key_down)
        self.root.bind("<KeyRelease-w>", self.key_up)
        self.root.bind("<KeyPress-s>", self.key_down)
        self.root.bind("<KeyRelease-s>", self.key_up)

        self.game_loop()

        self.update()
        self.root.mainloop()
    
    def key_down(self, event):
        if event.keysym == "w":
            self.w_pressed = True
        elif event.keysym == "s":
            self.s_pressed = True

    def key_up(self, event):
        if event.keysym == "w":
            self.w_pressed = False
        elif event.keysym == "s":
            self.s_pressed = False

    def move_player(self):
        x1, y1, x2, y2 = self.canvas.coords(self.player)

        if self.w_pressed and y1 > 0:
            self.canvas.move(self.player, 0, -self.paddle_speed)

        if self.s_pressed and y2 < HEIGHT:
            self.canvas.move(self.player, 0, self.paddle_speed)

    def move_enemy(self):
        ex1, ey1, ex2, ey2 = self.canvas.coords(self.enemy)

        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)
        ball_center = (by1 + by2) / 2
        enemy_center = (ey1 + ey2) / 2

        diff = ball_center - enemy_center

        if abs(diff) > 5:
            move = max(-self.ai_speed, min(self.ai_speed, diff))
            self.canvas.move(self.enemy, 0, move)

        ex1, ey1, ex2, ey2 = self.canvas.coords(self.enemy)

        if ey1 < 0:
            self.canvas.move(self.enemy, 0, -ey1)
        if ey2 > HEIGHT:
            self.canvas.move(self.enemy, 0, HEIGHT - ey2)

    def check_collision(self, paddle):
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)
        px1, py1, px2, py2 = self.canvas.coords(paddle)

        return (
            bx2 >= px1 and
            bx1 <= px2 and
            by2 >= py1 and
            by1 <= py2
        )

    def update(self):
        self.move_player()
        self.move_enemy()

        self.canvas.move(self.ball, self.dx, self.dy)

        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)

        if by1 <= 0 or by2 >= HEIGHT:
            self.dy = -self.dy

        if self.check_collision(self.player) and self.dx < 0:
            self.dx = -self.dx

        if self.check_collision(self.enemy) and self.dx > 0:
            self.dx = -self.dx

        if bx1 <= 0 or bx2 >= WIDTH:
            self.canvas.coords(self.ball, WIDTH // 2 - BALL_SIZE, HEIGHT // 2 - BALL_SIZE, WIDTH // 2 + BALL_SIZE, HEIGHT // 2 + BALL_SIZE)
            self.dx = -self.dx

        self.root.after(16, self.update)

    def game_loop(self):
        self.move_player()
        self.root.after(16, self.game_loop)

Game()