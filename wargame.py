#!/usr/bin/python3
import random
#This program plays the card game War. By default, the game will run automatically. For the masochists, manually drawing each round is possible if line 79 is uncommented.

#This function will create a new deck of cards and their values, stored in a dictionary.
def create_deck():
    cards = {"AH":14, "AS":14, "AD":14, "AC":14, \
        "KH":13,"KS":13,"KD":13,"KC":13, \
        "QH":12,"QS":12,"QD":12,"QC":12, \
        "JH":11,"JS":11,"JD":11,"JC":11, \
        "10H":10,"10S":10,"10D":10,"10C":10, \
        "9H":9,"9S":9,"9D":9,"9C":9, \
        "8H":8,"8S":8,"8D":8,"8C":8, \
        "7H":7,"7S":7,"7D":7,"7C":7, \
        "6H":6,"6S":6,"6D":6,"6C":6, \
        "5H":5,"5S":5,"5D":5,"5C":5, \
        "4H":4,"4S":4,"4D":4,"4C":4, \
        "3H":3,"3S":3,"3D":3,"3C":3, \
        "2H":2,"2S":2,"2D":2,"2C":2}
    
    return cards



#Function to shuffle a given deck of cards using random.sample(). Returns a list - card values are still obtained from the dictionary created with create_deck().
def shuffle_deck(deck):
    shuffled_cards = random.sample(deck.keys(),52)
    return shuffled_cards


#Initialization for the card game. A deck of cards is first created using create_deck(). A list of shuffled cards is then obtained using shuffle_deck().
#The decks for both players are then created by slicing the shuffled card list. NOTE: names of variables and functions reference a computer player, which should be
#considered synonymous with Player 2.
def init():
    global game_deck, shuffled, player_deck, computer_deck
    game_deck = create_deck()
    shuffled = shuffle_deck(game_deck)
    player_deck = shuffled[26:]
    computer_deck = shuffled[:26]

#Function to compare the values of two cards. Accesses the global variable game_deck (created above) to determine card values. Returns "Player 1" if Player 1 has the higher card,
#"Player 2" if Player 2 has the higher card, and None if the cards are tied in value.
def compare(card1,card2):
    global game_deck
    #print(card1,card2)
    if (game_deck[card1] > game_deck[card2]):
        return "Player 1"
    elif (game_deck[card2] > game_deck[card1]):
        return "Player 2"
#Draws a card from Player 1's deck. Uses the global variable player_deck (created above). A check is first made to ensure that there are available cards to draw. If so, a variable card
#is created and set equal to the item at the first location in the player_deck list. This item is then removed from the player's deck. The variable card is returned.
def player_draw():
    global player_deck
    if (len(player_deck) > 0):
        card = player_deck[0]
        del(player_deck[0])
        return card

#Draws a card from Player 2's deck. Uses the global variable computer_deck (created above). A check is first made to ensure that there are available cards to draw. If so, a variable card
#is created and set equal to the item at the first location in the computer_deck list. This item is then removed from Player 2's deck. The variable card is returned.
def computer_draw():
    global computer_deck
    if (len(computer_deck) > 0):
        card = computer_deck[0]
        del(computer_deck[0])
        return card
#Main game logic. The variable playing is created and set to True - this allows gameplay to loop. A variable win_pile is created and set to an empty list.
#While the game is being played (playing = True), the program runs through a number of checks to maintain the flow of the game.
#The program first checks if there are cards in both players' decks. If so, it creates two variables, card1 and card2, obtained by drawing a card from each player's deck (player_draw() and
#computer_draw()). These cards are then added to the win_pile list (the pot). Win_pile is randomized using random.shuffle().

#If the initial check fails, the program determines which player has no cards in their deck. Victory is then declared for the opposing party.
def play_round():
    global player_deck, computer_deck
    playing = True
    win_pile = []

    while playing:
        #playit = input("Press any key to draw the next round...")
        if (len(player_deck)>0 and len(computer_deck) >0):
            card1 = player_draw()
            card2 = computer_draw()
            print("Player 1 plays: " + card1)
            print("Player 2 plays: " + card2)
            win_pile.append(card1)
            win_pile.append(card2)
            random.shuffle(win_pile)
        elif (len(player_deck) == 0):
            print("Player 2 has won the game!")
            break
        elif(len(computer_deck) == 0):
            print("Player 1 has won the game!")
            break
#If the initial check succeeds and cards have been added to the win pile, the game proceeds. A variable result is created and set equal to the comparison of card1 and card2 (compare(card1,card2)).
#The program checks result for an identified winner. If there is one (i.e. result is equal to "Player 1" or "Player 2"), the cards in win_pile are added to the end of the winner's deck list. The win pile
#is then reset to an empty list. Using the continue statement, the program returns to the top of the playing loop and continues the game. 
        result = compare(card1,card2)
        if(result == "Player 1"):
            print("Player 1 wins!")
            player_deck.extend(win_pile)
            #print(len(player_deck),len(computer_deck))
            win_pile = []
            continue
        elif(result == "Player 2"):
            print("Player 2 wins!")
            computer_deck.extend(win_pile)
            #print(len(player_deck),len(computer_deck))
            win_pile = []
            continue
#If a winner is not identified by result (i.e. result = None), the program executes special rules for a tie hand (War!). The program first checks for available cards in each player's deck - in this version of War,
#drawing a tie with your last card is an automatic loss. If both players have the minimum number of cards needed (2) for War!, the tie round proceeds.
#A card is drawn from each player's deck and added to the win pile, which now holds four cards. The program continues to the top of the playing loop, where two cards are drawn and compared as normal. 
#The win pile is not reset until a comparison is made, so the winner of one tie will add six cards to their deck.
        
#NOTE: tie rounds where a player has two cards are resolved in the very next draw, with the winner again taking all cards in the win pile.
        elif(result == None):
            print("WAR!!!!!!!")
            if(len(player_deck) >= 2 and len(computer_deck) >= 2):
                card3 = player_draw()
                card4 = computer_draw()
                win_pile.append(card3)
                win_pile.append(card4)
                continue
            
        

#main function, allowing init() and play_round() to be executed automatically when the program is run. play_it allows the user to start the game with a key press, and the user can choose to init and start a new game once one finishes.
if __name__ == '__main__':
    play_it = input("Press any key to begin a game of War...")
    while True:
        init()
        play_round()
        retry = input("Play again? Enter 'yes' or 'no.'")
        if(retry == "yes"):
            continue
        else:
            break









