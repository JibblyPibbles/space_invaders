import time
from turtle import *
from time import *
from classes import *
from scoreboard import Scoreboard
import time

current_laser = 0
current_alien_laser = 0
sprite_phase = 0

def run_game():

    def new_game():
        screen.clear()
        run_game()



    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor('black')
    screen.title('Space Invaders')
    screen.tracer(0)

    #initiate player
    screen.register_shape('spaceship.gif')
    player = Player()
    player.shape('spaceship.gif')

    #initiate scoreboard
    scoreboard = Scoreboard()

    screen.register_shape('elite.gif')
    screen.register_shape('veteran.gif')
    screen.register_shape('skirmisher.gif')
    screen.register_shape('grunt.gif')
    screen.register_shape('elite_2.gif')
    screen.register_shape('veteran_2.gif')
    screen.register_shape('skirmisher_2.gif')
    screen.register_shape('grunt_2.gif')
    #initiate alien ships
    ship_manager = AlienShipManager()
    ship_manager.create_aliens()

    alien_laser_manager = AlienLaserManager()



    for ship in ship_manager.all_ships:
        if ship.type == 'elite':
            ship.shape('elite.gif')
        elif ship.type == 'veteran':
            ship.shape('veteran.gif')
        elif ship.type == 'skirmisher':
            ship.shape('skirmisher.gif')
        elif ship.type == 'grunt':
            ship.shape('grunt.gif')

    def change_sprite():
        global sprite_phase
        if sprite_phase == 1:
            for ship in ship_manager.all_ships:
                if ship.type == 'elite':
                    ship.shape('elite_2.gif')
                elif ship.type == 'veteran':
                    ship.shape('veteran_2.gif')
                elif ship.type == 'skirmisher':
                    ship.shape('skirmisher_2.gif')
                elif ship.type == 'grunt':
                    ship.shape('grunt_2.gif')
            sprite_phase = 0
        else:
            for ship in ship_manager.all_ships:
                if ship.type == 'elite':
                    ship.shape('elite.gif')
                elif ship.type == 'veteran':
                    ship.shape('veteran.gif')
                elif ship.type == 'skirmisher':
                    ship.shape('skirmisher.gif')
                elif ship.type == 'grunt':
                    ship.shape('grunt.gif')
            sprite_phase = 1


    clip = []
    for x in range(5):
        laser = Laser()
        clip.append(laser)

    alien_clip = []
    for y in range(5):
        alien_laser = alien_laser_manager.create_alien_laser(0, 0)
        alien_clip.append(alien_laser)

    # def fire_alien_laser():
    #     global current_alien_laser
    #     if current_alien_laser > 5:
    #         current_alien_laser = 0
    #     alien_clip[current_alien_laser].tracking = False
    #     current_alien_laser += 1


    def fire_laser():
        global current_laser
        if current_laser > 4:
            current_laser = 0
        clip[current_laser].tracking = False
        current_laser += 1



    timer = 0
    game_on = True

    while game_on:
        time.sleep(.05)
        screen.update()
        timer += 1
        # print(timer)
        #if game is won
        if len(ship_manager.all_ships) == 0:
            game_on = False
            scoreboard.goto(-100, 0)
            scoreboard.write(f'YOU WON!\nPlay Again?\n("n" for newgame)',
                             font=('Courier', 30, 'bold'))

        if timer % 10 == 0:
            change_sprite()

        ship_manager.move_all_right()
        ship_manager.move_all_left()
        # check for movement change
        ship_manager.change_direction()



        for laser in clip:
            if laser.tracking == True:
                laser.setx(player.xcor())
                laser.sety(player.ycor() + 15)
            elif laser.ycor() > 310 and laser.tracking == False:
                laser.hideturtle()
                laser.tracking = True
            else:
                laser.fire()

        #collisions
        #laser collisions
        #When a laser hits a ship, the ship disappears and is no longer able to
        #be hit by a laser (lasers will pass through and hit ships that aren't dead)
        ship_manager.identify_killed_ship()
        for laser in clip:
            for ship in ship_manager.all_ships:
                if laser.distance(ship) < 25 and ship.dead == False:
                    laser.hideturtle()
                    laser.tracking = True
                    ship.dead = True
                    scoreboard.score += ship.points
                    scoreboard.clear()
                    scoreboard.update_score()
                else:
                    pass

        #if player is hit by alien laser
        for laser in alien_laser_manager.all_lasers:
            if laser.distance(player) < 20:
                game_on = False
                scoreboard.clear()
                scoreboard.goto(-100,-250)
                scoreboard.write(f'GAME OVER\nYour Score Was: {scoreboard.score}\nPlay Again?\n("n" for newgame)',
                                 font=('Courier', 30, 'bold'),
                                 align='center')

        #fire alien lasers and reset
        alien_laser_manager.reset_laser()
        alien_laser_manager.fire_alien_laser()
        random_chance = randint(1, 100)
        if len(ship_manager.all_ships) > 0:
            random_ship = choice(ship_manager.all_ships)
            random_laser = choice(alien_laser_manager.all_lasers)
            for laser in alien_laser_manager.all_lasers:
                if laser.tracking == True:
                    if random_ship.type == 'elite' and random_chance < 20:
                        random_laser.goto(random_ship.xcor(), random_ship.ycor())
                        random_laser.tracking = False
                    elif random_ship.type == 'veteran' and random_chance < 15:
                        random_laser.goto(random_ship.xcor(), random_ship.ycor())
                        random_laser.tracking = False
                    elif random_ship.type == 'skirmisher' and random_chance < 5:
                        random_laser.goto(random_ship.xcor(), random_ship.ycor())
                        random_laser.tracking = False
                    elif random_ship.type == 'skirmisher' and random_chance < 2:
                        random_laser.goto(random_ship.xcor(), random_ship.ycor())
                        random_laser.tracking = False


        #fire laser
        screen.onkeypress(fire_laser, 'space')

        screen.onkeypress(player.move_left, 'Left')
        screen.onkeypress(player.move_right, 'Right')

        if game_on == False:
            screen.onkeypress(new_game, 'n')

        screen.listen()


    screen.mainloop()




run_game()
