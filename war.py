from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title('War Card Game')
root.geometry("900x550")
root.configure(background="black")

def resize_cards(card):
    our_card_img = Image.open(card)

    our_card_resize_img = our_card_img.resize((150, 210))

    


root.mainloop()