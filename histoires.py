
import classJeu
def choisir_titre():
	liste_histoires=["Une histoire de poils.","La forêt noire","Le petit chaperon rouge"]
	
	print("Voici la liste des titres possibles pour créer votre propre histoire : ")
	for i in range(len(liste_histoires)):
		print(i, " : ", liste_histoires[i])
	titre_choisi=input("Sélectionner le nombre associé à votre titre : ")
	while titre_choisi >= len(liste_histoires) or titre_choisi<0:
        print("Titre choisi incorrect.")
		titre_choisi = input("Choisir un nombre correspondant au titre souhaité: ")

	return liste_histoires[titre_choisi]

def charger_jeu(titre_choisi):
	jeu=Jeu()
	if titre_choisi=="a":
		jeu.ajouter_lieu(0, "place du village", "une belle place", {"bar":1})
		jeu.ajouter_lieu(1, "le bar du village", "un bar trop tranquille", {"dehors":0})
	if titre_choisi=="b":
		pass


	return jeu