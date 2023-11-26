# Pygame Vector Test
import pygame, sys
from user_interface import *

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
FPS = 75
CLOCK = pygame.time.Clock()

def test():
    print("hi")

def draw(ui):
    WIN.fill((255, 255, 255))
    ui.render(WIN)
    pygame.display.update()
    
pygame.init()
pygame.font.init()
    
ui = Root(WIN, width=WIDTH, height=HEIGHT)
menu = Menu(200, 200, 500, 500, ui, {"background": (255, 0, 0)})
button = UIElement(75, 75, 75, 75, menu, {"background": (0, 0, 0)}, {"background": (0, 255, 0)}, {"background": (0, 0, 255)}, test)
print(menu.children)

run = True
while run:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                menu.set_pos(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        menu.handle_event(event)
    ui.update(WIN)
    draw(ui)
pygame.quit()
sys.exit()
