from graphe import Graphe
from donnees.donnees import detecter_conflits

# Charger les vraies données
ues, conflits = detecter_conflits()

# Créer le graphe avec les vraies UE
g = Graphe(ues)

# Ajouter les  conflits détectés automatiquement
for ue1, ue2 in conflits:
    g.ajouter_arete(ue1, ue2)

# Afficher les stats
g.afficher_stats()

# Afficher la matrice
g.afficher_matrice()

# Afficher la liste d'adjacence
g.afficher_liste_adjacence()

# Visualiser
g.visualiser()