#Définition de la classe lieu : attributs et méthodes

class Lieu:
    def __init__(self, identifiant, nom, description, adjacence):
      self.identifiant = identifiant
      self.nom = nom
      self.description = description
      self.adjacence = adjacence
    def __repr__(self):
         s=self.nom
         s+= " ~~ \n"
         s+=self.description
         return(s)