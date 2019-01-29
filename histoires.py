import classJeu

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
		jeu.ajouter_lieu(0, "Place du Village", "Voici la place du village, traditionnel coeur de l'animation campagnarde. En cette fin d'après midi, nul pas ne vient cependant fouler les dalles de pierre. En face d'une \033[1m taverne \033[0m à l'agitation faible se trouve un \033[1m barbier \033[0m. Une massive \033[1m forge \033[0m se dresse, tenant fièrement la tête aux vétustes chaumières. Son propriétaire semble cependant absent. Enfin, un petit \033[1m chemin \033[0m tortueux serpente en s'éloignant du village.", {"taverne":1,"barbier":2,"forgeron":3,"chemin":4})
		jeu.ajouter_lieu(1, "La Taverne", "Votre intuition ne vous a pas trompé. Hormis l'ivrogne qui se noie dans la bière, il n'y a personne au \033[1m comptoir \033[0m. Sur les \033[1m tables \033[0m, un couple termine son repas. Depuis l'escalier, vous pouvez sentir l'odeur de renfermé de l'\033[1m etage \033[0m.", {"dehors":0})
		jeu.ajouter_lieu(2, "Chez Le Barbier", "Chez le barbier règne une mauvaise humeur. Pas un seul client, et le propriétaire fait les 100 pas, pestant contre la perte d'un objet. Vous pouvez aller \033[1m parler au barbier \033[0m, mais ce dernier ne vous écoutera sûrement pas",{"dehors":0})
		jeu.ajouter_lieu(3, "La Forge", "Vous rentrez dans la forge, mais personne n'est présent pour vous accueillir. Vous remarquez une belle \033[1m épée \033[0m qui est en train de refroidir. Il vaudrait mieux \033[1m ressortir \033[0m",{"dehors":0})
		jeu.ajouter_lieu(6, "La Forge", "Le forgeron est présent. ",{"dehors":0}) 
		jeu.ajouter_lieu(4, "Petit Chemin","blabla",{"place":0,"grotte":5})
		jeu.ajouter_lieu(5, "La Grotte", "blabla",{})
	if titre_choisi == "b":
		pass


	return jeu