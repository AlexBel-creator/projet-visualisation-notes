import csv
import matplotlib.pyplot as plt

# Lire les données depuis le fichier CSV
notes = []

with open('notes.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Ignorer l'en-tête
    for row in reader:
        notes.append(int(row[1]))  # Ajouter la note à la liste

# Créer un histogramme des notes
plt.figure(figsize=(8, 6))
plt.hist(notes, bins=5, color='skyblue', edgecolor='black')

# Ajouter un titre et des étiquettes pour les axes
plt.title("Histogramme des notes des étudiants")
plt.xlabel("Notes")
plt.ylabel("Nombre d'étudiants")

# Personnaliser l'apparence du graphique
plt.grid(True)

# Afficher le graphique
plt.show()