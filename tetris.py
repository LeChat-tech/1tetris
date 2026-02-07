import pygame
import os                                       
os.chdir(os.path.dirname(__file__))  
# Initialisation de Pygame
pygame.init()
pygame.font.init()

key_last_state = {}

# Configuration de la police pour le score
font = pygame.font.SysFont('Arial', 20)

# Paramètres de la fenêtre
largeur = 500
hauteur = 600
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Utilisation de Clock')

clock = pygame.time.Clock()
dimmension_carres = (20, 20)  
Vert = pygame.image.load("carre_vert.png").convert()             
Vert = pygame.transform.scale(Vert, dimmension_carres) 

Rouge = pygame.image.load("carre_rouge.png").convert()             
Rouge = pygame.transform.scale(Rouge, dimmension_carres) 

Jaune = pygame.image.load("carre_jaune.png").convert()             
Jaune = pygame.transform.scale(Jaune, dimmension_carres) 

Rose = pygame.image.load("carre_rose.png").convert()             
Rose = pygame.transform.scale(Rose, dimmension_carres)

Bleu = pygame.image.load("carre_bleu.png").convert()             
Bleu = pygame.transform.scale(Bleu, dimmension_carres) 

Bleu_ciel = pygame.image.load("carre_bleu_ciel.png").convert()             
Bleu_ciel = pygame.transform.scale(Bleu_ciel, dimmension_carres)

Orange = pygame.image.load("carre_orange.png").convert()
Orange = pygame.transform.scale(Orange, dimmension_carres)

Barre = [[(0, 0, 0, 1),
         (0, 0, 0, 1),
         (0, 0, 0, 1),
         (0, 0, 0, 1)],

         [(0, 0, 0, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0),
         (1, 1, 1, 1)],
         
        [(1, 0, 0, 0),
         (1, 0, 0, 0),
         (1, 0, 0, 0),
         (1, 0, 0, 0)],
         
         [(1,1, 1, 1),
         (0, 0, 0, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0)],]
etat_barre = 0
L = [(1, 1, 1, 1),
     (0, 0, 0, 1),
     (0, 0, 0, 0),
     (0, 0, 0, 0)]

x = True
tempo = 0
X = 100
Y = -5
ok = True
chrono_pour_touche = 0
while x:
    # bla 
    # bla 
    # bla

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_r]:  # pour arrêter la boucle avec la touche 'r'
        x = False

    screen.fill((100, 0, 205))
    screen.blit(Vert, (100,25))        
    screen.blit(Rouge, (100,65))        
    screen.blit(Orange, (100,105))        
    screen.blit(Bleu, (100,145))    
    screen.blit(Bleu_ciel, (100,185))        
    screen.blit(Rose, (100,225))   
    screen.blit(Jaune, (100, 265)) 


    if tempo%60 == 0 and Y + 9 < 505:
        Y += 10
    if keys[pygame.K_UP] and ok:
        etat_barre += 1    
        ok = False
    if keys[pygame.K_DOWN] and ok and Y + 40 < 505:
        Y += 40   
        ok = False
    if keys[pygame.K_LEFT] and ok:
        X -= 20  
        ok = False
    if keys[pygame.K_RIGHT] and ok:
        X += 20    
        ok = False

    for i in range(4):
        for u in range(4):
            if Barre[etat_barre%4][i][u] == 1:
                screen.blit(Vert, (X+u*20,Y+i*20))       
    for i in range(4):
        for u in range(4):
            if L[i][u] == 1:
                screen.blit(Rouge, (X+u*20+150,Y+i*20))  

    pygame.draw.line(screen, (255, 255, 255), (350, 20), (350, 590), 5)
    pygame.draw.line(screen, (255, 255, 255), (20, 20), (20, 590), 5)
    pygame.draw.line(screen, (255, 255, 255), (20, 590), (350, 590), 5)


    pygame.display.flip()
    if not ok:
        chrono_pour_touche += 1
    if chrono_pour_touche == 20:
        ok = True
        chrono_pour_touche = 0

    tempo += 1
    if tempo == 61:
        tempo = 0
    clock.tick(60)

pygame.quit()