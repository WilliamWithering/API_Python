#Définition de la classe Jeu : contient des objets, un état actuel et un personnage

import classLieu
import classPersonnage
import classObjet

class Jeu:
    def __init__(self):
        self.lieu_actuel = 0
        self.regles = "Regles du jeu : Regles du jeu : \n Pour vous déplacer dans le jeu, vous devez taper le lieu précedé du verbe 'aller'. Plusieurs fins sont possibles dans ce superbe jeu. Certaines sont tragiques, et une seule permet d'accèder au graal. Les lieux et objets disponibles pour des interactions sont mis en gras dans les textes. Que le sort puisse vous etre favorable."
        self.lieu = []
        self.objets = []
        self.transition = 1
        self.personnage = None

    def __repr__(self):
        if self.objets != None:
            print("Dans ce monde il y a des objets : ")
            for i in range(len(self.objets)):
                print(self.objets[i].nom)

        print("Dans ce monde il y a des lieux : ")
        for i in range(len(self.lieu)):
            print(self.lieu[i])
            if len(self.lieu[i].contenu) == 0:
                print("-> Vide")
            else :
                print("-> Non vide")
        return "C'est tout."

###---- LES AJOUTS UTILISES PAR HISTOIRE
    def ajouter_personnage(self, nom, inventaire = []):
        self.personnage = classPersonnage.Personnage(nom, inventaire)

    def ajouter_objet(self, id_objet, nom, raccourci, message):
        self.objets.append(classObjet.Objet(id_objet, nom, raccourci, message))

    def ajouter_lieu(self, id_lieu, nom, description, adjacence = {}):
        self.lieu.append(classLieu.Lieu(id_lieu, nom, description, adjacence))

    def mettre_objet_dans_lieu(self, id_objet, id_lieu):
        self.lieu[id_lieu].contenu.append(self.objets[id_objet])
        print("Ajout de " + self.objets[id_objet].nom + "dans " + self.lieu[id_lieu].nom )

    def delete_objets(self):
        self.objets = None

###---- LES FONCTIONS DE JEU
    def afficher_regles(self):
        print(self.regles)

    def decrire(self):
        print("\n")
        print("\033[1m" +  self.lieu[self.lieu_actuel].nom + " : \033[0m \n")
        print(self.lieu[self.lieu_actuel].description)
        desc_objets = ""
        for i in range(len(self.lieu[self.lieu_actuel].contenu)):
            desc_objets += self.lieu[self.lieu_actuel].contenu[i].message
        print(desc_objets)
        print("\n")
        pass

    def execute(self, commande):
        commande = commande.lower()
        words = commande.split(" ")

        mots_reconnus = 0

        if words[0] == "prendre":
            for i in range(len(words[1:])):
                for j in range(len(self.lieu[self.lieu_actuel].contenu)):
                    if words[i+1] == self.lieu[self.lieu_actuel].contenu[j].raccourci:
                        self.personnage.inventaire.append(self.lieu[self.lieu_actuel].contenu[j])
                        self.lieu[self.lieu_actuel].contenu.pop(j)

        elif words[0] == "poser":
            for i in range(len(words[1:])):
                for j in range(len(self.personnage.inventaire)):
                    if words[i+1] == self.personnage.inventaire[j].raccourci:
                        self.lieu[self.lieu_actuel].contenu.append(self.personnage.inventaire[j])
                        self.personnage.inventaire.pop(j)

        elif words[0] == "aller":
            for i in words[1:]:
                if i in self.lieu[self.lieu_actuel].adjacence.keys():
                    self.lieu_actuel = self.lieu[self.lieu_actuel].adjacence[i]
                    self.transition = 1
                    mots_reconnus+=1

            if mots_reconnus == 0 :
                print("La destination n'a pas été reconnue.")
            if mots_reconnus > 1 :
                print("Attention, plusieurs lieux ont été reconnus. Vous arrivez dans le dernier possible")

        elif words[0] == "inventaire":
            self.personnage.afficher_inventaire()

        else :
            print("Verbe non reconnu.")


    def est_fini(self):
        return len(self.lieu[self.lieu_actuel].adjacence) == 0
