#1 we import any module require for project
import random

#2 creat a class of card which have two options

class Card:
    def __init__(self,rank,shape):
        self.rank = rank
        self.shape = shape

    def __str__(self) -> str:
        return f"{self.rank} of {self.shape}"
    

#3 create a class Deck which contain all the 52 faces of cards

class Deck:
    shapes = ["Diamond", "Cubes", "Spades", "Heart"]
    ranks = ["2", "3","4","5", "6","7","8", "9","Jack","Queen", "King","Ace"]

    def __init__(self,) -> None:
        self.deck = [Card(rank,shape) for rank in Deck.ranks for shape in Deck.shapes]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()
    

#4 Create a Hand class for holding cards.

class Hand:
    def __init__(self) -> None:
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        
        if card.rank in ["Jack", "Queen", "King"]:
            self.value += 10
        
        elif card.rank == "Ace":
            self.value += 11
            self.aces += 1

        else: self.value += int(card.rank)

    def adjust_for_aces(self):
        while self.value >=21 and self.aces:
            self.value -=10
            self.aces -=1

# Defining of chips for players how they can bet
class Chips:
    def __init__(self, total =100) -> None:
        self.bet = 0
        self.total = total

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total-= self.bet

# Lets define some functions which will control the flow of game.

def take_bet(chips):
    while True:
        try:
            print()
            chips.bet = int(input("How many chips do you want to spend: "))
            if chips.bet > chips.total:
                print("You do not hvae enogh chips")
            else:
                break
        
        except ValueError:
            print("Please provide an intger for chips")


def hit(deck,hand):
    hand.add_card(deck.draw())
    hand.adjust_for_aces()


def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")

        if x[0]=="h":
            hit(deck,hand)

        elif x[0] == "s":
            print("Player Stands, Dealer is playing")
            playing = False

        else:
            print("Sorry please try again")
            continue
        break

def show_some(player,dealer):
    print("\nDealers Hand:")
    print("<Card Hidden>")
    print(f"{dealer.cards[1]}")
    print("\nPlayer's Hand:", *player.cards, sep="\n" )


def show_all(player,dealer):
    print("\nDealers Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n" )
    print("Player's Hand", player.value)



def player_bust(player,dealer,chips):
    print("Player busts")
    chips.lose_bet()


def player_win(player,dealer,chips):
    print("Player wins")
    chips.win_bet()


def dealer_win(player,dealer,chips):
    print("Dealer wins")
    chips.lose_bet()


def dealer_bust(player,dealer,chips):
    print("Dealer busts")
    chips.win_bet()


def push(player,dealer):
    print("Dealer and player tie. It's a push.")




if __name__ == "__main__":
    playing = True

    while True:
        print("Welcome to BlackJack!")

        #creating a new deck
        deck = Deck()

        #creating player hand
        player_hand = Hand()
        player_hand.add_card(deck.draw())
        player_hand.add_card(deck.draw())

        #creating dealer hand
        dealer_hand = Hand()
        dealer_hand.add_card(deck.draw())
        dealer_hand.add_card(deck.draw())

        #setting up the player chips

        player_chips = Chips()


        #taking bet

        take_bet(player_chips)

        #show cards but not all

        show_some(player_hand,dealer_hand)

        while playing:

            hit_or_stand(deck,player_hand)
            show_some(player_hand,dealer_hand)
            
            if player_hand.value>21:
                player_bust(player_hand,dealer_hand,player_chips)
            break
        
        if player_hand.value <= 21:
            
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)

            #show all card

            show_all(player_hand, dealer_hand)

            #run different game scenarios.

            if dealer_hand.value > 21:
                dealer_bust(player_hand,dealer_hand,player_chips)
            
            elif dealer_hand.value > player_hand.value:
                dealer_win(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_win(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand,dealer_hand)


        print(f"\nPlayers chips total:{player_chips.total}")

        new_game = input("Do you want to play again. Enter 'y' or 'n'")

        if new_game[0] == 'y':
            playing = True
            continue

        else:
            print("Thanks for playing")
            break

 