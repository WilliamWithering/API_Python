#Définition de la classe Jeu : contient des objets, un état actuel et un personnage

import classLieu 
import classPersonnage 
 
class Jeu: 
	def __init__(self): 
		self.lieu_initial="0" 
    	self.regles = "Regles du jeu : " 
     	lieu=[]
