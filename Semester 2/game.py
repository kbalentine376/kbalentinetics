import tkinter as tk
import random

WIDTH = 800
HEIGHT = WIDTH / 2

def game_over():
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text = "GAME OVER", fill = "white", font = ("Arial", 24))

root = tk.Tk()
root.title("Placeholder")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
canvas.pack()

button = tk.Button(root, text = "Restart", fill = "white", font = ("Arial", 12), bg = "black", command = game_over, anchor = "center")
canvas.create_window(WIDTH // 2, HEIGHT // 2 + 30, window = button)

root.mainloop()