import tkinter as tk
import random


# Fonction pour ouvrir une nouvelle fenêtre
def ouvrir_nouvelle_fenetre():
    # Ferme la fenêtre actuelle
    fenetre.destroy()

    # Crée une nouvelle fenêtre
    nouvelle_fenetre = tk.Tk()
    nouvelle_fenetre.title("Roulette russe")

    # Définir les dimensions de la nouvelle fenêtre
    largeur_nouvelle_fenetre = 400
    hauteur_nouvelle_fenetre = 300

    # Récupérer les dimensions de l'écran
    largeur_ecran = nouvelle_fenetre.winfo_screenwidth()
    hauteur_ecran = nouvelle_fenetre.winfo_screenheight()

    # Calculer la position pour centrer la nouvelle fenêtre
    x_position = (largeur_ecran - largeur_nouvelle_fenetre) // 2
    y_position = (hauteur_ecran - hauteur_nouvelle_fenetre) // 2

    # Positionner la nouvelle fenêtre au centre de l'écran et définir ses dimensions
    nouvelle_fenetre.geometry(
        f"{largeur_nouvelle_fenetre}x{hauteur_nouvelle_fenetre}+{x_position}+{y_position}"
    )

    # Ajout d'un label pour le texte
    label = tk.Label(
        nouvelle_fenetre,
        text="Chosie le nombre de munition dans le chargeur !(1 à 6)",
        font=("Arial", 10))
    label.pack()

    # Fonction de validation pour accepter uniquement les chiffres de 1 à 6
    def valider_entree(chaine):
        if chaine.isdigit() and 1 <= int(chaine) <= 6:
            return True
        elif chaine == "":
            return True
        else:
            return False

    # Enregistrement de la fonction de validation
    validation = nouvelle_fenetre.register(valider_entree)

    # Ajout d'une zone de saisie (Entry) pour saisir le nombre
    entry = tk.Entry(nouvelle_fenetre,
                     validate="key",
                     validatecommand=(validation, "%P"))
    entry.pack()

    # Fonction pour afficher le nombre saisi et ouvrir une autre fenêtre
    def afficher_nombre_et_ouvrir_fenetre_suivante():
        nombre_saisi = entry.get()
        nombre_affichage.config(text=nombre_saisi)
        # Ferme la fenêtre actuelle
        nouvelle_fenetre.destroy()
        # Ouvre la fenêtre suivante avec le nombre saisi
        ouvrir_fenetre_suivante(int(nombre_saisi))

    # Bouton pour afficher le nombre saisi et ouvrir une autre fenêtre
    bouton_afficher = tk.Button(
        nouvelle_fenetre,
        text="Lancer le jeu",
        command=afficher_nombre_et_ouvrir_fenetre_suivante,
        font=("Arial", 12))
    bouton_afficher.pack()

    # Label pour afficher le nombre saisi
    nombre_affichage = tk.Label(nouvelle_fenetre, text="")
    nombre_affichage.pack()

    nouvelle_fenetre.mainloop()


# Fonction pour ouvrir la fenêtre suivante
def ouvrir_fenetre_suivante(nombre):
    # Crée une nouvelle fenêtre
    fenetre_suivante = tk.Tk()
    fenetre_suivante.title("Roulette russe")

    # Définir les dimensions de la nouvelle fenêtre
    largeur_fenetre_suivante = 400
    hauteur_fenetre_suivante = 300

    # Récupérer les dimensions de l'écran
    largeur_ecran = fenetre_suivante.winfo_screenwidth()
    hauteur_ecran = fenetre_suivante.winfo_screenheight()

    # Calculer la position pour centrer la nouvelle fenêtre
    x_position = (largeur_ecran - largeur_fenetre_suivante) // 2
    y_position = (hauteur_ecran - hauteur_fenetre_suivante) // 2

    # Positionner la nouvelle fenêtre au centre de l'écran et définir ses dimensions
    fenetre_suivante.geometry(
        f"{largeur_fenetre_suivante}x{hauteur_fenetre_suivante}+{x_position}+{y_position}"
    )

    # Afficher le nombre saisi dans la nouvelle fenêtre
    label = tk.Label(fenetre_suivante,
                     text=f"Il y a {nombre} balle(s) dans un chargeur de 6",
                     font=("Arial", 12))
    label.pack()

    # Intervalle maximum pour le tir du pistolet
    intervalle_max = 6

    # Fonction pour tirer le pistolet
    def tirer():
        nonlocal intervalle_max
        # Générer un nombre aléatoire entre 1 et l'intervalle maximum
        resultat = random.randint(1, intervalle_max)
        if resultat <= nombre:
            resultat_label.config(text="BOOM ! TES MORT SALE FDP.",
                                  font=("Arial", 12))
            fenetre_suivante.after(
                1000,
                fenetre_suivante.destroy)  # Ferme la fenêtre après 3 secondes
        else:
            resultat_label.config(text="Clic. Vous avez de la chance !",
                                  font=("Arial", 12))
            intervalle_max -= 1
            if intervalle_max < 1:
                intervalle_max = 1  # Limite inférieure de l'intervalle

    # Bouton pour tirer le pistolet
    bouton_tirer = tk.Button(fenetre_suivante,
                             text="Tirer",
                             command=tirer,
                             font=("Arial", 12))
    bouton_tirer.pack(pady=10)

    # Label pour afficher le résultat
    resultat_label = tk.Label(fenetre_suivante, text="")
    resultat_label.pack()

    fenetre_suivante.mainloop()


# Crée la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Roulette russe")

# Définir les dimensions de la fenêtre principale
largeur_fenetre = 400
hauteur_fenetre = 200

# Récupérer les dimensions de l'écran
largeur_ecran = fenetre.winfo_screenwidth()
hauteur_ecran = fenetre.winfo_screenheight()

# Calculer la position pour centrer la fenêtre principale
x_position = (largeur_ecran - largeur_fenetre) // 2
y_position = (hauteur_ecran - hauteur_fenetre) // 2

# Positionner la fenêtre principale au centre de l'écran et définir ses dimensions
fenetre.geometry(
    f"{largeur_fenetre}x{hauteur_fenetre}+{x_position}+{y_position}")

# Crée un cadre dans la fenêtre principale
cadre = tk.Frame(fenetre)
cadre.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Ajout d'un label au cadre
texte = tk.Label(cadre, text="Roulette russe", font=("Arial", 16))
texte.pack()

# Ajout d'un bouton au cadre pour ouvrir une nouvelle fenêtre
bouton = tk.Button(cadre,
                   text="Play",
                   command=ouvrir_nouvelle_fenetre,
                   font=("Arial", 12))
bouton.pack(pady=10)

# Démarrer la boucle principale de la fenêtre
fenetre.mainloop()
