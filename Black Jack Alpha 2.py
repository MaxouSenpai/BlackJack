""" Black Jack version alpha 2 """
""" 1 o'clock """
""" 4th october 2017 """
from random import randint, seed


print("Bienvenue au Blackjack")
graine=int(input("Entrez la graine : "))
seed(graine)
argent = int(input("Veuillez entrer la quantité d'argent en votre possession : "))
poursuivre = 1
card_type = ["as", 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi"]
card_value = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 10, 10, 10]


while poursuivre == 1:
    points_player = 0
    points_bank = 0
    replay = 1
    mise = int(input("Veuillez entrer votre mise (vous avez : " + str(argent) + ") : "))
    while replay == 1:
        card = randint(1, 13)
        print("La carte tirée est : " + str(card_type[card-1]))
        if card == 1:
             points_player += int(input())
        else:
            points_player += card_value[card-1]
        if points_player > 21:
            print("Vous avez sauté")
            argent -= mise
            replay = 0
        else:
            replay = int(input("Souhaitez-vous une carte ? (1: oui, 2: non) "))
    if points_player <= 21:
        print("Vous avez obtenu " + str(points_player) + " points")
        print("La banque joue :")
        while points_bank < 17:
            card = randint(1, 13)
            print("La carte tirée est : " + str(card_type[card-1]))
            points_bank += card_value[card-1]
        print("La banque a obtenu " + str(points_bank) + " points")
        if points_bank > 21:
            print("La banque a sauté")
            print("Vous gagnez " + str(mise) + " points")
            argent += mise
        elif points_bank == points_player:
            print("Égalité")
        elif points_player > points_bank:
            print("Vous gagnez " + str(mise))
            argent += mise
        else:
            print("La banque gagne")
            argent -= mise
    print()  
    poursuivre = int(input("Souhaitez-vous jouer une autre partie ? (1: oui, 2: non) "))
