from donnees.donnees import detecter_conflits, charger_salles, charger_surveillants

ues, conflits = detecter_conflits()

print("=== UES DETECTEES ===")
for ue in ues:
    print(f"  {ue}")

print(f"\n=== CONFLITS DETECTES : {len(conflits)} ===")
for c in conflits:
    print(f"  {c[0]} <-> {c[1]}")

print("\n=== SALLES ===")
for salle in charger_salles():
    print(f"  {salle['code_salle']} - capacite: {salle['capacite']} - type: {salle['type_salle']}")

print("\n=== SURVEILLANTS ===")
for s in charger_surveillants():
    print(f"  {s['id_surveillant']} surveille {s['ue_surveillee']}")