import tkinter as tk
import random

# Window setup
window = tk.Tk()
window.title("Color Trail Bouncing Ball")
canvas_width = 600
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

# Ball properties
x, y = 300, 200
dx, dy = 4, 3
radius = 15
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "white"]

def move_ball():
    global x, y, dx, dy

    # Bounce off walls
    if x - radius <= 0 or x + radius >= canvas_width:
        dx = -dx
    if y - radius <= 0 or y + radius >= canvas_height:
        dy = -dy

    # Update position
    x += dx
    y += dy

    # Draw a trail with random color
    canvas.create_oval(
        x - radius, y - radius, x + radius, y + radius,
        fill=random.choice(colors), outline=""
    )

    # Fade old trails for the "motion blur" effect
    canvas.after(50, fade_trail)

    # Loop
    window.after(20, move_ball)

def fade_trail():
    # Overlay a translucent rectangle to create a fading trail effect
    canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="black", stipple="gray50", outline="")

# Start the animation
move_ball()
window.mainloop()
