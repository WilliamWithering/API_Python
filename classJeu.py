#Définition de la classe Jeu : contient des objets, un état actuel et un personnage

import classLieu
import classPersonnage

class Jeu:
    def __init__(self):
        self.lieu_actuel = 0
        self.regles = "Regles du jeu : "
        self.lieu=[]
        self.transition = 1

    def __repr__(self):
        for i in range(len(self.lieu)):
            print(self.lieu[i])
        return "C'est tout."

    def ajouter_lieu(self, id_lieu, nom, description, adjacence = {}, objet = []):
        self.lieu.append(Lieu(id_lieu, nom, description, adjacence, objet))

    def afficher_regles(self):
        print(self.regles)

    def decrire(self):
        print("\n")
        print("\033[1m" +  self.lieu[self.lieu_actuel].nom + " : \033[0m \n")
        print(self.lieu[self.lieu_actuel].description)
        print("\n")
        pass

    def execute(self, commande):
        commande = commande.lower()
        words = commande.split(" ")

        mots_reconnus = 0

        if words[0] == "aller":
            for i in words[1:]:
                if i in self.lieu[self.lieu_actuel].adjacence.keys():
                    self.lieu_actuel = self.lieu[self.lieu_actuel].adjacence[i]
                    self.transition = 1
                    mots_reconnus+=1

            if mots_reconnus == 0 :
                print("La destination n'a pas été reconnue.")
            if mots_reconnus > 1 :
                print("Attention, plusieurs mots ont été reconnus. Le dernier a été sélectionné.")

        elif word[0] == "inventaire":
            pass
            
        else :
            print("Verbe non reconnu.")


    def est_fini(self):
        return len(self.lieu[self.lieu_actuel].adjacence) == 0

#Personnage n'existe pas encore
    def set_nom_personnage(self, nom):
        pass
