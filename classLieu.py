#Définition de la classe lieu : attributs et méthodes

class Lieu:
    def __init__(self, nom, description, adjacence):
      self.nom = nom
      self.description = description
      self.adjacence = adjacence
      self.contenu = []
      self.triggers = {}
      self.dialogues = {}
      self.utilisation = {}

    def __repr__(self):
        """
        Fonction qui crée une chaine de caractères contenant le nom du lieu, le début de sa description ainsi que les objets qu'il contient.
        """
        s=self.nom
        s+= "  ~  "
        s+=self.description[:70] + "..."
        s+="\n"
        s+="Objets : "
        for obj in self.contenu:
            s+=obj.nom + " "
        return(s)
