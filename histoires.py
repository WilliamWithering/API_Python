def choisir_titre():
	liste_histoires=["a","b","c"]
	
	print("Voici la liste des titres possibles pour créer votre propre histoire : ")
	for i in range(len(liste_histoires)):
		print(i, " : ", liste_histoires[i])
	titre_choisi=input("Sélectionner le nombre associé à votre titre : ")
	while titre_choisi >= len(liste_histoires) or titre_choisi<0:
        print("Titre choisi incorrect.")
		titre_choisi = input("Choisir un nombre correspondant au titre souhaité: ")


	return liste_histoires[titre_choisi]
