import csv

def charger_ues():
    ues = []
    with open("donnees/ues.csv", "r") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            ues.append(ligne)
    return ues

def charger_etudiants():
    etudiants = []
    with open("donnees/etudiants.csv", "r") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            etudiants.append(ligne)
    return etudiants

def charger_salles():
    salles = []
    with open("donnees/salles.csv", "r") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            salles.append(ligne)
    return salles

def charger_surveillants():
    surveillants = []
    with open("donnees/surveillants.csv", "r") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            surveillants.append(ligne)
    return surveillants

def detecter_conflits():
    etudiants = charger_etudiants()
    ues = []
    conflits = []

    # Récupérer la liste des UE (toutes les colonnes sauf id_etudiant)
    premiere_ligne = etudiants[0]
    for cle in premiere_ligne:
        if cle != "id_etudiant":
            ues.append(cle)

    # Détecter les conflits
    for etudiant in etudiants:
        ues_etudiant = []
        for ue in ues:
            if etudiant[ue] == "1":
                ues_etudiant.append(ue)
        
        # Toutes les UE de cet étudiant sont en conflit entre elles
        for i in range(len(ues_etudiant)):
            for j in range(i+1, len(ues_etudiant)):
                paire = (ues_etudiant[i], ues_etudiant[j])
                if paire not in conflits:
                    conflits.append(paire)
    
    return ues, conflits