import csv

def analyser_notes(fichier):
    notes = []
    with open(fichier, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            notes.append(float(row['Note']))
    
    if not notes:
        print("Aucune note trouvée dans le fichier.")
        return

    # Calcul des statistiques
    note_max = max(notes)
    note_min = min(notes)
    moyenne = sum(notes) / len(notes)
    nb_au_dessus_moyenne = sum(1 for note in notes if note > moyenne)

    # Affichage des résultats
    print(f"Note la plus haute : {note_max}")
    print(f"Note la plus basse : {note_min}")
    print(f"Moyenne de la classe : {moyenne:.2f}")
    print(f"Nombre d'étudiants au-dessus de la moyenne : {nb_au_dessus_moyenne}")

# Exécution de l'analyse
analyser_notes('notes.csv')