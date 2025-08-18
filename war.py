from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title('War Card Game')
root.geometry("900x550")
root.configure(background="black")

# Resize cards
def resize_cards(card):
    our_card_img = Image.open(card)

    our_card_resize_img = our_card_img.resize((150, 210))

    global our_card_image
    our_card_img = ImageTk.PhotoImage(our_card_resize_img)

    return our_card_img

# Shuffle Cards
def shuffle():
    # Define deck
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)
    # 11 = Jack, 12 = Queen, 13 = King, 14 = Ace

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    # create our players
    global dealer, player, dscore, pscore
    dealer = []
    player = []
    dscore = []
    pscore = []

    # Grab random card for Dealer
    dealer_card = random.choice(deck)
    deck.remove(dealer_card)
    dealer.append(dealer_card)

    # output to screen
    global dealer_image
    dealer_image = resize_cards(f'images/cards/{dealer_card}.png')
    dealer_label.config(image=dealer_image)

    # Grab random card for Player
    player_card = random.choice(deck)
    deck.remove(player_card)
    player.append(player_card)

    # output to screen
    global player_image
    player_image = resize_cards(f'images/cards/{player_card}.png')
    player_label.config(image=player_image)

    # player_label.config(text=card)

    # put number of remaining cards in title bar
    root.title(f'War - {len(deck)} Cards Left')

    # total score
    score(dealer_card, player_card)

# Deal Cards
def deal_cards():
    try:
        # get Dealer Card
        dealer_card = random.choice(deck)
        deck.remove(dealer_card)
        dealer.append(dealer_card)

        # output to screen
        global dealer_image
        dealer_image = resize_cards(f'images/cards/{dealer_card}.png')
        dealer_label.config(image=dealer_image)
        #dealer_label.config(text=card)

        # get Player Card
        player_card = random.choice(deck)
        deck.remove(player_card)
        player.append(player_card)

        # output to screen
        global player_image
        player_image = resize_cards(f'images/cards/{player_card}.png')
        player_label.config(image=player_image)
        #player_label.config(text=card)

        # put number of cards remaining into title bar
        root.title(f'War - {len(deck)} Cards Left')

        # get the score
        score(dealer_card, player_card)

    except:
        # Tie
        if dscore.count("x") == pscore.count("x"):
            root.title(f'War - Game Over! Tie! {dscore.count("x")} to {pscore.count("x")}')
        # Dealer Wins
        elif dscore.count("x") > pscore.count("x"):
            root.title(f'War - Game Over! Dealer Wins! {dscore.count("x")} to {pscore.count("x")}')
        # Player Wins
        else:
            root.title(f'War - Game Over! Player Wins! {pscore.count("x")} to {dscore.count("x")}')

def score(dealer_card, player_card):
    # Split card numbers
    dealer_card = int(dealer_card.split("_", 1)[0])
    player_card = int(player_card.split("_", 1)[0])

    # compare card numbers
    if dealer_card == player_card:
        score_label.config(text="Tie! Play Again!")

    elif dealer_card > player_card:
        score_label.config("Dealer Wins!")
        dscore.append("x")
    else:
        score_label.config(text="Player Wins!")
        pscore.append("x")

    root.title(f'War - {len(deck)} Cards Left | Dealer: {dscore.count("x")} Player: {pscore.count("x")}')

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Create frames for cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

# put cards in frames
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

# Create Score Label
score_label = Label(root, text="", font=("helvetica", 14), bg="green")
score_label.pack(pady=20)

#Buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root, text="Draw Card", font=("Helvetica", 14), command=deal_cards)
card_button.pack(pady=20)

# Shuffle deck on start
shuffle()

root.mainloop()