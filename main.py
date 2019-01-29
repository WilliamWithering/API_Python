#FICHIER PRINCIPAL : EXECUTION DU JEU

import classJeu
import classLieu
import classPersonnage
import histoires

#Initialisation des variables utilisées dans main
titreChoisi = ""
transition = 1

histoires.afficherTitres()

while not histoires.titre_correct(titreChoisi):
    if titreChoisi :
        print("Titre choisi incorrect")
    titreChoisi = input("Choisir un titre d'histoire : ")

jeu = histoires.charger_jeu(titreChoisi)

jeu.afficher_regles()

jeu.set_nom_personnage(input())

#On commence vraiment le jeu
while not jeu.est_fini():
    if transition:
        jeu.decrire()
        transition = 0
    commande = input()
    jeu.execute(commande)

#On affiche le message du noeud final
jeu.decrire()
