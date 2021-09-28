import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = 10


def poser_question():
    nombre_aleatoire_a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nombre_aleatoire_b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)
    operateur = "+"
    if o == 1:
        calcul = nombre_aleatoire_a * nombre_aleatoire_b
        operateur = "x"
    else:
        calcul = nombre_aleatoire_a + nombre_aleatoire_b
        operateur = "+"

    # 0 -> +
    # 1 -> *
    print(f"Calculer : {nombre_aleatoire_a} {operateur} {nombre_aleatoire_b}")
    reponse_utilisateur = input("Quel est le résultat de cette opération?")
    reponse_utilisateur_int = int(reponse_utilisateur)
    resultat = calcul
    if reponse_utilisateur_int == resultat:
        return True
    return False


nb_points = 0


for i in range(0, NB_QUESTION):
    print(f"Question {i+1} sur {NB_QUESTION}")
    point_gagne = poser_question()
    print()
    if point_gagne:
        print("Bravo c'est la bonne réponse")
        nb_points += 1
    else:
        print(f"Erreur, ce n'est pas la bonne réponse")

print(f"votre note est :  {nb_points} / {NB_QUESTION}")
moyenne = int(NB_QUESTION/2)
if nb_points == NB_QUESTION:
    print("Excellent!")
elif nb_points == 0:
    print("Révisez vos maths")
elif nb_points < moyenne:
    print("Peut mieux faire")
elif nb_points > moyenne:
    print("Pas mal")
else:
    print("juste la moyenne")
