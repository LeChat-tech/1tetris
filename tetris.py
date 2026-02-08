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

Barre = [[(1, 1, 1, 1),
         (0, 0, 0, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0)],
         
        [(0, 0, 0, 1),
         (0, 0, 0, 1),
         (0, 0, 0, 1),
         (0, 0, 0, 1)],
         
        [(1, 1, 1, 1),
         (0, 0, 0, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0)],
         
        [(0, 0, 0, 1),
         (0, 0, 0, 1),
         (0, 0, 0, 1),
         (0, 0, 0, 1)]]
L = [[(1, 1, 1, 1),
     (0, 0, 0, 1),
     (0, 0, 0, 0),
     (0, 0, 0, 0)],

     [(0, 0, 0, 1),
     (0, 0, 0, 1),
     (0, 0, 0, 1),
     (0, 0, 1, 1)],

    [(1, 0, 0, 0),
     (1, 1, 1, 1),
     (0, 0, 0, 0),
     (0, 0, 0, 0)],

     [(1, 1, 0, 0),
     (1, 0, 0, 0),
     (1, 0, 0, 0),
     (1, 0, 0, 0)]]
Bloc = [[(0, 0, 0, 0),
          (0, 0, 0, 0), 
          (0, 0, 1, 1),
          (0, 0, 1, 1)],
          
        [(0, 0, 0, 0),
          (0, 0, 0, 0), 
          (0, 0, 1, 1),
          (0, 0, 1, 1)],

        [(0, 0, 0, 0),
          (0, 0, 0, 0), 
          (0, 0, 1, 1),
          (0, 0, 1, 1)],
        
        [(0, 0, 0, 0),
          (0, 0, 0, 0), 
          (0, 0, 1, 1),
          (0, 0, 1, 1)],]
Coin = [[(1, 1, 0, 0),
         (1, 0, 0, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0)],
         
        [(1, 1, 0, 0),
         (0, 1, 0, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0)],
         
        [(0, 1, 0, 0),
         (1, 1, 0, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0)],

        [(1, 0, 0, 0),
         (1, 1, 0, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0)],]
Double_coin = [[(0, 1, 0, 0),
                (1, 1, 1, 0), 
                (0, 0, 0, 0),
                (0, 0, 0, 0)],

                [(0, 1, 0, 0),
                (0, 1, 1, 0), 
                (0, 1, 0, 0),
                (0, 0, 0, 0)],

                [(0, 0, 0, 0),
                (1, 1, 1, 0), 
                (0, 1, 0, 0),
                (0, 0, 0, 0)],

                [(0, 1, 0, 0),
                (1, 1, 0, 0), 
                (0, 1, 0, 0),
                (0, 0, 0, 0)]]
Pont = [[(1, 1, 1, 1),
         (1, 0, 1, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0)],

         [(1, 1, 0, 0),
          (0, 1, 0, 0),
          (1, 1, 0, 0),
          (0, 1, 0, 0),],

          [(0, 1, 0, 1),
          (1, 1, 1, 1),
          (0, 0, 0, 0),
          (0, 0, 0, 0)],

          [(0, 1, 0, 0),
           (0, 1, 1, 0),
           (0, 1, 0, 0),
           (0, 1, 1, 0)]]
S = [[(0, 1, 1, 0),
      (1, 1, 0, 0),
      (0, 0, 0, 0),
      (0, 0, 0, 0)],

      [ (1, 0, 0, 0),
        (1, 1, 0, 0), 
        (0, 1, 0, 0),
        (0, 0, 0, 0)],

       [(1, 1, 0, 0),
        (0, 1, 1, 0), 
        (0, 0, 0, 0),
        (0, 0, 0, 0)],

       [(0, 1, 0, 0),
        (1, 1, 0, 0), 
        (1, 0, 0, 0),
        (0, 0, 0, 0)],]
Gros_bloc = [[(1, 1, 0, 0),
              (1, 1, 0, 0),
              (1, 1, 0, 0),
              (0, 0, 0, 0)],

              [(1, 1, 1, 0),
              (1, 1, 1, 0),
              (0, 0, 0, 0),
              (0, 0, 0, 0)],

              [(1, 1, 0, 0),
              (1, 1, 0, 0),
              (1, 1, 0, 0),
              (0, 0, 0, 0)],
              
              [(1, 1, 1, 0),
              (1, 1, 1, 0),
              (0, 0, 0, 0),
              (0, 0, 0, 0)]]

class Blocs:
    def __init__(self, x, types):
        self.x = x
        self.y = -5
        self.type = types

etat_barre = 0


x = True
tempo = 0
X = 100
Y = -5
ok = True
ok_bis = True
chrono_pour_touche = 0
chrono_pour_touche_bis = 0
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

    if tempo%60 == 0 and Y + 9 < 505 and (not keys[pygame.K_DOWN] or Y + 40 > 505):
        Y += 10                                     # Quand on arrive en bas la pièce descend plus lentement 
    if keys[pygame.K_UP] and ok:
        etat_barre += 1    
        ok = False
    if keys[pygame.K_DOWN] and ok and Y + 40 < 505:
        Y += 60   
        ok = False
    if keys[pygame.K_LEFT] and ok_bis:
        X -= 20  
        ok_bis = False
    if keys[pygame.K_RIGHT] and ok_bis:
        X += 20    
        ok_bis = False

    for i in range(4):
        for u in range(4):
            if Gros_bloc[etat_barre%4][i][u] == 1:
                screen.blit(Bleu_ciel, (X+u*20,Y+i*20))       

    pygame.draw.line(screen, (255, 255, 255), (343, 20), (343, 590), 5)
    pygame.draw.line(screen, (255, 255, 255), (18, 20), (18, 590), 5)
    pygame.draw.line(screen, (255, 255, 255), (18, 590), (343, 590), 5)


    pygame.display.flip()
    if not ok:
        chrono_pour_touche += 1
    if chrono_pour_touche == 12:
        ok = True
        chrono_pour_touche = 0
    if not ok_bis:
        chrono_pour_touche_bis += 1
    if chrono_pour_touche_bis == 6:
        ok_bis = True
        chrono_pour_touche_bis = 0

    tempo += 1
    if tempo == 61:
        tempo = 0
    clock.tick(60)

pygame.quit()