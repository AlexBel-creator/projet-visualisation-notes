import csv

# Lecture et affichage du fichier CSV
with open('notes.csv', 'r') as fichier:
    reader = csv.reader(fichier)
    next(reader)  # Ignorer l'en-tête
    print("\nNotes des étudiants:")
    for row in reader:
        print(f"{row[0]}: {row[1]}")

# Calcul et affichage de la moyenne
with open('notes.csv', 'r') as fichier:
    reader = csv.reader(fichier)
    next(reader)  # Ignorer l'en-tête
    notes = [int(row[1]) for row in reader]
    moyenne = sum(notes) / len(notes)
print(f"\nMoyenne des notes: {moyenne:.2f}")