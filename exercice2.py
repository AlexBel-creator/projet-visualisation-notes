objet1 = {
    "nom": "smartphone",
    "prix": 599,
    "quantite_en_stock": 25,
}

objet2 = {
    "nom": "casque audio",
    "prix": 89,
    "quantite_en_stock": 50,
}

objet3 = {
    "nom": "livre",
    "prix": 15,
    "quantite_en_stock": 200,
}

objet4 = {
    "nom": "vélo électrique",
    "prix": 1299,
    "quantite_en_stock": 3,
}

objet5 = {
    "nom": "montre connectée",
    "prix": 199,
    "quantite_en_stock": 30,
}

objet6 = {
    "nom": "sac à dos",
    "prix": 59,
    "quantite_en_stock": 3,
}

liste = [objet1, objet2, objet3, objet4, objet5, objet6]
for objet in liste:
    prix = objet["prix"]
    quantite = objet["quantite_en_stock"]
    nom = objet["nom"]
    total = prix * quantite
    if (quantite < 5):    
        print(f"Le prix total de {nom} est de {total}€")
