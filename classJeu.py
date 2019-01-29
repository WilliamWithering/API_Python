#Définition de la classe Jeu : contient des objets, un état actuel et un personnage

import classLieu
import classPersonnage

class Jeu:
	def __init__(self, lieu_initial):
		self.lieu_initial = lieu_initial
    	self.regles = "Regles du jeu : "
     	self.lieu=[]

    def ajouter_lieu(self, id_lieu, nom, description, adjacence):
        self.lieu.append(Lieu(id_lieu, nom, description, adjacence))

    def afficher_regles(self):
        print(self.regles)

    def decrire(self):
        pass

    def execute(self, commande):
        pass

#Personnage n'existe pas encore
    def set_nom_personnage(self, nom):
        pass
