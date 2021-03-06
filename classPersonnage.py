#Définition de la classe personnage : nom, inventaire...

class Personnage:
    def __init__(self, nom, inventaire = []):
        self.nom = nom
        self.inventaire = inventaire
        self.etats = {}

    def afficher_inventaire(self):
        """
        Affiche les noms des objets présents dans l'inventaire
        """
        if len(self.inventaire) > 0 :
            print("\033[1mInventaire : \033[0m")
            for k in self.inventaire:
                print(k.nom)
        else :
            print("Inventaire vide ! ")
