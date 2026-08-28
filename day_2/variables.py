# Day 2 : 30 Days of python programming


# ==========================================
# NIVEAU 1
# ==========================================

def exercice_1():
    prenom = "Noa"
    nom = "DOISY"
    nom_complet = "Noa DOISY"
    pays = "France"
    ville = "Avignon"
    age = 20
    annee = 2006
    est_marie = False
    est_vrai = True
    is_light_on = True

    a, b, c = 1, 2, 3

    print("Prénom :", prenom)
    print("Nom :", nom)
    print("Nom complet :", nom_complet)
    print("Pays :", pays)
    print("Ville :", ville)
    print("Âge :", age)
    print("Année :", annee)
    print("Est marié :", est_marie)
    print("Est vrai :", est_vrai)
    print("Lumière allumée :", is_light_on)
    print("a =", a, "b =", b, "c =", c)


# ==========================================
# NIVEAU 2
# ==========================================

def exercice_2():
    prenom = "Noa"
    nom = "DOISY"
    nom_complet = "Noa DOISY"
    pays = "France"
    ville = "Avignon"
    age = 20
    annee = 2006
    est_marie = False
    est_vrai = True
    is_light_on = True
    a, b, c = 1, 2, 3

    dico = [
        prenom,
        nom,
        nom_complet,
        pays,
        ville,
        age,
        annee,
        est_marie,
        est_vrai,
        is_light_on,
        a,
        b,
        c
    ]

    for i in dico:
        print(type(i))


def exercice_3():
    prenom = "Noa"

    print("La longueur de ton prénom est de :", len(prenom))


def exercice_4():
    prenom = "Noa"
    nom = "DOISY"

    if len(prenom) > len(nom):
        print("Ton prénom est plus long que ton nom")
    elif len(prenom) < len(nom):
        print("Ton nom est plus long que ton prénom")
    else:
        print("Ton prénom et ton nom ont la même longueur")


def exercice_5():
    num_one = 5
    num_two = 4

    total = num_one + num_two

    print("Total :", total)


def exercice_6():
    num_one = 5
    num_two = 4

    diff = num_one - num_two

    print("Différence :", diff)


def exercice_7():
    num_one = 5
    num_two = 4

    product = num_one * num_two

    print("Produit :", product)


def exercice_8():
    num_one = 5
    num_two = 4

    division = num_one / num_two

    print("Division :", division)


def exercice_9():
    num_one = 5
    num_two = 4

    remainder = num_two % num_one

    print("Reste :", remainder)


def exercice_10():
    num_one = 5
    num_two = 4

    exp = num_one ** num_two

    print("Puissance :", exp)


def exercice_11():
    num_one = 5
    num_two = 4

    floor_division = num_one // num_two

    print("Division entière :", floor_division)


def exercice_12():
    rayon = 30
    pi = 3.1415

    area_of_circle = (rayon ** 2) * pi
    circum_of_circle = 2 * pi * rayon

    print("Aire du cercle :", area_of_circle)
    print("Circonférence du cercle :", circum_of_circle)


def exercice_12_3():
    pi = 3.1415

    rayon_user = int(input("Quel est le rayon de votre cercle : "))

    aire = (rayon_user ** 2) * pi

    print("L'aire du cercle est :", aire)


def exercice_13():
    prenom_user = input("Quel est votre prénom : ")
    nom_user = input("Quel est votre nom : ")
    age_user = int(input("Quel est votre âge : "))
    pays_user = input("Quel est votre pays : ")

    print("\nInformations utilisateur :")
    print("Prénom :", prenom_user)
    print("Nom :", nom_user)
    print("Âge :", age_user)
    print("Pays :", pays_user)


def exercice_14():
    help("keywords")


# ==========================================
# MENU
# ==========================================

exercices = {
    "1": exercice_1,
    "2": exercice_2,
    "3": exercice_3,
    "4": exercice_4,
    "5": exercice_5,
    "6": exercice_6,
    "7": exercice_7,
    "8": exercice_8,
    "9": exercice_9,
    "10": exercice_10,
    "11": exercice_11,
    "12": exercice_12,
    "12.3": exercice_12_3,
    "13": exercice_13,
    "14": exercice_14
}


while True:
    print("""
========================================
       30 DAYS OF PYTHON - DAY 2
========================================

--- Niveau 1 ---

1  - Variables

--- Niveau 2 ---

2  - Type des variables
3  - Longueur du prénom
4  - Comparer prénom et nom
5  - Addition
6  - Soustraction
7  - Multiplication
8  - Division
9  - Modulo
10 - Puissance
11 - Division entière
12 - Aire et circonférence du cercle
12.3 - Aire avec rayon utilisateur
13 - Informations utilisateur
14 - Python keywords

0  - Quitter
""")

    choix = input("Quel exercice voulez-vous lancer ? ")

    if choix == "0":
        print("Au revoir !")
        break

    if choix in exercices:
        print("\n========== EXERCICE", choix, "==========\n")
        exercices[choix]()
        print("\n========================================")
    else:
        print("❌ Cet exercice n'existe pas.")