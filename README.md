# API_Python
Création d'un jeu d' "Aventure textuelle" pour l'API "Python pour les sciences" à l'UTC.

  Le but du projet est de créer un moteur narratif permettant de jouer à une aventure textuelle. Nous avons cherché à garder le programme le moins spécifique possible pour ne pas restreindre les histoires. 

  L'utilisateur intéragit via la console avec un objet "jeu". Cet objet contient un objet personnage avec un inventaire, et quelques attributs concernant son état interne, mais surtout une liste d'objets "lieu". 
  Chaque lieu possède un nom et un descriptif, ainsi qu'un dictionnaire de transitions vers d'autres lieux, une liste d'objets, un dictionnaire de dialogues et un dernier de "triggers", c'est à dire des couples "condition":"action" permettant de faire avancer l'histoire.
  L'objet jeu dispose de méthodes lui permettant de reconnaître des mots-clés dans les commandes saisies par l'utilisateur et d'exécuter les ordres reconnus. Il gère aussi la vérification des conditions de déclenchement des triggers. 

  Le fichier histoires contient des suites d'instructions permettant de charger les lieux, objets, triggers et dialogues utilisés dans l'histoire, avant le commencement du jeu. Ces instructions sont pour le moment générées manuellement et il serait donc intéressant de rendre le processus de création de ces instructions plus simple, via une interface graphique. 

# Contributeurs
LEPAGE Simon, MOUET Nicolas, WACQUEZ Arthur

# Cahier des charges 

Fonctionnalités implémentées : 
- Se déplacer entre différents lieux 
- Gestion des objets (inventaire, ramassage, utilisation...)
- Gestion des commandes
- Gestion d'évènements scénaristiques
- Tentative d'assouplissement de la saisie de texte : appostrophes, accents (ex : reconnaissance de "l'épée" comme "epee")

Quelques problèmes :
- Affichage du gras non disponible sous windows : les balises ayant cet effet pour UNIX ne sont pas reconnues par le cmd Windows.

Pour aller plus loin : 
- Créer plus d'évènements scénaristiques utilisables
- Ajouter des histoires
- Gérer des dialogues plus intéractifs
- Créer un éditeur d'histoires pour faciliter la création
