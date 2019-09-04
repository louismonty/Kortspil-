import random
import sys
import pygame
import classes
import mousepointer
import drawing



pygame.init()
pygame.font.init()
box_font = pygame.font.SysFont('Comic Sans MS', 30)
gameover_font = pygame.font.SysFont('Comic Sans MS', 60)

size = width, height = 1200, 640
black = 0, 0, 0

#choses a random pokemon 
def find_pokemon():
    random_pokemon = random.randint(1,3)
    if random_pokemon == 1:
     return(classes.Niggachu)
    if random_pokemon == 2:
        return(classes.Bulbabitch)
    if random_pokemon == 3:
        return(classes.whiteMander)
    if random_pokemon == 4:
        print ("squrt")
    print(pokemon.name)       
screen = pygame.display.set_mode(size)

pokemon = find_pokemon()
pygame.time.delay(100)
pokemon2 = find_pokemon()
pokemon2_hp_seperat = pokemon2.hp

def counter_attack():
    random_attack = random.randint(1,4)
    if random_attack == 1:
        pokemon.hp -= pokemon2.attack_one_dmg 
    if random_attack == 2:
        pokemon.hp -= pokemon2.attack_two_dmg
    if random_attack ==3:
        pokemon.hp -= pokemon2.attack_three_dmg
    if random_attack == 4:
        pokemon.hp -= pokemon2.attack_four_dmg



#gameloop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
   #checks if somone is clicking within the box 
    if mousepointer.box_one_detection_click() == True:
        pokemon2_hp_seperat -= pokemon.attack_one_dmg
        
        pygame.time.delay(100)
        counter_attack()
    if mousepointer.box_two_detection_click() == True:
        pokemon2_hp_seperat -= pokemon.attack_two_dmg
        pygame.time.delay(100)
        counter_attack()
    if mousepointer.box_three_detection_click() == True:
        pokemon2_hp_seperat -= pokemon.attack_three_dmg
        pygame.time.delay(100)
        counter_attack()
    if mousepointer.box_four_detection_click() == True:
        pokemon2_hp_seperat -= pokemon.attack_two_dmg
        pygame.time.delay(100)
        counter_attack()

    
    
    screen.fill(black)
    #draws pokemon 1
    screen.blit(pokemon.img,(1,1))
    #draws pokemon2
    screen.blit(pokemon2.img,(500,1))

#Rect(left, top, width, height)
    #box 1
    drawing.box(screen,mousepointer.box_one_detection(),10,500)
    drawing.text(screen,pokemon.attack_one_name,10,500)
    #box 2
    drawing.box(screen, mousepointer.box_two_detection(),280,500)
    drawing.text(screen,pokemon.attack_two_name,280,500)
    #box 3
    drawing.box(screen,mousepointer.box_three_detection(),550,500)
    drawing.text(screen,pokemon.attack_three_name,550,500)
    #box 4
    drawing.box(screen,mousepointer.box_four_detection(),820,500)
    drawing.text(screen,pokemon.attack_four_name,820,500)
    #hp text 
    screen.blit(box_font.render(str(pokemon.hp), False, (0, 250, 0)),(110,10))
    screen.blit(box_font.render(str(pokemon2_hp_seperat), False, (0, 250, 0)),(600,10))
    #pokemon name 
    screen.blit(box_font.render((pokemon.name), False, (0, 0, 250)),(200,330))
    screen.blit(box_font.render((pokemon2.name), False, (0, 0, 250)),(700,330))
    #hp bar
    pygame.draw.rect(screen, (0,250,0),pygame.Rect(10, 10, pokemon.hp, 50))
    pygame.draw.rect(screen, (0,250,0),pygame.Rect(510, 10, pokemon2_hp_seperat, 50))
    if pokemon2_hp_seperat <= 0 or pokemon.hp <= 0:
        screen.blit(gameover_font.render(str("gameover"), False, (0, 0, 250)),(400,320))
        pygame.time.delay(1000)
        sys.exit()
        

    pygame.display.flip()
    
