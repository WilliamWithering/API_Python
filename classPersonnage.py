#Définition de la classe personnage : nom, inventaire...

class Personnage:
  def __init__(self, nom, inventaire):
    self.nom = nom 
    self.inventaire = inventaire 

    def dispinvent(self):
        for k in self.inventaire:
            print(k)
    
