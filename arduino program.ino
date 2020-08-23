//programme controle moteurs, six moteurs pas à pas controlés depuis un programme python.

//############################################################################################################
//Définititon des port

//Définition A4998 F
#define pinEnableF 30                                   // Activer A4998
#define pinStepF   12                                   // Front montant = un pas.
#define pinDirF    31                                   // Direction 

//Définition A4998 R
#define pinEnableR 34                                   // Activer A4998
#define pinStepR   11                                   // Front montant = un pas.
#define pinDirR    35                                   // Direction 

//Définition A4998 B
#define pinEnableB 38                                   // Activer A4998
#define pinStepB   10                                   // Front montant = un pas.
#define pinDirB    39                                   // Direction 

//Définition A4998 L
#define pinEnableL 42                                   // Activer A4998
#define pinStepL    9                                   // Front montant = un pas.
#define pinDirL    43                                   // Direction 

//Définition A4998 D
#define pinEnableD 46                                   // Activer A4998
#define pinStepD    5                                   // Front montant = un pas.
#define pinDirD    47                                   // Direction 

//Définition A4998 U
#define pinEnableU 50                                   // Activer A4998
#define pinStepU    4                                   // Front montant = un pas.
#define pinDirU    51                                   // Direction 

//############################################################################################################
//Délaration des variables

#define del 320                                         //Delay en microseconde entre un frond montant et un frond descendant
#define acc 10                                          //Nombre de pas d'accélération et de décélération à éféctuer à chaque mouvement
#define vm  800                                         //Vitesse la plus lente en début d'accélération
#define x (vm - del)/acc                                //variable des fonction accélération

//############################################################################################################
//Table des mouvements

//Tout les cas F, R, B, L, D, U,#, F', R', B', L', D', U',#, F2, R2, B2, L2, D2, U2,#, FB, FB', FB2, F'B, F'B', F'B2, F2B, F2B', F2B2,#, RL, RL', RL2, R'L, R'L', R'L2, R2L, R2L', R2L2,#, DU, DU', DU2, D'U, D'U', D'U2, D2U, D2U', D2U2
//Ordre du tableau F, R, B, L, D, U,
//                 F', R', B', L', D', U',
//                 F2, R2, B2, L2, D2, U2,
//                 FB, FB', F'B, F'B',
//                 F2B2, RL, RL', R'L,
//                 R'L', R2L2, DU, DU',
//                 D'U, D'U', D2U2, FB2,
//                 F'B2, F2B, F2B', RL2,
//                 R'L2, R2L, R2L', DU2,
//                 D'U2, D2U, D2U'

int Tab[][8] = {{1, pinStepF, pinDirF, 0, 50}, {1, pinStepR, pinDirR, 0, 50}, {1, pinStepB, pinDirB, 0, 50}, {1, pinStepL, pinDirL, 0, 50}, {1, pinStepD, pinDirD, 0, 50}, {1, pinStepU, pinDirU, 0, 50},

               {1, pinStepF, pinDirF, 1, 50}, {1, pinStepR, pinDirR, 1, 50}, {1, pinStepB, pinDirB, 1, 50}, {1, pinStepL, pinDirL, 1, 50}, {1, pinStepD, pinDirD, 1, 50}, {1, pinStepU, pinDirU, 1, 50},
               
               {1, pinStepF, pinDirF, 0, 100}, {1, pinStepR, pinDirR, 0, 100}, {1, pinStepB, pinDirB, 0, 100}, {1, pinStepL, pinDirL, 0, 100}, {1, pinStepD, pinDirD, 0, 100}, {1, pinStepU, pinDirU, 0, 100},
               
               {2, pinStepF, pinStepB, pinDirF, pinDirB, 0, 0, 50}, {2, pinStepF, pinStepB, pinDirF, pinDirB, 0, 1, 50}, {2, pinStepF, pinStepB, pinDirF, pinDirB, 1, 0, 50}, {2, pinStepF, pinStepB, pinDirF, pinDirB, 1, 1, 50},

               {2, pinStepF, pinStepB, pinDirF, pinDirB, 0, 0, 100}, {2, pinStepR, pinStepL, pinDirR, pinDirL, 0, 0, 50}, {2, pinStepR, pinStepL, pinDirR, pinDirL, 0, 1, 50}, {2, pinStepR, pinStepL, pinDirR, pinDirL, 1, 0, 50},
               
               {2, pinStepR, pinStepL, pinDirR, pinDirL, 1, 1, 50}, {2, pinStepR, pinStepL, pinDirR, pinDirL, 0, 0, 100}, {2, pinStepD, pinStepU, pinDirD, pinDirU, 0, 0, 50}, {2, pinStepD, pinStepU, pinDirD, pinDirU, 0, 1, 50},
               
               {2, pinStepD, pinStepU, pinDirD, pinDirU, 1, 0, 50}, {2, pinStepD, pinStepU, pinDirD, pinDirU, 1, 1, 50}, {2, pinStepD, pinStepU, pinDirD, pinDirU, 0, 0, 100}, {3, pinStepF, pinStepB, pinDirF, pinDirB, 0},

               {3, pinStepF, pinStepB, pinDirF, pinDirB, 1}, {3, pinStepB, pinStepF, pinDirB, pinDirF, 0}, {3, pinStepB, pinStepF, pinDirB, pinDirF, 1}, {3, pinStepR, pinStepL, pinDirR, pinDirL, 0},

               {3, pinStepR, pinStepL, pinDirR, pinDirL, 1}, {3, pinStepL, pinStepR, pinDirL, pinDirR, 0}, {3, pinStepL, pinStepR, pinDirL, pinDirR, 1}, {3, pinStepD, pinStepU, pinDirD, pinDirU, 0},
               
               {3, pinStepD, pinStepU, pinDirD, pinDirU, 1}, {3, pinStepU, pinStepD, pinDirU, pinDirD, 0}, {3, pinStepU, pinStepD, pinDirU, pinDirD, 1}};

//############################################################################################################
//Setup

void setup() {

Serial.begin(9600);
Serial.println("Programme Moteur");

//Setup port de controle (5V)
pinMode(pinEnableF, OUTPUT);
pinMode(pinDirF, OUTPUT);
pinMode(pinStepF, OUTPUT);

//Setup port de controle (5V)
pinMode(pinEnableR, OUTPUT);
pinMode(pinDirR, OUTPUT);
pinMode(pinStepR, OUTPUT);

//Setup port de controle (5V)
pinMode(pinEnableB, OUTPUT);
pinMode(pinDirB, OUTPUT);
pinMode(pinStepB, OUTPUT);

//Setup port de controle (5V)
pinMode(pinEnableL, OUTPUT);
pinMode(pinDirL, OUTPUT);
pinMode(pinStepL, OUTPUT);

//Setup port de controle (5V)
pinMode(pinEnableD, OUTPUT);
pinMode(pinDirD, OUTPUT);
pinMode(pinStepD, OUTPUT);

//Setup port de controle (5V)
pinMode(pinEnableU, OUTPUT);
pinMode(pinDirU, OUTPUT);
pinMode(pinStepU , OUTPUT);

//Setup des ports "pinEnable" (bloquage des axes moteurs)
digitalWrite( pinEnableF, LOW );
digitalWrite( pinEnableR, LOW );
digitalWrite( pinEnableB, LOW );
digitalWrite( pinEnableL, LOW );
digitalWrite( pinEnableD, LOW );
digitalWrite( pinEnableU, LOW );
}
//############################################################################################################
//Méthode controle des mouvements

//
//Une seul face tourne (peu importe le sens et la direction)
//
void UneFaceMvt(int pinStep, int pinDir, bool dir, int nbrPas) {
digitalWrite(pinDir, dir);                              //choix de la direction
for (int i = 0; i < acc; i++){                          //une seul face tourne
   digitalWrite(pinStep, HIGH);                         //Le moteur avance de un pas (front montant)
   delayMicroseconds(vm - i*x);
   digitalWrite(pinStep, LOW);                          //front descendant
   delayMicroseconds(vm - i*x);
  }
for (int i = 0; i < nbrPas - 2*acc; i++){               //une seul face tourne
   digitalWrite(pinStep, HIGH);                         //Le moteur avance de un pas (front montant)
   delayMicroseconds(del);
   digitalWrite(pinStep, LOW);                          //front descendant
   delayMicroseconds(del);
  }
for (int i = 0; i < acc; i++){                          //une seul face tourne
   digitalWrite(pinStep, HIGH);                         //Le moteur avance de un pas (front montant)
   delayMicroseconds(del + i*x);
   digitalWrite(pinStep, LOW);                          //front descendant
   delayMicroseconds(del + i*x);
  }
}

//
//Les deux face font le même nombre de pas (peu importe le sens et la direction)
//
void DeuxFacesMemeMvt(int pinStep1, int pinStep2, int pinDir1, int pinDir2, bool dir1, bool dir2, int nbrPas) {
digitalWrite(pinDir1, dir1);
digitalWrite(pinDir2, dir2);
for (int i = 0; i < acc; i++){                          //Les deux faces tournent
   digitalWrite(pinStep1, HIGH);                        //Le moteur1 avance de un pas (front montant)
   digitalWrite(pinStep2, HIGH);                        //Le moteur2 avance de un pas (front montant)
   delayMicroseconds(vm - i*x);
   digitalWrite(pinStep1, LOW);                         //front descendant
   digitalWrite(pinStep2, LOW);                         //front descendant
   delayMicroseconds(vm - i*x);
  }
for (int i = 0; i < nbrPas - 2*acc; i++){               //Les deux faces tournent
   digitalWrite(pinStep1, HIGH);                        //Le moteur1 avance de un pas (front montant)
   digitalWrite(pinStep2, HIGH);                        //Le moteur2 avance de un pas (front montant)
   delayMicroseconds(del);
   digitalWrite(pinStep1, LOW);                         //front descendant
   digitalWrite(pinStep2, LOW);                         //front descendant
   delayMicroseconds(del);
  }
for (int i = 0; i < acc; i++){                          //Les deux faces tournent
   digitalWrite(pinStep1, HIGH);                        //Le moteur1 avance de un pas (front montant)
   digitalWrite(pinStep2, HIGH);                        //Le moteur2 avance de un pas (front montant)
   delayMicroseconds(del + i*x);
   digitalWrite(pinStep1, LOW);                         //front descendant
   digitalWrite(pinStep2, LOW);                         //front descendant
   delayMicroseconds(del + i*x);
  }
}

//
//une des deux face fait 50pas, l'autre en fait 100 (peu importe le sens et la direction)
//
void DeuxFacesPasMemeMvt(int pinStep1, int pinStep2, int pinDir1, int pinDir2, bool dir1) {
int nbrPas = 50;
digitalWrite(pinDir1, dir1);
digitalWrite(pinDir2, dir1);
for (int i = 0; i < acc; i++){                          //Les deux faces tournent
   digitalWrite(pinStep1, HIGH);                        //Le moteur1 avance de un pas (front montant)
   digitalWrite(pinStep2, HIGH);                        //Le moteur2 avance de un pas (front montant)
   delayMicroseconds(vm - i*x);
   digitalWrite(pinStep1, LOW);                         //front descendant
   digitalWrite(pinStep2, LOW);                         //front descendant
   delayMicroseconds(vm - i*x);
   digitalWrite(pinStep2, HIGH);                        //Le moteur2 avance de un pas (front montant)
   delayMicroseconds(vm - i*x);
   digitalWrite(pinStep2, LOW);                         //front descendant
   delayMicroseconds(vm - i*x); 
  }
for (int i = 0; i < nbrPas - 2*acc; i++){               //Les deux faces tournent
   digitalWrite(pinStep1, HIGH);                        //Le moteur1 avance de un pas (front montant)
   digitalWrite(pinStep2, HIGH);                        //Le moteur2 avance de un pas (front montant)
   delayMicroseconds(del);
   digitalWrite(pinStep1, LOW);                         //front descendant
   digitalWrite(pinStep2, LOW);                         //front descendant
   delayMicroseconds(del);
   digitalWrite(pinStep2, HIGH);                        //Le moteur2 avance de un pas (front montant)
   delayMicroseconds(del);
   digitalWrite(pinStep2, LOW);                         //front descendant
   delayMicroseconds(del); 
  }
for (int i = 0; i < acc; i++){                          //Les deux faces tournent
   digitalWrite(pinStep1, HIGH);                        //Le moteur1 avance de un pas (front montant)
   digitalWrite(pinStep2, HIGH);                        //Le moteur2 avance de un pas (front montant)
   delayMicroseconds(del + i*x);
   digitalWrite(pinStep1, LOW);                         //front descendant
   digitalWrite(pinStep2, LOW);                         //front descendant
   delayMicroseconds(del + i*x);
   digitalWrite(pinStep2, HIGH);                        //Le moteur2 avance de un pas (front montant)
   delayMicroseconds(del + i*x);
   digitalWrite(pinStep2, LOW);                         //front descendant
   delayMicroseconds(del + i*x); 
  }
}

//############################################################################################################

void loop() {
if (Serial.available()) {
  int r = Serial.read() - 65;                           //r: indice du mouvement dans le tableau Tab
  if (Tab[r][0] == 1) {                                 //appelle de la méthode UneFaceMvt
     UneFaceMvt(Tab[r][1], Tab[r][2], Tab[r][3], Tab[r][4]);
     Serial.print(r);
    }
  else if (Tab[r][0] == 2) {                            //appelle de la méthode DeuxFacesMemeMvt
    DeuxFacesMemeMvt(Tab[r][1], Tab[r][2], Tab[r][3], Tab[r][4], Tab[r][5], Tab[r][6], Tab[r][7]);
    }
  else if (Tab[r][0] == 3) {                            //appelle de la méthode DeuxFacesPasMemeMvt
    DeuxFacesPasMemeMvt(Tab[r][1], Tab[r][2], Tab[r][3], Tab[r][4], Tab[r][5]);
    }
  }
}
