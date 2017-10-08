from random import randint, seed

#Initialisation
print("Bienvenue au Blackjack")
graine = int(input("Entrez la graine : "))
seed(graine)
argent = int(input("Veuillez entrer la quantité d'argent en votre possession : "))
poursuivre = 1
card_type = ["as", 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi"]
card_value = [11, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 10, 10, 10]

while poursuivre == 1:      #Boucle pour rejouer
    points_player, points_bank, nb_card_player, nb_card_bank= 0, 0, 0, 0       #Reset
    replay = 1              #Reset
    card_as = 0             #Reset
    mise = int(input("Veuillez entrer votre mise (vous avez : " + str(argent) + ") : "))
    while replay == 1:      #Boucle pour piocher les cartes
        card = randint(1, 13)
        nb_card_player += 1
        print("La carte tirée est : " + str(card_type[card-1]))
        if card == 1:       #La carte as vaut 1 ou 11 points
            card_as += 1
        else:
            points_player += card_value[card-1]
        if points_player + card_as > 21:        #Le plus petite valeur d'une carte as est 1
            print("Vous avez sauté")
            argent -= mise
            replay = 0
        else:
            replay = int(input("Souhaitez-vous une carte ? (1: oui, 2: non) "))
    if card_as >= 1:        #Calcul de la valeur de la ou des carte(s) as
        if points_player + 11 + card_as - 1 <= 21:  #Au maximum 1 carte as qui vaut 11
            points_player += 11 + card_as - 1
        else:
            points_player += card_as
    if points_player <= 21:
        card_as = 0         #Reset
        print("Vous avez obtenu " + str(points_player) + " points")
        print("La banque joue :")   #La banque commence à jouer
        while points_bank < 17:     #La banque ne joue que si elle a strictement moins de 17 points
            card = randint(1, 13)
            print("La carte tirée est : " + str(card_type[card-1]))
            nb_card_bank += 1
            if card == 1:
                card_as += 1
            else:
                points_bank += card_value[card-1]
        if card_as >= 1:        #Calcul de la valeur de la ou des carte(s) as
            if points_bank + 11 + card_as - 1 <= 21:  #Au maximum 1 carte as qui vaut 11
                points_bank += 11 + card_as - 1
            else:
                points_bank += card_as
        if points_bank > 21:        #Vérifier si c'est le joueur ou la banque qui a le plus de points
            print("La banque a sauté")
            print("Vous gagnez " + str(mise))
            argent += mise
        elif points_bank == points_player:
            print("La banque a obtenu " + str(points_bank) + " points")
            #if points_bank == 21:
            #TODO
            
        elif points_player > points_bank:
            print("La banque a obtenu " + str(points_bank) + " points")
            print("Vous gagnez " + str(mise))
            argent += mise
        else:
            print("La banque a obtenu " + str(points_bank) + " points")
            print("La banque gagne")
            argent -= mise
    print()  
    poursuivre = int(input("Souhaitez-vous jouer une autre partie ? (1: oui, 2: non) "))

