# Day 4 : 30 Days of Python Programming
from xxlimited_35 import Null


# ==========================================
# EXERCICES
# ==========================================

def exercice_1():
    # Concaténez 'Thirty', 'Days', 'Of', 'Python'
    # pour obtenir 'Thirty Days Of Python'

    return "Thirty"+" "+"Days"+" "+'Of'+"Python"


def exercice_2():
    # Concaténez 'Coding', 'For', 'All'
    # pour obtenir 'Coding For All'

    return "Coding"+" "+"For"+" "+"All"


def exercice_3():
    # Déclarez company avec la valeur "Coding For All"
    company = "Coding For All"

    print("ok")



def exercice_4():
    company = "Coding For All"

    # Affichez company

    return(company)


def exercice_5():
    company = "Coding For All"

    # Affichez la longueur de company

    return len(company)


def exercice_6():
    company = "Coding For All"

    # Convertissez company en majuscules

    return company.upper()


def exercice_7():
    company = "Coding For All"

    # Convertissez company en minuscules

    return company.lower()


def exercice_8():
    company = "Coding For All"

    # Utilisez capitalize(), title() et swapcase()

    return company.capitalize().title().swapcase()


def exercice_9():
    company = "Coding For All"

    # Découpez le premier mot

    return company.split(" ")[0]


def exercice_10():
    company = "Coding For All"

    # Vérifiez si company contient "Coding"
    # avec index(), find() ou une autre méthode

    temp = company.split(" ")
    if "Coding" in temp:
        return temp.index("Coding")
    else:
        return False

def exercice_11():
    company = "Coding For All"

    # Remplacez "Coding" par "Python"

    temp = company.split(" ")
    if "Coding" in temp:
        index = temp.index("Coding")
        temp[index] = "Python"

        return " ".join(temp)
    else:
        return False


def exercice_12():
    texte = "Python for Everyone"

    # Transformez-le en "Python for All"

    temp = texte.split(" ")
    if "Everyone" in temp:
        index = temp.index("Everyone")
        temp[index] = "All"

        return " ".join(temp)
    else:
        return False


def exercice_13():
    company = "Coding For All"

    # Découpez la chaîne au niveau des espaces

    return company.split(" ")


def exercice_14():
    companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

    # Découpez la chaîne au niveau des virgules

    return companies.split(", ")


def exercice_15():
    company = "Coding For All"

    # Trouvez le caractère à l'indice 0

    return company[0]

def exercice_16():
    company = "Coding For All"

    # Trouvez le dernier indice

    return company[-1]


def exercice_17():
    company = "Coding For All"

    # Trouvez le caractère à l'indice 10

    return company[10]


def exercice_18():
    texte = "Python For Everyone"

    # Créez un acronyme / une abréviation

    temp = texte.split(" ")
    acronyme = ""
    for i in temp:
        acronyme+=i[0]
    return acronyme


def exercice_19():
    texte = "Coding For All"

    # Créez un acronyme / une abréviation

    temp = texte.split(" ")
    acronyme = ""
    for i in temp:
        acronyme += i[0]
    return acronyme


def exercice_20():
    company = "Coding For All"

    # Trouvez la position de la première occurrence de C avec index()

    return company.index("C")


def exercice_21():
    company = "Coding For All"

    # Trouvez la position de la première occurrence de F avec index()

    return company.index("F")


def exercice_22():
    texte = "Coding For All People"

    # Trouvez la dernière occurrence de l avec rfind()

    return texte.rfind('l')

def exercice_23():
    texte = "You cannot end a sentence with because because because is a conjunction"

    # Trouvez la première occurrence de "because"
    # avec index(), find() ou autre

    return texte.index("because")


def exercice_24():
    texte = "You cannot end a sentence with because because because is a conjunction"

    # Trouvez la dernière occurrence de "because" avec rindex()

    return texte.rindex("because")


def exercice_25():
    texte = "You cannot end a sentence with because because because is a conjunction"

    # Extrayez "because because because"

    debut = texte.find("because")
    fin = texte.rfind("because") + len("because")

    texte[debut:fin]
    return texte


def exercice_26():
    texte = "You cannot end a sentence with because because because is a conjunction"

    # Trouvez la première occurrence de "because"
    # avec index(), find() ou autre

    return texte.index("because")


def exercice_27():
    texte = "You cannot end a sentence with because because because is a conjunction"

    # Extrayez "because because because"

    debut = texte.find("because")
    fin = texte.rfind("because") + len("because")

    texte[debut:fin]
    return texte


def exercice_28():
    company = "Coding For All"

    # Vérifiez si company commence par "Coding"

    return company.startswith("Coding")


def exercice_29():
    company = "Coding For All"

    # Vérifiez si company se termine par "coding"

    return company.endswith("coding")


def exercice_30():
    texte = "   Coding For All   "

    # Supprimez les espaces au début et à la fin
    return texte.strip()


def exercice_31():
    # Vérifiez lesquels de ces noms sont des identifiants valides :
    # 30DaysOfPython
    # thirty_days_of_python
    t1 = "30DaysOfPython"
    t2 = "thirty_days_of_python"


    return t1.isidentifier(),t2.isidentifier()


def exercice_32():
    bibliotheques = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

    # Joignez la liste avec "# "

    "# ".join(bibliotheques)
    return bibliotheques


def exercice_33():
    # Utilisez \n pour séparer les deux phrases :
    #
    # I am enjoying this challenge.
    # I just wonder what is next.

    return "I am enjoying this challenge.\n I just wonder what is next."


def exercice_34():
    # Utilisez \t pour afficher :
    #
    # Name      Age     Country   City
    # Asabeneh  250     Finland   Helsinki

    return "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"


def exercice_35():
    radius = 10
    area = 3.14 * radius ** 2

    # Utilisez le formatage de chaînes pour obtenir :
    #
    # The area of a circle with radius 10 is 314 meters square.

    return f"The area of a circle with radius {radius} is {area:.0f} meters square."


def exercice_36():
    a = 8
    b = 6

    # Utilisez le formatage de chaînes pour afficher :
    #
    # 8 + 6 = 14
    # 8 - 6 = 2
    # 8 * 6 = 48
    # 8 / 6 = 1.33
    # 8 % 6 = 2
    # 8 // 6 = 1
    # 8 ** 6 = 262144



    return f"""{a} + {b} = {a + b}
    {a} - {b} = {a - b}
    {a} * {b} = {a * b}
    {a} / {b} = {a / b:.2f}
    {a} % {b} = {a % b}
    {a} // {b} = {a // b}
    {a} ** {b} = {a ** b}"""


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
    "13": exercice_13,
    "14": exercice_14,
    "15": exercice_15,
    "16": exercice_16,
    "17": exercice_17,
    "18": exercice_18,
    "19": exercice_19,
    "20": exercice_20,
    "21": exercice_21,
    "22": exercice_22,
    "23": exercice_23,
    "24": exercice_24,
    "25": exercice_25,
    "26": exercice_26,
    "27": exercice_27,
    "28": exercice_28,
    "29": exercice_29,
    "30": exercice_30,
    "31": exercice_31,
    "32": exercice_32,
    "33": exercice_33,
    "34": exercice_34,
    "35": exercice_35,
    "36": exercice_36
}


while True:
    print("""
========================================
       30 DAYS OF PYTHON - DAY 4
========================================

1  - Concaténation
2  - Concaténation
3  - Variable company
4  - Afficher company
5  - Longueur de company
6  - Majuscules
7  - Minuscules
8  - capitalize / title / swapcase
9  - Slicing du premier mot
10 - Vérifier "Coding"
11 - Remplacer Coding
12 - Remplacer Python for Everyone
13 - Split Coding For All
14 - Split des entreprises
15 - Indice 0
16 - Dernier indice
17 - Indice 10
18 - Acronyme Python For Everyone
19 - Acronyme Coding For All
20 - Position de C
21 - Position de F
22 - Dernier l
23 - Première occurrence de because
24 - Dernière occurrence de because
25 - Extraire because because because
26 - Première occurrence de because
27 - Extraire because because because
28 - Commence par Coding ?
29 - Termine par coding ?
30 - Supprimer les espaces
31 - isidentifier()
32 - Joindre une liste
33 - Nouvelle ligne
34 - Tabulation
35 - Formatage du cercle
36 - Formatage des opérations

0  - Quitter
""")

    choix = input("Quel exercice voulez-vous lancer ? ")

    if choix == "0":
        print("Au revoir !")
        break

    if choix in exercices:
        print(f"\n========== EXERCICE {choix} ==========\n")
        print(exercices[choix]())
        print("\n=======================================")
    else:
        print("❌ Cet exercice n'existe pas.")