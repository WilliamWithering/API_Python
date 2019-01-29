import classJeu

import classJeu
def choisir_titre():
	"""
		Fonction permettant de choisir le titre de l'histoire à charger.
		Output : string : titre d'une histoire
	"""
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
	"""
		Fonction permettant de charger une histoire
		Input : le titre de l'histoire à charge
		Output : un objet Jeu, initialisé avec les paramètres de l'histoire
	"""
	jeu = classJeu.Jeu()

	if titre_choisi == "Une histoire de poils.":
		jeu.ajouter_personnage("Johann")

		jeu.ajouter_objet(0,"Une paire de ciseaux","ciseaux", "Une paire de ciseaux y est posée. ")
		jeu.ajouter_objet(1,"Une belle épée", "epee", "Une lame à l'aspect redoutable se trouve là. ")

		jeu.ajouter_lieu(0, "Place du Village", "\033[1mVoici la place du village \033[0m, traditionnel coeur de l'animation campagnarde. En cette fin d'après midi, nul pas ne vient cependant fouler les dalles de pierre. En face d'une \033[1m taverne \033[0m à l'agitation faible se trouve un \033[1m barbier \033[0m. Une massive \033[1m forge \033[0m se dresse, tenant fièrement la tête aux vétustes chaumières. Son propriétaire semble cependant absent. Enfin, un petit \033[1m chemin \033[0m tortueux serpente en s'éloignant du village.", {"taverne":1,"barbier":2,"forge":3,"chemin":4})
		jeu.ajouter_lieu(1, "La Taverne", "Votre intuition ne vous a pas trompé. Hormis l'ivrogne qui se noie dans la bière, il n'y a personne au \033[1m comptoir \033[0m. Sur les \033[1m tables \033[0m, un couple termine son repas. Depuis l'escalier, vous pouvez sentir l'odeur de renfermé de l'\033[1m etage \033[0m.", {"dehors":0})
		jeu.ajouter_lieu(2, "Chez Le Barbier", "\033[1mChez le barbier \033[0m règne une mauvaise humeur. Pas un seul client, et le propriétaire fait les 100 pas, pestant contre la perte d'un objet. Vous pouvez aller \033[1m parler au barbier \033[0m, mais ce dernier ne vous écoutera sûrement pas",{"dehors":0})
		jeu.ajouter_lieu(3, "La Forge", "Vous rentrez dans la  \033[1m forge \033[0m, mais personne n'est présent pour vous accueillir. Vous remarquez une belle \033[1m épée \033[0m qui est en train de refroidir. Il vaudrait mieux \033[1m ressortir \033[0m",{"dehors":0})
		jeu.ajouter_lieu(4, "Petit Chemin","C'est un \033[1m petit chemin \033[0m en l'apparence bien tranquille mais qui vous conduira peut-etre vers bien des surprises. Assurez vous bien de vos arrieres ou il sera bientot trop tard..",{"place":0,"grotte":5})
		jeu.ajouter_lieu(5, "La Grotte", "Le chemin derrière vous s'avère trop glissant pour faire demi-tour. Vous êtes dans une belle \033[1m  grotte \033[0m. Enfin. Une \033[1m grotte \033[0m sombre. Une \033[1m grotte \033[0m qui pourrait cacher des trésors mais aussi de terribles créatures. Comme ce \033[1m  serpent \033[0m qui se dresse devant vous. Vous n'avez plus le choix, il va falloir faire face. A vraincre sans peril, on triomphe sans gloire. Nota : une arme peut etre utile.",{})
		jeu.ajouter_lieu(6, "La Forge", "Le forgeron est présent. ",{"dehors":0})


		jeu.mettre_objet_dans_lieu(0,1)
		jeu.mettre_objet_dans_lieu(1,3)

		jeu.delete_objets()

	if titre_choisi == "La forêt noire":
		print("Histoire non existante pour le moment.")
	
	if titre_choisi == "Le petit chaperon rouge":
		print("Histoire non existante pour le moment.")

	return jeu
