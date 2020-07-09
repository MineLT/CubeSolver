class Coin:

    def __init__(self, c1, c2, c3):
        self.couleur = [c1, c2, c3]

    def getCouleur(self, i):
        return self.couleur[i-1]

    def setCouleur(self, i, c):
        self.couleur[i-1] = c

    def contient(self, c1 ,c2, c3):

        for i in range(3):
            if self.couleur[i] == c1:
                if (self.couleur[(i+1) % 3] == c2 and self.couleur[(i+2) % 3] == c3 or
                    self.couleur[(i+2) % 3] == c3 and self.couleur[(i+1) % 3] == c3):
                    return True
        return False

    def has(self, c):

        if self.couleur[0] == c or self.couleur[1] == c or self.couleur[2] == c:
            return True
        return False
    
