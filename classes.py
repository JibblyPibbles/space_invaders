from turtle import *
from random import *

PLAYER_MOVE_DIST = 20


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.color('white')
        self.penup()
        self.setx(0)
        self.sety(-260)

    def move_right(self):
        self.forward(PLAYER_MOVE_DIST)

    def move_left(self):
        self.back(PLAYER_MOVE_DIST)



class Laser(Turtle):
    def __init__(self):
        super(Laser, self).__init__()
        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.color('red')
        self.shape('square')
        self.tracking = True
        self.shapesize(stretch_len=1, stretch_wid=0.2)

    def fire(self):
        self.showturtle()
        self.forward(20)

#Columns (9)
COLUMNS = [-300, -225, -150, -75, 0, 75, 150, 225, 300]

#Rows (7)
ROWS = [250, 190, 140, 90, 40, -10, -60]

ALIEN_MOVE_DIST = 1

#Colors,points,  rows == (1 elite, 1 vet, 2 skirmisher, 3 grunt)
ALIEN_CATEGORIES = {'elite': {'color': 'purple',
                              'points': 50},
                    'veteran': {'color': 'blue',
                                'points': 30},
                    'skirmisher': {'color': 'green',
                                   'points': 20},
                    'grunt': {'color': 'red',
                              'points': 10}
                    }

class AlienShipManager():
    def __init__(self):
        self.all_ships = []
        self.killed_ships = []
        self.ship_speed = ALIEN_MOVE_DIST
        self.direction = 'right'

    #create a 7x9 matrix of ships, with four different categories
    def create_aliens(self):
        for r in range(len(ROWS)):
            for c in range(len(COLUMNS)):
                new_ship = Turtle('square')
                self.all_ships.append(new_ship)
                new_ship.penup()
                new_ship.type = ''
                new_ship.dead = False
                #elites
                if r == 0:
                    new_ship.color(ALIEN_CATEGORIES['elite']['color'])
                    new_ship.points = ALIEN_CATEGORIES['elite']['points']
                    new_ship.type = 'elite'
                #veterans
                elif r == 1:
                    new_ship.color(ALIEN_CATEGORIES['veteran']['color'])
                    new_ship.points = ALIEN_CATEGORIES['veteran']['points']
                    new_ship.type = 'veteran'
                #skirmishers
                elif r == 2 or r == 3:
                    new_ship.color(ALIEN_CATEGORIES['skirmisher']['color'])
                    new_ship.points = ALIEN_CATEGORIES['skirmisher']['points']
                    new_ship.type = 'skirmisher'
                #grunts
                elif r > 3:
                    new_ship.color(ALIEN_CATEGORIES['grunt']['color'])
                    new_ship.points = ALIEN_CATEGORIES['grunt']['points']
                    new_ship.type = 'grunt'
                #place ship in location
                new_ship.goto(COLUMNS[c], ROWS[r])

    def identify_killed_ship(self):
        for ship in self.all_ships:
            # print(ship.is_killed)
            if ship.dead == True:
                ship.hideturtle()
                self.killed_ships.append(ship)
                self.all_ships.pop(self.all_ships.index(ship))
            else:
                pass


    def move_all_right(self):
        if self.direction == 'right':
            for ship in self.all_ships:
                ship.forward(self.ship_speed)
        else:
            pass

    def move_all_left(self):
        if self.direction == 'left':
            for ship in self.all_ships:
                ship.back(self.ship_speed)
        else:
            pass

    def move_all_down(self):
        if self.direction == 'down':
            for ship in self.all_ships:
                ship.sety(ship.ycor() - 10)
            self.direction = ''

    def change_direction(self):
        #ships change from right to left
        for ship in self.all_ships:
            if ship.xcor() > 360:
                self.direction = 'down'
                self.move_all_down()
                self.direction = 'left'
                self.move_all_left()
            elif ship.xcor() < -360:
                self.direction = 'down'
                self.move_all_down()
                self.direction = 'right'
                self.move_all_right()
            else:
                pass

class AlienLaserManager():
    def __init__(self):
        self.all_lasers = []
        self.laser_speed = 10

    def create_alien_laser(self, xcor, ycor):
        for x in range(5):
            new_laser = Turtle()
            new_laser.hideturtle()
            new_laser.penup()
            new_laser.goto(xcor, ycor)
            new_laser.setheading(270)
            new_laser.color('orange')
            new_laser.shape('square')
            new_laser.tracking = True
            new_laser.shapesize(stretch_len=2, stretch_wid=0.2)
            self.all_lasers.append(new_laser)

    def fire_alien_laser(self):
        for laser in self.all_lasers:
            if laser.tracking == True:
                pass
            else:
                laser.showturtle()
                laser.forward(self.laser_speed)

    def reset_laser(self):
        for laser in self.all_lasers:
            if laser.ycor() < -310:
                laser.tracking = True
                laser.forward(0)



