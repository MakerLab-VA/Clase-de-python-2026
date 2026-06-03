from random import randint
import time

WIDTH = 400
HEIGHT = 400

dots = []
lines = []

next_dot = 0

tiempo_inicio = None
tiempo_final = None
jugando = False
tiempo_limite = 45 

for dot in range(0, 10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

def draw():
    screen.fill("black")
    if tiempo_final is not None:
        elapsed = tiempo_final - tiempo_inicio
        screen.draw.text(f"Completado en {elapsed:.1f}s!!!", center=(WIDTH // 2, 20), color="yellow",fontsize=24)
    elif jugando and tiempo_inicio is not None:
        elapsed = time.time() - tiempo_inicio
        restante = max(0, tiempo_limite - elapsed)
        color = "red" if restante < 5 else "white"
        screen.draw.text(f"Tiempo: {restante:.1f}s", topleft=(10, 10), color = color, fontsize=22)
    else:
        screen.draw.text("Haz clic en el punto 1 para empezar", center =(WIDTH // 2, 20), color="grey", fontsize=18,)

    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255, 0, 0))

def update():
    global jugando, tiempo_final, next_dot, lines, tiempo_inicio
    if jugando and tiempo_inicio is not None and tiempo_final is None:
        elapsed = time.time() - tiempo_inicio
        if elapsed >= tiempo_limite:
           jugando = False
           reset_juego()

def on_mouse_down(pos):
    global next_dot, lines, tiempo_inicio, tiempo_final, jugando

    if dots[next_dot].collidepoint(pos):
        if next_dot == 0:
            tiempo_inicio = time.time()
            tiempo_final = None
            jugando = True

        if next_dot:
            lines.append((dots[next_dot -1].pos, dots[next_dot].pos))

        next_dot += 1

        if next_dot == len(dots):
            tiempo_final = time.time()
            jugando = False
            next_dot = 0

    else:
        reset_juego()

def reset_juego():
    global next_dot, lines, tiempo_inicio, tiempo_final, jugando

    dots.clear()
    for dot in range(0, 10):
        actor = Actor("dot")
        actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        dots.append(actor)
        
    lines = []
    next_dot = 0
    tiempo_inicio = None
    tiempo_final= None
    jugando = False
