#Définition de la classe Jeu : contient des objets, un état actuel et un personnage

import classLieu
import classPersonnage
import classObjet

class Jeu:
    def __init__(self):
        self.lieu_actuel = 0
        self.regles = "\n \n \n \033[1mRègles du jeu :\033[0m \n Pour vous déplacer dans le jeu, vous devez taper nom du lieu précedé du verbe 'aller'. D'autres verbes sont reconnus, tels que 'prendre' ou 'poser'. A tout moment, il est également possible d'utiliser la commande 'inventaire' pour afficher les objets présents dans l'inventaire. \n  Plusieurs fins sont possibles : certaines sont tragiques, et une seule permet d'accèder au graal. Les lieux et objets disponibles pour des interactions sont mis en gras dans les textes. Puisse le sort vous etre favorable.\n\n\n"
        self.lieu = []
        self.objets = []
        self.transition = 1
        self.personnage = None

    def __repr__(self):
        """
            Affiche tous les lieux et les objets de ce monde.
        """
        if self.objets != None:
            print("Dans ce monde il y a des objets : ")
            for i in range(len(self.objets)):
                print(self.objets[i].nom)

        print("Dans ce monde il y a des lieux : ")
        for i in range(len(self.lieu)):
            print(self.lieu[i])
        return "C'est tout."

###---- LES AJOUTS UTILISES PAR HISTOIRE
###---- Toutes ces fonctions servent à mettre à jour les listes de lieux et d'objets.

    def ajouter_personnage(self, nom, inventaire = []):
        self.personnage = classPersonnage.Personnage(nom, inventaire)

    def ajouter_objet(self, id_objet, nom, raccourci, message):
        self.objets.append(classObjet.Objet(id_objet, nom, raccourci, message))

    def ajouter_lieu(self, id_lieu, nom, description, adjacence = {}):
        self.lieu.append(classLieu.Lieu(id_lieu, nom, description, adjacence))

    def mettre_objet_dans_lieu(self, id_objet, id_lieu):
        self.lieu[id_lieu].contenu.append(self.objets[id_objet])

    def ajouter_trigger(self, id_lieu, dict_trigger):
        self.lieu[id_lieu].triggers.update(dict_trigger)

    def delete_objets(self):
        self.objets = None

###---- LES FONCTIONS DE JEU
    def afficher_regles(self):
        print(self.regles)


    def est_fini(self):
        """
        Fonction servant à évaluer l'état du jeu. Si le noeud (lieu) actuel n'est lié à aucun autre lieu, on estime que le joueur est dans un cul de sac (gagné ou perdu) et le jeu se termine.
        """
        return len(self.lieu[self.lieu_actuel].adjacence) == 0


    def decrire(self):
        """
        Fonction permettant d'afficher le contenu de l'histoire. On affiche d'abord le titre, puis la description du lieu. Enfin, on ajoute les phrases liées aux objets.
        """
        print('\n')
        print("\033[1m" +  self.lieu[self.lieu_actuel].nom + " : \033[0m \n")
        desc = self.lieu[self.lieu_actuel].description
        for i in range(len(self.lieu[self.lieu_actuel].contenu)):
            desc += self.lieu[self.lieu_actuel].contenu[i].message
        print(desc + '\n')

    def execute(self, commande):
        """
        Fonction permettant de reconnaître l'ordre donné par l'utilisateur.
        On vérifie d'abord la présence des verbes prendre et poser dans la chaine, puis celle d'aller.
        Pour prendre et poser, on change la position de l'objet. Pour aller, on modifie la position actuelle.

        On vérifie également la présence d'autres commandes comme l'inventaire.
        """
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

    def verif_triggers(self):
        for i in range(len(self.lieu)):
            for j in self.lieu[i].triggers:
                if self.condition_satisfaite(j):
                    self.declencher(i, self.lieu[i].triggers[j])

    def condition_satisfaite(self, condition):
        """
        Input : une chaine de caractères représentant une condition
        Output : un booléen indiquant si cette condition est satisfaite
        """
        #On commence par séparer les mots
        condition = condition.split("&")
        for i in range(len(condition)):
            condition[i] = condition[i].strip(" ").split(" ")

        # On crée un tableau qui contiendra un booléen pour chaque condition
        verification_bools = []
        for i in range(len(condition)):
            #vérification d'inventaire
            if condition[i][0] == "avoir":
                nom_objet = condition[i][1]
                objet_trouve = False
                for j in range(len(self.personnage.inventaire)):
                    if self.personnage.inventaire[i].raccourci == nom_objet:
                        objet_trouve = True
                verification_bools.append(objet_trouve)

            #vérification de position
            if condition[i][0] == "location":
                verification_bools.append(self.lieu_actuel == int(condition[i][1]))

        return all(verification_bools)

    def declencher(self, lieu, action):
        """
        Input : une chaine de caractères représentant l'action à déclencher
        """
        action = action.split("&")
        for i in range(len(action)):
            action[i] = action[i].strip(" ").split(" ")

        for i in range(len(action)):
            if action[i][0] == 'update_lien':
                tag = action[i][1]
                id_lieu = int(action[i][2])
                self.lieu[lieu].adjacence.update({tag:id_lieu})

            if action[i][0] == 'remove':
                objet = action[i][1]
                for j in range(len(self.personnage.inventaire)):
                    if self.personnage.inventaire[j].raccourci == objet:
                        self.personnage.inventaire.pop(j)
                        break

            if action[i][0] == 'teleport':
                self.lieu_actuel = int(action[i][1])
                self.transition = 1

            if action[i][0] == 'give':
                self.personnage.inventaire.append(self.objets[int(action[i][1])])
