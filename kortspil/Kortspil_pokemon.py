import random
import sys
import pygame
import classes
import mousepointer



pygame.init()
pygame.font.init()
box_font = pygame.font.SysFont('Comic Sans MS', 30)

size = width, height = 1200, 640
black = 0, 0, 0


random_pokemon = random.randint(1,2)
if random_pokemon == 1:
    pokemon = classes.Niggachu
if random_pokemon == 2:
    pokemon = classes.Bulbabitch
if random_pokemon == 3:
    pokemon = pygame.image.load("/Users/louis/Documents/GitHub/Kortspil-/kortspil/char.png")
    print ("char")
if random_pokemon == 4:
    print ("squrt")
print(pokemon.name)       
screen = pygame.display.set_mode(size)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
   
    if mousepointer.box_one_detection_click() == True:
        pokemon.hp -= pokemon.attack_one_dmg
        pygame.time.delay(100)
    if mousepointer.box_two_detection_click() == True:
        pokemon.hp -= pokemon.attack_two_dmg
        pygame.time.delay(100)
    if mousepointer.box_three_detection_click() == True:
        pokemon.hp -= pokemon.attack_three_dmg
        pygame.time.delay(100)
    if mousepointer.box_four_detection_click() == True:
        pokemon.hp -= pokemon.attack_two_dmg
        pygame.time.delay(100)

    
    
    screen.fill(black)
    screen.blit(pokemon.img,(1,1))
    screen.blit(pokemon.img,(1,1))

#Rect(left, top, width, height)
    #box 1
    pygame.draw.rect(screen, (mousepointer.box_one_detection()),pygame.Rect(10, 500, 250, 100))
    screen.blit(box_font.render(pokemon.attack_one_name, False, (0, 0, 0)),(10,500))
    #box 2
    pygame.draw.rect(screen, (mousepointer.box_two_detection()),pygame.Rect(280, 500, 250, 100))
    screen.blit(box_font.render(pokemon.attack_two_name, False, (0, 0, 0)),(280,500))
    #box 3
    pygame.draw.rect(screen, (mousepointer.box_three_detection()),pygame.Rect(550, 500, 250, 100))
    screen.blit(box_font.render(pokemon.attack_three_name, False, (0, 0, 0)),(550,500))
    #box 4
    pygame.draw.rect(screen, (mousepointer.box_four_detection()),pygame.Rect(820, 500, 250, 100))
    screen.blit(box_font.render(pokemon.attack_four_name, False, (0, 0, 0)),(820,500))
    screen.blit(box_font.render(str(pokemon.hp), False, (0, 0, 0)),(110,10))
    pygame.draw.rect(screen, (0,250,0),pygame.Rect(10, 10, pokemon.hp, 50))
    pygame.display.flip()
    
