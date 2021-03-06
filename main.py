import classJeu
import histoires

titre_choisi = histoires.choisir_titre()

jeu = histoires.charger_jeu(titre_choisi)

jeu.afficher_regles()

# Pour vérifier que le jeu a été chargé correctement
#print(jeu)
#On commence vraiment le jeu

nom_ancien_lieu = ""

while not jeu.est_fini():
    if jeu.transition:
        if nom_ancien_lieu != jeu.lieu[jeu.lieu_actuel].nom:
            jeu.afficher_nom_lieu()
            nom_ancien_lieu = jeu.lieu[jeu.lieu_actuel].nom
        jeu.decrire()
        jeu.transition = 0

    jeu.verif_triggers()

    if jeu.transition == 0:
        commande = input("> ").lower()
        jeu.execute(commande)


#On affiche le message du noeud final
jeu.afficher_nom_lieu()
jeu.decrire()
