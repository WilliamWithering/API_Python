
class Objet:

    def __init__(self, id_objet, nom, raccourci, message):
        self.id = id_objet
        self.nom = nom
        self.raccourci = raccourci
        self.message = message
        pass

    def __repr__(self):
        return self.nom + ":" +  self.message
