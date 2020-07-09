'''PROGRAMME INCLUANT QUELQUES METHODES'''
'''     UTILES ET UTILISEES SOUVENT    '''

import time
import random

# Liste des indices à échanger en fonction du mouvement à réaliser
R = [2, 5, 8, 29, 32, 35, 47, 50, 53, 9, 12, 15, 36, 37, 42, 39, 44, 43, 38, 41]
Rp = [47, 50, 53, 29, 32, 35, 2, 5, 8, 9, 12, 15, 36, 37, 38, 41, 44, 43, 42, 39]
R2 = [29, 32, 35, 15, 12, 9, 2, 5, 8, 47, 50, 53, 36, 37, 44, 43, 38, 41, 42, 39]

L = [45, 48, 51, 27, 30, 33, 0, 3, 6, 11, 14, 17, 18, 19, 24, 21, 26, 25, 20, 23]
Lp = [0, 3, 6, 27, 30, 33, 45, 48, 51, 11, 14, 17, 18, 19, 20, 23, 26, 25, 24, 21]
L2 = [0, 3, 6, 45, 48, 51, 27, 30, 33, 17, 14, 11, 18, 19, 26, 25, 20, 23, 24, 21]

F = [6, 7, 8, 26, 23, 20, 47, 46, 45, 36, 39, 42, 27, 28, 33, 30, 35, 34, 29, 32]
Fp = [6, 7, 8, 36, 39, 42, 47, 46, 45, 26, 23, 20, 27, 28, 29, 32, 35, 34 ,33, 30]
F2 = [6, 7, 8, 47, 46, 45, 20, 23, 26, 42, 39, 36, 27, 28, 35, 34, 29, 32, 33, 30]

B = [0, 1, 2, 38, 41, 44, 53, 52, 51, 24, 21, 18, 9, 10, 15, 12, 17, 16, 11, 14]
Bp = [0, 1, 2, 24, 21, 18, 53, 52, 51, 38, 41, 44, 9, 10, 11, 14, 17, 16, 15, 12]
B2 = [0, 1, 2, 53, 52, 51, 18, 21, 24, 44, 41, 38, 9, 10, 17, 16, 11, 14, 15, 12]

U = [27, 28, 29, 36, 37, 38, 9, 10, 11, 18, 19, 20, 0, 1, 6, 3, 8, 7, 2, 5]
Up = [27, 28, 29, 18, 19, 20, 9, 10, 11, 36, 37, 38, 0, 1, 2, 5, 8, 7, 6, 3]
U2 = [27, 28, 29, 9, 10, 11, 36, 37, 38, 18, 19, 20, 0, 1, 8, 7, 2, 5, 6, 3]

D = [33, 34, 35, 24, 25, 26, 15, 16 ,17, 42, 43, 44, 45 ,46, 51, 48, 53, 52, 47, 50]
Dp = [33, 34, 35, 42, 43, 44, 15, 16, 17, 24, 25, 26, 45, 46, 47, 50, 53, 52, 51, 48]
D2 = [33, 34, 35, 15, 16, 17, 42, 43, 44, 24, 25, 26, 45, 46, 53, 52, 47, 50, 51, 48]

S = [3, 4, 5, 25, 22, 19, 50, 49, 48, 37, 40, 43]
Sp = [3, 4, 5, 37, 40, 43, 50, 49, 48, 25, 22, 19]
S2 = [3, 4, 5, 50, 49, 48, 19, 22, 25, 43, 40 ,37]

M = [1, 4, 7, 16, 13, 10, 46, 49, 52, 28, 31, 34]
Mp = [1, 4, 7, 28, 31, 34, 46, 49, 52, 16, 13, 10]
M2 = [1, 4, 7, 46, 49, 52, 28, 31, 34, 16, 13, 10]

E = [30, 31, 32, 21, 22, 23, 12, 13, 14, 39, 40, 41]
Ep = [30, 31, 32, 39, 40, 41, 12, 13, 14, 21, 22, 23]
E2 = [30, 31, 32, 12, 13, 14, 21, 22, 23, 39, 40, 41]


def ESM(c, index):

    buf = c[index[0]], c[index[1]], c[index[2]]
    c[index[0]], c[index[1]], c[index[2]] = c[index[3]], c[index[4]], c[index[5]]
    c[index[3]], c[index[4]], c[index[5]] = c[index[6]], c[index[7]], c[index[8]]
    c[index[6]], c[index[7]], c[index[8]] = c[index[9]], c[index[10]], c[index[11]]
    c[index[9]], c[index[10]], c[index[11]] = buf[0], buf[1], buf[2]

    return c

def ESM2(c, index):

    c[index[0]], c[index[1]], c[index[2]], c[index[3]], c[index[4]], c[index[5]] = c[index[3]], c[index[4]], c[index[5]], c[index[0]], c[index[1]], c[index[2]]
    c[index[6]], c[index[7]], c[index[8]], c[index[9]], c[index[10]], c[index[11]] = c[index[9]], c[index[10]], c[index[11]], c[index[6]], c[index[7]], c[index[8]]

    return c

#---------------Méthode UDFBRL---------------#
# Execute le mouvement passé en paramètres
# sur le cube passé en paramètres (seulement
# les mouvements sans "2" sont acceptés)
# 
def UDFBRL(c, index):
    
    buf = c[index[0]], c[index[1]], c[index[2]]
    c[index[0]], c[index[1]], c[index[2]] = c[index[3]], c[index[4]], c[index[5]]
    c[index[3]], c[index[4]], c[index[5]] = c[index[6]], c[index[7]], c[index[8]]
    
    if index[1] == 5 or index[1] == 50 or index[1] == 32 or index[1] == 48 or index[1] == 3:

        c[index[6]], c[index[7]], c[index[8]] = c[index[11]], c[index[10]], c[index[9]]
        c[index[9]], c[index[10]], c[index[11]] = buf[2], buf[1], buf[0]

    else:

        c[index[6]], c[index[7]], c[index[8]] = c[index[9]], c[index[10]], c[index[11]]
        c[index[9]], c[index[10]], c[index[11]] = buf[0], buf[1], buf[2]    

    buf = c[index[12]], c[index[13]]
    c[index[12]], c[index[13]] = c[index[14]], c[index[15]]
    c[index[14]], c[index[15]] = c[index[16]], c[index[17]]
    c[index[16]], c[index[17]] = c[index[18]], c[index[19]]
    c[index[18]], c[index[19]] = buf[0], buf[1]
    
    return c


#---------------Méthode UDFBRL2---------------#
# Execute le mouvement passé en paramètres
# sur le cube passé en paramètres (seulement
# les mouvements en "2" sont acceptés)
# 
def UDFBRL2(c, index):
    
    c[index[0]], c[index[1]], c[index[2]], c[index[3]], c[index[4]], c[index[5]] = c[index[3]], c[index[4]], c[index[5]], c[index[0]], c[index[1]], c[index[2]]
    c[index[6]], c[index[7]], c[index[8]], c[index[9]], c[index[10]], c[index[11]] = c[index[9]], c[index[10]], c[index[11]], c[index[6]], c[index[7]], c[index[8]]

    c[index[12]], c[index[13]], c[index[14]], c[index[15]] = c[index[14]], c[index[15]], c[index[12]], c[index[13]]
    c[index[16]], c[index[17]], c[index[18]], c[index[19]] = c[index[18]], c[index[19]], c[index[16]], c[index[17]]
    
    return c

def numberMove(num, c):
    
    if num == 0:
        c = UDFBRL(c, R)
    elif num == 1:
        c = UDFBRL(c, Rp)
    elif num == 2:
        c = UDFBRL2(c, R2)
    elif num == 3:
        c = UDFBRL(c, L)
    elif num == 4:
        c = UDFBRL(c, Lp)
    elif num == 5:
        c = UDFBRL2(c, L2)
    elif num == 6:
        c = UDFBRL(c, F)
    elif num == 7:
        c = UDFBRL(c, Fp)
    elif num == 8:
        c = UDFBRL2(c, F2)
    elif num == 9:
        c = UDFBRL(c, B)
    elif num == 10:
        c = UDFBRL(c, Bp)
    elif num == 11:
        c = UDFBRL2(c, B2)
    elif num == 12:
        c = UDFBRL(c, U)
    elif num == 13:
        c = UDFBRL(c, Up)
    elif num == 14:
        c = UDFBRL2(c, U2)
    elif num == 15:
        c = UDFBRL(c, D)
    elif num == 16:
        c = UDFBRL(c, Dp)
    elif num == 17:
        c = UDFBRL2(c, D2)

#---------------Méthode minMove---------------#
# Compare deux listes de mouvements entrées en
# paramètres et retourne la plus petite (en
# prenant en compte que les mouvements en
# "2" comptent comme 2 mouvements)
#
def minMove(moves1, moves2):

    len1 = 0
    len2 = 0

    # Calcul de la longueur de la liste n°1
    for move in moves1:

        if (move == "0" and move == "1"
           or move == "3" and move == "4"
           or move == "6" and move == "7"
           or move == "9" and move == "A"
           or move == "C" and move == "D"
           or move == "F" and move == "G"):
            len1 += 1
        else:
            len1 += 2
    # Calcul de la longueur de la liste n°2
    for move in moves2:

        if (move == "0" or move == "1"
           or move == "3" or move == "4"
           or move == "6" or move == "7"
           or move == "9" or move == "A"
           or move == "C" or move == "D"
           or move == "F" or move == "G"):
            len2 += 1
        else:
            len2 += 2

    if len1 > len2:
        return moves2
    else:
        return moves1


#---------------optimizeMove---------------#
# Optimise la liste de mouvements entrée en
# paramètres et la retourne (RR -> R2,
# RR' -> /, ...)
#
def optimizeMove(moves):

    optimizedMove = ""

    i = 0
    
    while i < len(moves):
        
        if i != len(moves) - 1:

            if (moves[i] == "0" and moves[i+1] == "1"
               or moves[i] == "1" and moves[i+1] == "0"
               or moves[i] == "3" and moves[i+1] == "4"
               or moves[i] == "4" and moves[i+1] == "3"
               or moves[i] == "6" and moves[i+1] == "7"
               or moves[i] == "7" and moves[i+1] == "6"
               or moves[i] == "9" and moves[i+1] == "A"
               or moves[i] == "A" and moves[i+1] == "9"
               or moves[i] == "C" and moves[i+1] == "D"
               or moves[i] == "D" and moves[i+1] == "C"
               or moves[i] == "F" and moves[i+1] == "G"
               or moves[i] == "G" and moves[i+1] == "F"
               or moves[i] == "2" and moves[i+1] == "2"
               or moves[i] == "5" and moves[i+1] == "5"
               or moves[i] == "8" and moves[i+1] == "8"
               or moves[i] == "B" and moves[i+1] == "B"
               or moves[i] == "E" and moves[i+1] == "E"
               or moves[i] == "H" and moves[i+1] == "H"):
                   i += 1

            elif moves[i] == "0" and moves[i+1] == "0" or moves[i] == "1" and moves[i+1] == "1":
                optimizedMove += "2"
                i += 1
            elif moves[i] == "3" and moves[i+1] == "3" or moves[i] == "4" and moves[i+1] == "4":
                optimizedMove += "5"
                i += 1
            elif moves[i] == "6" and moves[i+1] == "6" or moves[i] == "7" and moves[i+1] == "7":
                optimizedMove += "8"
                i += 1
            elif moves[i] == "9" and moves[i+1] == "9" or moves[i] == "A" and moves[i+1] == "A":
                optimizedMove += "B"
                i += 1
            elif moves[i] == "C" and moves[i+1] == "C" or moves[i] == "D" and moves[i+1] == "D":
                optimizedMove += "E"
                i += 1
            elif moves[i] == "F" and moves[i+1] == "F" or moves[i] == "G" and moves[i+1] == "G":
                optimizedMove += "H"
                i += 1

            elif moves[i] == "0" and moves[i+1] == "2" or moves[i] == "2" and moves[i+1] == "0":
                optimizedMove += "1"
                i += 1
            elif moves[i] == "1" and moves[i+1] == "2" or moves[i] == "2" and moves[i+1] == "1":
                optimizedMove += "0"
                i += 1
            elif moves[i] == "3" and moves[i+1] == "5" or moves[i] == "5" and moves[i+1] == "3":
                optimizedMove += "4"
                i += 1
            elif moves[i] == "4" and moves[i+1] == "5" or moves[i] == "5" and moves[i+1] == "4":
                optimizedMove += "3"
                i += 1
            elif moves[i] == "6" and moves[i+1] == "8" or moves[i] == "8" and moves[i+1] == "6":
                optimizedMove += "7"
                i += 1
            elif moves[i] == "7" and moves[i+1] == "8" or moves[i] == "8" and moves[i+1] == "7":
                optimizedMove += "6"
                i += 1
            elif moves[i] == "9" and moves[i+1] == "B" or moves[i] == "B" and moves[i+1] == "9":
                optimizedMove += "A"
                i += 1
            elif moves[i] == "A" and moves[i+1] == "B" or moves[i] == "B" and moves[i+1] == "A":
                optimizedMove += "9"
                i += 1
            elif moves[i] == "C" and moves[i+1] == "E" or moves[i] == "E" and moves[i+1] == "C":
                optimizedMove += "D"
                i += 1
            elif moves[i] == "D" and moves[i+1] == "E" or moves[i] == "E" and moves[i+1] == "D":
                optimizedMove += "C"
                i += 1
            elif moves[i] == "F" and moves[i+1] == "H" or moves[i] == "H" and moves[i+1] == "F":
                optimizedMove += "G"
                i += 1
            elif moves[i] == "G" and moves[i+1] == "H" or moves[i] == "H" and moves[i+1] == "G":
                optimizedMove += "F"
                i += 1

            else:

                optimizedMove += moves[i]
                if i == len(moves) - 2:

                    optimizedMove += moves[len(moves)-1]
                    i+=1
        else:
            optimizedMove += moves[i]
            
        i += 1
        
    return optimizedMove

def applyLetterMove(moves, c):

    for move in moves:

        if move == "0":
            c = UDFBRL(c, R)
        elif move == "1":
            c = UDFBRL(c, Rp)
        elif move == "2":
            c = UDFBRL2(c, R2)
        elif move == "3":
            c = UDFBRL(c, L)
        elif move == "4":
            c = UDFBRL(c, Lp)
        elif move == "5":
            c = UDFBRL2(c, L2)
        elif move == "6":
            c = UDFBRL(c, F)
        elif move == "7":
            c = UDFBRL(c, Fp)
        elif move == "8":
            c = UDFBRL2(c, F2)
        elif move == "9":
            c = UDFBRL(c, B)
        elif move == "A":
            c = UDFBRL(c, Bp)
        elif move == "B":
            c = UDFBRL2(c, B2)
        elif move == "C":
            c = UDFBRL(c, U)
        elif move == "D":
            c = UDFBRL(c, Up)
        elif move == "E":
            c = UDFBRL2(c, U2)
        elif move == "F":
            c = UDFBRL(c, D)
        elif move == "G":
            c = UDFBRL(c, Dp)
        elif move == "H":
            c = UDFBRL2(c, D2)
        

def lenghtMove(moves):

    l = 0

    for move in moves:

        if move in ["2", "5", "8", "B", "E", "H"]:
            l += 2
        else:
            l += 1
            
    return l

#---------------Méthode printCube---------------#
# Affiche une représentation du cube entré
# en paramètres avec cette forme ci :
#     U0 U1 U2
#     U3 U4 U5
#     U6 U7 U8
#
#     B0 B1 B2
#     B3 B4 B5
#     B6 B7 B8
#
#     L0 L1 L2
#     L3 L4 L5
#     L6 L7 L8
#
#     F0 F1 F2
#     F3 F4 F5
#     F6 F7 F8
#
#     R0 R1 R2
#     R3 R4 R5
#     R6 R7 R8
#
#     D0 D1 D2
#     D3 D4 D5
#     D6 D7 D8
#
def printCube(c):
    
    for i in range(len(c)):
        if(i%3 == 2):
            print(c[i])
        else:
            print(c[i], end=" ")

        if(i%9 == 8):
            print()


#---------------Méthode printMoves---------------#
# Convertie la suite de mouvements entrés en
# paramètres (les mouvements étants indiqués avec la
# représentation du programme) en mouvements écrits
# avec la représentation algorithmique et l'affiche
#
def printMove(nums):

    moves = ""
    
    for num in nums:

        # Conversion du mouvement
        if num == "0":
            moves += "R"
        elif num == "1":
            moves += "R'"
        elif num == "2":
            moves += "R2"
        elif num == "3":
            moves += "L"
        elif num == "4":
            moves += "L'"
        elif num == "5":
            moves += "L2"
        elif num == "6":
            moves += "F"
        elif num == "7":
            moves += "F'"
        elif num == "8":
            moves += "F2"
        elif num == "9":
            moves += "B"
        elif num == "A":
            moves += "B'"
        elif num == "B":
            moves += "B2"
        elif num == "C":
            moves += "U"
        elif num == "D":
            moves += "U'"
        elif num == "E":
            moves += "U2"
        elif num == "F":
            moves += "D"
        elif num == "G":
            moves += "D'"
        elif num == "H":
            moves += "D2"

    print(moves)
        

d = {"R" : R, "R'" : Rp, "R2" : R2,
     "F" : F, "F'" : Fp, "F2" : F2,
     "L" : L, "L'" : Lp, "L2" : L2,
     "U" : U, "U'" : Up, "U2" : U2,
     "D" : D, "D'" : Dp, "D2" : D2,
     "B" : B, "B'" : Bp, "B2" : B2,
     "E" : E, "E'" : Ep, "E2" : E2,
     "S" : S, "S'" : Sp, "S2" : S2,
     "M" : M, "M'" : Mp, "M2" : M2}

d1 = {"R" : UDFBRL, "R'" : UDFBRL, "R2" : UDFBRL2,
      "F" : UDFBRL, "F'" : UDFBRL, "F2" : UDFBRL2,
      "L" : UDFBRL, "L'" : UDFBRL, "L2" : UDFBRL2,
      "U" : UDFBRL, "U'" : UDFBRL, "U2" : UDFBRL2,
      "D" : UDFBRL, "D'" : UDFBRL, "D2" : UDFBRL2,
      "B" : UDFBRL, "B'" : UDFBRL, "B2" : UDFBRL2,
      "E" : ESM, "E'" : ESM, "E2" : ESM2,
      "S" : ESM, "S'" : ESM, "S2" : ESM2,
      "M" : ESM, "M'" : ESM, "M2" : ESM2}

#---------------Méthode applyMove---------------#
# Exécute les mouvements sur le cube entré en
# paramètres (les mouvements étants indiqués avec
# la représentation algorithmique)
#
def applyMove(c, moves):
    
    for i in range(len(moves)):
        
        move = moves[i]

        # Les mouvements étant indiqués littéralement
        # (R', R, ...), il faut vérifier le caractère
        # suivant afin de vérifier si le mouvement est
        # en "'" ou "2"
        try:
            
            if moves[i+1] == "'":

                move += "'"
            elif moves[i+1] == "2":

                move += "2"
        except:
            pass
        
        try:
            d1[move](c, d[move])
        except:
            pass
    
    return c

def inverse(moves):

    inv = ""

    moves = moves[::-1]
    
    for move in moves:
        
        if move == "0":
            inv += "1"
        elif move == "1":
            inv += "0"
        elif move == "2":
            inv += "2"
        elif move == "3":
            inv += "4"
        elif move == "4":
            inv += "3"
        elif move == "5":
            inv += "5"
        elif move == "6":
            inv += "7"
        elif move == "7":
            inv += "6"
        elif move == "8":
            inv += "8"
        elif move == "9":
            inv += "A"
        elif move == "A":
            inv += "9"
        elif move == "B":
            inv += "B"
        elif move == "C":
            inv += "D"
        elif move == "D":
            inv += "C"
        elif move == "E":
            inv += "E"
        elif move == "F":
            inv += "G"
        elif move == "G":
            inv += "F"
        elif move == "H":
            inv += "H"
    
    return inv

inv = {"R" : "R'", "R'" : "R", "R2" : "R2",
     "F" : "F'", "F'" : "F", "F2" : "D2",
     "L" : "L'", "L'" : "L", "L2" : "L2",
     "U" : "U'", "U'" : "U", "U2" : "U2",
     "D" : "D'", "D'" : "D", "D2" : "D2",
     "B" : "B'", "B'" : "B", "B2" : "B2",
     "E" : "E'", "E'" : "E", "E2" : "E2",
     "S" : "S'", "S'" : "S", "S2" : "S2",
     "M" : "M'", "M'" : "M", "M2" : "M2"}

def invMove(moves):

    conv = ""
        
    for i in range(len(moves)):

        move = moves[i]

        # Les mouvements étant indiqués littéralement
        # (R', R, ...), il faut vérifier le caractère
        # suivant afin de vérifier si le mouvement est
        # en "'" ou "2"
        try:
    
            if moves[i+1] == "'":

                move += "'"
            elif moves[i+1] == "2":

                move += "2"
        except:
            pass

        try:
            conv += inv[move]
        except:
            pass

    return conv

faces = ["RX", "LX", "UY", "DY", "FZ", "BZ"]

def randomRotation():

    r = random.randint(0, 2)

    if r == 0:
        return ""
    elif r == 1:
        return "'"
    else:
        return "2"

def randomFace(lastFace):

    face = faces[random.randint(0, 5)]

    if face[1] == lastFace[1]:
        return randomFace(lastFace)
    else:
        return face

def generateScramble():

    scramble = ''
    lastFace = '  '

    for i in range(24):
        lastFace = randomFace(lastFace)
        scramble += lastFace[0] + randomRotation() + ' '

    return scramble[:-1]

Sdict = {"R" : "F", "R'" : "L", "R2" : "R",
         "U" : "D", "U'" : "J", "U2" : "P",
         "L" : "E", "L'" : "L", "L2" : "R",
         "D" : "B", "D'" : "H", "D2" : "N",
         "F" : "A", "F'" : "G", "F2" : "M",
         "B" : "C", "B'" : "I", "B2" : "O"}

Spdict = {"R" : "E", "R'" : "K", "R2" : "Q",
          "U" : "B", "U'" : "H", "U2" : "N",
          "L" : "F", "L'" : "L", "L2" : "R",
          "D" : "D", "D'" : "J", "D2" : "P",
          "F" : "A", "F'" : "G", "F2" : "M",
          "B" : "C", "B'" : "I", "B2" : "O"}

S2dict = {"R" : "D", "R'" : "J", "R2" : "P",
          "U" : "E", "U'" : "K", "U2" : "Q",
          "L" : "B", "L'" : "H", "L2" : "N",
          "D" : "F", "D'" : "L", "D2" : "R",
          "F" : "A", "F'" : "G", "F2" : "M",
          "B" : "C", "B'" : "I", "B2" : "O"}

Mdict = {"F" : "F", "F'" : "L", "F2" : "R",
         "U" : "C", "U'" : "I", "U2" : "O",
         "B" : "E", "B'" : "K", "B2" : "Q",
         "D" : "A", "D'" : "G", "D2" : "M",
         "R" : "B", "R'" : "H", "R2" : "N",
         "L" : "D", "L'" : "J", "L2" : "P"}

Mpdict = {"F" : "E", "F'" : "K", "F2" : "Q",
          "U" : "A", "U'" : "G", "U2" : "M",
          "B" : "F", "B'" : "L", "B2" : "R",
          "D" : "C", "D'" : "I", "D2" : "O",
          "R" : "B", "R'" : "H", "R2" : "N",
          "L" : "D", "L'" : "J", "L2" : "P"}

M2dict = {"F" : "C", "F'" : "I", "F2" : "O",
          "U" : "E", "U'" : "K", "U2" : "Q",
          "B" : "A", "B'" : "G", "B2" : "M",
          "D" : "F", "D'" : "L", "D2" : "R",
          "R" : "B", "R'" : "H", "R2" : "N",
          "L" : "D", "L'" : "J", "L2" : "P"}

Edict = {"R" : "A", "R'" : "G", "R2" : "M",
         "F" : "D", "F'" : "J", "F2" : "P",
         "L" : "C", "L'" : "I", "L2" : "O",
         "B" : "B", "B'" : "H", "B2" : "N",
         "U" : "F", "U'" : "L", "U2" : "R",
         "D" : "E", "D'" : "K", "D2" : "Q"}

Epdict = {"R" : "C", "R'" : "I", "R2" : "O",
          "F" : "B", "F'" : "H", "F2" : "N",
          "L" : "A", "L'" : "G", "L2" : "M",
          "B" : "D", "B'" : "J", "B2" : "P",
          "U" : "F", "U'" : "L", "U2" : "R",
          "D" : "E", "D'" : "K", "D2" : "Q"}

E2dict = {"R" : "D", "R'" : "J", "R2" : "P",
          "F" : "C", "F'" : "I", "F2" : "O",
          "L" : "B", "L'" : "H", "L2" : "N",
          "B" : "A", "B'" : "G", "B2" : "M",
          "U" : "F", "U'" : "L", "U2" : "R",
          "D" : "E", "D'" : "K", "D2" : "Q"}

symbol = {"R" : "B", "R'" : "H", "R2" : "N",
          "L" : "D", "L'" : "J", "L2" : "P",
          "F" : "A", "F'" : "G", "F2" : "M",
          "B" : "C", "B'" : "I", "B2" : "O",
          "U" : "F", "U'" : "L", "U2" : "R",
          "D" : "E", "D'" : "K", "D2" : "Q"}

def convertToSymbols(moves):

    Sb = False
    Spb = False
    S2b = False
    Mb = False
    Mpb = False
    M2b = False
    Eb = False
    Epb = False
    E2b = False

    conv = ""
    
    for i in range(len(moves)):
        
        move = moves[i]

        # Les mouvements étant indiqués littéralement
        # (R', R, ...), il faut vérifier le caractère
        # suivant afin de vérifier si le mouvement est
        # en "'" ou "2"
        try:
            
            if moves[i+1] == "'":

                move += "'"
            elif moves[i+1] == "2":

                move += "2"
        except:
            pass

        try:

            if move == "S":

                conv += "U"
                
                if Sb:

                    Sb = False
                    S2b = True

                elif Spb:
                    Spb = False

                elif S2b:

                    S2b = False
                    Spb = True

                else:
                    Sb = True

            elif move == "S'":

                conv += "T"
                    
                if Sb:
                    Sb = False

                elif Spb:

                    Spb = False
                    S2b = True

                elif S2b:

                    S2b = False
                    Sb = True

                else:
                    Spb = True

            elif move == "S2":

                conv += "W"
                
                if Sb:

                    Sb = False
                    Spb = True

                elif Spb:

                    Spb = False
                    Sb = True

                elif S2b:
                    S2b = False

                else:
                    S2b = True

            elif move == "M":

                conv += "Y"
                
                if Mb:

                    Mb = False
                    M2b = True

                elif Mpb:
                    Mpb = False

                elif M2b:

                    M2b = False
                    Mpb = True

                else:
                    Mb = True

            elif move == "M'":

                conv += "Z"
                
                if Mb:
                    Mb = False

                elif Mpb:

                    Mpb = False
                    M2b = True

                elif M2b:

                    M2b = False
                    Mb = True

                else:
                    Mpb = True

            elif move == "M2":

                conv += "\\"
            
                if Mb:

                    Mb = False
                    Mpb = True

                elif Mpb:

                    Mpb = False
                    Mb = True

                elif M2b:
                    M2b = False

                else:
                    M2b = True

            elif move == "E":

                conv += "_"
                
                if Eb:

                    Eb = False
                    E2b = True

                elif Epb:
                    Epb = False

                elif E2b:

                    E2b = False
                    Epb = True

                else:
                    Eb = True

            elif move == "E'":

                conv += "^"
                
                if Eb:
                    Eb = False

                elif Epb:

                    Epb = False
                    E2b = True

                elif E2b:

                    E2b = False
                    Eb = True

                else:
                    Epb = True

            elif move == "E2":

                conv += "a"
                
                if Eb:

                    Eb = False
                    Epb = True

                elif Epb:

                    Epb = False
                    Eb = True

                elif E2b:
                    E2b = False

                else:
                    E2b = True
            
            else:
                
                if Sb:
                    conv += Sdict[move]
                elif Spb:
                    conv += Spdict[move]
                elif S2b:
                    conv += S2dict[move]
                elif Mb:
                    conv += Mdict[move]
                elif Mpb:
                    conv += Mpdict[move]
                elif M2b:
                    conv += M2dict[move]
                elif Eb:
                    conv += Edict[move]
                elif Epb:
                    conv += Epdict[move]
                elif E2b:
                    conv += E2dict[move]
                elif move != "'" and move != "2":
                    conv += symbol[move]
        except:
            pass
        
    return conv

'''
F : A    F' : G    F2 : M
R : B    R' : H    R2 : N
B : C    B' : I    B2 : O
L : D    L' : J    L2 : P
D : E    D' : K    D2 : Q
U : F    U' : L    U2 : R

FB   : S    RL   : X    DU   : ]
FB'  : T    RL'  : Y    DU'  : ^
F'B  : U    R'L  : Z    D'U  : _
F'B' : V    R'L' : [    D'U' : `
F2B2 : W    R2L2 : \    D2U2 : a

FB2  : b    RL2  : f    DU2  : j
F'B2 : c    R'L2 : g    D'U2 : k
F2B  : d    R2L  : h    D2U  : l
F2B' : e    R2L' : i    D2U' : m
'''

letter = {'A' : "F", 'B' : "R", 'C' : "B", 'D' : "L", 'E' : "D", 'F' : 'U',
          'G' : "F'", 'H' : "R'", 'I' : "B'", 'J' : "L'", 'K' : "D'", 'L' : "U'",
          'M' : "F2", 'N' : "R2", 'O' : "B2", 'P' : "L2", 'Q' : "D2", 'R' : "U2",
          'S' : "FB", 'T' : "FB'", 'U' : "F'B", 'V' : "F'B'", 'W' : 'F2B2',
          'X' : "RL", 'Y' : "RL'", 'Z' : "R'L", '[' : "R'L'", '\\' : "R2L2",
          ']' : "DU", '^' : "DU'", '_' : "D'U", '`' : "D'U'", 'a' : "D2U2",
          'b' : "FB2", 'c' : "F'B2", 'd' : "F2B", 'e' : "F2B'",
          'f' : "RL2", 'g' : "R'L2", 'h' : "R2L", 'i' : "R2L'",
          'j' : "DU2", 'k' : "D'U2", 'l' : "D2U", 'm' : "D2U'"}
          
lenMove = {'A' : 1, 'B' : 1, 'C' : 1, 'D' : 1, 'E' : 1, 'F' : 1,
     'G' : 1, 'H' : 1, 'I' : 1, 'J' : 1, 'K' : 1, 'L' : 1,
     'M' : 2, 'N' : 2, 'O' : 2, 'P' : 2, 'Q' : 2, 'R' : 2,
     'S' : 1, 'T' : 1, 'U' : 1, 'V' : 1, 'W' : 2,
     'X' : 1, 'Y' : 1, 'Z' : 1, '[' : 1, '\\' : 2,
     ']' : 1, '^' : 1, '_' : 1, '`' : 1, 'a' : 2,
     'b' : 2, 'c' : 2, 'd' : 2, 'e' : 2,
     'f' : 2, 'g' : 2, 'h' : 2, 'i' : 2,
     'j' : 2, 'k' : 2, 'l' : 2, 'm' : 2}

def lenght(moves):

    l = 0

    for move in moves:
        l += lenMove[move]

    return l
    

def convertToLetters(moves):

    conv = ""

    for move in moves:
        conv += letter[move]

    return conv


optiDic2 = {'SA' : 'd', 'AS' : 'd', 'SG' : 'C', 'GS' : 'C', 'SM' : 'U', 'MS' : 'U',
            'TA' : 'e', 'AT' : 'e', 'TG' : 'I', 'GT' : 'I', 'TM' : 'V', 'MT' : 'V',
            'UA' : 'C', 'AU' : 'C', 'UG' : 'd', 'GU' : 'd', 'UM' : 'S', 'MU' : 'S',
            'VA' : 'I', 'AV' : 'I', 'VG' : 'e', 'GV' : 'e', 'VM' : 'T', 'MV' : 'T',
            'WA' : 'c', 'AW' : 'c', 'WG' : 'b', 'GW' : 'b', 'WM' : 'O', 'MW' : 'O',
            'SC' : 'b', 'CS' : 'b', 'SI' : 'A', 'IS' : 'A', 'SO' : 'T', 'OS' : 'T',
            'TC' : 'A', 'CT' : 'A', 'TI' : 'b', 'IT' : 'b', 'TO' : 'S', 'OT' : 'S',
            'UC' : 'c', 'CU' : 'c', 'UI' : 'G', 'IU' : 'G', 'UO' : 'V', 'OU' : 'V',
            'VC' : 'G', 'CV' : 'G', 'VI' : 'c', 'IV' : 'c', 'VO' : 'U', 'OV' : 'U',
            'WC' : 'e', 'CW' : 'e', 'WI' : 'd', 'IW' : 'd', 'WO' : 'M', 'OW' : 'M',
            
            'XB' : 'h', 'BX' : 'h', 'XH' : 'D', 'HX' : 'D', 'XN' : 'Z', 'NX' : 'Z',
            'YB' : 'i', 'BY' : 'i', 'YH' : 'J', 'HY' : 'J', 'YN' : '[', 'NY' : '[',
            'ZB' : 'D', 'BZ' : 'D', 'ZH' : 'h', 'HZ' : 'h', 'ZN' : 'X', 'NZ' : 'X',
            '[B' : 'J', 'B[' : 'J', '[H' : 'i', 'H[' : 'i', '[N' : 'Y', 'N[' : 'Y',
            '\\B' : 'g', 'B\\' : 'g', '\\H' : 'f', 'H\\' : 'f', '\\N' : 'P', 'N\\' : 'P',
            'XD' : 'f', 'DX' : 'f', 'XJ' : 'B', 'JX' : 'B', 'XP' : 'Y', 'PX' : 'Y',
            'YD' : 'B', 'DY' : 'B', 'YJ' : 'f', 'JY' : 'f', 'YP' : 'X', 'PY' : 'X',
            'ZD' : 'g', 'DZ' : 'g', 'ZJ' : 'H', 'JZ' : 'H', 'ZP' : '[', 'PZ' : '[',
            '[D' : 'H', 'D[' : 'H', '[J' : 'g', 'J[' : 'g', '[P' : 'Z', 'P[' : 'Z',
            '\\D' : 'i', 'D\\' : 'i', '\\J' : 'h', 'J\\' : 'h', '\\P' : 'N', '\\P' : 'N',

            ']E' : 'l', 'E]' : 'l', ']K' : 'F', 'K]' : 'F', ']Q' : '_', 'Q]' : '_',
            '^E' : 'm', 'E^' : 'm', '^K' : 'L', 'K^' : 'L', '^Q' : '`', 'Q^' : '`',
            '_E' : 'F', 'E_' : 'F', '_K' : 'l', 'K_' : 'l', '_Q' : ']', 'Q_' : ']',
            '`E' : 'L', 'E`' : 'L', '`K' : 'm', 'K`' : 'm', '`Q' : '^', 'Q`' : '^',
            'aE' : 'k', 'Ea' : 'k', 'aK' : 'j', 'Ka' : 'j', 'aQ' : 'R', 'Qa' : 'R',
            ']F' : 'j', 'F]' : 'j', ']L' : 'E', 'L]' : 'E', ']R' : '^', 'R]' : '^',
            '^F' : 'E', 'F^' : 'E', '^L' : 'j', 'L^' : 'j', '^R' : ']', 'R^' : ']',
            '_F' : 'k', 'F_' : 'k', '_L' : 'K', 'L_' : 'K', '_R' : '`', 'R_' : '`',
            '`F' : 'K', 'F`' : 'K', '`L' : 'k', 'L`' : 'k', '`R' : '_', 'R`' : '_',

            'bA' : 'W', 'Ab' : 'W', 'bG' : 'O', 'Gb' : 'O', 'bM' : 'c', 'Mb' : 'c',
            'cA' : 'O', 'Ac' : 'O', 'cG' : 'W', 'Gc' : 'W', 'cM' : 'b', 'Mc' : 'b',
            'dA' : 'U', 'Ad' : 'U', 'dG' : 'b', 'Gd' : 'b', 'dM' : 'C', 'Md' : 'C',
            'eA' : 'V', 'Ae' : 'V', 'eG' : 'T', 'Ge' : 'T', 'eM' : 'I', 'Me' : 'I',
            'bC' : 'T', 'Cb' : 'T', 'bI' : 'S', 'Ib' : 'S', 'bO' : 'A', 'Ob' : 'A',
            'cC' : 'V', 'Cc' : 'V', 'cI' : 'U', 'Ic' : 'U', 'cO' : 'G', 'Oc' : 'G',
            'dC' : 'W', 'Cd' : 'W', 'dI' : 'M', 'Id' : 'M', 'dO' : 'e', 'Od' : 'e',
            'eC' : 'M', 'Ce' : 'M', 'eI' : 'W', 'Ie' : 'W', 'eO' : 'd', 'Oe' : 'd',

            'fB' : '\\', 'Bf' : '\\', 'fH' : 'P', 'Hf' : 'P', 'fN' : 'g', 'Nf' : 'g',
            'gB' : 'P', 'Bg' : 'P', 'gH' : '\\', 'Hg' : '\\', 'gN' : 'f', 'Ng' : 'f',
            'hB' : 'Z', 'Bh' : 'Z', 'hH' : 'X', 'Hh' : 'X', 'hN' : 'D', 'Nh' : 'D',
            'iB' : '[', 'Bi' : '[', 'iH' : 'Y', 'Hi' : 'Y', 'iN' : 'J', 'Ni' : 'J',
            'fD' : 'Y', 'Df' : 'Y', 'fJ' : 'X', 'Jf' : 'X', 'fP' : 'B', 'Pf' : 'B',
            'gD' : 'Z', 'Dg' : 'Z', 'gJ' : 'Z', 'Jg' : 'Z', 'gP' : 'H', 'Pg' : 'H',
            'hD' : '\\', 'Dh' : '\\', 'hJ' : 'N', 'Jh' : 'N', 'hP' : 'i', 'Ph' : 'i',
            'iD' : 'N', 'Di' : 'N', 'iJ' : '\\', 'Ji' : '\\', 'iP' : 'h', 'Pi' : 'h',

            'jE' : 'a', 'Ej' : 'a', 'jK' : 'R', 'Kj' : 'R', 'jQ' : 'k', 'Qj' : 'k',
            'kE' : 'R', 'Ek' : 'R', 'kK' : 'a', 'Kk' : 'a', 'kQ' : 'j', 'Qk' : 'j',
            'lE' : '_', 'El' : '_', 'lK' : ']', 'Kl' : ']', 'lQ' : 'F', 'Ql' : 'F',
            'mE' : '`', 'Em' : '`', 'mK' : '^', 'Km' : '^', 'mQ' : 'L', 'Qm' : 'L',
            'jF' : '^', 'Fj' : '^', 'jL' : ']', 'Lj' : ']', 'jR' : 'E', 'Rj' : 'E',
            'kF' : '`', 'Fk' : '`', 'kL' : '_', 'Lk' : '_', 'kR' : 'K', 'Rk' : 'K',
            'lF' : 'a', 'Fl' : 'a', 'lL' : 'Q', 'Ll' : 'Q', 'lR' : 'm', 'Rl' : 'm',
            'mF' : 'Q', 'Fm' : 'Q', 'mL' : 'a', 'Lm' : 'a', 'mR' : 'l', 'Rm' : 'l',

            'UU' : '', 'TT' : '', 'WW' : '', 'YY' : '', 'ZZ' : '',
            '\\\\' : '', '__' : '', '^^' : '', 'aa' : ''}

optiDic = {'AG' : '', 'GA' : '', 'MM' : '', 'BH' : '', 'HB' : '', 'NN' : '',
           'CI' : '', 'IC' : '', 'OO' : '', 'DJ' : '', 'JD' : '', 'PP' : '',
           'EK' : '', 'KE' : '', 'QQ' : '', 'FL' : '', 'LF' : '', 'RR' : '',
           'AA' : 'M', 'GG' : 'M', 'BB' : 'N', 'HH' : 'N', 'CC' : 'O', 'II' : 'O',
           'DD' : 'P', 'JJ' : 'P', 'EE' : 'Q', 'KK' : 'Q', 'FF' : 'R', 'LL' : 'R',
           'AM' : 'G', 'MA' : 'G', 'GM' : 'A', 'MG' : 'A',
           'BN' : 'H', 'NB' : 'H', 'HN' : 'B', 'NH' : 'B',
           'CO' : 'I', 'OC' : 'I', 'IO' : 'C', 'OI' : 'C',
           'DP' : 'J', 'PD' : 'J', 'JP' : 'D', 'PJ' : 'D',
           'EQ' : 'K', 'QE' : 'K', 'KQ' : 'E', 'QK' : 'E',
           'FR' : 'L', 'RF' : 'L', 'LR' : 'F', 'RL' : 'F'}

def opti(moves):

    opti = moves[0]

    for move in moves[1:]:

        if len(opti) > 0:
            try :
                
                c = optiDic[opti[-1] + move]
                opti = opti[:-1]
                opti += c

            except:
                opti += move
        else:
            opti += move
    try:
        
        opti2 = opti[0]

        for move in opti[1:]:

            if len(opti2) > 0:
                
                try:
                    c = optiDic2[opti2[-1] + move]
                    opti2 = opti2[:-1]
                    opti2 += c

                except:
                    opti2 += move
            else:
                opti2 += move
    except:
        return ''
        
    return opti2
