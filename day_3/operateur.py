# =========================
# VARIABLES
# =========================

age = 20
taille = 183.0
complexe = 1 + 1j


# =========================
# EXERCICES
# =========================

def exercice_3():
    base = int(input("Entrez la base : "))
    hauteur = int(input("Entrez la hauteur : "))

    aire = 0.5 * base * hauteur

    print("L'aire du triangle est", aire)


def exercice_5():
    cote1 = int(input("Entrez le côté a : "))
    cote2 = int(input("Entrez le côté b : "))
    cote3 = int(input("Entrez le côté c : "))

    perimetre = cote1 + cote2 + cote3

    print("Le périmètre du triangle est", perimetre)


def exercice_6():
    longueur = int(input("Entrez la longueur : "))
    largeur = int(input("Entrez la largeur : "))

    aire = longueur * largeur
    perimetre = 2 * (longueur + largeur)

    print("L'aire du rectangle est", aire)
    print("Le périmètre du rectangle est", perimetre)


def exercice_7():
    rayon = int(input("Entrez le rayon du cercle : "))

    pi = 3.14
    aire = pi * rayon * rayon
    circonference = 2 * pi * rayon

    print("L'aire du cercle est", aire)
    print("La circonférence du cercle est", circonference)


def exercice_8():
    # y = 2x - 2
    pente = 2
    ordonnee_origine = -2
    abscisse_origine = 1

    print("Pente :", pente)
    print("Ordonnée à l'origine :", ordonnee_origine)
    print("Abscisse à l'origine :", abscisse_origine)


def exercice_9():
    x1 = 2
    y1 = 2

    x2 = 6
    y2 = 10

    pente = (y2 - y1) / (x2 - x1)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    print("Pente :", pente)
    print("Distance euclidienne :", distance)


def exercice_10():
    pente_8 = 2
    pente_9 = (10 - 2) / (6 - 2)

    print("Pente de l'exercice 8 :", pente_8)
    print("Pente de l'exercice 9 :", pente_9)

    if pente_8 == pente_9:
        print("Les deux pentes sont égales.")
    else:
        print("Les deux pentes sont différentes.")


def exercice_11():
    i = -100

    while (i ** 2 + (6 * i + 9)) != 0:
        i += 1

    print("x =", i)


def exercice_12():
    longueur_python = len("python")
    longueur_dragon = len("dragon")

    print("Longueur de python :", longueur_python)
    print("Longueur de dragon :", longueur_dragon)

    if longueur_python == longueur_dragon:
        print("True")
    else:
        print("False")


def exercice_13():
    if "on" in "python" and "on" in "dragon":
        print("True")
    else:
        print("False")


def exercice_14():
    phrase = "I hope this course is not full of jargon"

    if "jargon" in phrase:
        print("True")
    else:
        print("False")


def exercice_15():
    if "on" not in "python" and "on" not in "dragon":
        print("True")
    else:
        print("False")


def exercice_16():
    longueur = len("python")

    longueur_float = float(longueur)
    longueur_string = str(longueur_float)

    print(longueur_string)


def exercice_17():
    nombre = int(input("Entrez un nombre : "))

    if nombre % 2 == 0:
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")


def exercice_18():
    if int(7 / 3) == int(2.7):
        print("True")
    else:
        print("False")


def exercice_19():
    if type("10") == type(10):
        print("True")
    else:
        print("False")


def exercice_20():
    # int("9.8") provoque une erreur,
    # il faut d'abord convertir en float.
    if int(float("9.8")) == 10:
        print("True")
    else:
        print("False")


def exercice_21():
    nb_heure = float(input("Entrez les heures : "))
    taux_horaire = float(input("Entrez le taux horaire : "))

    salaire = nb_heure * taux_horaire

    print("Votre salaire hebdomadaire est", salaire)


def exercice_22():
    annee = int(input("Entrez le nombre d'années que vous avez vécues : "))

    secondes = annee * 365 * 24 * 60 * 60

    print("Vous avez vécu", secondes, "secondes.")


def exercice_23():
    for i in range(1, 6):
        print(i, 1, i, i ** 2, i ** 3)


# =========================
# MENU
# =========================

exercices = {
    3: exercice_3,
    5: exercice_5,
    6: exercice_6,
    7: exercice_7,
    8: exercice_8,
    9: exercice_9,
    10: exercice_10,
    11: exercice_11,
    12: exercice_12,
    13: exercice_13,
    14: exercice_14,
    15: exercice_15,
    16: exercice_16,
    17: exercice_17,
    18: exercice_18,
    19: exercice_19,
    20: exercice_20,
    21: exercice_21,
    22: exercice_22,
    23: exercice_23
}


while True:
    print("\n========== 30 DAYS OF PYTHON ==========")
    print("3  - Aire du triangle")
    print("5  - Périmètre du triangle")
    print("6  - Rectangle")
    print("7  - Cercle")
    print("8  - Pente / ordonnée / abscisse")
    print("9  - Pente / distance")
    print("10 - Comparaison des pentes")
    print("11 - Équation")
    print("12 - Python / Dragon")
    print("13 - Opérateur and")
    print("14 - Opérateur in")
    print("15 - Opérateur not in")
    print("16 - Conversion")
    print("17 - Nombre pair")
    print("18 - Division")
    print("19 - Type")
    print("20 - Conversion 9.8")
    print("21 - Salaire")
    print("22 - Secondes vécues")
    print("23 - Tableau")
    print("0  - Quitter")

    choix = int(input("\nQuel exercice voulez-vous lancer ? "))

    if choix == 0:
        print("Au revoir !")
        break

    if choix in exercices:
        exercices[choix]()
    else:
        print("Cet exercice n'est pas disponible.")