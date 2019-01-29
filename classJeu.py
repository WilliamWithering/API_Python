#Définition de la classe Jeu : contient des objets, un état actuel et un personnage

import classLieu
import classPersonnage

class Jeu:
    def __init__(self, lieu_initial):
        self.lieu_actuel = lieu_initial
        self.regles = "Regles du jeu : "
        self.lieu=[]

    def __repr__(self):
        for i in range(len(self.lieu)):
            print(self.lieu[i])
        return "C'est tout."

    def ajouter_lieu(self, id_lieu, nom, description, adjacence):
        self.lieu.append(Lieu(id_lieu, nom, description, adjacence))

    def afficher_regles(self):
        print(self.regles)

    def decrire(self):
        pass

    def execute(self, commande):
        pass

    def est_fini():
        return len(self.lieu[self.lieu_actuel].adjacence) == 0

#Personnage n'existe pas encore
    def set_nom_personnage(self, nom):
        pass
