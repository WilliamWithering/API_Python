def choisir_titre():
	liste_histoires=["a","b","c"]
	print("Voici la liste des titres possibles pour créer votre propre histoire") 
	print(liste_histoires[0]) 
	print(liste_histoires[1]) 
	print(liste_histoires[2]) 
	
	titre_choisi=""

	while not titre_choisi in liste_histoires:
    	if titre_choisi :
        	print("Titre choisi incorrect.")
    	titre_choisi = input("Choisir un titre d'histoire : ")

	return titre_choisi