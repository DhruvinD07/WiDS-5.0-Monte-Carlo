from tkinter import Tk, Canvas, Button, Label
from PIL import Image, ImageTk
import os
from blackjack import BlackJack

# ---------------------------
# 1. Initialize Tkinter root
# ---------------------------
root = Tk()
root.title("Blackjack")
root.geometry("800x600")

# ---------------------------
# 2. Load card images
# ---------------------------
image_folder = "images"
card_images = {}  # (rank_name, suit) -> PhotoImage

rank_map = {"A": "ace", "J": "jack", "Q": "queen", "K": "king"}

for suit in ["hearts", "spades", "diamonds", "clubs"]:
    for rank in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
        rank_name = rank_map.get(rank, rank).lower()
        file_path = os.path.join(image_folder, f"{rank_name}_of_{suit}.png")
        img = Image.open(file_path)
        img = img.resize((80, 120), Image.LANCZOS)
        card_images[(rank_name, suit)] = ImageTk.PhotoImage(img)

# Back of card
back_img = Image.open(os.path.join(image_folder, "blank.png"))
back_img = back_img.resize((80, 120), Image.LANCZOS)
back_card = ImageTk.PhotoImage(back_img)

# ---------------------------
# 3. Create canvas widgets
# ---------------------------
player_canvas = Canvas(root, width=800, height=200, bg="green")
player_canvas.pack(side="bottom")

dealer_canvas = Canvas(root, width=800, height=200, bg="green")
dealer_canvas.pack(side="top")

# ---------------------------
# 4. Initialize game
# ---------------------------
game = BlackJack()
game.start_round()

# ---------------------------
# 5. Status label
# ---------------------------
status_label = Label(root, text="", font=("Arial", 16))
status_label.pack(pady=10)

# ---------------------------
# 6. Keep references to images
# ---------------------------
canvas_images = {"player": [], "dealer": []}

# ---------------------------
# 7. Draw hand function
# ---------------------------
def draw_hand(canvas, hand, hidden=False, who="player"):
    canvas.delete("all")
    canvas_images[who].clear()
    x_offset = 20
    for i, card in enumerate(hand.cards):
        if hidden and i == 0:
            img = back_card
        else:
            rank_name = rank_map.get(card.rank, card.rank).lower()
            key = (rank_name, card.suit.name.lower())
            img = card_images[key]
        canvas.create_image(x_offset, 20, image=img, anchor="nw")
        canvas_images[who].append(img)  # keep reference
        x_offset += 100

# ---------------------------
# 8. Winner check
# ---------------------------
def check_winner():
    if game.round_over:
        status_label.config(text=f"Winner: {game.winner}")

# ---------------------------
# 9. Button callbacks
# ---------------------------
def hit():
    if game.round_over:
        return
    game.player_hit()
    draw_hand(player_canvas, game.player_hand, who="player")
    draw_hand(dealer_canvas, game.dealer_hand, hidden=True, who="dealer")
    check_winner()

def stand():
    if game.round_over:
        return
    game.player_stand()
    draw_hand(player_canvas, game.player_hand, who="player")
    draw_hand(dealer_canvas, game.dealer_hand, who="dealer")
    check_winner()

hit_button = Button(root, text="Hit", command=hit, width=10)
hit_button.pack(side="left", padx=20, pady=10)

stand_button = Button(root, text="Stand", command=stand, width=10)
stand_button.pack(side="right", padx=20, pady=10)

# ---------------------------
# 10. Start GUI after mainloop
# ---------------------------
def start_game():
    draw_hand(player_canvas, game.player_hand, who="player")
    draw_hand(dealer_canvas, game.dealer_hand, hidden=True, who="dealer")

root.after(100, start_game)  # wait 100ms for GUI to initialize
root.mainloop()
