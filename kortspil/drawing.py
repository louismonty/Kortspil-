import pygame

def box(screen,color,x,y):
    pygame.draw.rect(screen, (color),pygame.Rect(x, y, 250, 100))

def text(screen,text,x,y):
    box_font = pygame.font.SysFont('Comic Sans MS', 30)
    screen.blit(box_font.render(text, False, (0, 0, 0)),(x,y))



