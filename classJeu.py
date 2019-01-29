#Définition de la classe Jeu : contient des objets, un état actuel et un personnage

import classLieu
import classPersonnage

class Jeu:
    def __init__(self, lieu_initial):
        self.lieu_actuel = lieu_initial
        self.regles = "Regles du jeu : \n Pour vous déplacer dans le jeu, vous devez taper le lieu précedé du verbe 'aller'. Plusieurs fins sont possibles dans ce superbe jeu. Certaines sont tragiques, et une seule permet d'accèder au graal. Les lieux et objets disponibles pour des interactions sont mis en gras dans les textes. Que le sort puisse vous etre favorable."
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

        elif :
            pass
        else :
            print("Verbe non reconnu.")


    def est_fini():
        return len(self.lieu[self.lieu_actuel].adjacence) == 0

#Personnage n'existe pas encore
    def set_nom_personnage(self, nom):
        pass
