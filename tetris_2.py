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
         
         [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]],
         
         [[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         
         [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]]]
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
Bloc = [[[0, 0, 1, 1],
         [0, 0, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],

        [[0, 0, 1, 1],
         [0, 0, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],

        [[0, 0, 1, 1],
         [0, 0, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],

        [[0, 0, 1, 1],
         [0, 0, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]]
T = [[[0, 1, 0, 0],
      [1, 1, 1, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]],

     [[0, 1, 0, 0],
      [0, 1, 1, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0]],

     [[1, 1, 1, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0],
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
                if self.type[self.etat%4][i][u] == 1:
                    if not self.x+i < 0 and not self.x+i > 9 and not self.y > 17:
                        GRILLE[(self.x+i)][(self.y+u)] = self.color

    def check_collision(self, dx, dy, etat):
        for i in range(4):
            for u in range(4):
                if self.type[etat % 4][i][u] == 1:
                    X = self.x + i + dx
                    Y = self.y + u + dy

                    if X < 0 or X >= X_G or Y >= Y_G:
                        return True

                    if Y >= 0 and GRILLE_FIXE[X][Y] != "0":
                        return True
        return False


    def update(self):
        if self.active and not self.check_collision(0, 1, self.etat):            
            self.y += 1
        if self.check_collision(0, 1, self.etat):
            self.active = False
            for i in range(4):
                for u in range(4):
                    if self.type[self.etat % 4][i][u] == 1:
                        X = self.x + i
                        Y = self.y + u
                        if Y >= 0:
                            GRILLE_FIXE[X][Y] = self.color


    def Right(self):
        if self.active and not self.check_collision(1, 0, self.etat):
            self.x += 1

    def Left(self):
        if self.active and not self.check_collision(-1, 0, self.etat):
            self.x -= 1

run = True
BLOCS = [None]*100
derniere = 0

A = randint(0, 6)
BLOCS[derniere] = Pieces(175, 50, 0, piece_possible[A], couleurs_possibles[A])
Chrono = 0
Chrono_pour_touche = 0
VITESSE_POUR_LES_TOUCHES = 8
GRILLE_FIXE = [["0"] * Y_G for _ in range(X_G)]
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:  # pour arrêter la boucle avec la touche 'r'
        run = False
    GRILLE = [row[:] for row in GRILLE_FIXE]

    if Chrono_pour_touche == 0:
        if keys[pygame.K_LEFT]:
            BLOCS[derniere].Left()      
            Chrono_pour_touche = VITESSE_POUR_LES_TOUCHES
        if keys[pygame.K_RIGHT]: 
            BLOCS[derniere].Right() 
            Chrono_pour_touche = VITESSE_POUR_LES_TOUCHES
        if keys[pygame.K_UP] and not BLOCS[derniere].check_collision(0, 0, BLOCS[derniere].etat+1) and BLOCS[derniere].active:
            BLOCS[derniere].etat += 1
            Chrono_pour_touche = VITESSE_POUR_LES_TOUCHES

    if Chrono % 30 == 0:
        BLOCS[derniere].update()
        if not BLOCS[derniere].active:
            time.sleep(0.1)
            derniere += 1
            A = randint(0, len(piece_possible)-1)
            BLOCS[derniere] = Pieces(175, 50, 0, piece_possible[A], couleurs_possibles[A])
            if BLOCS[derniere].check_collision(0, 0, BLOCS[derniere].etat):
                run = False

    if keys[pygame.K_DOWN]:
        BLOCS[derniere].update()

    screen.fill((100, 0, 215))    
    lim_grille_x1 = 17
    lim_grille_x2 = 322
    lim_grille_y1 = 40
    lim_grille_y2 = 593
    pygame.draw.line(screen, (255, 255, 255), (lim_grille_x2, lim_grille_y1), (lim_grille_x2, lim_grille_y2), 5)
    pygame.draw.line(screen, (255, 255, 255), (lim_grille_x1, lim_grille_y1), (lim_grille_x1, lim_grille_y2), 5)
    pygame.draw.line(screen, (255, 255, 255), (lim_grille_x1, lim_grille_y2), (lim_grille_x2, lim_grille_y2), 5)

    for i in range(len(BLOCS)):
        if BLOCS[i] == None:
            break
        BLOCS[i].draw()                  # ajouter le bloc dans la grille

    for i in range(X_G):
        for u in range(Y_G):            # dessiner la grille
            if GRILLE[i][u] != "0":
                text_grille = GRILLE[i][u]
                screen.blit(text_grille, (20+Taille_cube*i, 50+Taille_cube*u)) 
            else:
                text_grille = font.render("0", True, (255, 255, 255))
                #screen.blit(text_grille, (25+Taille_cube*i, 50+Taille_cube*u))

    X, Y = pygame.mouse.get_pos()
    if keys[pygame.K_p]:        
        print("X:", X)     
        print("Y:", Y)

    if keys[pygame.K_a]:
        for i in range(len(BLOCS)):
            BLOCS[i] = None
            GRILLE_FIXE = [["0"] * Y_G for _ in range(X_G)]
            derniere = 0
            A = randint(0, 6)
            BLOCS[derniere] = Pieces(175, 50, 0, piece_possible[A], couleurs_possibles[A])


    Chrono += 1
    if Chrono_pour_touche > 0:
        Chrono_pour_touche -= 1
    if Chrono == 61:
        Chrono = 1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()