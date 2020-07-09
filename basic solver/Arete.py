class Arete():

    def __init__(self, c1, c2):
        self.couleur = [c1, c2]

    def getCouleur(self, i):
        return self.couleur[i-1]

    def setCouleur(self, i, c):
        self.couleur[i-1] = c

    def contient(self, c1, c2):

        if(self.couleur[0] == c1 and self.couleur[1] == c2 or
           self.couleur[0] == c2 and self.couleur[1] == c1):
            return True

        return False
        
    
