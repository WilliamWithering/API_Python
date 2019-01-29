
import classJeu

def choisir_titre():
	liste_histoires=["Une histoire de poils.","La forêt noire","Le petit chaperon rouge"]
	print("Voici la liste des titres possibles pour créer votre propre histoire : ")
	for i in range(len(liste_histoires)):
		print(i, " : ", liste_histoires[i])
	titre_choisi=int(input("Sélectionner le nombre associé à votre titre : "))
	while titre_choisi >= len(liste_histoires) or titre_choisi < 0:
		print("Titre choisi incorrect.")
		titre_choisi = int(input("Choisir un nombre correspondant au titre souhaité: "))

	return liste_histoires[titre_choisi]

def charger_jeu(titre_choisi):
	jeu = classJeu.Jeu()
	if titre_choisi == "Une histoire de poils.":
		jeu.ajouter_lieu(0, "place du village", "Voici la place du village, traditionnel coeur de l'animation campagnarde. En cette fin d'après midi, nul pas ne vient cependant fouler les dalles de pierre. En face d'une taverne à l'agitation faible se trouve un barbier. Une massive forge se dresse, tenant fièrement la tête aux vétustes chaumières. Son propriétaire semble cependant absent. Enfin, un petit chemin tortueux serpente en s'éloignant du village.", {"taverne":1,"barbier":2,"forgeron":3,"chemin":4})
		jeu.ajouter_lieu(1, "le bar du village", "blabla", {"dehors":0})
		jeu.ajouter_lieu(2, "le coiffeur", "blabla",{"dehors":0})
		jeu.ajouter_lieu(3, "le forgeron", "blabla",{"dehors":0})
		jeu.ajouter_lieu(4, "un petit chemin","blabla",{"place":0,"grotte":5})
		jeu.ajouter_lieu(5, "la grotte", "blabla","")
	if titre_choisi == "b":
		pass

	return jeu