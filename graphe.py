class Graphe:
    def __init__(self, ues):
        self.ues = ues
        self.n = len(ues)
        self.matrice = [[0] * self.n for _ in range(self.n)]
        self.liste = {ue: [] for ue in ues}

    def ajouter_arete(self, ue1, ue2):
        i = self.ues.index(ue1)
        j = self.ues.index(ue2)
        self.matrice[i][j] = 1
        self.matrice[j][i] = 1
        self.liste[ue1].append(ue2)
        self.liste[ue2].append(ue1)

    def afficher_stats(self):
        print("=== STATISTIQUES DU GRAPHE ===")
        print(f"Nombre de sommets : {self.n}")
        
        aretes = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.matrice[i][j] == 1:
                    aretes += 1
        print(f"Nombre d'arêtes : {aretes}")
        
        print("\nDegré de chaque sommet :")
        for ue in self.ues:
            degre = len(self.liste[ue])
            print(f"  {ue} : {degre}")

    def visualiser(self):
        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.Graph()
        G.add_nodes_from(self.ues)
        
        for ue in self.ues:
            for voisin in self.liste[ue]:
                G.add_edge(ue, voisin)
        
        nx.draw(G, with_labels=True, node_color='lightblue', 
                node_size=2000, font_size=10)
        plt.title("Graphe de conflits des UE")
        plt.show()

    def afficher_matrice(self):
        print("\n=== MATRICE D'ADJACENCE ===")
        print("     ", end="")
        for ue in self.ues:
            print(f"{ue[:6]:>7}", end="")
        print()
        for i in range(self.n):
            print(f"{self.ues[i][:6]:>6}", end="")
            for j in range(self.n):
                print(f"{self.matrice[i][j]:>7}", end="")
            print()

    def afficher_liste_adjacence(self):
        print("\n=== LISTE D'AJACENCE ===")
        for ue in self.ues:
            voisins = ", ".join(self.liste[ue])
            print(f" {ue} -> [{voisins}]")