import csv
import matplotlib.pyplot as plt

# Initialiser une liste pour stocker le nombre d'étudiants pour chaque note de 0 à 20
nombre_etudiant_par_note = [0] * 21  # Crée une liste avec 21 zéros

# Lire les données depuis le fichier CSV
with open('notes.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Ignorer l'en-tête
    for row in reader:
        note = int(row[1])  # Convertir la note en entier
        nombre_etudiant_par_note[note] += 1  # Incrémenter le nombre d'étudiants pour cette note

# Créer un graphique en barres
plt.figure(figsize=(10, 8))
plt.bar(range(21), nombre_etudiant_par_note, color='#800080', edgecolor='black')

# Ajouter un titre et des étiquettes pour les axes
plt.title("Nombre d'étudiants en fonction de leur note")
plt.xlabel('Note')
plt.ylabel("Nombre d'étudiants")

# Configurer les graduations sur les axes
plt.xticks(range(21))
plt.yticks(range(max(nombre_etudiant_par_note) + 1))

# Afficher le graphique
plt.show()
