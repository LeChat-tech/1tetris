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

piece_possible = [Barre, L_impair, L_pair, Bloc, T, S_impair, S_pair]           # 7
couleurs_possibles = [Vert, Bleu, Bleu_ciel, Rouge, Jaune, Orange, Rose]    # 7

class Blocs:
    def __init__(self, x, types, color):
        self.x = x
        self.y = 15
        self.type = copy.deepcopy(types)
        self.color = color
        self.etat = 0
        self.active = True
        self.ok = True
        self.ok_bis = True
        self.chrono = 0
        self.chrono_bis = 0
        self.tempo = 1
    def draw(self):
        for i in range(4):
            for u in range(4):
                if self.type[self.etat%4][i][u] == 1:
                        screen.blit(self.color, (self.x+u*20,self.y+i*20))  
    def check_collision(self, x_nv, y_nv):
        for piece in PIECE:
            if piece is None or piece is self:
                continue
            for i in range(4):
                for u in range(4):
                    if self.type[self.etat % 4][i][u] == 1:
                        X = x_nv + u * 20
                        Y = y_nv + i * 20
                        if X < 17 or X >= 343 or Y >= 590:
                            return True
                        for o in range(4):
                            for p in range(4):
                                if piece.type[piece.etat % 4][o][p] == 1:
                                    X2 = piece.x + p * 20
                                    Y2 = piece.y + o * 20
                                    if abs(X-X2) < 20 and (Y == Y2 and abs(X-X2) < 20):
                                        return True
        for i in range(4):
            for u in range(4):
                if self.type[self.etat % 4][i][u] == 1:
                    X = x_nv + u * 20
                    Y = y_nv + i * 20
                    if X < 17 or X >= 343 or Y >= 580:
                        return True
        return False                        

    def update(self):
        if not self.ok:
            self.chrono += 1
        if self.chrono == 12:
            self.ok = True
            self.chrono = 0

        if not self.ok_bis:
            self.chrono_bis += 1
        if self.chrono_bis == 6:
            self.ok_bis = True
            self.chrono_bis = 0

        if self.active:
            if keys[pygame.K_DOWN]:
                if not self.check_collision(self.x, self.y+20):
                    self.y += 20         
                else:
                    self.active = False 
            elif self.tempo % 60 == 0:
                if not self.check_collision(self.x, self.y+20):
                    self.y += 20
                else:
                    self.active = False
      

            if keys[pygame.K_UP] and self.ok:
                self.etat += 1    
                self.ok = False

            if keys[pygame.K_LEFT] and self.ok_bis and not self.check_collision(self.x-20, self.y):
                self.x -= 20  
                self.ok_bis = False
            if keys[pygame.K_RIGHT] and self.ok_bis and not self.check_collision(self.x+20, self.y):
                self.x += 20    
                self.ok_bis = False

def supprimer_ligne(y):
    for piece in PIECE:
        if piece is None:
            continue
        for i in range(4):
            for u in range(4):
                if piece.type[piece.etat % 4][i][u] == 1:
                    Y = piece.y + i * 20
                    if Y == y:
                        piece.type[piece.etat % 4][i][u] = 0

PIECE = [None] * 100
etat_barre = 0
nb_pieces = 1
PIECE[0] = Blocs(150, L_impair, Orange)
x = True
tempo = 0
X = 100
Y = 10
ok = True
ok_bis = True
chrono_pour_touche = 0
chrono_pour_touche_bis = 0
while x:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:  # pour arrêter la boucle avec la touche 'r'
        x = False


    screen.fill((100, 0, 205))    
    pygame.draw.line(screen, (255, 255, 255), (352, 20), (352, 597), 5)
    pygame.draw.line(screen, (255, 255, 255), (26, 20), (26, 597), 5)
    pygame.draw.line(screen, (255, 255, 255), (26, 597), (352, 597), 5)

    for i in range(nb_pieces):
        PIECE[i].update()
        PIECE[i].draw()

    if keys[pygame.K_e]:
        supprimer_ligne(575)

    dernier = PIECE[nb_pieces-1]
    if not keys[pygame.K_DOWN]:
        dernier.tempo += 1
    if dernier.tempo == 61:
        dernier.tempo = 1

    if not dernier.active:
        a = randint(0, 6)
        PIECE[nb_pieces] = Blocs(150, piece_possible[a], couleurs_possibles[a])
        nb_pieces += 1
        time.sleep(0.1)

    pygame.display.flip()
    
    X, Y = pygame.mouse.get_pos()
    if keys[pygame.K_p]:        
        print("X:", X)     
        print("Y:", Y)

    tempo += 1
    if tempo == 61:
        tempo = 0
    clock.tick(60)

pygame.quit()