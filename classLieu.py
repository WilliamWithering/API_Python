#Définition de la classe lieu : attributs et méthodes

class Lieu:
    def __init__(self, identifiant, nom, description, adjacence):
      self.identifiant = identifiant
      self.nom = nom
      self.description = description
      self.adjacence = adjacence
      self.contenu = []

    def __repr__(self):
         s=self.nom
         s+= "  ~  "
         s+=self.description[:70]
         s+="\n"
         s+="Objets : "
         for i in range(len(self.contenu)):
             s+=self.contenu[i].nom + " "
         return(s)
