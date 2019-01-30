import classJeu

liste_histoires = ["Première histoire","La forêt Kifaipeur."]

def choisir_titre():
	"""
		Fonction permettant de choisir le titre de l'histoire à charger.
		Output : string : titre d'une histoire
	"""
	print("Voici la liste des titres possibles pour créer votre propre histoire : ")
	for i in range(len(liste_histoires)):
		print(i, " : ", liste_histoires[i])

	try:
		titre_choisi=int(input("Sélectionner le nombre associé à votre titre : "))
	except ValueError:
		titre_choisi = -1
		print("Veuillez saisir un nombre.")

	while titre_choisi >= len(liste_histoires) or titre_choisi < 0:
		print("Titre choisi incorrect.")
		try:
			titre_choisi=int(input("Sélectionner le nombre associé à votre titre : "))
		except ValueError:
			print("Veuillez saisir un nombre.")

	return titre_choisi

def charger_jeu(titre_choisi):
	"""
		Fonction permettant de charger une histoire
		Input : le titre de l'histoire à charge
		Output : un objet Jeu, initialisé avec les paramètres de l'histoire
	"""
	jeu = classJeu.Jeu()

	prenom = input("Quel est le prénom de votre personnage?")

	jeu.ajouter_personnage(prenom)

	if titre_choisi == 0:
		jeu.ajouter_objet(0,"Une paire de ciseaux","ciseaux", "Une paire de ciseaux y est posée. ")
		jeu.ajouter_objet(1,"Une belle épée", "epee", "Une lame à l'aspect redoutable se trouve là. ")
		jeu.ajouter_objet(2,"Quelques pièces", "pieces", "Vous remarquez également quelques pièces qui trainent sans surveillance.")

		jeu.ajouter_lieu(0, "Place du Village", "Vous êtes sur la \033[1mplace du village\033[0m, traditionnel coeur de l'animation campagnarde. En cette fin d'après midi, nul pas ne vient cependant fouler les dalles de pierre. En face d'une \033[1m taverne \033[0m à l'agitation faible se trouve un \033[1m barbier \033[0m. Une massive \033[1m forge \033[0m se dresse, tenant fièrement la tête aux vétustes chaumières. Son propriétaire semble cependant absent. Enfin, un petit \033[1m chemin \033[0m tortueux serpente en s'éloignant du village. ", {"taverne":1,"barbier":2,"forge":3,"chemin":4})
		jeu.ajouter_lieu(1, "La Taverne", "Votre intuition ne vous a pas trompé. Sur les tables, un couple termine son repas. Depuis l'escalier, vous pouvez sentir l'odeur de renfermé de l'etage. Hormis l'ivrogne qui se noie dans la bière, il n'y a personne au comptoir. ", {"dehors":0})
		jeu.ajouter_lieu(2, "Chez Le Barbier", "\033[1mChez le barbier\033[0m règne une mauvaise humeur. Pas un seul client, et le propriétaire fait les 100 pas, pestant contre la perte d'un objet. Il ne semble pas remarquer votre présence. ",{"dehors":0})
		jeu.ajouter_lieu(3, "La Forge", "Vous rentrez dans la  \033[1m forge \033[0m, mais personne n'est présent pour vous accueillir. Vous remarquez une belle \033[1m épée \033[0m qui est en train de refroidir. Il vaudrait mieux \033[1m ressortir \033[0m.  ",{"dehors":0})
		jeu.ajouter_lieu(4, "Petit Chemin","C'est un \033[1m petit chemin \033[0m en l'apparence bien tranquille mais qui vous conduira peut-etre vers bien des surprises. Assurez vous bien de vos arrieres ou il sera bientot trop tard... Vous apercevez au loin une \033[1m grotte \033[0m ",{"place":0,"grotte":5})
		jeu.ajouter_lieu(5, "La Grotte", "Le chemin derrière vous s'avère trop glissant pour faire demi-tour. Vous êtes dans une belle \033[1m  grotte \033[0m. Enfin. Une \033[1m grotte \033[0m sombre. Une \033[1m grotte \033[0m qui pourrait cacher des trésors mais aussi de terribles créatures. Comme ce \033[1m  serpent \033[0m qui se dresse devant vous. Vous n'avez plus le choix, il va falloir faire face. Si vous avez une arme sur vous, vous pouvez l'\033[1mutiliser\033[0m. ",{})
		jeu.ajouter_lieu(6, "Chez Le Barbier", "Le barbier se retourne, et semble remarquer quelque chose dans votre poche. Il s'exclame 'MAIS. Vous avez retrouvé mes ciseaux?!'. Il s'empresse de s'approcher et de les prendre. 'Je ne sais pas comment vous remercier... Veuillez accepter cette maigre compensation financière.' Ils vous donne quelques pièces et retourne vaquer à ses occupations. ",{"dehors":0})
		jeu.ajouter_lieu(7, "Chez Le Barbier", "Le salon est calme. Il y flotte une légère odeur de mousse à raser. Dans un coin, le barbier sifflote gaiement. ", {"dehors":0})
		jeu.ajouter_lieu(8, "Game over", "L'épée était encore brulante, votre fin est tragique.", {})
		jeu.ajouter_lieu(9, "La Forge", "Le forgeron est entrain de forger. Rien de plus logique. Votre présence semble le pertuber. Peut-être qu'il a quelque chose à cacher ou à vendre. Votre curiosité est récompensée. Il se retourne enfin et vous propose d'acquérir une \033[1m belle épee \033[0m contre quelques \033[1m pièces \033[0m",{"dehors":0})
		jeu.ajouter_lieu(10, "Victoire !", "Vous saisissez votre épée et tranchez la tête du serpent d'un geste vif. Bravo !",{})
		jeu.ajouter_lieu(11,"Game over","Le serpent vous attaque et vous n'avez pas d'arme.")

		jeu.mettre_objet_dans_lieu(0,1)
		jeu.mettre_objet_dans_lieu(1,3)

		jeu.ajouter_trigger(0,{"avoir ciseaux":"update_lien barbier 6"})
		jeu.ajouter_trigger(0,{"location 6 & avoir ciseaux":"update_lien barbier 7 & remove ciseaux & give 2"})
		jeu.ajouter_trigger(3,{'avoir epee & location 3' : "teleport 8"})
		jeu.ajouter_trigger(0,{"avoir pieces":"update_lien forge 9"})
		jeu.ajouter_trigger(5,{"ne_pas_avoir epee & location 5":"teleport 11"})

		jeu.ajouter_utilisation(9, {"pieces":"remove pieces & give 1"})
		jeu.ajouter_utilisation(5, {"epee":"teleport 10"})

		jeu.ajouter_dialogue(2,{"barbier":"Vous voyez bien que je n'ai pas mes ciseaux?! Je ne peux pas m'occuper de vous !"})

	if titre_choisi == 1:

		jeu.ajouter_objet(0,"Une machette","machette", "Vous observez une vieille machette. Bien qu'un peu émoussée et sans doute peu efficace en combat, cet outil vous permettra de trancher des buissons. ")
		jeu.ajouter_objet(1,"Une vieille clé", "cle", "Dans une flaque de boue, vous observez un reflet argenté, c'est une vieille clé. ")
		jeu.ajouter_objet(2,"Parchemin des anciens", "parchemin", "Dans un imposant écrin de bronze se trouve un \033[1mparchemin\033[0m. Lorsque vous l'ouvrez, ce dernier semble vous abreuver de toutes les connaissances du monde. ")

		jeu.ajouter_lieu(0, "Orée de la forêt", "Vous êtes à l'orée de la forêt, il est encore temps d'aller en \033[1marrière\033[0m et de sortir. Vous pouvez sinon continuer en passant par le \033[1mchemin\033[0m", {"chemin":1,"arriere":8})
		jeu.ajouter_lieu(1, "Clairière", "Après avoir suivi le chemin, vous arrivez dans une clairière. En face de vous, une \033[1mcabane\033[0m massive trône. Un chemin à l'ouest vous mène vers un petit \033[1mlac\033[0m, tandis qu'à l'Est, un autre vous emmène plus profondèment dans la \033[1mforêt\033[0m.", {"arriere":0,"lac":2,"foret":4,"cabane":6})
		jeu.ajouter_lieu(2, "Lac", "Après que vous vous soyez approché du lac, une créature féérique en sort. Elle vous pose alors une énigme, qui semble insolvable pour votre cerveau d'humain. Vous pouvez prendre le chemin qui vous ramène dans la \033[1mclairière\033[0m, ou tenter quelque chose." , {"clairiere":1})
		jeu.ajouter_lieu(3, "Lac", "Vous sortez le parchemin, et à l'aide des connaissances qu'il renferme, vous répondez avec brio à cette dernière. La créature vous récompense alors d'une machette, puis disparait.", {"clairiere":1})
		jeu.ajouter_lieu(4, "Forêt profonde","Alors que vous vous enfoncez dans la forêt, votre attention est rapidement attirée par un immense arbre, dont le tronc semble creux. Cependant, un énorme buisson vous bloque le passage. Vous pouvez encore  retourner à la \033[1mclairiere\033[0m.", {"clairiere":1})
		jeu.ajouter_lieu(5, "Forêt profonde","A l'aide de votre machette fraichement acquise, vous coupez le buisson qui vous bloque le passage, et vous récupérez une clé dans le tronc de l'arbre.", {"clairiere":1})
		jeu.ajouter_lieu(6, "Cabane","La porte de la cabane est malheureusement verrouillée, impossible de rentrez ni même de forcer l'épaisse porte en bois. ", {"clairiere":1})
		jeu.ajouter_lieu(7, "Victoire !","Avec la clé fraichement acquise, vous ouvrez la porte de la cabane. Dedans, vous trouvez un fabuleux trésor !", {})
		jeu.ajouter_lieu(8, "Sortir","Vous êtes sortis de la forêt, fin du jeu",{})
		jeu.ajouter_lieu(9, "Lac","Le lac est parfaitement calme, pas la moindre trace d'une créature féerique. Vous pouvez emprunter le chemin pour retourner à la \033[1mclairière\033[0m.",{"clairiere":1})
		jeu.ajouter_lieu(10, "Forêt profonde","Vous êtes face à un arbre creux, vide. Devant cet arbre se trouve un buisson tailladé. Autour de vous la forêt est dense et il semble que vous ne puissiez pas vous y enfoncer davantage. Le chemin derrière vous vous ramène à la \033[1mclairière\033[0m.",{"clairiere":1})

		jeu.mettre_objet_dans_lieu(2,6)

		jeu.ajouter_trigger(1,{"location 5":"update_lien foret 10 & give 1 & teleport 10"})
		jeu.ajouter_trigger(1,{"location 3":"update_lien lac 9 & give 0 & teleport 9"})

		jeu.ajouter_utilisation(6,{"cle":"teleport 7"})
		jeu.ajouter_utilisation(4,{"machette":"teleport 5"})
		jeu.ajouter_utilisation(2,{"parchemin":"teleport 3"})
		
		jeu.ajouter_dialogue(2,{"creature":"Alors, vous avez la réponse? Il se peut que j'aie une récompense pour vous..."})

	return jeu
