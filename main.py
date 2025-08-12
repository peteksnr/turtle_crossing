import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_cars()
    car_manager.move()

    # level up
    if player.ycor() > 280:
        scoreboard.update_level()
        car_manager.increase_speed()
        player.goto(0, -280)

    # collision with the cars
    for car in car_manager.cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
