from PIL import Image, ImageTk
from tkinter import Tk, Button, Frame, RIGHT, Text, LEFT, YES, Y, BOTH, FLAT, Label, Canvas, GROOVE, TOP, BOTTOM, StringVar, Entry, Scrollbar
from functools import partial
import cv2
import pytesseract
import PIL
from tkinter.messagebox import *
from time import *
from timeit import default_timer
from datetime import datetime
import outils
import SolveBH
import serial

arduino = serial.Serial('COM3')
sleep(1)

fenetre = Tk()
#===========================================================================================#
#déclaration_frame/canvas

framePrinc = Frame(fenetre, borderwidth = 3, bg = '#C2BCBA')
framePrinc.pack()

#===============================================#
#titre principale/structure canvas

maintienBas = Canvas(framePrinc, width = 1400, height = 4, highlightthickness = 0, borderwidth = 0, bg = 'black')
maintienBas.pack(anchor = 's', side = BOTTOM)

maintienHaut = Canvas(framePrinc, width = 1400, height = 4, highlightthickness = 0, borderwidth = 0, bg = 'black')
maintienHaut.pack()

maintienDroite = Canvas(framePrinc, width = 4, height = 920, highlightthickness = 0, borderwidth = 0, bg = 'black')
maintienDroite.pack(anchor = 'e', side = RIGHT)

maintienGauche = Canvas(framePrinc, width = 4, height = 920, highlightthickness = 0, borderwidth = 0, bg = 'black')
maintienGauche.pack(anchor = 'w', side = LEFT)

frameTitrePrinc = Frame(framePrinc, bg = '#C2BCBA')
frameTitrePrinc.pack()

maintienTitreVert = Canvas(frameTitrePrinc, width = 1385, height = 0, borderwidth = 0, highlightthickness = 0, bg = '#C2BCBA')
maintienTitreVert.pack()

maintienTitreHor = Canvas(frameTitrePrinc, width = 0, height = 100, borderwidth = 0, highlightthickness = 0, bg = '#C2BCBA')
maintienTitreHor.pack(side = RIGHT)

fontConfTitrePrinc = "-family {DejaVu Sans} -size 30 -weight normal -underline 0 -overstrike 0"
titrePrinc = Label(frameTitrePrinc, text = "Cube Solver", fg = '#5F5F5F', bg = '#C2BCBA')
titrePrinc.configure(font=fontConfTitrePrinc)
titrePrinc.pack(side = LEFT, anchor = 'nw')

#crédit
fontConfCredit = "-family {DejaVu Sans} -size 10 -weight normal -underline 0 -overstrike 0"
credit = Label(framePrinc, text = "By Gros Antoine and Si Larbi Lucas.", fg = 'black', bg = '#C2BCBA')
credit.configure(font=fontConfCredit)
credit.pack(anchor = 'sw', side = BOTTOM)


#===============================================#
#Gestion du Patron

frameGestionCube = Frame(framePrinc, bg = '#C2BCBA', borderwidth = 3, relief = GROOVE)
frameGestionCube.pack(side = RIGHT, pady = 20, padx = 50, anchor = 'ne')

frameControlPatron = Frame(frameGestionCube)
frameControlPatron.pack(anchor = 'nw', pady = 5, padx = 5)

framePatron = Frame(frameGestionCube,  bg = '#C2BCBA')
framePatron.pack()

frameTitrePatron = Frame(frameGestionCube)
frameTitrePatron.pack(anchor = "s")

frameFaceL = Frame(framePatron)
frameFaceL.pack(anchor = 'nw', side = LEFT, pady = 168, padx = 10)

frameFaceR = Frame(framePatron)
frameFaceR.pack(anchor = 'ne', side = RIGHT, pady = 168, padx = 10)

frameFaceU = Frame(framePatron)
frameFaceU.pack(anchor = 'n', pady = 5)

frameFaceF = Frame(framePatron)
frameFaceF.pack(anchor = 'c', pady = 5)

frameFaceD = Frame(framePatron)
frameFaceD.pack(anchor = 's', pady = 5)

frameFaceB = Frame(framePatron)
frameFaceB.pack(anchor = 's', pady = 5)

mel = ""

#===============================================#
#Gestion de la partie gauche

frameOptionGauche = Frame(framePrinc, bg = '#C2BCBA', relief = GROOVE, borderwidth = 3)
frameOptionGauche.pack(anchor = 'nw',side = LEFT, pady = 20, padx = 40)

maintienOptionGauche = Canvas(frameOptionGauche, width = 660, height = 0,  highlightthickness = 0,
                        borderwidth = 0, bg = '#C2BCBA')
maintienOptionGauche.pack(anchor = 'n')

frameCommandeGauche = Frame(frameOptionGauche, bg = '#C2BCBA')
frameCommandeGauche.pack(anchor = 'nw', padx = 5, pady = 5)

frameAffichageGauche = Frame(frameOptionGauche, bg = '#C2BCBA', )
frameAffichageGauche.pack()

maintienGaucheAffichage = Canvas(frameAffichageGauche, width = 640, height = 0,  highlightthickness = 0,
                        borderwidth = 0, bg = '#C2BCBA')
maintienGaucheAffichage.pack(anchor = 'n')

frameTestMoteurs = Frame(frameAffichageGauche,  bg = '#C2BCBA')

frameMelange = Frame(frameAffichageGauche, bg = '#C2BCBA')

frameImageDeFond = Frame(frameAffichageGauche)

frameParametre = Frame(frameAffichageGauche, bg = '#C2BCBA')
                      
frameTitreCamera = Frame(frameAffichageGauche, bg = '#C2BCBA')
frameTitreCamera.pack(anchor = "n")

frameImage = Frame(frameAffichageGauche,   bg = '#C2BCBA')
frameImage.pack()

lmain = Label(frameImage,  bg = '#C2BCBA')
lmain.pack()

fontConf = "-family {DejaVu Sans} -size 18 -weight normal -underline 0 -overstrike 0"
labelFrameMelange = Label(frameMelange, text = "Scramble",   bg = '#C2BCBA')
labelFrameMelange.configure(font=fontConf)
labelFrameMelange.pack(anchor = 'n', side = TOP)

fontConfLabelFrameTestMoteurs = "-family {DejaVu Sans} -size 18 -weight normal -underline 0 -overstrike 0"
labelFrameTestMoteurs = Label(frameTestMoteurs, text = "Motors test",   bg = '#C2BCBA')
labelFrameTestMoteurs.configure(font=fontConfLabelFrameTestMoteurs)
labelFrameTestMoteurs.pack(anchor = 'n', side = TOP)

frameInfoTest = Frame(frameTestMoteurs, bg = '#C2BCBA')
frameInfoTest.pack(anchor = 'nw')

frameTestMoteursU = Frame(frameTestMoteurs, bg = '#C5B2B2', borderwidth = 2, relief = GROOVE)
frameTestMoteursU.pack(padx = 5, pady = 10, anchor = 'w')

frameTestMoteursF = Frame(frameTestMoteurs, bg = '#C5B2B2', borderwidth = 2, relief = GROOVE)
frameTestMoteursF.pack(padx = 5, pady = 10, anchor = 'w')

frameTestMoteursR = Frame(frameTestMoteurs, bg = '#C5B2B2', borderwidth = 2, relief = GROOVE)
frameTestMoteursR.pack(padx = 5, pady = 10, anchor = 'w')

frameTestMoteursB = Frame(frameTestMoteurs, bg = '#C5B2B2', borderwidth = 2, relief = GROOVE)
frameTestMoteursB.pack(padx = 5, pady = 10, anchor = 'w')

frameTestMoteursL = Frame(frameTestMoteurs, bg = '#C5B2B2', borderwidth = 2, relief = GROOVE)
frameTestMoteursL.pack(padx = 5, pady = 10, anchor = 'w')

frameTestMoteursD = Frame(frameTestMoteurs, bg = '#C5B2B2', borderwidth = 2, relief = GROOVE)
frameTestMoteursD.pack(padx = 5, pady = 10, anchor = 'w')

frameEntrezMelange = Frame(frameMelange, bg = '#C5B2B2', borderwidth = 2, relief = GROOVE)
frameEntrezMelange.pack(anchor = 'n', pady = 5)

frameTab = Frame(framePrinc, bg = '#C2BCBA')

frameResultat = Frame(framePrinc, bg = '#C2BCBA')

#===========================================================================================#
#patron du cube
couleur = ['yellow', 'blue', 'red', 'green', 'orange', 'white']
couleurTerne = ['#EBFF88', '#39B2FD', '#FF7171', '#5EFF7A', '#FFC35C', '#FFFFFF']


def updateCouleur(valFace,conteur, stick): #methode principale
    
    if stick != 4:
        conteur[stick] += 1
        for i in range(len(conteur)):
            if conteur[i] == 6:
                conteur[i] = 0
        valFace[stick].config(bg = couleur[conteur[stick]], activebackground = couleur[conteur[stick]])

    if valFace == valFaceU:
        SolveBH.setCouleur(0, conteur)
    elif valFace == valFaceL:
        SolveBH.setCouleur(2, conteur)
    elif valFace == valFaceF:
        SolveBH.setCouleur(3, conteur)
    elif valFace == valFaceR:
        SolveBH.setCouleur(4, conteur)
    elif valFace == valFaceD:
        SolveBH.setCouleur(5, conteur)
    elif valFace == valFaceB:
        SolveBH.setCouleur(1, conteur[::-1])
        
image = Image.open("contour.png")
photo = ImageTk.PhotoImage(image)

#===============================================#
#face F
valFaceF = []
conteurF = [1,1,1,1,1,1,1,1,1]

stick = 0
for i in range(3):
    for j in range(3):
        stickFaceF = Button(frameFaceF, relief = FLAT, borderwidth = 0, activebackground = couleur[conteurF[stick]],
                            width = 51,height = 51, bg = couleur[conteurF[stick]], image = photo,
                            command = partial(updateCouleur, valFaceF, conteurF,stick), highlightthickness = 0)
        valFaceF.append(stickFaceF)
        stickFaceF.grid(column = j, row = i)
        stick += 1
#===============================================#
#face R
valFaceR = []
conteurR = [2,2,2,2,2,2,2,2,2]

stick = 0
for i in range(3):
    for j in range(3):
        stickFaceR = Button(frameFaceR, relief = FLAT, borderwidth = 0, activebackground = couleur[conteurR[stick]],
                            width = 51,height = 51, bg = couleur[conteurR[stick]], image = photo,
                            command = partial(updateCouleur, valFaceR, conteurR, stick), highlightthickness = 0)
        valFaceR.append(stickFaceR)
        stickFaceR.grid(column = j, row = i)
        stick += 1
#===============================================#
#face L
valFaceL = []
conteurL = [4,4,4,4,4,4,4,4,4]

stick = 0
for i in range(3):
    for j in range(3):
        stickFaceL = Button(frameFaceL, relief = FLAT, borderwidth = 0, activebackground = couleur[conteurL[stick]],
                            width = 51,height = 51, bg = couleur[conteurL[stick]], image = photo,
                            command = partial(updateCouleur, valFaceL, conteurL, stick), highlightthickness = 0)
        valFaceL.append(stickFaceL)
        stickFaceL.grid(column = j, row = i)
        stick += 1
#===============================================#
#face B
valFaceB = []
conteurB = [3,3,3,3,3,3,3,3,3]

stick = 0
for i in range(3):
    for j in range(3):
        stickFaceB = Button(frameFaceB, relief = FLAT, borderwidth = 0, activebackground = couleur[conteurB[stick]],
                            width = 51,height = 51, bg = couleur[conteurB[stick]], image = photo,
                            command = partial(updateCouleur, valFaceB, conteurB, stick), highlightthickness = 0)
        valFaceB.append(stickFaceB)
        stickFaceB.grid(column = j, row = i)
        stick += 1
#===============================================#
#face U
valFaceU = []
conteurU = [0,0,0,0,0,0,0,0,0]

stick = 0
for i in range(3):
    for j in range(3):
        stickFaceU = Button(frameFaceU, relief = FLAT, borderwidth = 0, activebackground = couleur[conteurU[stick]],
                            width = 51,height = 51, bg = couleur[conteurU[stick]], image = photo,
                            command = partial(updateCouleur, valFaceU, conteurU, stick), highlightthickness = 0)
        valFaceU.append(stickFaceU)
        stickFaceU.grid(column = j, row = i)
        stick += 1
#===============================================#
#face D
valFaceD = []
conteurD = [5,5,5,5,5,5,5,5,5]

stick = 0
for i in range(3):
    for j in range(3):
        stickFaceD = Button(frameFaceD, relief = FLAT, borderwidth = 0, activebackground = couleur[conteurD[stick]],
                            width = 51,height = 51, bg = couleur[conteurD[stick]], image = photo,
                            command = partial(updateCouleur, valFaceD, conteurD, stick), highlightthickness = 0)
        valFaceD.append(stickFaceD)
        stickFaceD.grid(column = j, row = i)
        stick += 1
#===========================================================================================#        
#Label Patron du rubik's cube
fontConflabelFramePatron = "-family {DejaVu Sans} -size 22 -weight normal -underline 0 -overstrike 0"
labelFramePatron = Label(frameTitrePatron, text = "Rubik's Cube Pattern", bg = '#C2BCBA')
labelFramePatron.configure(font=fontConflabelFramePatron)
labelFramePatron.pack()

#===========================================================================================#
#Gestion de la camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    image = PIL.Image.fromarray(cv2image)
    imageTkinter = ImageTk.PhotoImage(image=image)
    lmain.imgtk = imageTkinter
    lmain.configure(image=imageTkinter)
    lmain.after(10, show_frame)

show_frame()
#===========================================================================================#
#Label Vue Camera
fontConflabelFrameCamera = "-family {DejaVu Sans} -size 18 -weight normal -underline 0 -overstrike 0"
labelFrameCamera = Label(frameTitreCamera, text = "Camera view",   bg = '#C2BCBA')
labelFrameCamera.configure(font=fontConflabelFrameCamera)
labelFrameCamera.pack()

#===========================================================================================#
#Onglet control camera
def Ouvrir_Fermer(etat):
    global open_closeCam
    global open_closeTest
    global open_closeMelange
    global open_closeParametre

    if open_closeCam == 1:
        frameImage.pack_forget()
        frameTitreCamera.pack_forget()
        frameImageDeFond.pack()
        ouvrir_fermer.config(text = "Turn on cameras")
    else:
        frameTestMoteurs.pack_forget()
        frameMelange.pack_forget()
        frameParametre.pack_forget()
        frameImageDeFond.pack_forget()
        frameAffichageGauche.pack_forget()
        testMoteurs.config(text = 'motors test')
        melange.config(text = 'Scramble')
        open_closeTest = 0
        open_closeMelange = 0
        open_closeParametre = 0
        frameTitreCamera.pack()
        frameImage.pack()
        frameAffichageGauche.pack()
        ouvrir_fermer.config(text = "Turn off cameras")
    open_closeCam = 1 - open_closeCam

open_closeCam = 1
ouvrir_fermer = Button(frameCommandeGauche, text = "Turn off cameras",
                       command = partial(Ouvrir_Fermer, open_closeCam))
ouvrir_fermer.pack(side = LEFT)
#===========================================================================================#
#control patron/reset
def resetAction():
    conteurF = [1,1,1,1,1,1,1,1,1]
    resetCouleur(valFaceF, conteurF)
    conteurR = [2,2,2,2,2,2,2,2,2]
    resetCouleur(valFaceR, conteurR)
    conteurB = [3,3,3,3,3,3,3,3,3]
    resetCouleur(valFaceB, conteurB)
    conteurL = [4,4,4,4,4,4,4,4,4]
    resetCouleur(valFaceL, conteurL)
    conteurD = [5,5,5,5,5,5,5,5,5]
    resetCouleur(valFaceD, conteurD)
    conteurU = [0,0,0,0,0,0,0,0,0]
    resetCouleur(valFaceU, conteurU)
    SolveBH.resetCube()
    updateCube(SolveBH.getCube())
    
def resetCouleur(valFace, conteur):

    global melange
        
    for i in range(9):
        valFace[i].config(bg = couleur[conteur[i]], activebackground = couleur[conteur[i]])

    SolveBH.resetCube()
    updateCube(SolveBH.getCube())
    mel = ""
    
reset = Button(frameControlPatron, text = 'Reset colors', command = resetAction)
reset.pack()
#===========================================================================================#
#Onglet test moteurs
def TestMoteurs():
    global open_closeTest
    global open_closeCam
    global open_closeMelange
    global open_closeParametre
    
    if open_closeTest == 1:
        frameTestMoteurs.pack_forget()
        frameImageDeFond.pack()
        testMoteurs.config(text = 'Motors test')
    else:
        frameImage.pack_forget()
        frameMelange.pack_forget()
        frameParametre.pack_forget()
        frameTitreCamera.pack_forget()
        frameImageDeFond.pack_forget()
        frameAffichageGauche.pack_forget()
        ouvrir_fermer.config(text = "Turn on cameras")
        melange.config(text = 'Scramble')
        open_closeCam = 0
        open_closeMelange = 0
        open_closeParametre = 0
        frameTestMoteurs.pack(side = TOP)
        frameAffichageGauche.pack()
        testMoteurs.config(text = 'Close motors test')
    open_closeTest = 1 - open_closeTest

open_closeTest = 0
testMoteurs = Button(frameCommandeGauche, text = 'Motors test', command = TestMoteurs)
testMoteurs.pack(side = LEFT)

def envoie(moves):

    global arduino
    arduino.write(outils.convertToSymbols(moves).encode())

def envoieS(moves):

    global arduino
    arduino.write(moves.encode())

def TestMoteurs(moteur, action):

    global conteurTest
    
    if conteurTest > 50:
        showwarning('Alert', 'Test limit reached')
        return
    if action == 0:

        SolveBH.setCube(outils.applyMove(SolveBH.getCube(), Face[moteur]))
        updateCube(SolveBH.getCube())
        envoie(Face[moteur])
        
        if Face[moteur] == Mvt.get()[-1] and Face[moteur] == Mvt.get()[-2] and Face[moteur] == Mvt.get()[-3]:
            conteurTest -=3
            Mvt.set(Mvt.get()[:-3])
            del mvtInverse[:3]
            return
        if Mvt.get()[-2:] == Face[moteur]+'\'':
            conteurTest -= 2
            Mvt.set(Mvt.get()[:-2])
            del mvtInverse[0]
        else:
            Mvt.set(Mvt.get()+ Face[moteur])
            conteurTest += 1
            mvtInverse.insert(0, Face[moteur]+'\'')
    elif action == 1:

        SolveBH.setCube(outils.applyMove(SolveBH.getCube(), Face[moteur] + "'"))
        updateCube(SolveBH.getCube())
        envoie(Face[moteur] + "'")
        
        #print(Mvt.get()[-2:])
        #print('face:' +Face[moteur] + '\'')
        if Face[moteur] + '\'' == Mvt.get()[-2:] and Face[moteur] + '\'' == Mvt.get()[-4:-2] and Face[moteur] + '\'' == Mvt.get()[-6:-4]:
            conteurTest -=6
            Mvt.set(Mvt.get()[:-6])
            del mvtInverse[:3]
            return
        if Mvt.get()[-1] == Face[moteur]:
            conteurTest -= 1
            Mvt.set(Mvt.get()[:-1])
            del mvtInverse[0]
        else:
            Mvt.set(Mvt.get()+ Face[moteur]+'\'')
            conteurTest += 2
            mvtInverse.insert(0, Face[moteur])
    elif action == 2:

        SolveBH.setCube(outils.applyMove(SolveBH.getCube(), Face[moteur] + '2'))
        updateCube(SolveBH.getCube())
        envoie(Face[moteur] + "2")
        
        if Mvt.get()[-2:] == Face[moteur]+'2':
            conteurTest -= 2
            Mvt.set(Mvt.get()[:-2])
            del mvtInverse[0]
        else:
            Mvt.set(Mvt.get()+ Face[moteur]+'2')
            conteurTest += 2
            mvtInverse.insert(0, Face[moteur]+'2')

mvtInverse = []
conteurTest = 0
conteurMvtHoraire = 0
conteurMvtAntiHoraire = 0
Moteurs = [frameTestMoteursU, frameTestMoteursF, frameTestMoteursR, frameTestMoteursB, frameTestMoteursL, frameTestMoteursD]
texte = ['     Clockwise turn(90°)     ', '         Anti-clockwise turn(90°)         ', '     Full turn(180°)     ']
moteurs = ['Motor U', 'Motor F', 'Motor R', 'Motor B', 'Motor L', 'Motor D']
Face = ['U', 'F', 'R', 'B', 'L', 'D']

for i,frame in enumerate(Moteurs):
    quelMoteurs = Label(frame, text = moteurs[i], bg= '#C5B2B2').pack()
    for j in range(3):
        Button(frame, text = texte[j], command = partial(TestMoteurs, i, j),
               highlightthickness =0, pady = 10, padx = 2, bg = couleurTerne[i], activebackground = couleurTerne[i]).pack(side = LEFT)
        
Mvt = StringVar(frameInfoTest, 'Mouvements to do: ')
MvtEffectues = Label(frameInfoTest, textvariable = Mvt, bg = '#C2BCBA').pack()

def ResetTest():
    global conteurTest
    global mvtInverse
    conteurTest = 0
    Mvt.set('Mouvements to do: ')
    SolveBH.resetCube()
    envoie(mvtInverse)
    mvtInverse = []
    updateCube(SolveBH.getCube())
    #faire les mouvement de cette liste : 'mvtInverse'
    
resteTest = Button(frameInfoTest, text = 'Reset test', command = ResetTest)
resteTest.pack(side = LEFT, padx = 4)

#===========================================================================================#
#Onglet Mélange...
def TestMoteurs():
    global open_closeMelange
    global open_closeCam
    global open_closeTest
    global open_closeParametre
    
    if open_closeMelange == 1:
        frameMelange.pack_forget()
        frameImageDeFond.pack()
        melange.config(text = 'Scramble')
    else:
        frameImage.pack_forget()
        frameTitreCamera.pack_forget()
        frameTestMoteurs.pack_forget()
        frameParametre.pack_forget()
        frameImageDeFond.pack_forget()
        frameAffichageGauche.pack_forget()
        ouvrir_fermer.config(text = "Turn on cameras")
        testMoteurs.config(text = "Motors test")
        open_closeCam = 0
        open_closeTest = 0
        open_closeParametre = 0
        frameMelange.pack(side = TOP)
        frameAffichageGauche.pack()
        melange.config(text = 'Close Scramble')
    open_closeMelange = 1 - open_closeMelange

open_closeMelange = 0
melange = Button(frameCommandeGauche, text = 'Scramble', command = TestMoteurs)
melange.pack(side = LEFT)

lebelEntry = Label(frameEntrezMelange, text = 'Enter Scramble: ', bg = '#C5B2B2')
lebelEntry.grid(column = 0, row = 0)

melangeEntre = StringVar(frameEntrezMelange)
entryMelange = Entry(frameEntrezMelange, textvariable = melangeEntre)
entryMelange.grid(column = 1, row = 0, ipadx = 180, padx = 5)
melangeEnvoye = StringVar(frameEntrezMelange)
textEnvoye = Text(frameEntrezMelange, bg = '#C2BCBA', width = 60, height = 20, state = 'disabled', fg = '#291E1E')
ScrollBar = Scrollbar(frameEntrezMelange, bg = '#C2BCBA')
ScrollBar.config(command=textEnvoye.yview)
textEnvoye.config(yscrollcommand=ScrollBar.set)
ScrollBar.grid(column= 2, row = 1, padx = 2, ipady = 120)
textEnvoye.grid(column = 1, row = 1, pady = 9)

def updateCube(cube):

    for i in range(54):
        if i < 9:
            valFaceU[i%9].config(bg = couleur[cube[i]], activebackground = couleur[cube[i]])
        elif i < 18:
            valFaceB[i%9].config(bg = couleur[cube[17-(i%9)]], activebackground = couleur[cube[17-(i%9)]])
        elif i < 27:
            valFaceL[i%9].config(bg = couleur[cube[i]], activebackground = couleur[cube[i]])
        elif i < 36:
            valFaceF[i%9].config(bg = couleur[cube[i]], activebackground = couleur[cube[i]])
        elif i < 45:
            valFaceR[i%9].config(bg = couleur[cube[i]], activebackground = couleur[cube[i]])
        elif i < 54:
            valFaceD[i%9].config(bg = couleur[cube[i]], activebackground = couleur[cube[i]])
    

def viderEntry(e):
    if askyesno('Send', 'Are you sure you want to send this scramble?'):
        textEnvoye.config(state = 'normal')
        textEnvoye.insert('1.0', melangeEntre.get() + '\n')
        #envoie(melangeEntre.get())
        Melange = textEnvoye.get('1.0', '1.end')
        textEnvoye.config(state = 'disabled')
        SolveBH.setCube(outils.applyMove(SolveBH.getCube(), melangeEntre.get()))
        updateCube(SolveBH.getCube())
        melangeEntre.set('')
    else:
        return
entryMelange.bind('<Return>', viderEntry)

def Resolution():

    s = SolveBH.solve(SolveBH.getCube())
    #envoie(s)
    print(s)
    SolveBH.resetCube()
    updateCube(SolveBH.getCube())

resolutionMelange = Button(frameEntrezMelange, text = 'Solve', command = Resolution, bg = '#9F8787', activebackground = '#9F8787')
resolutionMelange.grid(column = 0, row = 1, ipadx = 25, sticky = 'n', pady = 120, ipady = 30)

def GenererMelange():

    global mel
    mel = outils.generateScramble()
    melangeEntre.set(mel)
    entryMelange.focus_force()
genererMelange = Button(frameEntrezMelange, text = 'Generate Scramble', command  = GenererMelange, bg = '#9F8787', activebackground = '#9F8787')
genererMelange.grid(column = 0, row = 1, sticky = 'n', pady = 20, padx = 5, ipady = 30)

#===========================================================================================#
#Onglet officiel
FontTimer = "-family {DejaVu Sans} -size 80 -weight normal -underline 0 -overstrike 0"
timer = Canvas(framePrinc, bg = '#C2BCBA', width=600, height=110, highlightthickness = 0)
text_clock = timer.create_text(260, 65, fill = 'red', font = FontTimer)
def UpdateTimer(e):
    global tourne
    global str_time
    titrePrinc.focus_force()
    titrePrinc.bind('<space>', ResetTimer)
    start = time()
    tourne = True
    while tourne == True:
        now = time() - start
        centiemeSeconde = int((now - int(now))*100)
        seconde = (int(now) % 60)
        minute = int(now/60)
        str_time = "%02d:%02d:%02d" % (minute, seconde, centiemeSeconde)
        timer.itemconfigure(text_clock, text=str_time)
        framePrinc.update()
        
def ResetTimer(e):
    global tourne
    global str_time
    tourne = False
    timer.itemconfigure(text_clock, text=str_time)
    Resultat.config(state = 'normal')
    Resultat.insert('1.0', 'Rubik\'s cube solved in: ' + str_time + '\n')
    temps = textEnvoye.get('1.0', '1.end') #variable a recuperer si on veux le temps
    Resultat.config(state = 'disabled')
    str_time = '00:00:00'
    timer.focus_force()
    timer.bind('<space>', UpdateTimer)

def ActiverModeOfficiel():
    global modeOfficielBouton
    global open_closeTest
    global open_closeMelange
    global open_closeCam
    global open_closeParametre
    frameTestMoteurs.pack_forget()
    frameMelange.pack_forget()
    frameParametre.pack_forget()
    frameImageDeFond.pack_forget()
    testMoteurs.config(text = 'Motors test')
    melange.config(text = 'Scramble')
    open_closeParametre = 0
    open_closeTest = 0
    open_closeMelange = 0
    open_closeCam = 1
    frameTitrePatron.pack_forget()
    frameTitreCamera.pack_forget()
    frameImage.pack()
    frameAffichageGauche.pack()
    frameCommandeGauche.pack_forget()
    frameControlPatron.pack_forget()
    frameGestionCube.config(borderwidth = 0, relief = FLAT)
    frameGestionCube.pack(anchor = 'ne', pady = 59, padx = 53)
    maintienOptionGauche.pack_forget()
    frameOptionGauche.config(borderwidth = 0, relief = FLAT)
    frameOptionGauche.pack(side = TOP, padx = 49, pady = 95)
    for i in range(30, 52):
        fontConf = "-family {DejaVu Sans} -size " + str(i) + " -weight normal -underline 0 -overstrike 0"
        titrePrinc.configure(font=fontConf)
        titrePrinc.update()
        frameOptionGauche.config(borderwidth = 0, relief = FLAT)
        frameOptionGauche.pack(pady = ((-30/7)*i+(1530/7)))
    maintienBas.config(bg = '#00B1FF')
    maintienGauche.config(bg = '#00B1FF')
    maintienHaut.config(bg = '#00B1FF')
    maintienDroite.config(bg = '#00B1FF')
    timer.pack()
    timer.focus_force()
    frameTab.pack(side = TOP, anchor = 'nw', padx = 230)
    frameResultat.pack(side = TOP, anchor = 'nw', padx = 145)
    timer.bind('<space>', UpdateTimer)
    minute, seconde, centiemeSeconde = 0, 0, 0
    str_time = "%02d:%02d:%02d" % (minute, seconde, centiemeSeconde)
    timer.itemconfigure(text_clock, text=str_time)
    modeOfficielBouton = Button(frameTitrePrinc, text = 'Turn off official mode', command = DesactiverModeOfficiel)
    modeOfficielBouton.pack(side = TOP, anchor = 'ne', padx = 5, pady = 5)


    
def DesactiverModeOfficiel():
    global modeOfficielBouton
    ouvrir_fermer.config(text = "Turn off cameras")
    modeOfficielBouton.pack_forget()
    timer.pack_forget()
    frameTab.pack_forget()
    frameResultat.pack_forget()
    maintienBas.config(bg = 'black')
    maintienGauche.config(bg = 'black')
    maintienHaut.config(bg = 'black')
    maintienDroite.config(bg = 'black')
    for i in range(30, 52):
        fontConf = "-family {DejaVu Sans} -size " + str(-i+80) + " -weight normal -underline 0 -overstrike 0"
        titrePrinc.configure(font=fontConf)
        titrePrinc.update()
        frameOptionGauche.config(borderwidth = 0, relief = FLAT)
        frameOptionGauche.pack(pady = ((30/7)*i-(900/7)))
    frameAffichageGauche.pack_forget()
    maintienOptionGauche.pack()
    frameCommandeGauche.pack(anchor = 'nw', padx = 5, pady = 5)
    frameOptionGauche.config(bg = '#C2BCBA', relief = GROOVE, borderwidth = 3, padx = 3, pady = 0)
    frameOptionGauche.pack(anchor = 'nw',side = LEFT, pady = 20, padx = 40)
    frameTitreCamera.config()
    frameImage.pack_forget()
    frameTitreCamera.pack(anchor = "n")
    frameImage.pack()
    frameAffichageGauche.pack()
    framePatron.pack_forget()
    frameGestionCube.config(bg = '#C2BCBA', borderwidth = 3, relief = GROOVE)
    frameGestionCube.pack(side = RIGHT, pady = 20, padx = 50, anchor = 'ne')
    frameControlPatron.pack(anchor = 'nw', pady = 5, padx = 5)
    framePatron.pack()
    frameTitrePatron.pack(anchor = "s")


Label(frameTab, text = "Press tab to solve the Rubik's cube", bg = '#C2BCBA').pack()


Resultat = Text(frameResultat, bg = '#C2BCBA', width = 50, height = 10, state = 'disabled', fg = '#291E1E')
Resultat.grid(column = 0, row = 0)

ScrollBar = Scrollbar(frameResultat, bg = '#C2BCBA')
ScrollBar.config(command=Resultat.yview)
Resultat.config(yscrollcommand=ScrollBar.set)
ScrollBar.grid(column= 1, row = 0, padx = 3, ipady = 50)

modeOfficiel = Button(frameCommandeGauche, text = 'Turn on official mode', command = ActiverModeOfficiel)
modeOfficiel.pack(side = LEFT)

#===========================================================================================#
#Onglet Parametre
def Parametre():
    global open_closeTest
    global open_closeCam
    global open_closeMelange
    global open_closeParametre
    if open_closeParametre == 1:
        frameParametre.pack_forget()
        frameImageDeFond.pack()
        ParametreBouton.config(text = "Robot parameters")

    else:
        frameImage.pack_forget()
        frameTitreCamera.pack_forget()
        frameTestMoteurs.pack_forget()
        frameMelange.pack_forget()
        frameImageDeFond.pack_forget()
        frameAffichageGauche.pack_forget()
        ouvrir_fermer.config(text = "Turn on cameras")
        testMoteurs.config(text = "Motors test")
        melange.config(text = 'Scramble')
        open_closeCam = 0
        open_closeTest = 0
        open_closeMelange = 0
        frameParametre.pack(side = TOP, padx = 10, pady = 10)
        frameAffichageGauche.pack()
    open_closeParametre = 1 - open_closeParametre

def Save():
    global VitesseDepartEntree
    global VitesseMaxEntree
    global AccelerationEntree
    if int(VitesseDepartEntree.get()) < 700 or int(VitesseDepartEntree.get()) > 2000:
        entryVitesseDepart.config(bg = "red")
    if 700 < int(VitesseDepartEntree.get()) and int(VitesseDepartEntree.get()) < 2000:
        entryVitesseDepart.config(bg = '#C2BCBA')    
    if int(VitesseMaxEntree.get()) < 320 or int(VitesseMaxEntree.get()) > int(VitesseDepartEntree.get()):
        entryVitesseMax.config(bg = "red")
    if int(VitesseMaxEntree.get()) >= 320 and int(VitesseMaxEntree.get()) <= int(VitesseDepartEntree.get()):
        entryVitesseMax.config(bg = '#C2BCBA')
    if int(AccelerationEntree.get()) > 25 or int(AccelerationEntree.get()) < 5:
        entryAcceleration.config(bg = "red")
    if int(AccelerationEntree.get()) <= 25 and int(AccelerationEntree.get()) >= 5:
        entryAcceleration.config(bg = '#C2BCBA')
        
    Parametre_data = open("Parametre_data.txt", "r")
    lignes = Parametre_data.readlines()
    Parametre_data.close()
    L0 = lignes[0].split()
    L1 = lignes[1].split()
    L2 = lignes[2].split()
    L0[2] = VitesseDepartEntree.get()
    L1[2] = VitesseMaxEntree.get()
    L2[2] = AccelerationEntree.get()
    lignes[0] = " ".join(L0)
    lignes[1] = " ".join(L1)
    lignes[2] = " ".join(L2)
    Parametre_data = open("Parametre_data.txt", "w")
    for ligne in lignes:
        Parametre_data.write(ligne+"\n")
    Parametre_data.close()

    #envoyer les valueurs à l'arduino
    

ParametreBouton = Button(frameCommandeGauche, text = 'Robot parameters', command = Parametre)
ParametreBouton.pack(side = LEFT)
open_closeParametre = 0

save = Button(frameParametre, text = "Save", command = Save, bg = '#9F8787', activebackground = '#9F8787')
save.pack(side = TOP, anchor = "nw")

LabelVitesseDepartEntree = Label(frameParametre, text = "Starting speed: ",  bg = '#C2BCBA')
LabelVitesseDepartEntree.pack(side = TOP, anchor = "w")
VitesseDepartEntree = StringVar(frameParametre)
entryVitesseDepart = Entry(frameParametre, textvariable = VitesseDepartEntree, bg = '#C2BCBA')
entryVitesseDepart.pack(side = TOP, anchor = "w")

LabelVitesseMaxEntree = Label(frameParametre, text = "Maximal speed: ",  bg = '#C2BCBA')
LabelVitesseMaxEntree.pack(side = TOP, anchor = "w")
VitesseMaxEntree = StringVar(frameParametre)
entryVitesseMax = Entry(frameParametre, textvariable = VitesseMaxEntree, bg = '#C2BCBA')
entryVitesseMax.pack(side = TOP, anchor = "w")

LabelAccelerationEntree = Label(frameParametre, text = "Acceleration (step): ",  bg = '#C2BCBA')
LabelAccelerationEntree.pack(side = TOP, anchor = "w")
AccelerationEntree = StringVar(frameParametre)
entryAcceleration = Entry(frameParametre, textvariable = AccelerationEntree, bg = '#C2BCBA')
entryAcceleration.pack(side = TOP, anchor = "w")

Parametre_data = open("Parametre_data.txt", "r")
lignes = Parametre_data.readlines()
VitesseDepartEntree.set((lignes[0].split())[2])
VitesseMaxEntree.set((lignes[1].split())[2])
AccelerationEntree.set((lignes[2].split())[2])
Parametre_data.close()



#===========================================================================================#
#Image de fond
image = Image.open("ImageRubik'sCube.png")
imageDeFond = ImageTk.PhotoImage(image)
canvasImage = Canvas(frameImageDeFond, width = 660, height = 660, bg = '#C2BCBA', highlightthickness = 0)
canvasImage.create_image(330, 330, image = imageDeFond)
canvasImage.pack()


fenetre.mainloop()
