#Définition de la classe Jeu : contient des objets, un état actuel et un personnage

import classLieu
import classPersonnage
import classObjet

class Jeu:
    def __init__(self):
        self.lieu_actuel = 0
        self.regles = "\n \n \n \033[1mRègles du jeu :\033[0m \n Pour vous déplacer dans le jeu, vous devez taper nom du lieu précedé du verbe 'aller'. D'autres verbes sont reconnus, tels que 'prendre', 'poser' ou parfois 'parler'. A tout moment, il est également possible d'utiliser la commande 'inventaire' pour afficher les objets présents dans l'inventaire. \
        \n  Plusieurs fins sont possibles : certaines sont tragiques, d'autres moins. Les lieux et objets disponibles pour des interactions sont mis en gras dans les textes. Puisse le sort vous etre favorable.\n\n \
        Quelques exemples de commandes disponibles dans certaines situations : \n\
        • aller dehors \n\
        • prendre les ciseaux \n\
        • poser les ciseaux \n\
        • parler au barbier \n\
        • aller dans la taverne / chez le barbier... \n"
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
            for obj in self.objets:
                print(obj.nom)

        print("Dans ce monde il y a des lieux : ")
        for lieu in self.lieu:
            print(lieu)
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

    def ajouter_dialogue(self, id_lieu, dict_dialogue):
        self.lieu[id_lieu].dialogues.update(dict_dialogue)

    def ajouter_utilisation(self, id_lieu, dict_utilisation):
        self.lieu[id_lieu].utilisation.update(dict_utilisation)

    def delete_objets(self):
        self.objets = None


###---- LES FONCTIONS DE JEU
    def afficher_regles(self):
        print(self.regles)


    def est_fini(self):
        """
        Fonction servant à évaluer l'état du jeu. Si le noeud (lieu) actuel n'est lié à aucun autre lieu, on estime que le joueur est dans un cul de sac (gagné ou perdu) et le jeu se termine.
        """
        return len(self.lieu[self.lieu_actuel].adjacence) + len(self.lieu[self.lieu_actuel].utilisation) == 0

    def afficher_nom_lieu(self):
        print("\n\033[1m" +  self.lieu[self.lieu_actuel].nom + " : \033[0m \n")

    def decrire(self):
        """
        Fonction permettant d'afficher le contenu de l'histoire. On affiche d'abord le titre, puis la description du lieu. Enfin, on ajoute les phrases liées aux objets.
        """
        desc = self.lieu[self.lieu_actuel].description
        for obj in self.lieu[self.lieu_actuel].contenu:
            desc += obj.message
        print(desc + '\n')

    def execute(self, commande):
        """
        Fonction permettant de reconnaître l'ordre donné par l'utilisateur.
        On vérifie d'abord la présence des verbes prendre et poser dans la chaine, puis celle d'aller.
        Pour prendre et poser, on change la position de l'objet. Pour aller, on modifie la position actuelle.

        On vérifie également la présence d'autres commandes comme l'inventaire.
        """
        words = commande.strip(" ").split(" ")

        mots_reconnus = 0

        if words[0] == "prendre":
            for mot in words[1:]:
                for obj in self.lieu[self.lieu_actuel].contenu:
                    if mot == obj.raccourci:
                        self.personnage.inventaire.append(obj)
                        self.lieu[self.lieu_actuel].contenu.remove(obj)
                        print("Vous avez obtenu : " + obj.nom)

        elif words[0] == "poser":
            for mot in words[1:]:
                for obj in self.personnage.inventaire:
                    if mot == obj.raccourci:
                        self.lieu[self.lieu_actuel].contenu.append(obj)
                        self.personnage.inventaire.remove(obj)

        elif words[0] == "aller":
            for mot in words[1:]:
                if mot in self.lieu[self.lieu_actuel].adjacence:
                    self.lieu_actuel = self.lieu[self.lieu_actuel].adjacence[mot]
                    self.transition = 1
                    mots_reconnus+=1

            if mots_reconnus == 0 :
                print("La destination n'a pas été reconnue.")
            if mots_reconnus > 1 :
                print("Attention, plusieurs lieux ont été reconnus. Vous arrivez dans le dernier possible")

        elif words[0] == "parler":
            for mot in words[1:]:
                if mot in self.lieu[self.lieu_actuel].dialogues:
                    print("\n- " + self.lieu[self.lieu_actuel].dialogues[mot])

        elif words[0] == "utiliser":
            for mot in words[1:]:
                if (mot in self.lieu[self.lieu_actuel].utilisation):
                    for obj in self.personnage.inventaire:
                        if mot == obj.raccourci:
                            self.declencher(self.lieu_actuel, self.lieu[self.lieu_actuel].utilisation[mot])
                            mots_reconnus += 1

            if not mots_reconnus:
                print("Utilisation impossible.")

        elif words[0] == "inventaire":
            self.personnage.afficher_inventaire()

        else :
            print("Verbe non reconnu.")

    def verif_triggers(self):
        for lieu in self.lieu:
            for trigger in lieu.triggers:
                if self.condition_satisfaite(trigger):
                    self.declencher(lieu.identifiant, lieu.triggers[trigger])

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
        for cond in condition:
            #vérification d'inventaire
            if cond[0] == "avoir":
                nom_objet = cond[1]
                objet_trouve = False
                for obj in self.personnage.inventaire:
                    if obj.raccourci == nom_objet:
                        objet_trouve = True
                verification_bools.append(objet_trouve)

            #vérification de position : on check lieu actuel = location x
            if cond[0] == "location":
                verification_bools.append(self.lieu_actuel == int(cond[1]))

            if cond[0] = "ne_pas_avoir":
                objet_trouve = False
                for obj in self.personnage.inventaire:
                    if obj.raccourci = cond[1]:
                        objet_trouve = True
                verification_bools.append(not objet_trouve)
                
        return all(verification_bools)

    def declencher(self, lieu, action):
        """
        Input : une chaine de caractères représentant l'action à déclencher
        """
        action = action.split("&")
        for i in range(len(action)):
            action[i] = action[i].strip(" ").split(" ")

        for act in action:
            if act[0] == 'update_lien':
                tag = act[1]
                id_lieu = int(act[2])
                self.lieu[lieu].adjacence.update({tag:id_lieu})

            if act[0] == 'remove':
                objet = act[1]
                for obj in self.personnage.inventaire:
                    if obj.raccourci == objet:
                        self.personnage.inventaire.remove(obj)
                        print("Vous avez donné : " + obj.nom)
                        break

            if act[0] == 'teleport':
                self.lieu_actuel = int(act[1])
                self.transition = 1

            if act[0] == 'give':
                self.personnage.inventaire.append(self.objets[int(act[1])])
                print("Vous avez obtenu : " + self.objets[int(act[1])].nom)
