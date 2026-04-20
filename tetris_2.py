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
font = pygame.font.SysFont('Arial', 25)

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

Barre = [[[0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         
         [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]],
         
        [[0, 0, 0, 0],
          [1, 1, 1, 1],
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

          [[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 0]],

          [[0, 1, 0, 0],
           [0, 1, 1, 1],
           [0, 0, 0, 0],
           [0, 0, 0, 0]],

          [[0, 1, 1, 0],
           [0, 1, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 0]]]
L_impair = [[[0, 1, 1, 1],
             [0, 1, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 1, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0]],

            [[0, 0, 0, 1],
             [0, 1, 1, 1],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 1, 0],
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
T = [[[0, 0, 0, 0],
      [1, 1, 1, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0]],

     [[0, 1, 0, 0],
      [1, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0]],

     [[0, 1, 0, 0],
      [1, 1, 1, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]],

     [[0, 1, 0, 0],
      [0, 1, 1, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0]]]
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
         
X_G = 10
Y_G = 20
GRILLE = ["0"]*X_G
for i in range(len(GRILLE)):
    GRILLE[i] = ["0"]*Y_G

piece_possible = [Barre, L_impair, L_pair, Bloc, T, S_impair, S_pair, ]           # 7
couleurs_possibles = [Vert, Bleu, Bleu_ciel, Rouge, Jaune, Orange, Rose, ]    # 7

class Pieces:
    def __init__(self, x, y, etat, types, couleur):
        self.x = x
        self.y = y
        self.etat = 0
        self.color = couleur
        self.type = types
        self.active = True

    def draw(self):
        global GRILLE
        for i in range(4): 
            for u in range(4):  
                if self.type[self.etat%4][i][u] == 1:
                    X = self.x + u  
                    Y = self.y + i  
                    if 0 <= X < X_G and 0 <= Y < Y_G:
                        GRILLE[X][Y] = self.color

    def check_collision(self, dx, dy, etat):
        for i in range(4):
            for u in range(4):
                if self.type[etat % 4][i][u] == 1:
                    X = self.x + u + dx
                    Y = self.y + i + dy

                    if X < 0 or X >= X_G or Y >= Y_G:
                        return True

                    if Y >= 0 and GRILLE_FIXE[X][Y] != "0":
                        return True
        return False

    def update(self):
        if self.check_collision(0, 1, self.etat):
                    self.active = False
                    for i in range(4):
                        for u in range(4):
                            if self.type[self.etat % 4][i][u] == 1:
                                X = self.x + u
                                Y = self.y + i
                                if Y >= 0:
                                    GRILLE_FIXE[X][Y] = self.color
        if self.active and not self.check_collision(0, 1, self.etat):            
            self.y += 1
        
    def Right(self):
        if self.active and not self.check_collision(1, 0, self.etat):
            self.x += 1
    def Left(self):
        if self.active and not self.check_collision(-1, 0, self.etat):
            self.x -= 1

run = True
BLOCS = [None]*100
derniere = 0

def Adpater_y_pour_le_spawn(piece_a_mettre_ensuite):
    if piece_a_mettre_ensuite == T or piece_a_mettre_ensuite == Barre:
        return 1
    else:
        return 2

A = randint(0, 6)
yp = Adpater_y_pour_le_spawn(piece_possible[A])
BLOCS[derniere] = Pieces(4, yp, 0, piece_possible[A], couleurs_possibles[A])

Chrono = 0
Chrono_pour_touche = 0
Chrono_pour_positions = 0
VITESSE_POUR_LES_TOUCHES = 7
GRILLE_FIXE = [["0"] * Y_G for _ in range(X_G)]

PETITE_GRILLE = [["0"] * 4 for i in range(4)]

B = -1
PAUSE = False
score = 0
x_score = 480

vitesse_de_depart = 30
VITESSE_DE_JEU = vitesse_de_depart
nb_total_lignes = 0
ok = False
################################################################################################################
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if B == -1:
        B = randint(0, len(piece_possible)-1)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:  # pour arrêter la boucle avec la touche 'r'
        run = False

    GRILLE = [row[:] for row in GRILLE_FIXE]
    BLOCS[derniere].draw()

    if Chrono_pour_touche == 0 and not PAUSE:
        if keys[pygame.K_LEFT]:
            BLOCS[derniere].Left()      
            Chrono_pour_touche = VITESSE_POUR_LES_TOUCHES
        if keys[pygame.K_RIGHT]: 
            BLOCS[derniere].Right() 
            Chrono_pour_touche = VITESSE_POUR_LES_TOUCHES
    if Chrono_pour_positions == 0 and not PAUSE:
        if keys[pygame.K_UP] and not BLOCS[derniere].check_collision(0, 0, BLOCS[derniere].etat+1) and BLOCS[derniere].active:
            BLOCS[derniere].etat += 1
            Chrono_pour_positions = VITESSE_POUR_LES_TOUCHES

    if Chrono % VITESSE_DE_JEU == 0 and not PAUSE:
        BLOCS[derniere].update()
        if not BLOCS[derniere].active:
            #time.sleep(0.075)
            derniere += 1
            
            Chrono_pour_touche = 20
            
            yp = Adpater_y_pour_le_spawn(piece_possible[B])
            BLOCS[derniere] = Pieces(4, yp, 0, piece_possible[B], couleurs_possibles[B])
            PETITE_GRILLE = [["0"] * 4 for i in range(4)]
            B = randint(0, len(piece_possible)-1)

            nb_lignes = 0
            for i in range(Y_G):
                ligne_complete = True

                for u in range(X_G):
                    if GRILLE_FIXE[u][i] == "0":
                        ligne_complete = False
                        break

                if ligne_complete:
                    nb_total_lignes += 1
                    nb_lignes += 1
                    time.sleep(0.1)
                    for u in range(X_G):
                        GRILLE_FIXE[u][i] = "0"

                    for y in range(i, 0, -1):
                        for u in range(X_G):
                            GRILLE_FIXE[u][y] = GRILLE_FIXE[u][y-1]

                    for u in range(X_G):
                        GRILLE_FIXE[u][0] = "0"
                    
                    GRILLE = [row[:] for row in GRILLE_FIXE]
            if nb_lignes == 1:
                score += 40
            elif nb_lignes == 2:
                score += 100
            elif nb_lignes == 3:
                score += 300
            elif nb_lignes == 4:
                score += 1200
            nb_lignes = 0



            if BLOCS[derniere].check_collision(0, 0, BLOCS[derniere].etat):
                PAUSE = True

        for i in range(4): 
            for u in range(4):  
                if piece_possible[B][0][i][u] == 1:
                    PETITE_GRILLE[u][i+1] = couleurs_possibles[B]

    if keys[pygame.K_DOWN] and not PAUSE:
        BLOCS[derniere].update()
                ########## DESSIN ########################################################################
    screen.fill((100, 0, 215))    
    lim_grille_x1 = 17
    lim_grille_x2 = 322
    lim_grille_y1 = 40
    lim_grille_y2 = 593
    pygame.draw.line(screen, (255, 255, 255), (lim_grille_x2, lim_grille_y1), (lim_grille_x2, lim_grille_y2), 5)
    pygame.draw.line(screen, (255, 255, 255), (lim_grille_x1, lim_grille_y1), (lim_grille_x1, lim_grille_y2), 5)
    pygame.draw.line(screen, (255, 255, 255), (lim_grille_x1, lim_grille_y2), (lim_grille_x2, lim_grille_y2), 5)

    lim_petite_grille_x1 = 347
    lim_petite_grille_x2 = 473
    lim_petite_grille_y1 = 98
    lim_petite_grille_y2 = 223

    pygame.draw.line(screen, (255, 255, 255), (lim_petite_grille_x1, lim_petite_grille_y1), (lim_petite_grille_x2, lim_petite_grille_y1), 5)
    pygame.draw.line(screen, (255, 255, 255), (lim_petite_grille_x2, lim_petite_grille_y1), (lim_petite_grille_x2, lim_petite_grille_y2), 5)
    pygame.draw.line(screen, (255, 255, 255), (lim_petite_grille_x2, lim_petite_grille_y2), (lim_petite_grille_x1, lim_petite_grille_y2), 5)
    pygame.draw.line(screen, (255, 255, 255), (lim_petite_grille_x1, lim_petite_grille_y2), (lim_petite_grille_x1, lim_petite_grille_y1), 5)

    text_score = font.render(f"Score:", True, (255, 255, 255))
    screen.blit(text_score, (365, 270))  
    autre_text_score = font.render(f"{score}", True, (255, 255, 255))

    if score != 0 and x_score == 480:
        x_score -= 10
    if score > 99 and x_score == 480-10:
        x_score -= 20
    if score > 999 and x_score == 480-20-10:
        x_score -= 20
    if score > 9999 and x_score == 480-20*2-10:
            x_score -= 20
    if score > 99999 and x_score == 480-20*3-10:
        x_score -= 20
    if score > 999999 and x_score == 480-20*4-10:
        x_score -= 20
    screen.blit(autre_text_score, (x_score, 300))

    pygame.draw.line(screen, (125, 125, 125), (335, 345), (485, 345), 5)


    text_lignes = font.render(f"Lignes:", True, (255, 255, 255))
    screen.blit(text_lignes, (365, 360))  
    autre_text_lignes = font.render(f"{nb_total_lignes}", True, (255, 255, 255))
    screen.blit(autre_text_lignes, (355, 390)) 

    for i in range(X_G):
        for u in range(Y_G):            # dessiner la grille
            if GRILLE[i][u] != "0":
                text_grille = GRILLE[i][u]
                screen.blit(text_grille, (20+Taille_cube*i, 50+Taille_cube*u - 2*Taille_cube)) 
            else:
                text_grille = font.render("0", True, (255, 255, 255))
               # screen.blit(text_grille, (25+Taille_cube*i, 50+Taille_cube*u - 2 *Taille_cube))

    for i in range(4):
        for u in range(4):            # dessiner la petite grille
            if PETITE_GRILLE[i][u] != "0":
                text_grille = PETITE_GRILLE[i][u]
                screen.blit(text_grille, (350+Taille_cube*i, 100+Taille_cube*u)) 
            else:
                text_grille = font.render("0", True, (255, 255, 255))
                #screen.blit(text_grille, (355+Taille_cube*i, 100+Taille_cube*u))



    X, Y = pygame.mouse.get_pos()
    if keys[pygame.K_p]:        
        print("X:", X)     
        print("Y:", Y)

    if keys[pygame.K_a]:
        for i in range(len(BLOCS)):
            PAUSE = False
            BLOCS[i] = None
            GRILLE_FIXE = [["0"] * Y_G for i in range(X_G)]
            PETITE_GRILLE = [["0"] * 4 for i in range (4)]
            derniere = 0
            A = randint(0, len(piece_possible)-1)
            Chrono_pour_touche = 20
            score = 0
            yp = Adpater_y_pour_le_spawn(piece_possible[A])
            BLOCS[derniere] = Pieces(4, yp, 0, piece_possible[A], couleurs_possibles[A])
            VITESSE_DE_JEU = 30
            B = -1


    Chrono += 1
    if Chrono_pour_touche > 0:
        Chrono_pour_touche -= 1
    if Chrono_pour_positions > 0:
        Chrono_pour_positions -= 1
    if Chrono == 61:
        Chrono = 1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()