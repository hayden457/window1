import tkinter as tk
import random
import math

WIDTH, HEIGHT = 700, 500
GRAVITY = 0.25
MAX_PARTICLES = 150
COLORS = ["#ff4d4d", "#ffd11a", "#33ccff", "#66ff66", "#ff66cc", "#ffffff"]

root = tk.Tk()
root.title("Fireworks")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#0b0d17")
canvas.pack()

particles = []


def launch_rocket(event):
    if len(particles) > MAX_PARTICLES:
        return
    x, y = event.x, HEIGHT - 5
    dot = canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="#ffffff",
                             outline="")
    particles.append({
        "id": dot,
        "type": "rocket",
        "vx": random.uniform(-1, 1),
        "vy": random.uniform(-14, -10),
        "life": 100
    })


def explode(x, y):
    if len(particles) > MAX_PARTICLES:
        return
    color = random.choice(COLORS)
    for _ in range(35):
        angle = random.umiform(0, 2 * math.pi)
        speed = random.uniform(2, 7)
        dot = canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=color, outline="")
        particles.append({
            "id": dot,
            "type": "spark",
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,
            "life": random.randint(25, 45)
        })

def spawn_dot(event):
    color = random.choice(COLORS)
    canvas.create_oval(
        event.x - 3, event.y - 3,
        event.x + 3, event.y + 3,
        fill=color, outline=""
    )

def spawn_firework(event):
    if len(particles) > MAX_PARTICLES:
        return

    color = random.choice(COLORS)
    for _ in range(35):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 7)

        vx = math.cos(angle) * speed
        vy = math.sin(angle) * speed

        dot = canvas.create_oval(
            event.x - 3, event.y - 3,
            event.x + 3, event.y + 3,
            fill=color, outline=""
        )
        particles.append({
            "id": dot,
            "vx": vx,
            "vy": vy,
            "life": random.randint(25, 45)
        })

def update():
    alive = []
    for p in particles:
        p["vy"] += GRAVITY
        canvas.move(p["id"], p["vx"], p["vy"])
        p["life"] -= 1

        if p["life"] > 0:
            alive.append(p)
        else:
            canvas.delete(p["id"])

    particles[:] = alive
    root.after(33, update)



canvas.bind("<Button-1>", spawn_dot)
update()
root.mainloop()
