import random

#function to pick 21 random cards
def getCards():
    suits=['♥','♣','♠','♦']
    values= ['Ace','Two','Three',"Four",'Five','Six','Seven','Eight','Nine',
             'Ten','Jack','Queen','King']
    cards=[]
    while(len(cards)<21):
        Suit = random.choice(suits)
        Value = random.choice(values)
        Card =Value + " of " + Suit
        if not (Card in cards):
            cards.append(Card)
    return cards
	
# function to display the three decks of cards
def showCards(a,b,c):
    print("Pile 1: ", a)
    print("Pile 2: ", b)
    print("Pile 3: ", c)
	
#welcome
print("Welcome to the 21 Card Trick Game")
print("---------------------------------")


# Generate and display list of cards to choose
cards = getCards()
for card in cards:
    print(card)
print()
print("please pick a card from above")
input("Press ENTER once you have picked a card")
print()
for i in range(3):
#create 3 piles of cards
    pile1=[]
    pile2=[]
    pile3=[]
    for i in range(0,21,3):
        pile1.append(cards[0+i])
        pile2.append(cards[1+i])
        pile3.append(cards[2+i])
    showCards(pile1,pile2,pile3)
    validChoice=False
    choice=""
    while(not validChoice):
        choice=input("what pile is your card in?: ")
        if("1" in choice or "2" in choice or "3" in choice):
            validChoice = True
        else:
            print("invalid choice")
            print()

    cards=[]
    if(choice=="1"):
        cards.extend(pile2)
        cards.extend(pile1)
        cards.extend(pile3)
    elif(choice =="2"):
        cards.extend(pile1)
        cards.extend(pile2)
        cards.extend(pile3)
    else:
        cards.extend(pile1)
        cards.extend(pile3)
        cards.extend(pile2)
	
# after three passes, display the middle card.
print()
print("the card you chose was...")
print(cards[10])



