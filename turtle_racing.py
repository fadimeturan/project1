import turtle
import time
import random

width, height = 500, 500
COLORS= ["red", "blue", "black", "pink", "purple", "green", "yellow", "gray", "brown", "orange"]


def set_screen():
    screen= turtle.Screen()
    screen.setup(width, height)
    screen.title("Turtle Racing!")

def turtle_number():

    while True:
    
        racers = input("Enter the number of turtle (2 - 10): ")
        if racers.isdigit():
            racers= int(racers)
        else:
           print("Input is not numeric. Try again!")
           continue

        if 2<= racers <=10:
            return racers
        else:
            print("Number is not valid.")

def create_turtles(colors):
    turtles= []
    spacing_turtles= width// (len(colors) +1)
    for i, color in enumerate(colors):         #ENUMERATE HEM INDEXE HEM DEĞERE ULAŞMAK İÇİN
        racer= turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-width//2 + (i+1) * spacing_turtles, -height//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def choose_color(colors):
    turtles= create_turtles(colors)

    while True:
        for racer in turtles:
            distance= random.randrange(1,20)
            racer.forward(distance)

            x, y= racer.pos()
            if y> height//2 -10:
                return colors[turtles.index(racer)]


racers= turtle_number()
set_screen()

random.shuffle(COLORS)
colors= COLORS[:racers]


winner= choose_color(colors)
print("The winner is", winner,".")
time.sleep(5)

"""racer= turtle.Turtle()
racer.speed(6)
racer.shape("turtle")
racer.forward(100)
racer.left(90)
racer.forward(100)
racer.left(90)
time.sleep(30)"""