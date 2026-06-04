from graphe import Graphe

# On crée nos UE
ues = ["INF212", "INF222", "INF232", "MAT232", "INF252"]

# On crée le graphe
g = Graphe(ues)

# On ajoute les conflits (UE qui partagent des étudiants)
g.ajouter_arete("INF212", "INF222")
g.ajouter_arete("INF212", "INF232")
g.ajouter_arete("INF222", "MAT232")
g.ajouter_arete("INF232", "INF252")
g.ajouter_arete("MAT232", "INF252")

# On affiche les stats
g.afficher_stats()

#on affiche la matrice
g.afficher_matrice()

# On visualise
g.visualiser()