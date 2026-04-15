apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = 300
    apple.y = 200

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print('Buen disparo!!!')
        place_apple()
    else:
        print('Has fallado!!!')
        quit()


place_apple()
