from Arete import *
from Coin import *
from outils import *
import ast
import time

'''print('Valentin le plus beau gosse de la prépa')'''

f = open('BH.txt', 'r')

bh = ast.literal_eval(f.readline())

fini = [0,0,0,0,0,0,0,0,0,
         3,3,3,3,3,3,3,3,3,
         4,4,4,4,4,4,4,4,4,
         1,1,1,1,1,1,1,1,1,
         2,2,2,2,2,2,2,2,2,
         5,5,5,5,5,5,5,5,5]

cube = [0,0,0,0,0,0,0,0,0,
        3,3,3,3,3,3,3,3,3,
        4,4,4,4,4,4,4,4,4,
        1,1,1,1,1,1,1,1,1,
        2,2,2,2,2,2,2,2,2,
        5,5,5,5,5,5,5,5,5]

# Déclaration des couleurs
JAUNE = 0
BLEU = 1
ROUGE = 2
VERT = 3
ORANGE = 4
BLANC = 5

# Booléens représetant si les 4 coins blancs
# sont bien placés
BOBllibre = True
BRBllibre = True
RVBllibre = True
VOBllibre = True

# Algorithmes d'alignement des 8 coins
pllT = "R'FR'F2RU'R'F2R2"
diag = "RU'R'U'F2U'RUR'DR2U"
inv = "R2U'R2U2B2U'B2"
pllTdiag = "RU'RF2R'UR'"
doublediag = "R2F2R2"

# Algorithmes pour faire la face jaune
chaise = "RUR'URU2R'"
chaiseinv = "R'ULU'RUL'"
Pi = "R'UR2U'R2U'R2UR'"
frere = "FRUR'U'F'"
L = "FR'F'RURU'R'"
T = "RUR'U'R'FRF'"
H = "R2U2RU2R2"

# Algorithmes pour placer les coins
# en fonction de leur orientations
JVOj = "LU2L'U'LUL'"
JVOv = "B'U'B"
JVOo = "LUL'"
JRVj = "BU2B'U'BUB'"
JRVr = "R'U'R"
JRVv = "BUB'"
JBRj = "RU2R'U'RUR'"
JBRb = "F'U'F"
JBRr = "RUR'"
JBOj = "L'U2LUL'U'L"
JBOb = "FUF'"
JBOo = "L'U'L"
BOBlb = "FUF'U'FUF'"
BOBlo = "L'U'LUL'U'L"
BRBlb = "F'U'FUF'U'F"
BRBlr = "RUR'U'RUR'"
RVBlr = "R'U'RUR'U'R"
RVBlv = "BUB'U'BUB'"
VOBlv = "B'U'BUB'U'B"
VOBlo = "LUL'U'LUL'"

# Garde en mémoire les coins jaunes et
# leur orientation si mal orientés
facejaune = []

# Compte le nombre de coins jaunes
# bien oritentés
comptjaune = 0
# Compte le nombre de coins jaunes
# orientés sur chaque face
Fcompt = 0
Rcompt = 0
Lcompt = 0
Bcompt = 0

# Booléens représentants les orientations
# des coins de la face jaune et de la face
# blanche
jaunef = False
jauneplltF = False
jauneplltR = False
jauneplltB = False
jauneplltL = False
jaunediag = False
jaunediagF = False
jaunediagR = False
blancf = False
blancplltF = False
blancplltR = False
blancplltB = False
blancplltL = False
blancdiag = False
blancdiagR = False
blancdiagF = False

# Déclaration des 12 arêtes
JV = Arete(0, 0)
JR = Arete(0, 0)
JB = Arete(0, 0)
JO = Arete(0, 0)
VO = Arete(0, 0)
RV = Arete(0, 0)
BR = Arete(0, 0)
BO = Arete(0, 0)
BBl = Arete(0, 0)
RBl = Arete(0, 0)
VBl = Arete(0, 0)
OBl = Arete(0, 0)

# Déclaration des 8 coins
JVO = Coin(0, 0, 0)
JRV = Coin(0, 0, 0)
JBR = Coin(0, 0, 0)
JBO = Coin(0, 0, 0)
BOBl = Coin(0, 0, 0)
BRBl = Coin(0, 0, 0)
RVBl = Coin(0, 0, 0)
VOBl = Coin(0, 0, 0)

# Tableau gardant les arêtes mal placées
Aretes = ['JV', 'JO', 'JB', 'BO', 'BR', 'BBl', 'RV', 'RBl', 'VO', 'OBl', 'VBl']

# 
buf = False

# Mouvements utilisés lors de la remise
# en place des arêtes inversées
resoInter = ''

# String pour stocker les mouvements de
# la résolution
noConvertRes = ''
noConvertSol = ''
Resolution = ''
reso = ''


#---------------Méthode getCube---------------#
# Méthode qui retourne la représentation
# du cube actuelle
#
def getCube():

    global cube
    return cube


#---------------Méthode setCube---------------#
# Méthode qui permet de définir la
# représentation actuelle du cube
#
def setCube(c):

    global cube
    cube = c

#---------------Méthode resetCube---------------#
# Méthode qui permet de remettre la
# représentation du cube à son état initial
#
def resetCube():

    global cube

    cube = [0,0,0,0,0,0,0,0,0,
        3,3,3,3,3,3,3,3,3,
        4,4,4,4,4,4,4,4,4,
        1,1,1,1,1,1,1,1,1,
        2,2,2,2,2,2,2,2,2,
        5,5,5,5,5,5,5,5,5]

#---------------Méthode setCouleur---------------#
# Méthode qui permet de définir les couleurs
# d'une des faces du cube
#
def setCouleur(face, couleur):

    global cube
    
    for i in range(9):
        cube[face*9 + i] = couleur[i]


def randomCube(c):
    
    mel = ""
    
    for i in range(24):

        r = random.randint(0, 17)
        mel += str(r) + " "
        numberMove(r, c)

    return mel


#---------------Méthode colorOpposed---------------#
# Méthode testant si deux couleurs sont opposées
# ROUGE opposé à ORANGE
# VERT opposé à BLEU
#
def colorOpposed(c1, c2):

    if(c1 == VERT and c2 == BLEU or
       c1 == BLEU and c2 == VERT):
        return True

    elif(c1 == ORANGE and c2 == ROUGE or
         c1 == ROUGE and c2 == ORANGE):
        return True

    return False


#---------------Méthode yConversion---------------#
# Méthode convertissant un algorithme pour
# le réaliser après un mouvement y
#
def yConversion(alg):

    conv = ''
    
    for c in alg:

        if c == 'R':
            conv += 'B'
        elif c == 'L':
            conv += 'F'
        elif c == 'B':
            conv += 'L'
        elif c == 'F':
            conv += 'R'
        else:
            conv += c

    return conv


#---------------Méthode yConversion---------------#
# Méthode convertissant un algorithme pour
# le réaliser après un mouvement y'
#
def ypConversion(alg):
    
    conv = ''

    for c in alg:

        if c == 'R':
            conv += 'F'
        elif c == 'L':
            conv += 'B'
        elif c == 'B':
            conv += 'R'
        elif c == 'F':
            conv += 'L'
        else:
            conv += c

    return conv


#---------------Méthode yConversion---------------#
# Méthode convertissant un algorithme pour
# le réaliser après un mouvement y2
#
def y2Conversion(alg):
    
    conv = ''

    for c in alg:

        if c == 'R':
            conv += 'L'
        elif c == 'L':
            conv += 'R'
        elif c == 'B':
            conv += 'F'
        elif c == 'F':
            conv += 'B'
        else:
            conv += c

    return conv


#---------------Méthode yConversion---------------#
# Méthode convertissant un algorithme pour
# le réaliser après un mouvement x
#
def xConversion(alg):

    conv = ''

    for c in alg:

        if c == 'R':
            conv += 'L'
        elif c == 'U':
            conv += 'D'
        elif c == 'L':
            conv += 'R'
        elif c == 'D':
            conv += 'U'
        else:
            conv += c

    return conv

#---------------Méthode chooseCorner---------------#
# Choisi un coin de la face du bas qui est libre
# afin d'y placer la coin du dessus
#
def chooseCorner(coin, reso, c):

    global BOBllibre
    global BRBllibre
    global RVBllibre
    global VOBllibre
    
    if coin == 'JVO':

        if RVBllibre:

            if BRBllibre:

                if c == 'j':

                    BRBllibre = False
                    return "UR2"

                elif c == 'v':

                    BRBllibre = False
                    return "U2R'"

                elif c == 'o':

                    RVBllibre = False
                    return "UR"

            else:

                RVBllibre = False
                return "U" + ypConversion(reso)

        elif BOBllibre:
            
            if BRBllibre:

                if c == 'j':

                    BRBllibre = False
                    return "U'F2"

                elif c == 'v':

                    BOBllibre = False
                    return "U'F'"

                elif c == 'o':

                    BRBllibre = False
                    return "U2F"

            else:

                BOBllibre = False
                return "U'" + yConversion(reso)
        else:

            BRBllibre = False
            return "U2" + y2Conversion(reso)

    elif coin == 'JRV':

        if VOBllibre:

            if BOBllibre:

                if c == 'j':

                    BOBllibre = False
                    return "U'L2"

                elif c == 'r':

                    VOBllibre = False
                    return "U'L'"

                elif c == 'v':

                    BOBllibre = False
                    return "U2L"

            else:

                VOBllibre = False
                return "U'" + yConversion(reso)

        elif BRBllibre:

            if BOBllibre:

                if c == 'j':

                    BOBllibre = False
                    return "UF2"

                elif c == 'r':

                    BOBllibre = False
                    return "U2F'"

                elif c == 'v':

                    BRBllibre = False
                    return "UF"

            else:

                BRBllibre = False
                return "U" + ypConversion(reso)

        else:

            BOBllibre = False
            return "U2" + y2Conversion(reso)

    elif coin == 'JBR':
        
        if RVBllibre:

            if VOBllibre:

                if c == 'j':

                    VOBllibre = False
                    return "U'B2"

                elif c == 'b':

                    RVBllibre = False
                    return "U'B'"

                elif c == 'r':

                    VOBllibre = False
                    return "U2B"

            else:

                RVBllibre = False
                return "U'" + yConversion(reso)

        elif BOBllibre:

            if VOBllibre:

                if c == 'j':

                    VOBllibre = False
                    return "UL2"

                elif c == 'b':

                    VOBllibre = False
                    return "U2L'"

                elif c == 'r':

                    BOBllibre = False
                    return "UL"

            else:

                BOBllibre = False
                return "U" + ypConversion(reso)

        else:

            VOBllibre = False
            return "U2" + y2Conversion(reso)

    elif coin == 'JBO':

        if BRBllibre:

            if RVBllibre:

                if c == 'j':

                    RVBllibre = False
                    return "U'R2"

                elif c == 'b':

                    RVBllibre = False
                    return "U2R"

                elif c == 'o':

                    BRBllibre = False
                    return "U'R'"

            else:

                BRBllibre = False
                return "U'" + yConversion(reso)

        elif VOBllibre:

            if RVBllibre:

                if c == 'j':

                    RVBllibre = False
                    return "UB2"

                elif c == 'b':

                    VOBllibre = False
                    return "UB"

                elif c == 'o':

                    RVBllibre = False
                    return "U2B'"

            else:

                VOBllibre = False
                return "U" + ypConversion(reso)
        else:

            RVBllibre = False
            return "U2" + y2Conversion(reso)


#---------------Méthode bufProcessing1---------------#
# Méthode appellée si l'arête buffer (JAUNE-ROUGE)
# est à sa place
# Cherche une arête mal placée, la place tout en
# envoyant le buffer dans cette arête
#
def bufProcessing1():

    global reso
    global Aretes
    global bh
    global JV
    global JR
    global JB
    global JO
    global VO
    global RV
    global BR
    global BO
    global BBl
    global RBl
    global VBl
    global OBl
    
    if 'JV' in Aretes:
        
        c1 = JV.getCouleur(1)
        c2 = JV.getCouleur(2)
        reso += bh[3*100 + c1*10 + c2]

    elif 'JO' in Aretes:

        c1 = JO.getCouleur(1)
        c2 = JO.getCouleur(2)
        reso += bh[4*100 + c1*10 + c2]

    elif 'JB' in Aretes:

        c1 = JB.getCouleur(1)
        c2 = JB.getCouleur(2)
        reso += bh[1*100 + c1*10 + c2]

    elif 'BO' in Aretes:

        c1 = BO.getCouleur(1)
        c2 = BO.getCouleur(2)
        reso += bh[14*100 + c1*10 + c2]

    elif 'BR' in Aretes:

        c1 = BR.getCouleur(1)
        c2 = BR.getCouleur(2)
        reso += bh[12*100 + c1*10 + c2]

    elif 'BBl' in Aretes:

        c1 = BBl.getCouleur(1)
        c2 = BBl.getCouleur(2)
        reso += bh[15*100 + c1*10 + c2]

    elif 'RV' in Aretes:

        c1 = RV.getCouleur(1)
        c2 = RV.getCouleur(2)
        reso += bh[23*100 + c1*10 + c2]

    elif 'RBl' in Aretes:

        c1 = RBl.getCouleur(1)
        c2 = RBl.getCouleur(2)
        reso += bh[25*100 + c1*10 + c2]

    elif 'VO' in Aretes:

        c1 = VO.getCouleur(1)
        c2 = VO.getCouleur(2)
        reso += bh[34*100 + c1*10 + c2]

    elif 'OBl' in Aretes:

        c1 = OBl.getCouleur(1)
        c2 = OBl.getCouleur(2)
        reso += bh[45*100 + c1*10 + c2]

    elif 'VBl' in Aretes:

        c1 = VBl.getCouleur(1)
        c2 = VBl.getCouleur(2)
        reso += bh[35*100 + c1*10 + c2]

    if((c1 == JAUNE or c1 == VERT) and (c2 == JAUNE or c2 == VERT)):
        Aretes.remove('JV')
    elif((c1 == JAUNE or c1 == ROUGE) and (c2 == JAUNE or c2 == ROUGE)):
        Aretes.remove('JR')
    elif((c1 == JAUNE or c1 == BLEU) and (c2 == JAUNE or c2 == BLEU)):
        Aretes.remove('JB')
    elif((c1 == JAUNE or c1 == ORANGE) and (c2 == JAUNE or c2 == ORANGE)):
        Aretes.remove('JO')
    elif((c1 == VERT or c1 == ORANGE) and (c2 == VERT or c2 == ORANGE)):
        Aretes.remove('VO')
    elif((c1 == ROUGE or c1 == VERT) and (c2 == ROUGE or c2 == VERT)):
        Aretes.remove('RV')
    elif((c1 == BLEU or c1 == ROUGE) and (c2 == BLEU or c2 == ROUGE)):
        Aretes.remove('BR')
    elif((c1 == BLEU or c1 == ORANGE) and (c2 == BLEU or c2 == ORANGE)):
        Aretes.remove('BO')
    elif((c1 == BLEU or c1 == BLANC) and (c2 == BLEU or c2 == BLANC)):
        Aretes.remove('BBl')
    elif((c1 == ROUGE or c1 == BLANC) and (c2 == ROUGE or c2 == BLANC)):
        Aretes.remove('RBl')
    elif((c1 == VERT or c1 == BLANC) and (c2 == VERT or c2 == BLANC)):
        Aretes.remove('VBl')
    elif((c1 == ORANGE or c1 == BLANC) and (c2 == ORANGE or c2 == BLANC)):
        Aretes.remove('OBl')


#---------------Méthode bufProcessing2---------------#
# Méthode appellée si l'arête buffer (JAUNE-ROUGE)
# est à la place de l'arête actuellement dans le
# buffer
# Cherche une place libre pour envoyer l'arête buffer
#
def bufProcessing2():

    global reso
    global buf
    global Aretes
    global bh
    global JV
    global JR
    global JB
    global JO
    global VO
    global RV
    global BR
    global BO
    global BBl
    global RBl
    global VBl
    global OBl

    ALibre = 0
    
    buf = False

    c1 = JR.getCouleur(1)
    c2 = JR.getCouleur(2)

    if((c1 == JAUNE or c1 == VERT) and (c2 == JAUNE or c2 == VERT)):

        Aretes.remove('JV')
        ALibre = c1*10 + c2

    elif((c1 == JAUNE or c1 == ORANGE) and (c2 == JAUNE or c2 == ORANGE)):

        Aretes.remove('JO')
        ALibre = c1*10 + c2
    
    elif((c1 == JAUNE or c1 == BLEU) and (c2 == JAUNE or c2 == BLEU)):

        Aretes.remove('JB')
        ALibre = c1*10 + c2

    elif((c1 == BLEU or c1 == ORANGE) and (c2 == BLEU or c2 == ORANGE)):

        Aretes.remove('BO')
        ALibre = c1*10 + c2

    elif((c1 == BLEU or c1 == ROUGE) and (c2 == BLEU or c2 == ROUGE)):

        Aretes.remove('BR')
        ALibre = c1*10 + c2

    elif((c1 == BLEU or c1 == BLANC) and (c2 == BLEU or c2 == BLANC)):

        Aretes.remove('BBl')
        ALibre = c1*10 + c2

    elif((c1 == ROUGE or c1 == VERT) and (c2 == ROUGE or c2 == VERT)):

        Aretes.remove('RV')
        ALibre = c1*10 + c2

    elif((c1 == ROUGE or c1 == BLANC) and (c2 == ROUGE or c2 == BLANC)):

        Aretes.remove('RBl')
        ALibre = c1*10 + c2

    elif((c1 == VERT or c1 == ORANGE) and (c2 == VERT or c2 == ORANGE)):

        Aretes.remove('VO')
        ALibre = c1*10 + c2

    elif((c1 == ORANGE or c1 == BLANC) and (c2 == ORANGE or c2 == BLANC)):

        Aretes.remove('OBl')
        ALibre = c1*10 + c2

    elif((c1 == VERT or c1 == BLANC) and (c2 == VERT or c2 == BLANC)):

        Aretes.remove('VBl')
        ALibre = c1*10 + c2

    if 'JV' in Aretes and ALibre is not 3 and ALibre is not 30:
        reso += bh[ALibre*100 + 3]
    elif 'JO' in Aretes and ALibre is not 4 and ALibre is not 40:
        reso += bh[ALibre*100 + 4]
    elif 'JB' in Aretes and ALibre is not 1 and ALibre is not 10:
        reso += bh[ALibre*100 + 1]
    elif 'BO' in Aretes and ALibre is not 14 and ALibre is not 41:
        reso += bh[ALibre*100 + 14]
    elif 'BR' in Aretes and ALibre is not 12 and ALibre is not 21:
        reso += bh[ALibre*100 + 12]
    elif 'BBl' in Aretes and ALibre is not 15 and ALibre is not 51:
        reso += bh[ALibre*100 + 15]
    elif 'RV' in Aretes and ALibre is not 23 and ALibre is not 32:
        reso += bh[ALibre*100 + 23]
    elif 'RBl' in Aretes and ALibre is not 25 and ALibre is not 52:
        reso += bh[ALibre*100 + 25]
    elif 'VO' in Aretes and ALibre is not 34 and ALibre is not 43:
        reso += bh[ALibre*100 + 34]
    elif 'OBl' in Aretes and ALibre is not 45 and ALibre is not 54:
        reso += bh[ALibre*100 + 45]
    elif 'VBl' in Aretes and ALibre is not 35 and ALibre is not 53:
        reso += bh[ALibre*100 + 35]

moveFor = {"R" : ["L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
           "R'" : ["L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
           "R2" : ["L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
           "L" : ["F", "F'", "F2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
           "L'" : ["F", "F'", "F2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
           "L2" : ["F", "F'", "F2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
           "F" : ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
           "F'" : ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
           "F2" : ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
           "B" : ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", " "],
           "B'" : ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", " "],
           "B2" : ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", " "],
           "U" : ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "B", "B'", "B2", " "],
           "U'" : ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "B", "B'", "B2", " "],
           "U2" : ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "B", "B'", "B2", " "],
           "D" : ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "B", "B'", "B2", " "],
           "D'" : ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "B", "B'", "B2", " "],
           "D2" : ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "B", "B'", "B2", " "]}

buffer_cube = []

def solve(cube):

    global JAUNE
    global BLEU
    global ROUGE
    global VERT
    global ORANGE
    global BLANC

    global BOBllibre
    global BRBllibre
    global RVBllibre
    global VOBllibre

    global pllT
    global diag
    global inv
    global pllTdiag
    global doublediag

    global chaise
    global chaiseinv
    global Pi
    global frere
    global L
    global T
    global H

    global JVOj
    global JVOv
    global JVOo
    global JRVj
    global JRVr
    global JRVv
    global JBRj
    global JBRb
    global JBRr
    global JBOj
    global JBOb
    global JBOo
    global BOBlb
    global BOBlo
    global BRBlb
    global BRBlr
    global RVBlr
    global RVBlv
    global VOBlv
    global VOBlo

    global facejaune
    global comptjaune
    global Fcompt
    global Rcompt
    global Lcompt
    global Bcompt

    global jaunef
    global jauneplltF
    global jauneplltR
    global jauneplltB
    global jauneplltL
    global jaunediag
    global jaunediagF
    global jaunediagR
    global blancf
    global blancplltF
    global blancplltR
    global blancplltB
    global blancplltL
    global blancdiag
    global blancdiagR
    global blancdiagF

    global Resolution

    global reso
    global buf
    global Aretes
    global bh
    global JV
    global JR
    global JB
    global JO
    global VO
    global RV
    global BR
    global BO
    global BBl
    global RBl
    global VBl
    global OBl

    global buffer_cube
    
    Resolution = ''
    Solution = 'AB'*40

    buffer_cube[:] = cube[:]
    
    for m in ["R", "R'", "R2", "F", "F'", "F2", "U", "U'", "U2", "L", "L'", "L2", "D", "D'", "D2", "B", "B'", "B2"]:
        
        for d in moveFor[m]:

            cube[:] = buffer_cube[:]
            
            cube[:] = applyMove(cube[:], m+d)[:]
            Resolution += m + d

            BOBllibre = True
            BRBllibre = True
            RVBllibre = True
            VOBllibre = True

            facejaune = []
            comptjaune = 0
            Fcompt = 0
            Rcompt = 0
            Lcompt = 0
            Bcompt = 0

            jaunef = False
            jauneplltF = False
            jauneplltR = False
            jauneplltB = False
            jauneplltL = False
            jaunediag = False
            jaunediagF = False
            jaunediagR = False
            blancf = False
            blancplltF = False
            blancplltR = False
            blancplltB = False
            blancplltL = False
            blancdiag = False
            blancdiagR = False
            blancdiagF = False
    
            # Affectation des couleurs du cube aux coins
            JVO = Coin(cube[0], cube[11], cube[18])
            JRV = Coin(cube[2], cube[38], cube[9])
            JBR = Coin(cube[8], cube[29], cube[36])
            JBO = Coin(cube[6], cube[27], cube[20])
            BOBl = Coin(cube[33], cube[26], cube[45])
            BRBl = Coin(cube[35], cube[42], cube[47])
            RVBl = Coin(cube[44], cube[15], cube[53])
            VOBl = Coin(cube[17], cube[24], cube[51])

            # Retrait des coins blancs déja bien placés
            if BOBl.getCouleur(3) == BLANC:
                BOBllibre = False
            if BRBl.getCouleur(3) == BLANC:
                BRBllibre = False
            if RVBl.getCouleur(3) == BLANC:
                RVBllibre = False
            if VOBl.getCouleur(3) == BLANC:
                VOBllibre = False

            # Boucle tournant tant que les 4 coins blancs ne
            # sont pas placés
            while(BOBllibre or BRBllibre or RVBllibre or VOBllibre):
                
                partReso = ''
                reso = ''
                coin = ''
                ori = ''

                # Reaffectation des coins à chaque tour de boucle
                JVO = Coin(cube[0], cube[11], cube[18])
                JRV = Coin(cube[2], cube[38], cube[9])
                JBR = Coin(cube[8], cube[29], cube[36])
                JBO = Coin(cube[6], cube[27], cube[20])
                BOBl = Coin(cube[33], cube[26], cube[45])
                BRBl = Coin(cube[35], cube[42], cube[47])
                RVBl = Coin(cube[44], cube[15], cube[53])
                VOBl = Coin(cube[17], cube[24], cube[51])

                # Retrait des coins blancs déja bien placés
                # à chaque tour de boucle
                if BOBl.getCouleur(3) == BLANC:
                    BOBllibre = False
                if BRBl.getCouleur(3) == BLANC:
                    BRBllibre = False
                if RVBl.getCouleur(3) == BLANC:
                    RVBllibre = False
                if VOBl.getCouleur(3) == BLANC:
                    VOBllibre = False

                # Vérification si le coin JAUNE-VERT-ORANGE
                # contient la couleur blanche
                if JVO.has(BLANC):

                    # Si c'est la face JAUNE qui est blanche
                    if JVO.getCouleur(1) == BLANC:

                        # Si le coin juste en dessous n'est pas libre
                        # on ne fait rien et on utilise la méthode
                        # chooseCorner
                        if(not VOBllibre):

                            partReso = JVOj
                            coin = 'JVO'
                            ori = 'j'

                        # Si les coins BLEU-ORANGE-BLANC et
                        # VERT-ORANGE-BLANC sont libre, on place
                        # le coin en BLEU-ORANGE-BLANC (car cela
                        # demande moins de mouvements)
                        elif(BOBllibre and VOBllibre):

                            reso += "L2"
                            BOBllibre = False

                        # Si les coins ROUGE-VERT-BLANC et
                        # VERT-ORANGE-BLANC sont libre, on place
                        # le coin en ROUGE-VERT-BLANC (car cela
                        # demande moins de mouvements)
                        elif(VOBllibre and RVBllibre):

                            reso += "B2"
                            RVBllibre = False

                        # Sinon on le place en dessous sans
                        # casser les autres
                        else:

                            reso += JVOj
                            VOBllibre = False

                    # Même raisonnement si la couleur est du
                    # coté VERT
                    elif JVO.getCouleur(2) == BLANC:

                        if(not VOBllibre):

                            partReso = JVOv
                            coin = 'JVO'
                            ori = 'v'

                        elif(BOBllibre and VOBllibre):

                            reso += "L'"
                            VOBllibre = False

                        else:

                            reso += JVOv
                            VOBllibre = False

                    # Même raisonnement si la couleur est du
                    # coté ORANGE
                    elif JVO.getCouleur(3) == BLANC:

                        if(not VOBllibre):
                            
                            partReso = JVOo
                            coin = 'JVO'
                            ori = 'o'

                        elif(RVBllibre and VOBllibre):

                            reso += "B"
                            VOBllibre = False

                        else:

                            reso += JVOo
                            VOBllibre = False

                # Même raisonnement avec le coin
                # JAUNE-ROUGE-VERT etc ...
                elif JRV.has(BLANC):

                    if JRV.getCouleur(1) == BLANC:

                        if(not RVBllibre):

                            partReso = JRVj
                            coin = 'JRV'
                            ori = 'j'

                        elif(RVBllibre and VOBllibre):

                            reso += "B2"
                            VOBllibre = False

                        elif(RVBllibre and BRBllibre):

                            reso += "R2"
                            BRBllibre = False

                        else:

                            reso += JRVj
                            RVBllibre = False

                    elif JRV.getCouleur(2) == BLANC:

                        if(not RVBllibre):

                            partReso = JRVr
                            coin = 'JRV'
                            ori = 'r'

                        elif(RVBllibre and VOBllibre):

                            reso += "B'"
                            RVBllibre = False

                        else:

                            reso += JRVr
                            RVBllibre = False

                    elif JRV.getCouleur(3) == BLANC:

                        if(not RVBllibre):

                            partReso = JRVv
                            coin = 'JRV'
                            ori = 'v'

                        elif(BRBllibre and RVBllibre):

                            reso += "R"
                            RVBllibre = False

                        else:

                            reso += JRVv
                            RVBllbre = False
                            
                elif JBR.has(BLANC):

                    if JBR.getCouleur(1) == BLANC:

                        if(not BRBllibre):

                            partReso = JBRj
                            coin = 'JBR'
                            ori = 'j'

                        elif(BRBllibre and RVBllibre):

                            reso += "R2"
                            RVBllibre = False

                        elif(BRBllibre and BOBllibre):

                            reso += "F2"
                            BOBllibre = False

                        else:

                            reso += JBRj
                            BRBllibre = False

                    elif JBR.getCouleur(2) == BLANC:

                        if(not BRBllibre):

                            partReso = JBRb
                            coin = 'JBR'
                            ori = 'b'

                        elif(BRBllibre and RVBllibre):

                            reso += "R'"
                            BRBllibre = False

                        else:

                            reso += JBRb
                            BRBllibre = False

                    elif JBR.getCouleur(3) == BLANC:

                        if(not BRBllibre):

                            partReso = JBRr
                            coin = 'JBR'
                            ori = 'r'

                        elif(BOBllibre and BRBllibre):

                            reso += "F"
                            BRBllibre = False

                        else:

                            reso += JBRr
                            BRBllibre = False
                            
                elif JBO.has(BLANC):

                    if JBO.getCouleur(1) == BLANC:

                        if(not BOBllibre):

                            partReso = JBOj
                            coin = 'JBO'
                            ori = 'j'

                        elif(BOBllibre and BRBllibre):

                            reso += "F2"
                            BRBllibre = False

                        elif(BOBllibre and VOBllibre):

                            reso += "L2"
                            VOBllibre = False

                        else:

                            reso += JBOj
                            BOBllibre = False

                    elif JBO.getCouleur(2) == BLANC:

                        if(not BOBllibre):

                            partReso = JBOb
                            coin = 'JBO'
                            ori = 'b'

                        elif(BOBllibre and VOBllibre):

                            reso = reso + "L"
                            BOBllibre = False

                        else:

                            reso += JBOb
                            BOBllibre = False

                    elif JBO.getCouleur(3) == BLANC:

                        if(not BOBllibre):

                            partReso = JBOo
                            coin = 'JBO'
                            ori = 'o'

                        elif(BOBllibre and BRBllibre):

                            reso += "F'"
                            BOBllibre = False

                        else:

                            reso += JBOo
                            BOBllibre = False

                elif BOBl.has(BLANC) and BOBllibre:

                    if BOBl.getCouleur(1) == BLANC:

                        if(not VOBllibre):

                            reso += BOBlb
                            BOBllibre = False

                        else:

                            reso += "L"
                            VOBllibre = False

                    elif BOBl.getCouleur(2) == BLANC:

                        if(not BRBllibre):

                            reso += BOBlo
                            BOBllibre = False

                        else:

                            reso += "F'"
                            BRBllibre = False
                            
                elif BRBl.has(BLANC) and BRBllibre:

                    if BRBl.getCouleur(1) == BLANC:

                        if(not RVBllibre):

                            reso += BRBlb
                            BRBllibre = False

                        else:

                            reso += "R'"
                            RVBllibre = False

                    elif BRBl.getCouleur(2) == BLANC:

                        if(not BOBllibre):

                            reso += BRBlr
                            BRBllibre = False

                        else:

                            reso += "F"
                            BOBllibre = False

                elif RVBl.has(BLANC) and RVBllibre:

                    if RVBl.getCouleur(1) == BLANC:

                        if(not VOBllibre):

                            reso += RVBlr
                            RVBllibre = False

                        else:

                            reso += "B'"
                            VOBllibre = False

                    elif RVBl.getCouleur(2) == BLANC:

                        if(not BRBllibre):

                            reso += RVBlv
                            RVBllibre = False

                        else:

                            reso += "R"
                            BRBllibre = False
                            
                elif VOBl.has(BLANC) and VOBllibre:

                    if VOBl.getCouleur(1) == BLANC:

                        if(not BOBllibre):

                            reso += VOBlv
                            VOBllibre = False

                        else:

                            reso += "L'"
                            BOBllibre = False

                    elif VOBl.getCouleur(2) == BLANC:

                        if(not RVBllibre):

                            reso += VOBlo
                            VOBllibre = False

                        else:

                            reso += "B"
                            RVBllibre = False

                # on rentre ici si le coin n'a pas pu être placé
                if(partReso != ''):
                    reso += chooseCorner(coin, partReso, ori)
                
                Resolution += reso
                cube = applyMove(cube, reso)

            # Les 4 coins blancs sont maitenant placés
            
            reso = ''
            partReso = ''

            # Reaffectation des coins après les mouvements
            # trouvés précédement
            JVO = Coin(cube[0], cube[11], cube[18])
            JRV = Coin(cube[2], cube[38], cube[9])
            JBR = Coin(cube[8], cube[29], cube[36])
            JBO = Coin(cube[6], cube[27], cube[20])
            BOBl = Coin(cube[33], cube[26], cube[45])
            BRBl = Coin(cube[35], cube[42], cube[47])
            RVBl = Coin(cube[44], cube[15], cube[53])
            VOBl = Coin(cube[17], cube[24], cube[51])

            # Vérification des coins jaunes déja bien placés
            if JVO.getCouleur(1) == JAUNE:

                comptjaune += 1
                facejaune.append('JVO')

            if JRV.getCouleur(1) == JAUNE:

                comptjaune += 1
                facejaune.append('JRV')

            if JBR.getCouleur(1) == JAUNE:

                comptjaune += 1
                facejaune.append('JBR')

            if JBO.getCouleur(1) == JAUNE:

                comptjaune += 1
                facejaune.append('JBO')

            # Si le coin JAUNE-VERT-ORANGE est mal orienté
            if('JVO' not in facejaune):

                # Si c'est la face VERT qui est jaune
                if JVO.getCouleur(2) == JAUNE:

                    # Stockage du coin et de l'orientation
                    facejaune.append('JVOv')
                    # Comptage de jaune sur la face B
                    Bcompt += 1

                else:
                    
                    # Même rasionnement mais pour la
                    # face ORANGE
                    facejaune.append('JVOo')
                    Lcompt += 1

            # Même raisonnement avec le coin
            # JAUNE-ROUGE-VERT etc ...
            if('JRV' not in facejaune):

                if JRV.getCouleur(2) == JAUNE:

                    facejaune.append('JRVr')
                    Rcompt += 1

                else:

                    facejaune.append('JRVv')
                    Bcompt += 1

            if('JBR' not in facejaune):

                if JBR.getCouleur(2) == JAUNE:

                    facejaune.append('JBRb')
                    Fcompt += 1

                else:

                    facejaune.append('JBRr')
                    Rcompt += 1

            if('JBO' not in facejaune):

                if JBO.getCouleur(2) == JAUNE:

                    facejaune.append('JBOb')
                    Fcompt += 1

                else:

                    facejaune.append('JBOo')
                    Lcompt += 1

            
            # Si tous les coins ne sont pas bien orientés
            if comptjaune != 4:

                # Si aucun coin n'est bien orienté
                if comptjaune == 0:

                    # Cas des JAUNE en face à face : H
                    if(Fcompt == 2 and Bcompt == 2 or
                       Rcompt == 2 and Lcompt == 2):

                        if Fcompt == 2:
                            reso += H

                        else:
                            reso += ypConversion(H)

                    # Sinon c'est l'autre cas : PI
                    else:

                        if Fcompt == 2:
                            reso += yConversion(Pi)

                        elif Rcompt == 2:
                            reso += y2Conversion(Pi)

                        elif Lcompt == 2:
                            reso += Pi

                        else:
                            reso += ypConversion(Pi)

                # Si il n'y a qu'un seule jaune bien orienté : chaise
                elif comptjaune == 1:

                    # Si c'est JAUNE-VERT-ORANGE qui est
                    # bien orienté
                    if 'JVO' in facejaune:

                        # Chaiseinv
                        if 'JBOb' in facejaune:
                            reso += chaiseinv

                        # Chaise
                        else:
                            reso += ypConversion(chaise)
                    
                    # Si c'est JAUNE-ROUGE-VERT qui est
                    # bien orienté
                    elif 'JRV' in facejaune:

                        # Chaise
                        if 'JVOv' in facejaune:
                            reso += y2Conversion(chaise)

                        # Chaiseinv
                        else:
                            reso += ypConversion(chaiseinv)

                    # Si c'est JAUNE-BLEU-ROUGE qui est
                    # bien orienté
                    elif 'JBR' in facejaune:

                        # Chaise
                        if 'JRVr' in facejaune:
                            reso += yConversion(chaise)

                        # Chaiseinv
                        else:
                            reso += y2Conversion(chaiseinv)

                    # Si c'est JAUNE-BLEU-ORANGE qui est
                    # bien orienté
                    elif 'JBO' in facejaune:

                        # Chaise
                        if 'JBRb' in facejaune:
                            reso += chaise

                        # Chaiseinv
                        else:
                            reso += yConversion(chaiseinv)

                # Sinon c'est qu'il y a 2 coins bien orientés
                else:

                    # Si JAUNE-VERT-ORANGE et JAUNE-ROUGE-VERT sont
                    # bien orientés
                    if('JVO' in facejaune and 'JRV' in facejaune):

                        # Frere
                        if 'JBRb' in facejaune:
                            reso += yConversion(frere)

                        # T
                        else:
                            reso += yConversion(T)

                    # Si JAUNE-ROUGE-VERT et JAUNE-BLEU-ROUGE sont
                    # bien orientés
                    elif('JRV' in facejaune and 'JBR' in facejaune):

                        # Frere
                        if 'JBOo' in facejaune:
                            reso += frere

                        # T
                        else:
                            reso += T

                    # Si JAUNE-BLEU-ROUGE et JAUNE-BLEU-ORANGE sont
                    # bien orientés
                    elif('JBR' in facejaune and 'JBO' in facejaune):

                        # Frere
                        if 'JVOv' in facejaune:
                            reso += ypConversion(frere)

                        # T
                        else:
                            reso += ypConversion(T)

                    # Si JAUNE-VERT-ORANGE et JAUNE-BLEU-ORANGE sont
                    # bien orientés
                    elif('JVO' in facejaune and 'JBO' in facejaune):

                        # Frere
                        if 'JRVr' in facejaune:
                            reso += y2Conversion(frere)

                        # T
                        else:
                            reso += y2Conversion(T)

                    # Si JAUNE-VERT-ORANGE et JAUNE-BLEU-ROUGE sont
                    # bien orientés
                    elif('JVO' in facejaune and 'JBR' in facejaune):

                        # L
                        if 'JBOb' in facejaune:
                            reso += L

                        # L
                        else:
                            reso += y2Conversion(L)

                    # Si JAUNE-BLEU-ORANGE et JAUNE-ROUGE-VERT sont
                    # bien orientés
                    elif('JBO' in facejaune and 'JRV' in facejaune):

                        # L
                        if 'JBRb' in facejaune:
                            reso += ypConversion(L)

                        # L
                        else:
                            reso += yConversion(L)

            Resolution += reso
            cube = applyMove(cube, reso)

            comptjaune = 0
            comptblanc = 0
            
            # Les faces jaunes et blanches sont mainteant faites
            
            reso = ''

            # Reaffectation des coins après les mouvements
            # trouvés précédement
            JVO = Coin(cube[0], cube[11], cube[18])
            JRV = Coin(cube[2], cube[38], cube[9])
            JBR = Coin(cube[8], cube[29], cube[36])
            JBO = Coin(cube[6], cube[27], cube[20])
            BOBl = Coin(cube[33], cube[26], cube[45])
            BRBl = Coin(cube[35], cube[42], cube[47])
            RVBl = Coin(cube[44], cube[15], cube[53])
            VOBl = Coin(cube[17], cube[24], cube[51])

            # Vérification si la face jaune est faite
            if(JBO.getCouleur(2) == JBR.getCouleur(2) and
               JBR.getCouleur(3) == JRV.getCouleur(2) and
               JRV.getCouleur(3) == JVO.getCouleur(2) and
               JVO.getCouleur(3) == JBO.getCouleur(3)):
                jaunef = True

            # Vérification si la face blanche est faite
            if(BOBl.getCouleur(1) == BRBl.getCouleur(1) and
               BRBl.getCouleur(2) == RVBl.getCouleur(1) and
               RVBl.getCouleur(2) == VOBl.getCouleur(1) and
               VOBl.getCouleur(2) == BOBl.getCouleur(2)):
                blancf = True

            # Détermination de comment sont orientés les couleurs :
            # cas du pllT (2 couleurs de coins côte à côte sont opposées
            # et les deux couleurs sont les mêmes)
            if(colorOpposed(JRV.getCouleur(3), JVO.getCouleur(2)) and
               JBR.getCouleur(2) == JBO.getCouleur(2)):
                jauneplltB = True
            elif(colorOpposed(JBR.getCouleur(3), JRV.getCouleur(2)) and
                 JBO.getCouleur(3) == JVO.getCouleur(3)):
                jauneplltR = True
            elif(colorOpposed(JBO.getCouleur(2), JBR.getCouleur(2)) and
                 JVO.getCouleur(2) == JRV.getCouleur(3)):
                jauneplltF = True
            elif(colorOpposed(JVO.getCouleur(3), JBO.getCouleur(3)) and
                 JRV.getCouleur(2) == JBR.getCouleur(3)):
                jauneplltL = True
            if(colorOpposed(RVBl.getCouleur(2), VOBl.getCouleur(1)) and
                 BRBl.getCouleur(1) == BOBl.getCouleur(1)):
                blancplltB = True
            elif(colorOpposed(BRBl.getCouleur(2), RVBl.getCouleur(1)) and
                 BOBl.getCouleur(2) == VOBl.getCouleur(2)):
                blancplltR = True
            elif(colorOpposed(BRBl.getCouleur(1), BOBl.getCouleur(1)) and
                 VOBl.getCouleur(1) == RVBl.getCouleur(2)):
                blancplltF = True
            elif(colorOpposed(VOBl.getCouleur(2), BOBl.getCouleur(2)) and
                 BRBl.getCouleur(2) == RVBl.getCouleur(1)):
                blancplltL = True

            # Détermination de comment sont orientés les couleurs :
            # cas de la diagonale (chaque couleur côte à côte sont
            # opposées)
            if(colorOpposed(JRV.getCouleur(3), JVO.getCouleur(2)) and
               colorOpposed(JBR.getCouleur(2), JBO.getCouleur(2))):

                if JBR.getCouleur(2) == BLEU:
                    jaunediagF = True

                jaunediag = True

            if(colorOpposed(RVBl.getCouleur(2), VOBl.getCouleur(1)) and
               colorOpposed(BRBl.getCouleur(1), BOBl.getCouleur(1))):

                if BOBl.getCouleur(1) == BLEU:
                    blancdiagF = True

                blancdiag = True
            
            # Si diagonale jaune et blanche : cas de la double diagonale
            if(blancdiag and jaunediag):
                reso += doublediag

            # Si une diagonale et un pllT : cas de pllTdiag
            elif(blancdiag and (jauneplltF or jauneplltR or jauneplltB or jauneplltL)):

                if jauneplltF:
                    reso += y2Conversion(pllTdiag)
                elif jauneplltR:
                    reso += ypConversion(pllTdiag)
                elif jauneplltB:
                    reso += pllTdiag
                elif jauneplltL:
                    reso += yConversion(pllTdiag)
            
            elif(jaunediag and (blancplltF or blancplltR or blancplltL or blancplltB)):

                if blancplltF:
                    reso += y2Conversion(xConversion(pllTdiag))
                elif blancplltR:
                    reso += ypConversion(xConversion(pllTdiag))
                elif blancplltB:
                    reso += xConversion(pllTdiag)
                elif blancplltL:
                    reso += yConversion(xConversion(pllTdiag))

            # Si pllT blanc et jaune : cas du double pllT(inv)
            elif((jauneplltF or jauneplltR or jauneplltB or jauneplltL) and
                  (blancplltF or blancplltR or blancplltB or blancplltL)):

                if jauneplltF:

                    if blancplltF:
                        reso += inv

                    elif blancplltR:
                        reso += ("D'" + inv)

                    elif blancplltB:
                        reso += ("D2" + inv)

                    elif blancplltL:
                        reso += ("D" + inv)

                elif jauneplltR:

                    if blancplltF:
                        reso += ("D" + yConversion(inv))

                    elif blancplltR:
                        reso += yConversion(inv)

                    elif blancplltB:
                        reso += ("D'" + yConversion(inv))

                    elif blancplltL:
                        reso += ("D2" + yConversion(inv))

                elif jauneplltB:

                    if blancplltF:
                        reso += ("D2" + y2Conversion(inv))

                    elif blancplltR:
                        reso += ("D" + y2Conversion(inv))

                    elif blancplltB:
                        reso += y2Conversion(inv)

                    elif blancplltL:
                        reso += ("D'" + y2Conversion(inv))

                elif jauneplltL:

                    if blancplltF:
                        reso += ("D'" + ypConversion(inv))

                    elif blancplltR:
                        reso += ("D2" + ypConversion(inv))

                    elif blancplltB:
                        reso += ("D" + ypConversion(inv))

                    elif blancplltL:
                        reso += ypConversion(inv)

            # Si une face et faite et l'autre a un pllT : pllT
            elif(blancf and (jauneplltF or jauneplltR or jauneplltB or jauneplltL)):

                if jauneplltF:
                    reso += pllT

                elif jauneplltR:
                    reso += yConversion(pllT)

                elif jauneplltB:
                    reso += y2Conversion(pllT)

                elif jauneplltL:
                    reso += ypConversion(pllT)

            elif(jaunef and (blancplltF or blancplltR or blancplltB or blancplltL)):

                if blancplltF:
                    reso += xConversion(pllT)

                elif blancplltR:
                    reso += yConversion(xConversion(pllT))

                elif blancplltB:
                    reso += y2Conversion(xConversion(pllT))

                elif blancplltL:
                    reso += ypConversion(xConversion(pllT))

            # Si une face est faite et l'autre a une diagonale : diag
            elif jaunediag:

                if jaunediagF:
                    reso += ("U2" + diag)

                else:
                    reso += diag

            elif blancdiag:

                if blancdiagF:
                    reso += ("D2" + xConversion(diag))

                else:
                    reso += xConversion(diag)

            Resolution += (reso + ' ')
            cube = applyMove(cube, reso)

            # La résolution en 2x2 est presque fini, il faut réaligner
            # les faces avec des U et D
            
            reso = ''

            if cube[27] == ROUGE:
                reso += "U'"

            if cube[27] == VERT:
                reso += "U2"

            if cube[27] == ORANGE:
                reso += "U"

            if cube[35] == ROUGE:
                reso += "D"

            if cube[35] == VERT:
                reso += "D2"

            if cube[35] == ORANGE:
                reso += "D'"

            Resolution += reso
            applyMove(cube, reso)

            # Résolution en 2x2 fini
            
            JVLibre = True
            JOLibre = True
            JBLibre = True
            JRLibre = True

            resoInter = ''

            reso = ''
            ori = ''
            coin = ''

            buf = False

            Aretes = ['JV', 'JO', 'JB', 'BO', 'BR', 'BBl', 'RV', 'RBl', 'VO', 'OBl', 'VBl']
            AretesDesor = []

            # Affectation des couleurs du cube aux arêtes
            JV = Arete(cube[1], cube[10])
            JR = Arete(cube[5], cube[37])
            JB = Arete(cube[7], cube[28])
            JO = Arete(cube[3], cube[19])
            VO = Arete(cube[14], cube[21])
            RV = Arete(cube[41], cube[12])
            BR = Arete(cube[32], cube[39])
            BO = Arete(cube[30], cube[23])
            BBl = Arete(cube[34], cube[46])
            RBl = Arete(cube[43], cube[50])
            VBl = Arete(cube[16], cube[52])
            OBl = Arete(cube[25], cube[48])

            # Retrait des arêtes si elles sont dans leur bon
            # emplacement et ajout dans la liste des
            # mal-orientées si elles le sont
            if JV.contient(JAUNE, VERT):

                Aretes.remove('JV')

                if JV.getCouleur(1) == VERT:

                    AretesDesor.append('JV')
                    JVLibre = False

            if JO.contient(JAUNE, ORANGE):

                Aretes.remove('JO')

                if JO.getCouleur(1) == ORANGE:

                    AretesDesor.append('JO')
                    JOLibre = False

            if JB.contient(JAUNE, BLEU):

                Aretes.remove('JB')

                if JB.getCouleur(1) == BLEU:

                    AretesDesor.append('JB')
                    JBLibre = False

            if BO.contient(BLEU, ORANGE):

                Aretes.remove('BO')

                if BO.getCouleur(1) == ORANGE:
                    AretesDesor.append('BO')

            if BR.contient(BLEU, ROUGE):

                Aretes.remove('BR')

                if BR.getCouleur(1) == ROUGE:
                    AretesDesor.append('BR')

            if BBl.contient(BLEU, BLANC):

                Aretes.remove('BBl')

                if BBl.getCouleur(1) == BLANC:
                    AretesDesor.append('BBl')

            if RV.contient(ROUGE, VERT):

                Aretes.remove('RV')

                if RV.getCouleur(1) == VERT:
                    AretesDesor.append('RV')

            if RBl.contient(ROUGE, BLANC):

                Aretes.remove('RBl')

                if RBl.getCouleur(1) == BLANC:
                    AretesDesor.append('RBl')

            if VO.contient(VERT, ORANGE):

                Aretes.remove('VO')

                if VO.getCouleur(1) == ORANGE:
                    AretesDesor.append('VO')

            if OBl.contient(ORANGE, BLANC):

                Aretes.remove('OBl')

                if OBl.getCouleur(1) == BLANC:
                    AretesDesor.append('OBl')

            if VBl.contient(VERT, BLANC):

                Aretes.remove('VBl')

                if VBl.getCouleur(1) == BLANC:
                    AretesDesor.append('VBl')

            # Boucle tournant tant que les arêtes ne sont pas
            # dans leur emplacement et le plus orientées
            # possibles
            while Aretes:
                
                reso = ""

                # Initialisation des 4 couleurs des 2 arêtes
                # celles du buffer et celles d'où doit aller
                # cette arête
                c1, c2, c3, c4 = None, None, None, None

                # Reaffectation des coins à chaque tour de boucle
                JV = Arete(cube[1], cube[10])
                JR = Arete(cube[5], cube[37])
                JB = Arete(cube[7], cube[28])
                JO = Arete(cube[3], cube[19])
                VO = Arete(cube[14], cube[21])
                RV = Arete(cube[41], cube[12])
                BR = Arete(cube[32], cube[39])
                BO = Arete(cube[30], cube[23])
                BBl = Arete(cube[34], cube[46])
                RBl = Arete(cube[43], cube[50])
                VBl = Arete(cube[16], cube[52])
                OBl = Arete(cube[25], cube[48])

                # Récupération des couleurs de l'arête à
                # l'emplacement du buffer
                c1 = JR.getCouleur(1)
                c2 = JR.getCouleur(2)

                # Si l'arête JAUNE-VERT est à l'emplacement du buffer (peu
                # importe son orientation)
                if((c1 == JAUNE or c1 == VERT) and (c2 == JAUNE or c2 == VERT)):

                    # Retrait de l'arête de la liste
                    Aretes.remove('JV')

                    # Récupération des couleurs de l'emplacement de l'arête
                    c3 = JV.getCouleur(1)
                    c4 = JV.getCouleur(2)

                    # Si l'arête buffer est où doit aller l'arête à la place
                    # du buffer
                    if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

                        buf = True
                        Aretes.append('JV')

                # Même raisonnement pour l'arête JAUNE-BLEU etc ...
                elif((c1 == JAUNE or c1 == BLEU) and (c2 == JAUNE or c2 == BLEU)):

                    Aretes.remove('JB')
                    c3 = JB.getCouleur(1)
                    c4 = JB.getCouleur(2)

                    if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

                        buf = True
                        Aretes.append('JB')

                elif((c1 == JAUNE or c1 == ORANGE) and (c2 == JAUNE or c2 == ORANGE)):

                    Aretes.remove('JO')
                    c3 = JO.getCouleur(1)
                    c4 = JO.getCouleur(2)

                    if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

                        buf = True
                        Aretes.append('JO')

                elif((c1 == VERT or c1 == ORANGE) and (c2 == VERT or c2 == ORANGE)):

                    Aretes.remove('VO')
                    c3 = VO.getCouleur(1)
                    c4 = VO.getCouleur(2)

                    if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

                        buf = True
                        Aretes.append('VO')

                elif((c1 == ROUGE or c1 == VERT) and (c2 == ROUGE or c2 == VERT)):

                    Aretes.remove('RV')
                    c3 = RV.getCouleur(1)
                    c4 = RV.getCouleur(2)

                    if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

                        buf = True
                        Aretes.append('RV')

                elif((c1 == BLEU or c1 == ROUGE) and (c2 == BLEU or c2 == ROUGE)):

                    Aretes.remove('BR')
                    c3 = BR.getCouleur(1)
                    c4 = BR.getCouleur(2)

                    if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

                        buf = True
                        Aretes.append('BR')

                elif((c1 == BLEU or c1 == ORANGE) and (c2 == BLEU or c2 == ORANGE)):

                    Aretes.remove('BO')
                    c3 = BO.getCouleur(1)
                    c4 = BO.getCouleur(2)

                    if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

                        buf = True
                        Aretes.append('BO')

                elif((c1 == BLEU or c1 == BLANC) and (c2 == BLEU or c2 == BLANC)):

                    Aretes.remove('BBl')
                    c3 = BBl.getCouleur(1)
                    c4 = BBl.getCouleur(2)

                    if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

                        buf = True
                        Aretes.append('BBl')

                elif((c1 == ROUGE or c1 == BLANC) and (c2 == ROUGE or c2 == BLANC)):

                    Aretes.remove('RBl')
                    c3 = RBl.getCouleur(1)
                    c4 = RBl.getCouleur(2)

                    if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

                        buf = True
                        Aretes.append('RBl')

                elif((c1 == VERT or c1 == BLANC) and (c2 == VERT or c2 == BLANC)):

                    Aretes.remove('VBl')
                    c3 = VBl.getCouleur(1)
                    c4 = VBl.getCouleur(2)

                    if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

                        buf = True
                        Aretes.append('VBl')

                elif((c1 == ORANGE or c1 == BLANC) and (c2 == ORANGE or c2 == BLANC)):

                    Aretes.remove('OBl')
                    c3 = OBl.getCouleur(1)
                    c4 = OBl.getCouleur(2)

                    if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

                        buf = True
                        Aretes.append('OBl')

                # Si aucune arête était à la place du buffer, c'est que c'est lui
                # qui y est 
                elif not buf:
                    bufProcessing1()

                # Si l'arête buffer était à la place d'où devait aller l'arête
                if buf:
                    bufProcessing2()

                # Retrait de l'arête qui était à la place de la première
                if((c3 == JAUNE or c3 == VERT) and (c4 == JAUNE or c4 == VERT)):
                    Aretes.remove('JV')
                elif((c3 == JAUNE or c3 == BLEU) and (c4 == JAUNE or c4 == BLEU)):
                    Aretes.remove('JB')
                elif((c3 == JAUNE or c3 == ORANGE) and (c4 == JAUNE or c4 == ORANGE)):
                    Aretes.remove('JO')
                elif((c3 == VERT or c3 == ORANGE) and (c4 == VERT or c4 == ORANGE)):
                    Aretes.remove('VO')
                elif((c3 == ROUGE or c3 == VERT) and (c4 == ROUGE or c4 == VERT)):
                    Aretes.remove('RV')
                elif((c3 == BLEU or c3 == ROUGE) and (c4 == BLEU or c4 == ROUGE)):
                    Aretes.remove('BR')
                elif((c3 == BLEU or c3 == ORANGE) and (c4 == BLEU or c4 == ORANGE)):
                    Aretes.remove('BO')
                elif((c3 == BLEU or c3 == BLANC) and (c4 == BLEU or c4 == BLANC)):
                    Aretes.remove('BBl')
                elif((c3 == ROUGE or c3 == BLANC) and (c4 == ROUGE or c4 == BLANC)):
                    Aretes.remove('RBl')
                elif((c3 == VERT or c3 == BLANC) and (c4 == VERT or c4 == BLANC)):
                    Aretes.remove('VBl')
                elif((c3 == ORANGE or c3 == BLANC) and (c4 == ORANGE or c4 == BLANC)):
                    Aretes.remove('OBl')
                    
                try:
                    # Calcul de l'indice donnant l'algorithme
                    # à faire pour placer les 2 arêtes
                    c = c1 * 10**3 + c2 * 10**2 + c3 * 10 + c4

                    # Récupération de l'algorithme dans le dictionnaire
                    reso = bh[c]
                except:
                    pass
                cube = applyMove(cube, reso)
                Resolution += reso

            # Les arêtes sont maintenant bien placés et la plupart sont
            # bien orientées
            
            reso = ''

            # Reaffectation des arêtes après les mouvements
            # trouvés précédement
            JV = Arete(cube[1], cube[10])
            JR = Arete(cube[5], cube[37])
            JB = Arete(cube[7], cube[28])
            JO = Arete(cube[3], cube[19])
            VO = Arete(cube[14], cube[21])
            RV = Arete(cube[41], cube[12])
            BR = Arete(cube[32], cube[39])
            BO = Arete(cube[30], cube[23])
            BBl = Arete(cube[34], cube[46])
            RBl = Arete(cube[43], cube[50])
            VBl = Arete(cube[16], cube[52])
            OBl = Arete(cube[25], cube[48])

            # Recherche des arêtes mal orientées
            if(JR.getCouleur(1) == ROUGE and JR.getCouleur(2) == JAUNE and 'JR' not in AretesDesor):

                AretesDesor.append('JR')
                JRLibre = False

            if(JV.getCouleur(1) == VERT and JV.getCouleur(2) == JAUNE and 'JV' not in AretesDesor):

                AretesDesor.append('JV')
                JVLibre = False

            if(JO.getCouleur(1) == ORANGE and JO.getCouleur(2) == JAUNE and 'JO' not in AretesDesor):

                AretesDesor.append('JO')
                JOLibre = False
                
            if(JB.getCouleur(1) == BLEU and JB.getCouleur(2) == JAUNE and 'JB' not in AretesDesor):

                AretesDesor.append('JB')
                JBLibre = False

            if(BO.getCouleur(1) == ORANGE and BO.getCouleur(2) == BLEU and 'BO' not in AretesDesor):
                AretesDesor.append('BO')

            if(BR.getCouleur(1) == ROUGE and BR.getCouleur(2) == BLEU and 'BR' not in AretesDesor):
                AretesDesor.append('BR')

            if(BBl.getCouleur(1) == BLANC and BBl.getCouleur(2) == BLEU and 'BBl' not in AretesDesor):
                AretesDesor.append('BBl')

            if(RV.getCouleur(1) == VERT and RV.getCouleur(2) == ROUGE and 'RV' not in AretesDesor):
                AretesDesor.append('RV')

            if(RBl.getCouleur(1) == BLANC and RBl.getCouleur(2) == ROUGE and 'RBl' not in AretesDesor):
                AretesDesor.append('RBl')

            if(VO.getCouleur(1) == ORANGE and VO.getCouleur(2) == VERT and 'VO' not in AretesDesor):
                AretesDesor.append('VO')

            if(OBl.getCouleur(1) == BLANC and OBl.getCouleur(2) == ORANGE and 'OBl' not in AretesDesor):
                AretesDesor.append('OBl')

            if(VBl.getCouleur(1) == BLANC and VBl.getCouleur(2) == VERT and 'VBl' not in AretesDesor):
                AretesDesor.append('VBl')

            # Cas des arêtes mal orientées en face
            if('JB' in AretesDesor and 'JV' in AretesDesor):

                reso += "M'UM'UM'U2MUMUMU2"
                AretesDesor.remove('JB')
                AretesDesor.remove('JV')
                JBLibre = True
                JVLibre = True

            if('JR' in AretesDesor and 'JO' in AretesDesor):

                reso += "S'US'US'U2SUSUSU2"
                AretesDesor.remove('JR')
                AretesDesor.remove('JO')
                JRLibre = True
                JOLibre = True

            if('JB' in AretesDesor and 'BBl' in AretesDesor):

                reso += "M'FM'FM'F2MFMFMF2"
                AretesDesor.remove('JB')
                AretesDesor.remove('BBl')
                JBLibre = True

            if('BO' in AretesDesor and 'BR' in AretesDesor):

                reso += "EFEFEF2E'FE'FE'F2"
                AretesDesor.remove('BO')
                AretesDesor.remove('BR')

            if('JR' in AretesDesor and 'RBl' in AretesDesor):

                reso += "SRSRSR2S'RS'RS'R2"
                AretesDesor.remove('JR')
                AretesDesor.remove('RBl')
                JRLibre = True

            if('BR' in AretesDesor and 'RV' in AretesDesor):

                reso += "ERERER2E'RE'RE'R2"
                AretesDesor.remove('BR')
                AretesDesor.remove('RV')


            if('JV' in AretesDesor and 'VBl' in AretesDesor):

                reso += "M'BM'BM'B2MBMBMB2"
                AretesDesor.remove('JV')
                AretesDesor.remove('VBl')
                JVLibre = True

            if('RV' in AretesDesor and 'VO' in AretesDesor):

                reso += "EBEBEB2E'BE'BE'B2"
                AretesDesor.remove('RV')
                AretesDesor.remove('VO')

            if('JO' in AretesDesor and 'OBl' in AretesDesor):

                reso += "SLSLSL2S'LS'LS'L2"
                AretesDesor.remove('JO')
                AretesDesor.remove('OBl')
                JOLibre = True

            if('VO' in AretesDesor and 'BO' in AretesDesor):

                reso += "ELELEL2E'LE'LE'L2"
                AretesDesor.remove('VO')
                AretesDesor.remove('BO')

            if('BBl' in AretesDesor and 'VBl' in AretesDesor):

                reso += "MDMDMD2M'DM'DM'D2"
                AretesDesor.remove('BBl')
                AretesDesor.remove('VBl')

            if('OBl' in AretesDesor and 'RBl' in AretesDesor):

                reso += "SDSDSD2S'DS'DS'D2"
                AretesDesor.remove('OBl')
                AretesDesor.remove('RBl')

            # Cas des arêtes mal orientées en coin
            if('JB' in AretesDesor and 'JR' in AretesDesor):

                reso += "RBMUMUMU2M'UM'UM'U2B'R'"
                AretesDesor.remove('JB')
                AretesDesor.remove('JR')
                JBLibre = True
                JRLibre = True

            if('JB' in AretesDesor and 'JO' in AretesDesor):

                reso += "L'B'MUMUMU2M'UM'UM'U2BL"
                AretesDesor.remove('JB')
                AretesDesor.remove('JO')
                JBLibre = True
                JOLibre = True

            if('JV' in AretesDesor and 'JR' in AretesDesor):

                reso += "R'F'MUMUMU2M'UM'UM'U2FR"
                AretesDesor.remove('JV')
                AretesDesor.remove('JR')
                JVLibre = True
                JRLibre = True

            if('JV' in AretesDesor and 'JO' in AretesDesor):

                reso += "LFMUMUMU2M'UM'UM'U2F'L'"
                AretesDesor.remove('JV')
                AretesDesor.remove('JO')
                JVLibre = True
                JOLibre = True

            if('BBl' in AretesDesor and 'BR' in AretesDesor):

                reso += "RUMFMFMF2M'FM'FM'F2U'R'"
                AretesDesor.remove('BBl')
                AretesDesor.remove('BR')

            if('BBl' in AretesDesor and 'BO' in AretesDesor):

                reso += "L'U'MFMFMF2M'FM'FM'F2UL"
                AretesDesor.remove('BBl')
                AretesDesor.remove('BO')

            if('JB' in AretesDesor and 'BR' in AretesDesor):

                reso += "R'D'MFMFMF2M'FM'FM'F2DR"
                AretesDesor.remove('JB')
                AretesDesor.remove('BR')
                JBLibre = True

            if('JB' in AretesDesor and 'BO' in AretesDesor):

                reso += "LDMFMFMF2M'FM'FM'F2D'L'"
                AretesDesor.remove('JB')
                AretesDesor.remove('BO')
                JBLibre = True

            if('RBl' in AretesDesor and 'RV' in AretesDesor):

                reso += "BUSRSRSR2S'RS'RS'R2U'B'"
                AretesDesor.remove('RBl')
                AretesDesor.remove('RV')

            if('RBl' in AretesDesor and 'BR' in AretesDesor):

                reso += "F'U'SRSRSR2S'RS'RS'R2UF"
                AretesDesor.remove('RBl')
                AretesDesor.remove('BR')

            if('JR' in AretesDesor and 'RV' in AretesDesor):

                reso += "B'D'SRSRSR2S'RS'RS'R2DB"
                AretesDesor.remove('JR')
                AretesDesor.remove('RV')
                JRLibre = True

            if('JR' in AretesDesor and 'BR' in AretesDesor):

                reso += "FDSRSRSR2S'RS'RS'R2D'F'"
                AretesDesor.remove('JR')
                AretesDesor.remove('BR')
                JRLibre = True

            if('VBl' in AretesDesor and 'VO' in AretesDesor):

                reso += "LUMBMBMB2M'BM'BM'B2U'L'"
                AretesDesor.remove('VBl')
                AretesDesor.remove('VO')

            if('VBl' in AretesDesor and 'RV' in AretesDesor):

                reso += "R'U'MBMBMB2M'BM'BM'B2UR"
                AretesDesor.remove('VBl')
                AretesDesor.remove('RV')

            if('JV' in AretesDesor and 'VO' in AretesDesor):

                reso += "L'D'MBMBMB2M'BM'BM'B2DL"
                AretesDesor.remove('JV')
                AretesDesor.remove('VO')
                JVLibre = True

            if('JV' in AretesDesor and 'RV' in AretesDesor):

                reso += "RDMBMBMB2M'BM'BM'B2D'R'"
                AretesDesor.remove('JV')
                AretesDesor.remove('RV')
                JVLibre = True

            if('OBl' in AretesDesor and 'BO' in AretesDesor):

                reso += "FUSLSLSL2S'LS'LS'L2U'F'"
                AretesDesor.remove('OBl')
                AretesDesor.remove('BO')

            if('OBl' in AretesDesor and 'VO' in AretesDesor):

                reso += "B'U'SLSLSL2S'LS'LS'L2UB"
                AretesDesor.remove('OBl')
                AretesDesor.remove('VO')

            if('JO' in AretesDesor and 'BO' in AretesDesor):

                reso += "F'D'SLSLSL2S'LS'LS'L2DF"
                AretesDesor.remove('JO')
                AretesDesor.remove('BO')
                JOLibre = True

            if('JO' in AretesDesor and 'VO' in AretesDesor):

                reso += "BDSLSLSL2S'LS'LS'L2D'B'"
                AretesDesor.remove('JO')
                AretesDesor.remove('VO')
                JOLibre = True

            if('VBl' in AretesDesor and 'RBl' in AretesDesor):

                reso += "RFMDMDMD2M'DM'DM'D2F'R'"
                AretesDesor.remove('VBl')
                AretesDesor.remove('RBl')

            if('VBl' in AretesDesor and 'oBl' in AretesDesor):

                reso += "L'F'MDMDMD2M'DM'DM'D2FL"
                AretesDesor.remove('VBl')
                AretesDesor.remove('OBl')

            if('VBl' in AretesDesor and 'OBl' in AretesDesor):

                reso += "L'F'MDMDMD2M'DM'DM'D2FL"
                AretesDesor.remove('VBl')
                AretesDesor.remove('OBl')

            if('BBl' in AretesDesor and 'RBl' in AretesDesor):

                reso += "R'B'MDMDMD2M'DM'DM'D2BR"
                AretesDesor.remove('BBl')
                AretesDesor.remove('RBl')

            if('BBl' in AretesDesor and 'OBl' in AretesDesor):

                reso += "LBMDMDMD2M'DM'DM'D2B'L'"
                AretesDesor.remove('BBl')
                AretesDesor.remove('OBl')

            # On arrive ici si les arêtes mal orientées ne sont pas
            # à des emplacements propices

            # Si l'arête BLEU-ROUGE est mal orientée
            if 'BR' in AretesDesor:

                # Si l'arête à l'emplacement JAUNE-ORANGE est mal orientée
                if not JOLibre:

                    # Placement de l'arête en face et orientation
                    reso += resoInter + "RSUSUSU2S'US'US'U2R'" + invMove(resoInter)

                    # Retrait de l'arête JAUNE-ORANGE si c'était
                    # bien elle qui était mal orientée à cet
                    # emplacement
                    if JO.contient(JAUNE, ORANGE):
                        AretesDesor.remove('JO')
                    AretesDesor.remove('BR')
                    JOLibre = True
                    resoInter = ''

                # Même raisonnement avec l'emplacement JAUNE-VERT etc ...
                elif not JVLibre:

                    reso += resoInter + "F'MUMUMU2M'UM'UM'U2F" + invMove(resoInter)
                    if JV.contient(JAUNE, VERT):
                        AretesDesor.remove('JV')
                    AretesDesor.remove('BR')
                    JOLibre = True
                    resoInter = ''

                # Sinon on monte l'arête au dessus à
                # l'emplacement JAUNE-ROUGE
                else:

                    resoInter += "R"
                    AretesDesor.remove('BR')
                    JRLibre = False

            # Même raisonnement avec l'arête ROUGE-VERT etc ...
            if 'RV' in AretesDesor:

                if not JBLibre:

                    reso += resoInter + "BMUMUMU2M'UM'UM'U2B'" + invMove(resoInter)
                    if JV.contient(JAUNE, BLEU):
                        AretesDesor.remove('JB')
                    AretesDesor.remove('RV')
                    JBLibre = True
                    resoInter = ''

                elif not JOLibre:

                    reso += resoInter + "R'SUSUSU2S'US'US'U2R" + invMove(resoInter)
                    if JV.contient(JAUNE, ORANGE):
                        AretesDesor.remove('JO')
                    AretesDesor.remove('RV')
                    JOLibre = True
                    resoInter = ''

                else:

                    resoInter += "R'"
                    AretesDesor.remove('RV')
                    JRLibre = False

            if 'VO' in AretesDesor:

                if not JBLibre:

                    reso += resoInter + "B'MUMUMU2M'UM'UM'U2B" + invMove(resoInter)
                    if JV.contient(JAUNE, BLEU):
                        AretesDesor.remove('JB')
                    AretesDesor.remove('VO')
                    JBLibre = True
                    resoInter = ''

                elif not JRLibre:

                    reso += resoInter + "LSUSUSU2S'US'US'U2L'" + invMove(resoInter)
                    if JV.contient(JAUNE, ROUGE):
                        AretesDesor.remove('JR')
                    AretesDesor.remove('VO')
                    JRLibre = True
                    resoInter = ''

                else:

                    resoInter += "L"
                    AretesDesor.remove('VO')
                    JOLibre = False

            if 'BO' in AretesDesor:

                if not JVLibre:

                    reso += resoInter + "FMUMUMU2M'UM'UM'U2F'" + invMove(resoInter)
                    if JV.contient(JAUNE, VERT):
                        AretesDesor.remove('JV')
                    AretesDesor.remove('BO')
                    JVLibre = True
                    resoInter = ''

                elif not JRLibre:

                    reso += resoInter + "L'SUSUSU2S'US'US'U2L" + invMove(resoInter)
                    if JV.contient(JAUNE, ROUGE):
                        AretesDesor.remove('JR')
                    AretesDesor.remove('BO')
                    JRLibre = True
                    resoInter = ''

                else:

                    resoInter += "L'"
                    AretesDesor.remove('BO')
                    JOLibre = False

            if 'BBl' in AretesDesor:

                if not JVLibre:

                    reso += resoInter + "F2MUMUMU2M'UM'UM'U2F2" + invMove(resoInter)
                    if JV.contient(JAUNE, VERT):
                        AretesDesor.remove('JV')
                    AretesDesor.remove('BBl')
                    JVLibre = True
                    resoInter = ''

                elif not JRLibre:

                    reso += resoInter + "D'L2SUSUSU2S'US'US'U2L2D" + invMove(resoInter)
                    if JV.contient(JAUNE, ROUGE):
                        AretesDesor.remove('JR')
                    AretesDesor.remove('BBl')
                    JRLibre = True
                    resoInter = ''

                elif not JOLibre:

                    reso += resoInter + "DR2SUSUSU2S'US'US'U2R2D'" + invMove(resoInter)
                    if JV.contient(JAUNE, ORANGE):
                        AretesDesor.remove('JO')
                    AretesDesor.remove('BBl')
                    JRLibre = True
                    resoInter = ''

                else:

                    resoInter += "F2"
                    AretesDesor.remove('BBl')
                    JBLibre = False

            if 'RBl' in AretesDesor:

                if not JOLibre:

                    reso += resoInter + "R2SUSUSU2S'US'US'U2R2" + invMove(resoInter)
                    if JV.contient(JAUNE, ORANGE):
                        AretesDesor.remove('JO')
                    AretesDesor.remove('RBl')
                    JOLibre = True
                    resoInter = ''

                elif not JVLibre:

                    reso += resoInter + "D'F2MUMUMU2M'UM'UM'U2F2D" + invMove(resoInter)
                    if JV.contient(JAUNE, VERT):
                        AretesDesor.remove('JV')
                    AretesDesor.remove('RBl')
                    JVLibre = True
                    resoInter = ''

                elif not JBLibre:

                    reso += resoInter + "DB2MUMUMU2M'UM'UM'U2B2D'" + invMove(resoInter)
                    if JV.contient(JAUNE, BLEU):
                        AretesDesor.remove('JB')
                    AretesDesor.remove('RBl')
                    JBLibre = True
                    resoInter = ''

                else:

                    resoInter += "R2"
                    AretesDesor.remove('RBl')
                    JRLibre = False

            if 'VBl' in AretesDesor:

                if not JBLibre:

                    reso += resoInter + "B2MUMUMU2M'UM'UM'U2B2" + invMove(resoInter)
                    if JV.contient(JAUNE, BLEU):
                        AretesDesor.remove('JB')
                    AretesDesor.remove('VBl')
                    JBLibre = True
                    resoInter = ''

                elif not JRLibre:

                    reso += resoInter + "DL2SUSUSU2S'US'US'U2L2D'" + invMove(resoInter)
                    if JV.contient(JAUNE, ROUGE):
                        AretesDesor.remove('JR')
                    AretesDesor.remove('VBl')
                    JRLibre = True
                    resoInter = ''

                elif not JOLibre:

                    reso += resoInter + "D'R2SUSUSU2S'US'US'U2R2D" + invMove(resoInter)
                    if JV.contient(JAUNE, ORANGE):
                        AretesDesor.remove('JO')
                    AretesDesor.remove('VBl')
                    JOLibre = True
                    resoInter = ''

                else:

                    resoInter += "B2"
                    AretesDesor.remove('VBl')
                    JVLibre = False

            if 'OBl' in AretesDesor:

                if not JRLibre:

                    reso += resoInter + "L2SUSUSU2S'US'US'U2L2" + invMove(resoInter)
                    if JV.contient(JAUNE, ROUGE):
                        AretesDesor.remove('JR')
                    AretesDesor.remove('OBl')
                    JRLibre = True
                    resoInter = ''

                elif not JBLibre:

                    reso += resoInter + "D'B2MUMUMU2M'UM'UM'U2B2D" + invMove(resoInter)
                    if JV.contient(JAUNE, BLEU):
                        AretesDesor.remove('JB')
                    AretesDesor.remove('OBl')
                    JBLibre = True
                    resoInter = ''

                elif not JVLibre:

                    reso += resoInter + "DF2MUMUMU2M'UM'UM'U2F2D'" + invMove(resoInter)
                    if JV.contient(JAUNE, VERT):
                        AretesDesor.remove('JV')
                    AretesDesor.remove('OBl')
                    JVLibre = True
                    resoInter = ''

            # Toutes les arêtes sont maintenant bien orientées

            #---CUBE FINI---#
            
            Resolution += reso
            cube = applyMove(cube, reso)
            noConvertRes = Resolution
            Resolution = convertToSymbols(Resolution)
            Resolution = opti(Resolution)
            if lenght(Solution) > lenght(Resolution) and Resolution != '':
                Solution = Resolution
                noConvertSol = noConvertRes
                
            
            reso = ''
            Resolution = ''

    return Solution, noConvertSol
