import sys, pygame, random
pygame.init()

size = width, height = 920, 640
speed = [2, 2]
black = 0, 0, 0


random_pokemon = random.randint(1,4)
if random_pokemon == 1:
    pokemon = pygame.image.load("/Users/louis/Documents/GitHub/Kortspil-/kortspil/pica.png")
if random_pokemon == 2:
    pokemon = pygame.image.load("/Users/louis/Documents/GitHub/Kortspil-/kortspil/bulba.png")
    print ("bulba")
if random_pokemon == 3:
    pokemon = pygame.image.load("/Users/louis/Documents/GitHub/Kortspil-/kortspil/char.png")
    print ("char")
if random_pokemon == 4:
    print ("squrt")
        
screen = pygame.display.set_mode(size)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)
    screen.blit(pokemon,(1,1))
    pygame.display.flip()
