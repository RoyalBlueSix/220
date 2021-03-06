"""
Name: Sean Faust
Lab4.py

Problem: This lab has me using the graphics library to create a valentines day card using a multitude
of functions and has me using the time.sleep function within python to make an arrow seemingly fly across the
screen.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

def greeting_card():
    # Setting up the Window
    height = 400
    width = 400
    win = GraphWin("GREETINGS!", width, height)
    win.setBackground("Pink")
    # Creating the Heart
    heart = Polygon(Point(200, 170), Point(230, 150), Point(260, 140), Point(280, 150), Point(300, 170),
                   Point(305, 200), Point(295, 235), Point(270, 260), Point(260, 280), Point(200, 370),
                    Point(140, 280), Point(130, 260), Point(105, 235), Point(95, 200), Point(100, 170),
                    Point(120, 150), Point(140, 140), Point(170, 150), Point(200, 170))
    heart.setOutline("Red")
    heart.setFill("Red")
    heart.draw(win)
    # Creating the text on the card
    card_text = Text(Point(200, 50), "Nothing quite as Sweet as you.")
    card_text.setTextColor("Red")
    card_text.draw(win)
    # Creating the arrow. I'm bad at drawing this way.
    arrow = Polygon(Point(5, 5), Point(3, 10), Point(50, 60), Point(40, 70), Point(75, 85),
                    Point(65, 45), Point(53, 55), Point(5, 5))
    arrow.setFill("Black")
    arrow.draw(win)
    # Creating the loop to make the arrow fly across the screen.
    for i in range(20):
        time.sleep(0.1)
        arrow.move(15, 15)
    # Making the text to let the user know they can click the window to close the program.
    close_txt = Text(Point(200, 200), "Click to Close")
    close_txt.draw(win)
    # Allowing the screen to stay up until the user wants to close it themselves with a mouse click.
    win.getMouse()
    win.close()