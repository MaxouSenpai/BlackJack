from random import randint, seed

"""
Ce programme est une version simplifiée pour un seul joueur du célèbre jeu de casino, le BlackJack
Le joueur affronte la banque jouée par l'ordinateur
Le but du jeu est d'avoir plus de points que la banque tout en ne dépassant pas 21 points
La carte As vaut 1 ou 11 points(choisit automatiquement en favorisant celui qui l'a obtenu)
Les cartes de 2 à 10 vallent la valeur faciale de la carte (le 2 vaut 2 points etc)
Les cartes "Valet", "Dame" et "Roi" valent chacune 10 points
Pour jouer il suffit de suivre les instructions affichées a l'écran
"""

def as_value(points, nb_as):
    """
    Cette fonction calcule la valeur de la ou des cartes "As"
    Elle prend en entrée les points ainsi que le nombre de cartes "As" obtenus
    Elle renvoie le nombre de points à ajouter
    """
    if points + 11 + nb_as - 1 <= 21:  #Au maximum 1 carte as qui vaut 11
        points_to_add = 11 + nb_as - 1
    else:
        points_to_add = nb_as
    return points_to_add
    
#Initialisation
print("Bienvenue au Blackjack")
graine = int(input("Entrez la graine : "))
seed(graine)
money = int(input("Veuillez entrer la quantité d'argent en votre possession : "))
poursuivre = 1
card_type = [0, "as", 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi"]   #Rajout d'une valeur (0) au début pour faire directement correspondre la carte à son indice
card_value = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 10, 10, 10]                 #Exemple : Carte 2 correspond à l'indice 2

while poursuivre == 1:      #Boucle pour rejouer
    points_player, points_bank, nb_card_player, nb_card_bank= 0, 0, 0, 0       #Reset
    repiocher, card_as = 1,0             #Reset
    mise = int(input("Veuillez entrer votre mise (vous avez : " + str(money) + ") : "))
    while repiocher == 1:      #Tour du joueur
        card = randint(1, 13)
        nb_card_player += 1
        print("La carte tirée est : " + str(card_type[card]))
        if card == 1:       #Permet de compter les cartes "as", les points des cartes "as" sont ajoutés après
            card_as += 1
        else:
            points_player += card_value[card]
        if points_player + card_as > 21:        #Le plus petite valeur d'une carte as est 1
            print("Vous avez sauté")
            money -= mise
            repiocher = 0
        else:
            repiocher = int(input("Souhaitez-vous une carte ? (1: oui, 2: non) ")) #Demande si on veut piocher une autre carte
    if card_as >= 1:        #Calcul de la valeur de la ou des carte(s) as
        points_player += as_value(points_player, card_as)
    if points_player <= 21:
        card_as, repiocher = 0, 1   #Reset
        print("Vous avez obtenu " + str(points_player) + " points")
        print("La banque joue :")   #La banque commence à jouer
        while points_bank + card_as < 17 and repiocher == 1:     #La banque ne joue que si elle a strictement moins de 17 points
            card = randint(1, 13)
            print("La carte tirée est : " + str(card_type[card]))
            nb_card_bank += 1
            if card == 1:
                card_as += 1
            else:
                points_bank += card_value[card]
            potential_points = points_bank + as_value(points_bank, card_as)
            if card_as >= 1 and potential_points < 17 and potential_points >= 21:
                repiocher = 0
        if card_as >= 1:        #Calcul de la valeur de la ou des carte(s) as
            points_bank += as_value(points_bank, card_as)
        if points_bank > 21:        #Vérifier si c'est le joueur ou la banque qui a le plus de points
            print("La banque a sauté")
            print("Vous gagnez " + str(mise))
            money += mise
        elif points_bank == points_player:
            print("La banque a obtenu " + str(points_bank) + " points")
            if points_bank == 21:   #Verifie si un des deux ou les deux ont obtenu un BlackJack (Un as + une carte valant 10)
                if nb_card_player == 2 and nb_card_bank > 2:
                    print("Vous gagnez " + str(mise))
                    money += mise
                elif nb_card_bank == 2 and nb_card_player > 2:
                    print("La banque gagne")
                    money -= mise
                else:
                    print("Égalité")
            else:
                print("Égalité")
        elif points_player > points_bank:
            print("La banque a obtenu " + str(points_bank) + " points")
            print("Vous gagnez " + str(mise))
            money += mise
        else:
            print("La banque a obtenu " + str(points_bank) + " points")
            print("La banque gagne")
            money -= mise
    print()
    poursuivre = int(input("Souhaitez-vous jouer une autre partie ? (1: oui, 2: non) "))
