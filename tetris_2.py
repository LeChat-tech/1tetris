import pygame
import os                                       
os.chdir(os.path.dirname(__file__))  
from random import randint
import time
import copy
# Initialisation de Pygame
pygame.init()
pygame.font.init()

key_last_state = {}

# Configuration de la police pour le score
font = pygame.font.SysFont('Arial', 20)

# Paramètres de la fenêtre
largeur = 500
hauteur = 610
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Tétris')

clock = pygame.time.Clock()

Taille_cube = 30
dimmension_carres = (Taille_cube, Taille_cube)  

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

Barre = [[[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         
         [[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1]],
         
         [[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         
         [[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1]]]
L_pair = [[[0, 1, 1, 1],
           [0, 0, 0, 1],
           [0, 0, 0, 0],
           [0, 0, 0, 0]],

          [[0, 0, 0, 1],
           [0, 0, 0, 1],
           [0, 0, 1, 1],
           [0, 0, 0, 0]],

          [[0, 1, 0, 0],
           [0, 1, 1, 1],
           [0, 0, 0, 0],
           [0, 0, 0, 0]],

          [[0, 1, 1, 0],
           [0, 1, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 0]]]
L_impair = [[[0, 0, 0, 1],
             [0, 1, 1, 1],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 0, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 1, 1],
             [0, 0, 0, 0]],

            [[0, 1, 1, 1],
             [0, 1, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 1, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0]]]
Bloc = [[[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 1, 1],
         [0, 0, 1, 1]],

        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 1, 1],
         [0, 0, 1, 1]],

        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 1, 1],
         [0, 0, 1, 1]],

        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 1, 1],
         [0, 0, 1, 1]]]
T = [[[0, 1, 0, 0],
      [1, 1, 1, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]],

     [[0, 1, 0, 0],
      [0, 1, 1, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0]],

     [[0, 0, 0, 0],
      [1, 1, 1, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0]],

     [[0, 1, 0, 0],
      [1, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0]]]
Pont = [[[1, 1, 1, 1],
         [1, 0, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],

        [[1, 1, 0, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 0, 0]],

        [[0, 1, 0, 1],
         [1, 1, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],

        [[0, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 1, 0, 0],
         [0, 1, 1, 0]]]
S_pair = [[[0, 1, 1, 0],
           [1, 1, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]],

          [[1, 0, 0, 0],
           [1, 1, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 0]],

          [[0, 1, 1, 0],
           [1, 1, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]],

          [[1, 0, 0, 0],
           [1, 1, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 0]]]
S_impair = [[[1, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 1, 0, 0],
             [1, 1, 0, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 0]],

            [[1, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 1, 0, 0],
             [1, 1, 0, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 0]]]

X_G = 10
Y_G = 18
GRILLE = ["0"]*X_G
for i in range(len(GRILLE)):
    GRILLE[i] = ["0"]*Y_G

piece_possible = [Barre, L_impair, L_pair, Bloc, T, S_impair, S_pair]           # 7
couleurs_possibles = [Vert, Bleu, Bleu_ciel, Rouge, Jaune, Orange, Rose]    # 7

class Pieces:
    def __init__(self, x, y, etat, types, couleur):
        self.x = (x-20)//30
        self.y = (y-40)//30
        self.etat = etat
        self.color = couleur
        self.type = types
        self.active = True
    def draw(self):
        global GRILLE
        for i in range(4):
            for u in range(4):
                if L_impair[0][i][u] == 1:
                    GRILLE[(self.x+i)][(self.y+u)] = Vert
    def update(self):
        if self.active:
            for i in range(4):
                for u in range(4):
                    if L_impair[0][i][u] == 1:
                        GRILLE[(self.x+i)][(self.y+u)] = "0"
            self.y += 1
    def Right(self):
        for i in range(4):
            for u in range(4):
                if L_impair[0][i][u] == 1:
                    GRILLE[(self.x+i)][(self.y+u)] = "0"
        self.x += 1

    def Left(self):
        for i in range(4):
            for u in range(4):
                if L_impair[0][i][u] == 1:
                    GRILLE[(self.x+i)][(self.y+u)] = "0"
        self.x -= 1

run = True
TET = Pieces(250, 50, 0, L_impair, Vert)
Chrono = 0
Chrono_pour_touche = 0
VITESSE_POUR_LES_TOUCHES = 15
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:  # pour arrêter la boucle avec la touche 'r'
        run = False
    
    if Chrono == 60:
        TET.update()


    screen.fill((100, 0, 205))    
    lim_grille_x1 = 17
    lim_grille_x2 = 322
    lim_grille_y1 = 40
    lim_grille_y2 = 593
    pygame.draw.line(screen, (255, 255, 255), (lim_grille_x2, lim_grille_y1), (lim_grille_x2, lim_grille_y2), 5)
    pygame.draw.line(screen, (255, 255, 255), (lim_grille_x1, lim_grille_y1), (lim_grille_x1, lim_grille_y2), 5)
    pygame.draw.line(screen, (255, 255, 255), (lim_grille_x1, lim_grille_y2), (lim_grille_x2, lim_grille_y2), 5)

    TET.draw()
    if Chrono_pour_touche == 0:
        if keys[pygame.K_LEFT] and TET.x > 0:
            TET.Left()      
            Chrono_pour_touche = VITESSE_POUR_LES_TOUCHES
        if keys[pygame.K_RIGHT] and TET.x < 9: 
            TET.Right() 
            Chrono_pour_touche = VITESSE_POUR_LES_TOUCHES

    for i in range(X_G):
        for u in range(Y_G):
            if GRILLE[i][u] != "0":
                text_grille = GRILLE[i][u]
                screen.blit(text_grille, (20+Taille_cube*i, 50+Taille_cube*u)) 


    
    X, Y = pygame.mouse.get_pos()
    if keys[pygame.K_p]:        
        print("X:", X)     
        print("Y:", Y)

    Chrono += 1
    if Chrono_pour_touche > 0:
        Chrono_pour_touche -= 1
    if Chrono == 61:
        Chrono = 1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()