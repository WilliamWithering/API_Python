#Définition de la classe lieu : attributs et méthodes

class Lieu:
    def __init__(self, identifiant, nom, description, adjacence, objet ):
      self.identifiant = identifiant
      self.nom = nom
      self.description = description
      self.adjacence = adjacence
      self.objet=objet

    def __repr__(self):
         s=self.nom
         s+= "  ~  "
         s+=self.description
         return(s)