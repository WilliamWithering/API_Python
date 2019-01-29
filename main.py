import classJeu
import histoires


titre_choisi = histoires.choisir_titre()

jeu = histoires.charger_jeu(titre_choisi)

jeu.afficher_regles()

# Pour vérifier que le jeu a été chargé correctement
print(jeu)

#On commence vraiment le jeu
while not jeu.est_fini():
    if jeu.transition:
        jeu.decrire()
        jeu.transition = 0
    commande = input("> ")
    jeu.execute(commande)

#On affiche le message du noeud final
jeu.decrire()
