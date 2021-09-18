import random
import turtle

SYMBOLS = {
    "C": "♣",
    "D": "♦",
    "H": "♥",
    "S": "♠"
}
STANDARD_NAMES = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

window = turtle.Screen()
window.bgcolor("black")
window.setup(800, 600)
window.title("Standard Deck of Card Simulator")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


class Card:
    def __init__(self, name, suit, color):
        self.name = name
        self.suit = suit
        self.color = color

    def print_card(self):
        """
        Method is used to print the cards.
        :return: None
        """
        print(self.name, self.suit)

    def render(self, x, y, pen):
        """
        Methods is used to render card on the screen.
        :param x: axis of the x for card
        :param y: axis ot the y for card
        :param pen: pass the turtle object to draw
        :return: None
        """
        pen.penup()
        pen.goto(x, y)
        pen.color("white")
        pen.goto(x - 50, y + 75)
        pen.begin_fill()
        pen.pendown()
        pen.goto(x + 50, y + 75)
        pen.goto(x + 50, y - 75)
        pen.goto(x - 50, y - 75)
        pen.goto(x - 50, y + 75)
        pen.end_fill()
        pen.penup()

        # Draw suit in the middle
        pen.color(self.color)
        pen.goto(x - 18, y - 30)
        pen.write(SYMBOLS[self.suit], False, font=("Courier New", 48, "normal"))

        # Draw top left
        pen.goto(x - 40, y + 45)
        pen.write(self.name, False, font=("Courier New", 18, "normal"))
        pen.goto(x - 40, y + 25)
        pen.write(SYMBOLS[self.suit], False, font=("Courier New", 18, "normal"))

        # Draw bottom right
        pen.goto(x + 30, y - 60)
        pen.write(self.name, False, font=("Courier New", 18, "normal"))
        pen.goto(x + 30, y - 80)
        pen.write(SYMBOLS[self.suit], False, font=("Courier New", 18, "normal"))


class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["D", "C", "H", "S"]
        self.set_card()

    def set_card(self):
        """
        Method is used to set or reset all the card in the deck.
        :return: None
        """
        for name in STANDARD_NAMES:
            for suit in self.suits:
                color = "red" if suit in ["D", "H"] else "black"
                card = Card(name, suit, color)
                self.cards.append(card)
        self.shuffle()

    def shuffle(self):
        """
        To shuffle the cards we used this method.
        :return: None
        """
        random.shuffle(self.cards)

    def get_card(self):
        """
        For get a single card from the deck.
        :return: None
        """
        card = self.cards.pop()
        return card


# create deck
deck = Deck()

# shuffle deck
deck.shuffle()

# render the 5 cards.
for i in range(5):
    card = deck.get_card()
    card.render(-250 + i * 125, 0, pen)

window.mainloop()
