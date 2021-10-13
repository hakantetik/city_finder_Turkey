import turtle

import pandas

screen = turtle.Screen()
screen.setup(width=1409, height=749)
screen.title("Vilayet bulma oyunu")
image = "harita.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("konumlar.csv")
all_cities = data.iller.to_list()
guessed_cities = []
cities_missed = []

while len(guessed_cities) < 81:
    answer = turtle.textinput(title=f"City Finder Turkey ({len(guessed_cities)}/81)", prompt="Your guess?").title()
    if answer == "Exit":
        for city in all_cities:
            if city not in guessed_cities:
                cities_missed.append(city)
            df = pandas.DataFrame(cities_missed)
            # noinspection PyTypeChecker
            df.to_csv("missed_cities")
        break
    if answer in all_cities:
        answer_city = data[data.iller == answer]
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.goto(int(answer_city.x), int(answer_city.y))
        text.write(answer, font=("Arial", 12, "normal"))
        guessed_cities.append(answer)
