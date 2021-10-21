#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input('Enter a value: \n'))
    values.sort()
    num_values = [float(value) for value in values if value.isdigit()]
    str_values = [value for value in values if not value.isdigit()]
    return sorted(num_values) + sorted(str_values)

def anagrams(words: list = None) -> bool:
    sum1 = 0
    sum2 = 0
    bool = False
    if words is None:
        # TODO: demander les mots ici
        mot1 = input('mot1: ')
        mot2 = input('mot2: ')
        words = [mot1, mot2]
    if len(words[0]) == len(words[1]):
        bool = True
        mot1 = sorted(mot1.lower())
        mot2 = sorted(mot2.lower())
        for i in range(len(mot1)):
            if mot1[i] != mot2[i]:
                bool = False
                continue
    print(bool)
    return bool


    print(bool)
    return bool


def contains_doubles(items: list) -> bool:
    if len(items) != len(set(items)):
        return True
    return False

def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    dico = {"Alice": sum(student_grades["Alice"])/len(student_grades["Alice"])}
    if sum(student_grades["Bob"])/len(student_grades["Bob"]) > sum(student_grades["Alice"])/len(student_grades["Alice"]):
        dico = {"Bob": sum(student_grades["Bob"])/len(student_grades["Bob"])}
    return dico


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    phrase = sorted(sentence)
    set_phrase = set(phrase)
    nb_lettre = 1
    dico = {}
    liste = []
    max=0

    for i in range(len(phrase)-1):
        if phrase[i] == phrase[i+1]:
            nb_lettre += 1
        else:
            if nb_lettre > 5:
                liste.append(phrase[i])
                liste.append(nb_lettre)
            nb_lettre = 1
    longueur = len(liste)
    for k in range(longueur//2):
        for j in range(1, len(liste)+1, 2):
            if liste[j] > max:
                max = liste[j]
                cle = liste[j-1]
                index = j
        dico[cle] = max
        max = 0
        liste[index] = 0
        liste[index-1] = 0
    print(dico)
    return dico


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recettes = []
    x = input('entrez 1 pour ecrire un recette: ')
    j = 0
    while ord(x) == ord('1'):
        nom_recette = input('Nom de la recette: ')
        ingredients = input('Entrez les ingredients: ')
        recettes.append(nom_recette)
        recettes.append(ingredients)
        x = input('Entrez 1 pour ecrire une autre recette: ')



def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
