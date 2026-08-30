# Day 5 : 30 Days of Python Programming


# ==========================================
# NIVEAU 1
# ==========================================

def exercice_1():
    # Déclarez une liste vide

    liste = []
    return liste


def exercice_2():
    # Déclarez une liste avec plus de 5 éléments

    liste=[ i for i in range(5) ]
    return liste

def exercice_3():
    ma_liste = [1, 2, 3, 4, 5, 6]

    return len(ma_liste)


def exercice_4():
    ma_liste = [1, 2, 3, 4, 5, 6]

    # Obtenez le premier élément,
    # l'élément du milieu et le dernier élément

    premier = ma_liste[0]
    milieu = ma_liste[len(ma_liste)//2]
    dernier = ma_liste[-1]

    return premier,milieu,dernier


def exercice_5():
    # Créez mixed_data_types contenant :
    # votre nom, âge, taille, situation matrimoniale, adresse

    mixed_data_types = ["DOISY",20,183,"celibataire","45 impasse marderic 30126 st laurent des arbres"]
    return mixed_data_types



def exercice_6():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    return it_companies


def exercice_7():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Affichez la liste avec print()

    return it_companies

def exercice_8():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Affichez le nombre d'entreprises

    return len(it_companies)


def exercice_9():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Affichez la première,
    # celle du milieu et la dernière entreprise

    premier = it_companies[0]
    milieu = it_companies[len(it_companies) // 2]
    dernier = it_companies[-1]

    return premier, milieu, dernier


def exercice_10():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Modifiez l'une des entreprises
    # puis affichez la liste

    it_companies[-1]="Koesio"
    return it_companies


def exercice_11():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Ajoutez une entreprise IT à la liste

    it_companies.append("Koesio")


def exercice_12():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Insérez une entreprise IT au milieu de la liste

    it_companies.insert(len(it_companies)//2,"Koesio")
    return it_companies


def exercice_13():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Changez l'un des noms en majuscules
    # IBM doit rester inchangé

    it_companies[0] = it_companies[0].upper()
    return it_companies


def exercice_14():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Joignez les entreprises avec "# "

    chaine = ""
    for companies in it_companies:
        chaine+=f"#{companies} "
    return chaine


def exercice_15():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Vérifiez si une certaine entreprise
    # existe dans la liste

    return True if "Apple" in it_companies else False

def exercice_16():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Triez la liste avec sort()

    return it_companies.sort()


def exercice_17():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Inversez la liste avec reverse()

    return it_companies.reverse()


def exercice_18():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Découpez les 3 premières entreprises

    return it_companies[:3]


def exercice_19():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Découpez les 3 dernières entreprises

    return it_companies[-3:]


def exercice_20():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Découpez l'entreprise du milieu
    # (ou les entreprises du milieu)

    return it_companies[(len(it_companies)//2)+1]


def exercice_21():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Supprimez la première entreprise IT

    it_companies.pop(0)
    return it_companies


def exercice_22():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Supprimez l'entreprise du milieu
    # (ou les entreprises du milieu)

    it_companies.pop((len(it_companies) // 2) + 1)
    return it_companies


def exercice_23():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Supprimez la dernière entreprise IT

    return it_companies.pop(-1)

def exercice_24():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Supprimez toutes les entreprises IT

    for i in range(len(it_companies)):
        it_companies.pop()

    return it_companies


def exercice_25():
    it_companies = [
        "Facebook",
        "Google",
        "Microsoft",
        "Apple",
        "IBM",
        "Oracle",
        "Amazon"
    ]

    # Détruisez la liste des entreprises IT

    it_companies.clear()

    return it_companies


def exercice_26():
    front_end = ["HTML", "CSS", "JS", "React", "Redux"]
    back_end = ["Node", "Express", "MongoDB"]

    # Joignez les deux listes

    final_list = front_end + back_end
    return final_list


def exercice_27():
    front_end = ["HTML", "CSS", "JS", "React", "Redux"]
    back_end = ["Node", "Express", "MongoDB"]

    # Joignez les deux listes.
    # Copiez la liste jointe dans full_stack.
    # Insérez Python et SQL après Redux.

    front_end+=back_end
    final_list = front_end.copy()

    for index in range(len(final_list)):
        if final_list[index] == "Redux":
            final_list.insert(index+1,"Python")
            final_list.insert(index+2,"SQL")
            break

    return final_list

# ==========================================
# NIVEAU 2
# ==========================================

def exercice_28():
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    # Triez la liste et trouvez l'âge minimum et maximum.

    ages.sort()

    return ages[0],ages[-1]


def exercice_29():
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    # Ajoutez à nouveau l'âge minimum
    # et l'âge maximum à la liste.
    ages.sort()
    min_age = ages[0]
    max_age = ages[-1]

    ages.append(min_age)
    ages.append(max_age)
    return ages



def exercice_30():
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    # Trouvez l'âge médian.

    ages.sort()

    return ages[len(ages)//2] if len(ages)%2==0 else (ages[len(ages)//2] + ages[(len(ages)//2)+1])/2

def exercice_31():
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    # Trouvez l'âge moyen.

    somme = 0

    for i in range(len(ages)):
        somme += ages[i]

    total = somme / len(ages)

    return total


def exercice_32():
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    # Trouvez l'étendue des âges.
    # max - min

    ages.sort()

    return ages[-1]-ages[0]


def exercice_33():
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    # Comparez :
    # abs(min - moyenne)
    # abs(max - moyenne)

    ages.sort()

    min = ages[0]
    max = ages[-1]
    moyenne = sum(ages)/len(ages)

    return abs(max-moyenne),abs(min-moyenne)


def exercice_34():
    # Importez/utilisez la liste countries du fichier
    # data/countries.py
    #
    # Trouvez le(s) pays du milieu.

    from data import countries

    return countries.countries[len(countries.countries)//2]


def exercice_35():
    # Importez/utilisez la liste countries du fichier
    # data/countries.py
    #
    # Divisez la liste en deux listes égales.
    # Si le nombre est impair,
    # un pays de plus pour la première moitié.

    from data.countries import countries

    # Calcul de l'index du milieu (arrondi au supérieur en cas d'impair)
    milieu = (len(countries) + 1) // 2

    liste_1 = countries[:milieu]
    liste_2 = countries[milieu:]

    return liste_1,liste_2


def exercice_36():
    countries = [
        "China",
        "Russia",
        "USA",
        "Finland",
        "Sweden",
        "Norway",
        "Denmark"
    ]

    # Dépaquetez les trois premiers pays
    # et le reste comme pays scandinaves.

    liste_first,liste_scandinaves = countries[:3],countries[3:]
    return liste_first,liste_scandinaves



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
       30 DAYS OF PYTHON - DAY 5
========================================

--- Niveau 1 ---

1  - Liste vide
2  - Liste de plus de 5 éléments
3  - Longueur d'une liste
4  - Premier / milieu / dernier
5  - mixed_data_types
6  - it_companies
7  - Afficher it_companies
8  - Nombre d'entreprises
9  - Première / milieu / dernière
10 - Modifier une entreprise
11 - Ajouter une entreprise
12 - Insérer au milieu
13 - Mettre une entreprise en majuscules
14 - Joindre avec "# "
15 - Vérifier une entreprise
16 - Trier avec sort()
17 - Inverser avec reverse()
18 - 3 premières entreprises
19 - 3 dernières entreprises
20 - Entreprise(s) du milieu
21 - Supprimer la première
22 - Supprimer le milieu
23 - Supprimer la dernière
24 - Supprimer toutes
25 - Détruire la liste
26 - Joindre front_end et back_end
27 - Créer full_stack

--- Niveau 2 ---

28 - Minimum et maximum
29 - Ajouter min et max
30 - Médiane
31 - Moyenne
32 - Étendue
33 - Comparaison avec abs()
34 - Pays du milieu
35 - Diviser les pays
36 - Dépaquetage des pays

0  - Quitter
""")

    choix = input("Quel exercice voulez-vous lancer ? ")

    if choix == "0":
        print("Au revoir !")
        break

    if choix in exercices:
        print(f"\n========== EXERCICE {choix} ==========\n")

        resultat = exercices[choix]()

        if resultat is not None:
            print(resultat)

        print("\n=======================================")

    else:
        print("❌ Cet exercice n'existe pas.")