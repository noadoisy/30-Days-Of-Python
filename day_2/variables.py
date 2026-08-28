# Day 2 : 30 Days of python programming
from itertools import product

#Exercice 1
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
a,b,c = 1,2,3


#Exercice 2

dico = [prenom,nom,nom_complet,pays,ville,age,annee,est_marie,est_vrai,is_light_on,a,b,c]

for i in dico:
    print(type(i))

print("La longueur de ton prenom est de :",len(prenom))

if len(prenom) > len(nom):
    print("Ton prenom est plus long que ton nom")
else:
    print("Ton nom est plus long que ton prenom")

num_one,num_two = 5,4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_div = num_one // num_two

area_of_circle = (30**2)*3.1415
circum_of_circle = 2*3.1415*30

rayon_user = int(input("Quel est le rayon de votre cercle : "))
print((rayon_user**2)*3,1415)

prenom_user = input("Quel est votre prenom : ")
nom_user = input("Quel est votre nom : ")
age_user = int(input("Quel est votre age : "))
pays_user = input("Quel est votre pays : ")

help('keywords')