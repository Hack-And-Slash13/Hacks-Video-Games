import time, random

play = "yes"
just_entered = True

def round_to(variable):
    try:
        new_variable = round(variable)
        return new_variable
    except:
        return variable
def more_than(a, b):
    try:
        if a > b:
            return True
        else:
            return False
    except:
        return True
def less_than(a, b):
    try:
        if a < b:
            return True
        else:
            return False
    except:
        return True
def clear_screen():
    for lines in range(35):
        print("")
def game_over():
    global play
    global x
    global y
    global floor
    global direction
    x = 0
    y = 0
    direction = "north"
    floor = -1
    if play == "no":
        play = "no"
        for lines in range (24):
            print("")
        print("                                                                                     GAME OVER")
        for lines in range(23):
            print("")
        time.sleep(2)
        print("")
        play = input(str("Would you like to keep playing? Type 'yes' to keep playing. Type 'no' to quit."))
        while play != "yes" and play != "no":
            play = input(str("type 'yes' to keep playing. Type 'no' to quit"))
        if play == "no":
            exit()
        if play == "yes":
            return

def print_area():
    global direction
    global x
    global y
    global floor
    global enemy
    global battle_end
    global play
    global player1
    if play == "no":
        return
    clear_screen()
    if player1.accessory == "cursed life-sucking amulet":
        player1.health -= 1
    if player1.hunger != "full":
        player1.hunger -= .25
        if player1.hunger < 1:
            play = "no"
            for lines in range (23):
                print("")
            print("                                                                                 You starved to death")
            print("                                                                                      GAME OVER")
            for lines in range(23):
                print("")
            time.sleep(2)
            print("")
            play = input(str("Would you like to keep playing? Type 'yes' to keep playing. Type 'no' to quit."))
            while play != "yes" and play != "no":
                play = input(str("type 'yes' to keep playing. Type 'no' to quit"))
            if play == "no":
                exit()
    enemy = "none"
    if battle_end == False:
        number = random.randint(1,10)
        if floor == -1 and just_entered == False:
            if number < 3:
                enemy = "enemy"
                fight()
        elif floor == -2 and just_entered == False:
            if number < 5:
                enemy = "enemy"
                fight()
        elif floor == -3 and just_entered == False:
            if number < 6:
                enemy = "enemy"
                fight()
    else:
        battle_end = False
    if enemy != "enemy":
        if x == 0 and y == 0 and floor == -1 and direction == "west":
            south_entrance_room_facingwest()
        elif x == 0 and y == 0 and floor == -1 and direction == "south":
            entrance_stairs()
        elif x == 0 and y == 0 and floor == -1 and direction == "north":
            south_entrance_room_facingnorth()
        elif x == 0 and y == 0 and floor == -1 and direction == "east":
            south_entrance_room_facingeast()
        elif x == 0 and y == 1 and floor == -1 and direction == "west":
            door2()
        elif x == 0 and y == 1 and floor == -1 and direction == "south":
            entrance_stairs2()
        elif x == 0 and y == 1 and floor == -1 and direction == "north":
            door()
        elif x == 0 and y == 1 and floor == -1 and direction == "east":
            door3()
        elif x == 1 and y == 0 and floor == -1 and direction == "west":
            southeast_entrance_room_facingwest()
        elif x == 1 and y == 0 and floor == -1 and direction == "south":
            wall()
        elif x == 1 and y == 0 and floor == -1 and direction == "north":
            twodoors()
        elif x == 1 and y == 0 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == 2 and floor == -1 and direction == "north":
            t_hall_right()
        elif x == 1 and y == 2 and floor == -1 and direction == "west":
            door()
        elif x == 1 and y == 2 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == 2 and floor == -1 and direction == "south":
            hall()
        elif x == -1 and y == 0 and floor == -1 and direction == "west":
            wall()
        elif x == -1 and y == 0 and floor == -1 and direction == "south":
            wall()
        elif x == -1 and y == 0 and floor == -1 and direction == "north":
            twodoors2()
        elif x == -1 and y == 0 and floor == -1 and direction == "east":
            southwest_entrance_room_facingeast()
        elif x == -1 and y == 1 and floor == -1 and direction == "west":
            door()
        elif x == -1 and y == 1 and floor == -1 and direction == "south":
            northwest_entrance_room_facingsouth()
        elif x == -1 and y == 1 and floor == -1 and direction == "north":
            wall()
        elif x == -1 and y == 1 and floor == -1 and direction == "east":
            twodoors2()
        elif x == 1 and y == 1 and floor == -1 and direction == "west":
            twodoors()
        elif x == 1 and y == 1 and floor == -1 and direction == "south":
            northeast_entrance_room_facingsouth()
        elif x == 1 and y == 1 and floor == -1 and direction == "north":
            wall()
        elif x == 1 and y == 1 and floor == -1 and direction == "east":
            door()
        elif  x == 2 and y == 1 and floor == -1 and direction == "north":
            t_hall_right()
        elif  x == 2 and y == 1 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == 1 and floor == -1 and direction == "west":
            door()
        elif x == 2 and y == 1 and floor == -1 and direction == "south":
            hall()
        elif x == 2 and y == 0 and floor == -1 and direction == "north":
            hall_door_on_left()
        elif x == 2 and y == 0 and floor == -1 and direction == "west":
            wall()
        elif x == 2 and y == 0 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == 0 and floor == -1 and direction == "south":
            hall()
        elif x == 2 and y == -1 and floor == -1 and direction == "north":
            hall()
        elif x == 2 and y == -1 and floor == -1 and direction == "west":
            wall()
        elif x == 2 and y == -1 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == -1 and floor == -1 and direction == "south":
            hall()
        elif x == 2 and y == -2 and floor == -1 and direction == "north":
            hall()
        elif x == 2 and y == -2 and floor == -1 and direction == "west":
            door()
        elif x == 2 and y == -2 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == -2 and floor == -1 and direction == "south":
            hall_door_on_right()
        elif x == 2 and y == -3 and floor == -1 and direction == "north":
            hall()
        elif x == 2 and y == -3 and floor == -1 and direction == "west":
            locked_door()
        elif x == 2 and y == -3 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == -3 and floor == -1 and direction == "south":
            hall()
        elif x == 2 and y == -4 and floor == -1 and direction == "north":
            hall_door_on_left()
        elif x == 2 and y == -4 and floor == -1 and direction == "west":
            wall()
        elif x == 2 and y == -4 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == -4 and floor == -1 and direction == "south":
            hall_4way_split()
        elif x == 2 and y == -5 and floor == -1 and direction == "north":
            hall()
        elif x == 2 and y == -5 and floor == -1 and direction == "west":
            hall()
        elif x == 2 and y == -5 and floor == -1 and direction == "east":
            hall_door_on_end()
        elif x == 2 and y == -5 and floor == -1 and direction == "south":
            hall()
        elif x == 2 and y == -6 and floor == -1 and direction == "north":
            hall_4way_split()
        elif x == 2 and y == -6 and floor == -1 and direction == "west":
            wall()
        elif x == 2 and y == -6 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == -6 and floor == -1 and direction == "south":
            hall_2doors()
        elif x == 2 and y == -7 and floor == -1 and direction == "north":
            hall()
        elif x == 2 and y == -7 and floor == -1 and direction == "west":
            door()
        elif x == 2 and y == -7 and floor == -1 and direction == "east":
            door()
        elif x == 2 and y == -7 and floor == -1 and direction == "south":
            hall()
        elif x == 2 and y == -8 and floor == -1 and direction == "north":
            hall_2doors()
        elif x == 2 and y == -8 and floor == -1 and direction == "west":
            wall()
        elif x == 2 and y == -8 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == -8 and floor == -1 and direction == "south":
            hall()
        elif x == 2 and y == -9 and floor == -1 and direction == "north":
            hall()
        elif x == 2 and y == -9 and floor == -1 and direction == "west":
            wall()
        elif x == 2 and y == -9 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == -9 and floor == -1 and direction == "south":
            hall_turning_left()
        elif x == 2 and y == -10 and floor == -1 and direction == "north":
            hall()
        elif x == 2 and y == -10 and floor == -1 and direction == "west":
            wall()
        elif x == 2 and y == -10 and floor == -1 and direction == "east":
            hall()
        elif x == 2 and y == -10 and floor == -1 and direction == "south":
            wall()
        elif x == 3 and y == -10 and floor == -1 and direction == "north":
            wall()
        elif x == 3 and y == -10 and floor == -1 and direction == "west":
            hall_turning_right()
        elif x == 3 and y == -10 and floor == -1 and direction == "east":
            hall_door_on_left()
        elif x == 3 and y == -10 and floor == -1 and direction == "south":
            wall()
        elif x == 4 and y == -10 and floor == -1 and direction == "north":
            door()
        elif x == 4 and y == -10 and floor == -1 and direction == "west":
            hall()
        elif x == 4 and y == -10 and floor == -1 and direction == "east":
            hall_turning_left()
        elif x == 4 and y == -9 and floor == -1 and direction == "north":
            right_corner()
        elif x == 4 and y == -9 and floor == -1 and direction == "west":
            left_corner()
        elif x == 4 and y == -9 and floor == -1 and direction == "east":
            wall()
        elif x == 4 and y == -9 and floor == -1 and direction == "south":
            door()
        elif x == 4 and y == -8 and floor == -1 and direction == "north":
            wall()
        elif x == 4 and y == -8 and floor == -1 and direction == "west":
            chest()
        elif x == 4 and y == -8 and floor == -1 and direction == "east":
            wall()
        elif x == 4 and y == -8 and floor == -1 and direction == "south":
            door2()
        elif x == 3 and y == -9 and floor == -1 and direction == "north":
            chest()
        elif x == 3 and y == -9 and floor == -1 and direction == "west":
            wall()
        elif x == 3 and y == -9 and floor == -1 and direction == "east":
            door_right_corner()
        elif x == 3 and y == -9 and floor == -1 and direction == "south":
            wall()
        elif x == 5 and y == -10 and floor == -1 and direction == "north":
            hall()
        elif x == 5 and y == -10 and floor == -1 and direction == "west":
            hall_door_on_right()
        elif x == 5 and y == -10 and floor == -1 and direction == "east":
            wall()
        elif x == 5 and y == -10 and floor == -1 and direction == "south":
            wall()
        elif x == 5 and y == -9 and floor == -1 and direction == "north":
            hall_door_on_end()
        elif x == 5 and y == -9 and floor == -1 and direction == "west":
            wall()
        elif x == 5 and y == -9 and floor == -1 and direction == "east":
            wall()
        elif x == 5 and y == -9 and floor == -1 and direction == "south":
            hall()
        elif x == 5 and y == -8 and floor == -1 and direction == "north":
            door()
        elif x == 5 and y == -8 and floor == -1 and direction == "west":
            wall()
        elif x == 5 and y == -8 and floor == -1 and direction == "east":
            wall()
        elif x == 5 and y == -8 and floor == -1 and direction == "south":
            hall()
        elif x == 5 and y == -7 and floor == -1 and direction == "north":
            right_corner()
        elif x == 5 and y == -7 and floor == -1 and direction == "west":
            far_left_corner()
        elif x == 5 and y == -7 and floor == -1 and direction == "east":
            wall()
        elif x == 5 and y == -7 and floor == -1 and direction == "south":
            door()
        elif x == 5 and y == -6 and floor == -1 and direction == "north":
            chest()
        elif x == 5 and y == -6 and floor == -1 and direction == "west":
            door()
        elif x == 5 and y == -6 and floor == -1 and direction == "east":
            door_right_corner()
        elif x == 5 and y == -6 and floor == -1 and direction == "south":
            wall()
        elif x == 4 and y == -7 and floor == -1 and direction == "north":
            far_wall()
        elif x == 4 and y == -7 and floor == -1 and direction == "west":
            door3()
        elif x == 4 and y == -7 and floor == -1 and direction == "east":
            door2()
        elif x == 4 and y == -7 and floor == -1 and direction == "south":
            wall()
        elif x == 4 and y == -6 and floor == -1 and direction == "north":
            wall()
        elif x == 4 and y == -6 and floor == -1 and direction == "west":
            chest_right_corner()
        elif x == 4 and y == -6 and floor == -1 and direction == "east":
            left_corner()
        elif x == 4 and y == -6 and floor == -1 and direction == "south":
            south_entrance_room_facingeast()
        elif x == 3 and y == -7 and floor == -1 and direction == "north":
            chest()
        elif x == 3 and y == -7 and floor == -1 and direction == "west":
            door()
        elif x == 3 and y == -7 and floor == -1 and direction == "east":
            door_far_right_corner()
        elif x == 3 and y == -7 and floor == -1 and direction == "south":
            wall()
        elif x == 1 and y == -3 and floor == -1 and direction == "north":
            right_corner()
        elif x == 1 and y == -3 and floor == -1 and direction == "west":
            fountain()
        elif x == 1 and y == -3 and floor == -1 and direction == "east":
            door()
        elif x == 1 and y == -3 and floor == -1 and direction == "south":
            left_corner()
        elif x == 1 and y == -2 and floor == -1 and direction == "north":
            wall()
        elif x == 1 and y == -2 and floor == -1 and direction == "west":
            far_right_corner()
        elif x == 1 and y == -2 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == -2 and floor == -1 and direction == "south":
            door_right_corner()
        elif x == 1 and y == -4 and floor == -1 and direction == "north":
            door_left_corner()
        elif x == 1 and y == -4 and floor == -1 and direction == "west":
            far_left_corner()
        elif x == 1 and y == -4 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == -4 and floor == -1 and direction == "south":
            wall()
        elif x == 0 and y == -4 and floor == -1 and direction == "north":
            fountain()
        elif x == 0 and y == -4 and floor == -1 and direction == "west":
            left_corner()
        elif x == 0 and y == -4 and floor == -1 and direction == "east":
            right_corner
        elif x == 0 and y == -4 and floor == -1 and direction == "south":
            wall()
        elif x == -1 and y == -4 and floor == -1 and direction == "north":
            door_left_corner()
        elif x == -1 and y == -4 and floor == -1 and direction == "west":
            wall()
        elif x == -1 and y == -4 and floor == -1 and direction == "east":
            far_right_corner()
        elif x == -1 and y == -4 and floor == -1 and direction == "south":
            wall()
        elif x == 1 and y == -2 and floor == -1 and direction == "north":
            wall()
        elif x == 1 and y == -2 and floor == -1 and direction == "west":
            far_right_corner()
        elif x == 1 and y == -2 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == -2 and floor == -1 and direction == "south":
            door_left_corner()
        elif x == 0 and y == -2 and floor == -1 and direction == "north":
            wall()
        elif x == 0 and y == -2 and floor == -1 and direction == "west":
            right_corner()
        elif x == 0 and y == -2 and floor == -1 and direction == "east":
            left_corner
        elif x == 0 and y == -2 and floor == -1 and direction == "south":
            fountain()
        elif x == -1 and y == -2 and floor == -1 and direction == "north":
            wall()
        elif x == -1 and y == -2 and floor == -1 and direction == "west":
            wall()
        elif x == -1 and y == -2 and floor == -1 and direction == "east":
            left_corner()
        elif x == -1 and y == -2 and floor == -1 and direction == "south":
            door_right_corner()
        elif x == -1 and y == -3 and floor == -1 and direction == "north":
            left_corner()
        elif x == -1 and y == -3 and floor == -1 and direction == "west":
            door()
        elif x == -1 and y == -3 and floor == -1 and direction == "east":
            far_left_corner()
        elif x == -1 and y == -3 and floor == -1 and direction == "south":
            right_corner()
        elif x == 3 and y == -5 and floor == -1 and direction == "north":
            wall()
        elif x == 3 and y == -5 and floor == -1 and direction == "west":
            hall_4way_split()
        elif x == 3 and y == -5 and floor == -1 and direction == "east":
            door()
        elif x == 3 and y == -5 and floor == -1 and direction == "south":
            wall()
        elif x == 4 and y == -5 and floor == -1 and direction == "north":
            door2()
        elif x == 4 and y == -5 and floor == -1 and direction == "west":
            door()
        elif x == 4 and y == -5 and floor == -1 and direction == "east":
            right_corner()
        elif x == 4 and y == -5 and floor == -1 and direction == "south":
            wall()
        elif x == 4 and y == -4 and floor == -1 and direction == "north":
            door()
        elif x == 4 and y == -4 and floor == -1 and direction == "west":
            wall()
        elif x == 4 and y == -4 and floor == -1 and direction == "east":
            left_corner()
        elif x == 4 and y == -4 and floor == -1 and direction == "south":
            door_right_corner()
        elif x == 4 and y == -3 and floor == -1 and direction == "north":
            far_wall()
        elif x == 4 and y == -3 and floor == -1 and direction == "west":
            left_corner()
        elif x == 4 and y == -3 and floor == -1 and direction == "east":
            right_corner()
        elif x == 4 and y == -3 and floor == -1 and direction == "south":
            door()
        elif x == 5 and y == -3 and floor == -1 and direction == "north":
            door2()
        elif x == 5 and y == -3 and floor == -1 and direction == "west":
            door_left_corner()
        elif x == 5 and y == -3 and floor == -1 and direction == "east":
            wall()
        elif x == 5 and y == -3 and floor == -1 and direction == "south":
            wall()
        elif x == 3 and y == -3 and floor == -1 and direction == "north":
            left_corner()
        elif x == 3 and y == -3 and floor == -1 and direction == "east":
            door_left_corner()
        elif x == 3 and y == -3 and floor == -1 and direction == "west":
            wall()
        elif x == 3 and y == -3 and floor == -1 and direction == "south":
            wall()
        elif x == 3 and y == -2 and floor == -1 and direction == "north":
            wall()
        elif x == 3 and y == -2 and floor == -1 and direction == "west":
            wall()
        elif x == 3 and y == -2 and floor == -1 and direction == "east":
            door_far_left_corner()
        elif x == 3 and y == -2 and floor == -1 and direction == "south":
            right_corner()
        elif x == 4 and y == -2 and floor == -1 and direction == "north":
            wall()
        elif x == 4 and y == -2 and floor == -1 and direction == "west":
            right_corner()
        elif x == 4 and y == -2 and floor == -1 and direction == "east":
            door_left_corner()
        elif x == 4 and y == -2 and floor == -1 and direction == "south":
            south_entrance_room_facingnorth()
        elif x == 5 and y == -2 and floor == -1 and direction == "north":
            door()
        elif x == 5 and y == -2 and floor == -1 and direction == "west":
            far_right_corner()
        elif x == 5 and y == -2 and floor == -1 and direction == "east":
            wall()
        elif x == 5 and y == -2 and floor == -1 and direction == "south":
            left_corner()
        elif x == 5 and y == -1 and floor == -1 and direction == "north":
            hall_door_on_left()
        elif x == 5 and y == -1 and floor == -1 and direction == "west":
            wall()
        elif x == 5 and y == -1 and floor == -1 and direction == "east":
            wall()
        elif x == 5 and y == -1 and floor == -1 and direction == "south":
            door()
        elif x == 5 and y == 0 and floor == -1 and direction == "north":
            hall()
        elif x == 5 and y == 0 and floor == -1 and direction == "west":
            door()
        elif x == 5 and y == 0 and floor == -1 and direction == "east":
            wall()
        elif x == 5 and y == 0 and floor == -1 and direction == "south":
            hall_door_on_end()
        elif x == 4 and y == 0 and floor == -1 and direction == "north":
            right_corner()
        elif x == 4 and y == 0 and floor == -1 and direction == "west":
            far_wall()
        elif x == 4 and y == 0 and floor == -1 and direction == "east":
            door()
        elif x == 4 and y == 0 and floor == -1 and direction == "south":
            left_corner()
        elif x == 4 and y == 1 and floor == -1 and direction == "north":
            wall()
        elif x == 4 and y == 1 and floor == -1 and direction == "west":
            right_corner()
        elif x == 4 and y == 1 and floor == -1 and direction == "east":
            wall()
        elif x == 4 and y == 1 and floor == -1 and direction == "south":
            door_left_corner()
        elif x == 4 and y == -1 and floor == -1 and direction == "north":
            door_right_corner()
        elif x == 4 and y == -1 and floor == -1 and direction == "west":
            chest()
        elif x == 4 and y == -1 and floor == -1 and direction == "east":
            wall()
        elif x == 4 and y == -1 and floor == -1 and direction == "south":
            wall()
        elif x == 3 and y == 1 and floor == -1 and direction == "north":
            wall()
        elif x == 3 and y == 1 and floor == -1 and direction == "west":
            wall()
        elif x == 3 and y == 1 and floor == -1 and direction == "east":
            left_corner()
        elif x == 3 and y == 1 and floor == -1 and direction == "south":
            chest_right_corner()
        elif x == 3 and y == 0 and floor == -1 and direction == "north":
            left_corner()
        elif x == 3 and y == 0 and floor == -1 and direction == "west":
            wall()
        elif x == 3 and y == 0 and floor == -1 and direction == "east":
            south_entrance_room_facingnorth()
        elif x == 3 and y == 0 and floor == -1 and direction == "south":
            chest()
        elif x == 5 and y == 1 and floor == -1 and direction == "north":
            hall_turning_left()
        elif x == 5 and y == 1 and floor == -1 and direction == "west":
            wall()
        elif x == 5 and y == 1 and floor == -1 and direction == "east":
            wall()
        elif x == 5 and y == 1 and floor == -1 and direction == "south":
            hall_door_on_right()
        elif x == 5 and y == 2 and floor == -1 and direction == "north":
            wall()
        elif x == 5 and y == 2 and floor == -1 and direction == "west":
            hall()
        elif x == 5 and y == 2 and floor == -1 and direction == "east":
            wall()
        elif x == 5 and y == 2 and floor == -1 and direction == "south":
            hall()
        elif x == 4 and y == 2 and floor == -1 and direction == "north":
            wall()
        elif x == 4 and y == 2 and floor == -1 and direction == "west":
            hall_door_on_right()
        elif x == 4 and y == 2 and floor == -1 and direction == "east":
            hall_turning_right()
        elif x == 4 and y == 2 and floor == -1 and direction == "south":
            wall()
        elif x == 3 and y == 2 and floor == -1 and direction == "north":
            door()
        elif x == 3 and y == 2 and floor == -1 and direction == "west":
            t_hall()
        elif x == 3 and y == 2 and floor == -1 and direction == "east":
            hall()
        elif x == 3 and y == 2 and floor == -1 and direction == "south":
            wall()
        elif x == 2 and y == 2 and floor == -1 and direction == "north":
            hall()
        elif x == 2 and y == 2 and floor == -1 and direction == "west":
            wall()
        elif x == 2 and y == 2 and floor == -1 and direction == "east":
            hall_door_on_left()
        elif x == 2 and y == 2 and floor == -1 and direction == "south":
            hall_door_on_right()
        elif x == 2 and y == 3 and floor == -1 and direction == "north":
            hall()
        elif x == 2 and y == 3 and floor == -1 and direction == "west":
            wall()
        elif x == 2 and y == 3 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == 3 and floor == -1 and direction == "south":
            t_hall_left()
        elif x == 2 and y == 4 and floor == -1 and direction == "north":
            hall_turning_left()
        elif x == 2 and y == 4 and floor == -1 and direction == "west":
            wall()
        elif x == 2 and y == 4 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == 4 and floor == -1 and direction == "south":
            hall()
        elif x == 2 and y == 5 and floor == -1 and direction == "north":
            wall()
        elif x == 2 and y == 5 and floor == -1 and direction == "west":
            hall_turning_left()
        elif x == 2 and y == 5 and floor == -1 and direction == "east":
            wall()
        elif x == 2 and y == 5 and floor == -1 and direction == "south":
            hall()
        elif x == 1 and y == 5 and floor == -1 and direction == "north":
            wall()
        elif x == 1 and y == 5 and floor == -1 and direction == "west":
            wall()
        elif x == 1 and y == 5 and floor == -1 and direction == "east":
            hall_turning_right()
        elif x == 1 and y == 5 and floor == -1 and direction == "south":
            hall_door_on_end()
        elif x == 1 and y == 4 and floor == -1 and direction == "north":
            hall()
        elif x == 1 and y == 4 and floor == -1 and direction == "west":
            wall()
        elif x == 1 and y == 4 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == 4 and floor == -1 and direction == "south":
            door()
        elif x == 0 and y == 2 and floor == -1 and direction == "north":
            threedoors()
        elif x == 0 and y == 2 and floor == -1 and direction == "west":
            left_corner()
        elif x == 0 and y == 2 and floor == -1 and direction == "east":
            right_corner()
        elif x == 0 and y == 2 and floor == -1 and direction == "south":
            door()
        elif x == -1 and y == 2 and floor == -1 and direction == "north":
            door3()
        elif x == -1 and y == 2 and floor == -1 and direction == "west":
            wall()
        elif x == -1 and y == 2 and floor == -1 and direction == "east":
            door_right_corner()
        elif x == -1 and y == 2 and floor == -1 and direction == "south":
            wall()
        elif x == 1 and y == 2 and floor == -1 and direction == "north":
            door2()
        elif x == 1 and y == 2 and floor == -1 and direction == "west":
            door_left_corner()
        elif x == 1 and y == 2 and floor == -1 and direction == "south":
            wall()
        elif x == 1 and y == 3 and floor == -1 and direction == "north":
            door()
        elif x == 1 and y == 3 and floor == -1 and direction == "west":
            twodoors_far_right_corner()
        elif x == 1 and y == 3 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == 3 and floor == -1 and direction == "south":
            left_corner()
        elif x == 0 and y == 3 and floor == -1 and direction == "north":
            door()
        elif x == 0 and y == 3 and floor == -1 and direction == "west":
            door_right_corner()
        elif x == 0 and y == 3 and floor == -1 and direction == "east":
            door_left_corner()
        elif x == 0 and y == 3 and floor == -1 and direction == "south":
            south_entrance_room_facingnorth()
        elif x == -1 and y == 3 and floor == -1 and direction == "north":
            door()
        elif x == -1 and y == 3 and floor == -1 and direction == "west":
            wall()
        elif x == -1 and y == 3 and floor == -1 and direction == "east":
            twodoors_far_left_corner()
        elif x == -1 and y == 3 and floor == -1 and direction == "south":
            right_corner()
        elif x == 0 and y == 4 and floor == -1 and direction == "north":
            hall_door_on_end()
        elif x == 0 and y == 4 and floor == -1 and direction == "west":
            wall()
        elif x == 0 and y == 4 and floor == -1 and direction == "east":
            wall()
        elif x == 0 and y == 4 and floor == -1 and direction == "south":
            door()
        elif x == 0 and y == 5 and floor == -1 and direction == "north":
            door()
        elif x == 0 and y == 5 and floor == -1 and direction == "west":
            wall()
        elif x == 0 and y == 5 and floor == -1 and direction == "east":
            wall()
        elif x == 0 and y == 5 and floor == -1 and direction == "south":
            hall_door_on_end()()
        elif x == 0 and y == 6 and floor == -1 and direction == "north":
            chest()
        elif x == 0 and y == 6 and floor == -1 and direction == "west":
            left_corner()
        elif x == 0 and y == 6 and floor == -1 and direction == "east":
            right_corner()
        elif x == 0 and y == 6 and floor == -1 and direction == "south":
            door()
        elif x == -1 and y == 6 and floor == -1 and direction == "north":
            left_corner()
        elif x == -1 and y == 6 and floor == -1 and direction == "west":
            wall()
        elif x == -1 and y == 6 and floor == -1 and direction == "east":
            door_right_corner()
        elif x == -1 and y == 6 and floor == -1 and direction == "south":
            wall()
        elif x == 1 and y == 6 and floor == -1 and direction == "north":
            right_corner()
        elif x == 1 and y == 6 and floor == -1 and direction == "west":
            door_left_corner()
        elif x == 1 and y == 6 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == 6 and floor == -1 and direction == "south":
            wall()
        elif x == 1 and y == 7 and floor == -1 and direction == "north":
            wall()
        elif x == 1 and y == 7 and floor == -1 and direction == "west":
            chest()
        elif x == 1 and y == 7 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == 7 and floor == -1 and direction == "south":
            left_corner()
        elif x == -1 and y == 7 and floor == -1 and direction == "north":
            wall()
        elif x == -1 and y == 7 and floor == -1 and direction == "west":
            wall()
        elif x == -1 and y == 7 and floor == -1 and direction == "east":
            chest()
        elif x == -1 and y == 7 and floor == -1 and direction == "south":
            right_corner()
        elif x == 3 and y == 3 and floor == -1 and direction == "north":
            left_corner()
        elif x == 3 and y == 3 and floor == -1 and direction == "west":
            wall()
        elif x == 3 and y == 3 and floor == -1 and direction == "east":
            chest()
        elif x == 3 and y == 3 and floor == -1 and direction == "south":
            door()
        elif x == 3 and y == 4 and floor == -1 and direction == "north":
            wall()
        elif x == 3 and y == 4 and floor == -1 and direction == "west":
            wall()
        elif x == 3 and y == 4 and floor == -1 and direction == "east":
            left_corner()
        elif x == 3 and y == 4 and floor == -1 and direction == "south":
            door3
        elif x == 4 and y == 4 and floor == -1 and direction == "north":
            wall()
        elif x == 3 and y == 4 and floor == -1 and direction == "west":
            right_corner()
        elif x == 3 and y == 4 and floor == -1 and direction == "east":
            wall()
        elif x == 3 and y == 4 and floor == -1 and direction == "south":
            chest()
        elif x == -1 and y == 4 and floor == -1 and direction == "north":
            hall_turning_left()
        elif x == -1 and y == 4 and floor == -1 and direction == "west":
            wall()
        elif x == -1 and y == 4 and floor == -1 and direction == "east":
            wall()
        elif x == -1 and y == 4 and floor == -1 and direction == "south":
            door()
        elif x == -1 and y == 5 and floor == -1 and direction == "north":
            wall()
        elif x == -1 and y == 5 and floor == -1 and direction == "west":
            hall_turning_left()
        elif x == -1 and y == 5 and floor == -1 and direction == "east":
            wall()
        elif x == -1 and y == 5 and floor == -1 and direction == "south":
            hall_door_on_end()
        elif x == -2 and y == 5 and floor == -1 and direction == "north":
            wall()
        elif x == -2 and y == 5 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == 5 and floor == -1 and direction == "east":
            hall_turning_right()
        elif x == -2 and y == 5 and floor == -1 and direction == "south":
            hall()
        elif x == -2 and y == 4 and floor == -1 and direction == "north":
            hall_turning_right()
        elif x == -2 and y == 4 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == 4 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == 4 and floor == -1 and direction == "south":
            hall()
        elif x == -2 and y == 3 and floor == -1 and direction == "north":
            hall()
        elif x == -2 and y == 3 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == 3 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == 3 and floor == -1 and direction == "south":
            t_hall_right()
        elif x == -2 and y == 2 and floor == -1 and direction == "north":
            hall()
        elif x == -2 and y == 2 and floor == -1 and direction == "west":
            hall_door_on_right()
        elif x == -2 and y == 2 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == 2 and floor == -1 and direction == "south":
            hall_door_on_left()
        elif x == -2 and y == 1 and floor == -1 and direction == "north":
            hall()
        elif x == -2 and y == 1 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == 1 and floor == -1 and direction == "east":
            door()
        elif x == -2 and y == 1 and floor == -1 and direction == "south":
            hall()
        elif x == -2 and y == 0 and floor == -1 and direction == "north":
            t_hall_left()
        elif x == -2 and y == 0 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == 0 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == 0 and floor == -1 and direction == "south":
            hall()
        elif x == -2 and y == -1 and floor == -1 and direction == "north":
            hall()
        elif x == -2 and y == -1 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == -1 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == -1 and floor == -1 and direction == "south":
            hall()
        elif x == -2 and y == 0 and floor == -1 and direction == "north":
            hall_door_on_right()
        elif x == -2 and y == 0 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == 0 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == 0 and floor == -1 and direction == "south":
            hall()
        elif x == -2 and y == -1 and floor == -1 and direction == "north":
            wall()
        elif x == -2 and y == -1 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == -1 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == -2 and floor == -1 and direction == "north":
            hall()
        elif x == -2 and y == -2 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == -2 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == -2 and floor == -1 and direction == "south":
            hall_door_on_left()
        elif x == -2 and y == -3 and floor == -1 and direction == "north":
            hall()
        elif x == -2 and y == -3 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == -3 and floor == -1 and direction == "east":
            locked_door()
        elif x == -2 and y == -3 and floor == -1 and direction == "south":
            hall()
        elif x == -3 and y == 2 and floor == -1 and direction == "north":
            door()
        elif x == -3 and y == 2 and floor == -1 and direction == "west":
            hall()
        elif x == -3 and y == 2 and floor == -1 and direction == "east":
            t_hall()
        elif x == -3 and y == 2 and floor == -1 and direction == "south":
            wall()
        elif x == -3 and y == 3 and floor == -1 and direction == "north":
            left_corner()
        elif x == -3 and y == 3 and floor == -1 and direction == "west":
            chest()
        elif x == -3 and y == 3 and floor == -1 and direction == "east":
            wall()
        elif x == -3 and y == 3 and floor == -1 and direction == "south":
            door()
        elif x == -3 and y == 4 and floor == -1 and direction == "north":
            wall()
        elif x == -3 and y == 4 and floor == -1 and direction == "west":
            right_corner()
        elif x == -3 and y == 4 and floor == -1 and direction == "east":
            wall()
        elif x == -3 and y == 4 and floor == -1 and direction == "south":
            door3()
        elif x == -2 and y == 4 and floor == -1 and direction == "north":
            wall()
        elif x == -2 and y == 4 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == 4 and floor == -1 and direction == "east":
            left_corner()
        elif x == -2 and y == 4 and floor == -1 and direction == "south":
            chest()
        elif x == -4 and y == 2 and floor == -1 and direction == "north":
            wall()
        elif x == -4 and y == 2 and floor == -1 and direction == "west":
            hall_turning_left()
        elif x == -4 and y == 2 and floor == -1 and direction == "east":
            hall_door_on_left()
        elif x == -4 and y == 2 and floor == -1 and direction == "south":
            wall()
        elif x == -5 and y == 2 and floor == -1 and direction == "north":
            wall()
        elif x == -5 and y == 2 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == 2 and floor == -1 and direction == "east":
            hall()
        elif x == -5 and y == 2 and floor == -1 and direction == "south":
            hall()
        elif x == -5 and y == 1 and floor == -1 and direction == "north":
            hall_tuurning_right()
        elif x == -5 and y == 1 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == 1 and floor == -1 and direction == "east":
            wall()
        elif x == -5 and y == 1 and floor == -1 and direction == "south":
            hall_door_on_left()
        elif x == -5 and y == 0 and floor == -1 and direction == "north":
            hall()
        elif x == -5 and y == 0 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == 0 and floor == -1 and direction == "east":
            door()
        elif x == -5 and y == 0 and floor == -1 and direction == "south":
            hall_door_on_end()
        elif x == -4 and y == 0 and floor == -1 and direction == "north":
            left_corner()
        elif x == -4 and y == 0 and floor == -1 and direction == "west":
            door()
        elif x == -4 and y == 0 and floor == -1 and direction == "east":
            far_wall()
        elif x == -4 and y == 0 and floor == -1 and direction == "south":
            chest()
        elif x == -3 and y == -1 and floor == -1 and direction == "north":
            far_right_corner()
        elif x == -3 and y == -1 and floor == -1 and direction == "west":
            chest()
        elif x == -3 and y == -1 and floor == -1 and direction == "east":
            wall()
        elif x == -3 and y == -1 and floor == -1 and direction == "south":
            wall()
        elif x == -3 and y == 0 and floor == -1 and direction == "north":
            right_corner()
        elif x == -3 and y == 0 and floor == -1 and direction == "west":
            south_entrance_room_facingnorth()
        elif x == -3 and y == 0 and floor == -1 and direction == "east":
            wall()
        elif x == -3 and y == 0 and floor == -1 and direction == "south":
            left_corner()
        elif x == -3 and y == 1 and floor == -1 and direction == "north":
            wall()
        elif x == -3 and y == 1 and floor == -1 and direction == "west":
            right_corner()
        elif x == -3 and y == 1 and floor == -1 and direction == "east":
            wall()
        elif x == -3 and y == 1 and floor == -1 and direction == "south":
            far_left_corner()
        elif x == -4 and y == 1 and floor == -1 and direction == "north":
            wall()
        elif x == -4 and y == 1 and floor == -1 and direction == "west":
            wall()
        elif x == -4 and y == 1 and floor == -1 and direction == "east":
            left_corner()
        elif x == -4 and y == 1 and floor == -1 and direction == "south":
            chest_right_corner()
        elif x == -5 and y == -1 and floor == -1 and direction == "north":
            hall_door_on_right()
        elif x == -5 and y == -1 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == -1 and floor == -1 and direction == "east":
            wall()
        elif x == -5 and y == -1 and floor == -1 and direction == "south":
            door()
        elif x == -5 and y == -2 and floor == -1 and direction == "north":
            door()
        elif x == -5 and y == -2 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == -2 and floor == -1 and direction == "east":
            far_left_corner()
        elif x == -5 and y == -2 and floor == -1 and direction == "south":
            right_corner()
        elif x == -4 and y == -2 and floor == -1 and direction == "north":
            wall()
        elif x == -4 and y == -2 and floor == -1 and direction == "west":
            door_right_corner()
        elif x == -4 and y == -2 and floor == -1 and direction == "east":
            left_corner()
        elif x == -4 and y == -2 and floor == -1 and direction == "south":
            south_entrance_room_facingnorth()
        elif x == -5 and y == -3 and floor == -1 and direction == "north":
            door3()
        elif x == -5 and y == -3 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == -3 and floor == -1 and direction == "east":
            door_right_corner()
        elif x == -5 and y == -3 and floor == -1 and direction == "south":
            wall()
        elif x == -4 and y == -3 and floor == -1 and direction == "north":
            far_wall()
        elif x == -4 and y == -3 and floor == -1 and direction == "west":
            left_corner()
        elif x == -4 and y == -3 and floor == -1 and direction == "east":
            right_corner()
        elif x == -4 and y == -3 and floor == -1 and direction == "south":
            door()
        elif x == -3 and y == -3 and floor == -1 and direction == "north":
            right_corner()
        elif x == -3 and y == -3 and floor == -1 and direction == "west":
            door_left_corner()
        elif x == -3 and y == -3 and floor == -1 and direction == "east":
            wall()
        elif x == -3 and y == -3 and floor == -1 and direction == "south":
            wall()
        elif x == -4 and y == -4 and floor == -1 and direction == "north":
            door()
        elif x == -4 and y == -4 and floor == -1 and direction == "west":
            right_corner()
        elif x == -4 and y == -4 and floor == -1 and direction == "east":
            wall()
        elif x == -5 and y == -4 and floor == -1 and direction == "north":
            wall()
        elif x == -5 and y == -4 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == -4 and floor == -1 and direction == "east":
            door_left_corner()
        elif x == -5 and y == -4 and floor == -1 and direction == "south":
            right_corner()
        elif x == -5 and y == -5 and floor == -1 and direction == "north":
            left_corner()
        elif x == -5 and y == -5 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == -5 and floor == -1 and direction == "east":
            door2()
        elif x == -5 and y == -5 and floor == -1 and direction == "south":
            wall()
        elif x == -4 and y == -5 and floor == -1 and direction == "north":
            door2()
        elif x == -4 and y == -5 and floor == -1 and direction == "west":
            left_corner()
        elif x == -4 and y == -5 and floor == -1 and direction == "east":
            door()
        elif x == -4 and y == -5 and floor == -1 and direction == "south":
            wall()
        elif x == -3 and y == -5 and floor == -1 and direction == "north":
            wall()
        elif x == -3 and y == -5 and floor == -1 and direction == "west":
            door()
        elif x == -3 and y == -5 and floor == -1 and direction == "east":
            hall_4way_split()
        elif x == -3 and y == -5 and floor == -1 and direction == "south":
            wall()
        elif x == -2 and y == -5 and floor == -1 and direction == "north":
            hall()
        elif x == -2 and y == -5 and floor == -1 and direction == "west":
            hall_door_on_end()
        elif x == -2 and y == -5 and floor == -1 and direction == "east":
            hall()
        elif x == -2 and y == -5 and floor == -1 and direction == "south":
            hall()
        elif x == -1 and y == -5 and floor == -1 and direction == "north":
            wall()
        elif x == -1 and y == -5 and floor == -1 and direction == "west":
            hall_4way_split()
        elif x == -1 and y == -5 and floor == -1 and direction == "east":
            hall()
        elif x == -1 and y == -5 and floor == -1 and direction == "south":
            wall()
        elif x == 0 and y == -5 and floor == -1 and direction == "north":
            wall()
        elif x == 0 and y == -5 and floor == -1 and direction == "west":
            hall()
        elif x == 0 and y == -5 and floor == -1 and direction == "east":
            hall()
        elif x == 0 and y == -5 and floor == -1 and direction == "south":
            wall()
        elif x == 1 and y == -5 and floor == -1 and direction == "north":
            wall()
        elif x == 1 and y == -5 and floor == -1 and direction == "west":
            hall()
        elif x == 1 and y == -5 and floor == -1 and direction == "east":
            hall_4way_split()
        elif x == 1 and y == -5 and floor == -1 and direction == "south":
            wall()
        elif x == -2 and y == -4 and floor == -1 and direction == "north":
            hall_door_on_right()
        elif x == -2 and y == -4 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == -4 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == -4 and floor == -1 and direction == "south":
            hall_4way_split()
        elif x == -2 and y == -6 and floor == -1 and direction == "north":
            hall_4way_split()
        elif x == -2 and y == -6 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == -6 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == -6 and floor == -1 and direction == "south":
            hall_2doors()
        elif x == -2 and y == -7 and floor == -1 and direction == "north":
            hall()
        elif x == -2 and y == -7 and floor == -1 and direction == "west":
            door()
        elif x == -2 and y == -7 and floor == -1 and direction == "east":
            door()
        elif x == -2 and y == -7 and floor == -1 and direction == "south":
            hall()
        elif x == -2 and y == -8 and floor == -1 and direction == "north":
            hall_2doors()
        elif x == -2 and y == -8 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == -8 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == -8 and floor == -1 and direction == "south":
            hall()
        elif x == -2 and y == -9 and floor == -1 and direction == "north":
            hall()
        elif x == -2 and y == -9 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == -9 and floor == -1 and direction == "east":
            wall()
        elif x == -2 and y == -9 and floor == -1 and direction == "south":
            hall_turning_right()
        elif x == -2 and y == -10 and floor == -1 and direction == "north":
            hall()
        elif x == -2 and y == -10 and floor == -1 and direction == "west":
            wall()
        elif x == -2 and y == -10 and floor == -1 and direction == "east":
            hall()
        elif x == -2 and y == -10 and floor == -1 and direction == "south":
            wall()
        elif x == -3 and y == -10 and floor == -1 and direction == "north":
            wall()
        elif x == -3 and y == -10 and floor == -1 and direction == "west":
            hall_door_on_right()
        elif x == -3 and y == -10 and floor == -1 and direction == "east":
            hall_turning_left()
        elif x == -3 and y == -10 and floor == -1 and direction == "south":
            wall()
        elif x == -4 and y == -10 and floor == -1 and direction == "north":
            door()
        elif x == -4 and y == -10 and floor == -1 and direction == "west":
            hall_turning_right()
        elif x == -4 and y == -10 and floor == -1 and direction == "east":
            hall()
        elif x == -5 and y == -10 and floor == -1 and direction == "north":
            hall()
        elif x == -5 and y == -10 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == -10 and floor == -1 and direction == "east":
            hall_door_on_left()
        elif x == -5 and y == -10 and floor == -1 and direction == "south":
            wall()
        elif x == -5 and y == -9 and floor == -1 and direction == "north":
            hall_door_on_end()
        elif x == -5 and y == -9 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == -9 and floor == -1 and direction == "east":
            wall()
        elif x == -5 and y == -9 and floor == -1 and direction == "south":
            hall_turning_left()
        elif x == -5 and y == -8 and floor == -1 and direction == "north":
            door()
        elif x == -5 and y == -8 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == -8 and floor == -1 and direction == "east":
            wall()
        elif x == -5 and y == -8 and floor == -1 and direction == "south":
            hall()
        elif x == -5 and y == -7 and floor == -1 and direction == "north":
            left_corner()
        elif x == -5 and y == -7 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == -7 and floor == -1 and direction == "east":
            far_right_corner()
        elif x == -5 and y == -7 and floor == -1 and direction == "south":
            door()
        elif x == -5 and y == -6 and floor == -1 and direction == "north":
            wall()
        elif x == -5 and y == -6 and floor == -1 and direction == "west":
            wall()
        elif x == -5 and y == -6 and floor == -1 and direction == "east":
            far_left_corner()
        elif x == -5 and y == -6 and floor == -1 and direction == "south":
            door2()
        elif x == -4 and y == -7 and floor == -1 and direction == "north":
            far_wall()
        elif x == -4 and y == -7 and floor == -1 and direction == "west":
            door_left_corner()
        elif x == -4 and y == -7 and floor == -1 and direction == "east":
            door2
        elif x == -4 and y == -7 and floor == -1 and direction == "south":
            wall()
        elif x == -4 and y == -6 and floor == -1 and direction == "north":
            wall()
        elif x == -4 and y == -6 and floor == -1 and direction == "west":
            right_corner()
        elif x == -4 and y == -6 and floor == -1 and direction == "east":
            left_corner()
        elif x == -4 and y == -6 and floor == -1 and direction == "south":
            far_wall()
        elif x == -3 and y == -7 and floor == -1 and direction == "north":
            right_corner()
        elif x == -3 and y == -7 and floor == -1 and direction == "west":
            far_left_corner()
        elif x == -3 and y == -7 and floor == -1 and direction == "east":
            door()
        elif x == -3 and y == -7 and floor == -1 and direction == "south":
            wall()
        elif x == -3 and y == -6 and floor == -1 and direction == "north":
            wall()
        elif x == -3 and y == -6 and floor == -1 and direction == "west":
            far_right_corner()
        elif x == -3 and y == -6 and floor == -1 and direction == "east":
            wall()
        elif x == -3 and y == -6 and floor == -1 and direction == "south":
            wall_left_corner()
        elif x == -4 and y == -9 and floor == -1 and direction == "north":
            left_corner()
        elif x == -4 and y == -9 and floor == -1 and direction == "west":
            wall()
        elif x == -4 and y == -9 and floor == -1 and direction == "east":
            right_corner()
        elif x == -4 and y == -9 and floor == -1 and direction == "south":
            door()
        elif x == -4 and y == -8 and floor == -1 and direction == "north":
            wall()
        elif x == -4 and y == -8 and floor == -1 and direction == "west":
            wall()
        elif x == -4 and y == -8 and floor == -1 and direction == "east":
            chest()
        elif x == -4 and y == -8 and floor == -1 and direction == "south":
            door2()
        elif x == -3 and y == -9 and floor == -1 and direction == "north":
            chest()
        elif x == -3 and y == -9 and floor == -1 and direction == "west":
            door_left_corner()
        elif x == -3 and y == -9 and floor == -1 and direction == "east":
            wall()
        elif x == -3 and y == -9 and floor == -1 and direction == "south":
            wall()
        elif x == 1 and y == -7 and floor == -1 and direction == "north":
            right_corner()
        elif x == 1 and y == -7 and floor == -1 and direction == "west":
            twodoors2()
        elif x == 1 and y == -7 and floor == -1 and direction == "east":
            door()
        elif x == 1 and y == -7 and floor == -1 and direction == "south":
            wall()
        elif x == 0 and y == -7 and floor == -1 and direction == "north":
            far_wall()
        elif x == 0 and y == -7 and floor == -1 and direction == "west":
            door3()
        elif x == 0 and y == -7 and floor == -1 and direction == "east":
            door2()
        elif x == 0 and y == -7 and floor == -1 and direction == "south":
            door()
        elif x == -1 and y == -7 and floor == -1 and direction == "north":
            left_corner()
        elif x == -1 and y == -7 and floor == -1 and direction == "west":
            door()
        elif x == -1 and y == -7 and floor == -1 and direction == "east":
            twodoors()
        elif x == -1 and y == -7 and floor == -1 and direction == "south":
            wall()
        elif x == -1 and y == -6 and floor == -1 and direction == "north":
            wall()
        elif x == -1 and y == -6 and floor == -1 and direction == "west":
            wall()
        elif x == -1 and y == -6 and floor == -1 and direction == "east":
            far_left_corner()
        elif x == -1 and y == -6 and floor == -1 and direction == "south":
            door_right_corner()
        elif x == 0 and y == -6 and floor == -1 and direction == "north":
            wall()
        elif x == 0 and y == -6 and floor == -1 and direction == "west":
            right_corner()
        elif x == 0 and y == -6 and floor == -1 and direction == "east":
            left_corner()
        elif x == 0 and y == -6 and floor == -1 and direction == "south":
            south_entrance_room_facingnorth()
        elif x == 1 and y == -6 and floor == -1 and direction == "north":
            wall()
        elif x == 1 and y == -6 and floor == -1 and direction == "west":
            far_right_corner()
        elif x == 1 and y == -6 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == -6 and floor == -1 and direction == "south":
            door3()
        elif x == 0 and y == -8 and floor == -1 and direction == "north":
            door()
        elif x == 0 and y == -8 and floor == -1 and direction == "west":
            right_corner()
        elif x == 0 and y == -8 and floor == -1 and direction == "east":
            left_corner()
        elif x == 0 and y == -8 and floor == -1 and direction == "south":
            far_stairs()
        elif x == -1 and y == -8 and floor == -1 and direction == "north":
            wall()
        elif x == -1 and y == -8 and floor == -1 and direction == "west":
            wall()
        elif x == -1 and y == -8 and floor == -1 and direction == "east":
            far_left_corner()
        elif x == -1 and y == -8 and floor == -1 and direction == "south":
            right_corner()
        elif x == 1 and y == -8 and floor == -1 and direction == "north":
            wall()
        elif x == 1 and y == -8 and floor == -1 and direction == "west":
            far_right_corner()
        elif x == 1 and y == -8 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == -8 and floor == -1 and direction == "south":
            left_corner()
        elif x == 1 and y == -9 and floor == -1 and direction == "north":
            right_corner()
        elif x == 1 and y == -9 and floor == -1 and direction == "west":
            far_left_corner()
        elif x == 1 and y == -9 and floor == -1 and direction == "east":
            wall()
        elif x == 1 and y == -9 and floor == -1 and direction == "south":
            wall()
        elif x == 0 and y == -9 and floor == -1 and direction == "north":
            south_entrance_room_facingnorth()
        elif x == 0 and y == -9 and floor == -1 and direction == "west":
            left_corner()
        elif x == 0 and y == -9 and floor == -1 and direction == "east":
            right_corner()
        elif x == 0 and y == -9 and floor == -1 and direction == "south":
            stairs()
        elif x == -1 and y == -9 and floor == -1 and direction == "north":
            left_corner()
        elif x == -1 and y == -9 and floor == -1 and direction == "west":
            door()
        elif x == -1 and y == -9 and floor == -1 and direction == "east":
            far_right_corner()
        elif x == -1 and y == -9 and floor == -1 and direction == "south":
            wall()
        elif x == 0 and y == -10 and floor == -1 and direction == "south":
            if level1boss_alive == True:
                x = 0
                y = -11
                direction = "south"
                floor = -2
                level1boss()
            else:
                x = 0
                y = -11
                direction = "south"
                floor = -2
                print_area()
        elif x == 0 and y == -11 and floor == -2 and direction == "north":
            up_stairs()
        elif x == 0 and y == -11 and floor == -2 and direction == "west":
            wall()
        elif x == 0 and y == -11 and floor == -2 and direction == "east":
            wall()
        elif x == 0 and y == -11 and floor == -2 and direction == "south":
            hall()
        elif x == 0 and y == -12 and floor == -2 and direction == "north":
            hall()
        elif x == 0 and y == -12 and floor == -2 and direction == "west":
            wall()
        elif x == 0 and y == -12 and floor == -2 and direction == "east":
            wall()
        elif x == 0 and y == -12 and floor == -2 and direction == "south":
            hall_4way_split()
        elif x == 0 and y == -13 and floor == -2 and direction == "north":
            hall()
        elif x == 0 and y == -13 and floor == -2 and direction == "west":
            hall()
        elif x == 0 and y == -13 and floor == -2 and direction == "east":
            hall()
        elif x == 0 and y == -13 and floor == -2 and direction == "south":
            hall()
        elif x == 2 and y == -13 and floor == -2 and direction == "north":
            wall()
        elif x == 2 and y == -13 and floor == -2 and direction == "west":
            hall()
        elif x == 2 and y == -13 and floor == -2 and direction == "east":
            hall_4way_split()
        elif x == 2 and y == -13 and floor == -2 and direction == "south":
            wall()
        elif x == 1 and y == -13 and floor == -2 and direction == "north":
            wall()
        elif x == 1 and y == -13 and floor == -2 and direction == "west":
            hall_4_way_split()
        elif x == 1 and y == -13 and floor == -2 and direction == "east":
            hall()
        elif x == 1 and y == -13 and floor == -2 and direction == "south":
            wall()
        elif x == 0 and y == -14 and floor == -2 and direction == "north":
            hall_4way_split()
        elif x == 0 and y == -14 and floor == -2 and direction == "west":
            wall()
        elif x == 0 and y == -14 and floor == -2 and direction == "east":
            wall()
        elif x == 0 and y == -14 and floor == -2 and direction == "south":
            hall()
        elif x == 0 and y == -15 and floor == -2 and direction == "north":
            hall()
        elif x == 0 and y == -15 and floor == -2 and direction == "west":
            wall()
        elif x == 0 and y == -15 and floor == -2 and direction == "east":
            wall()
        elif x == 0 and y == -15 and floor == -2 and direction == "south":
            t_hall()
        elif x == 0 and y == -16 and floor == -2 and direction == "north":
            hall()
        elif x == 0 and y == -16 and floor == -2 and direction == "west":
            hall()
        elif x == 0 and y == -16 and floor == -2 and direction == "east":
            hall()
        elif x == 0 and y == -16 and floor == -2 and direction == "south":
            wall()
        elif x == 1 and y == -16 and floor == -2 and direction == "north":
            wall()
        elif x == 1 and y == -16 and floor == -2 and direction == "west":
            t_hall_right()
        elif x == 1 and y == -16 and floor == -2 and direction == "east":
            hall()
        elif x == 1 and y == -16 and floor == -2 and direction == "south":
            wall()
        elif x == 2 and y == -16 and floor == -2 and direction == "north":
            wall()
        elif x == 2 and y == -16 and floor == -2 and direction == "west":
            hall()
        elif x == 2 and y == -16 and floor == -2 and direction == "east":
            hall_turning_left()
        elif x == 2 and y == -16 and floor == -2 and direction == "south":
            wall()
        elif x == 3 and y == -16 and floor == -2 and direction == "north":
            hall_4way_split()
        elif x == 3 and y == -16 and floor == -2 and direction == "west":
            hall()
        elif x == 3 and y == -16 and floor == -2 and direction == "east":
            wall()
        elif x == 3 and y == -16 and floor == -2 and direction == "south":
            wall()
        elif x == 3 and y == -15 and floor == -2 and direction == "north":
            hall()
        elif x == 3 and y == -15 and floor == -2 and direction == "west":
            hall()
        elif x == 3 and y == -15 and floor == -2 and direction == "east":
            hall()
        elif x == 3 and y == -15 and floor == -2 and direction == "south":
            hall_turning_right()
        elif x == 2 and y == -15 and floor == -2 and direction == "north":
            wall()
        elif x == 2 and y == -15 and floor == -2 and direction == "west":
            hall_turning_right()
        elif x == 2 and y == -15 and floor == -2 and direction == "east":
            hall_4way_split()
        elif x == 2 and y == -15 and floor == -2 and direction == "south":
            wall()
        elif x == 1 and y == -15 and floor == -2 and direction == "north":
            hall_turning_right()
        elif x == 1 and y == -15 and floor == -2 and direction == "west":
            wall()
        elif x == 1 and y == -15 and floor == -2 and direction == "east":
            hall()
        elif x == 1 and y == -15 and floor == -2 and direction == "south":
            wall()
        elif x == 1 and y == -14 and floor == -2 and direction == "north":
            wall()
        elif x == 1 and y == -14 and floor == -2 and direction == "west":
            wall()
        elif x == 1 and y == -14 and floor == -2 and direction == "east":
            hall()
        elif x == 1 and y == -14 and floor == -2 and direction == "south":
            hall_turning_left()
        elif x == 2 and y == -14 and floor == -2 and direction == "north":
            wall()
        elif x == 2 and y == -14 and floor == -2 and direction == "west":
            hall_turning_left()
        elif x == 2 and y == -14 and floor == -2 and direction == "east":
            wall()
        elif x == 2 and y == -14 and floor == -2 and direction == "south":
            wall()
        elif x == 3 and y == -14 and floor == -2 and direction == "north":
            hall_4way_split()
        elif x == 3 and y == -14 and floor == -2 and direction == "west":
            wall()
        elif x == 3 and y == -14 and floor == -2 and direction == "east":
            wall()
        elif x == 3 and y == -14 and floor == -2 and direction == "south":
            hall_4way_split()
        elif x == 3 and y == -13 and floor == -2 and direction == "north":
            hall()
        elif x == 3 and y == -13 and floor == -2 and direction == "west":
            hall()
        elif x == 3 and y == -13 and floor == -2 and direction == "east":
            hall()
        elif x == 3 and y == -13 and floor == -2 and direction == "south":
            hall()
        elif x == 3 and y == -12 and floor == -2 and direction == "north":
            t_hall_right()
        elif x == 3 and y == -12 and floor == -2 and direction == "west":
            wall()
        elif x == 3 and y == -12 and floor == -2 and direction == "east":
            wall()
        elif x == 3 and y == -12 and floor == -2 and direction == "south":
            hall_4way_split()
        elif x == 3 and y == -11 and floor == -2 and direction == "north":
            hall()
        elif x == 3 and y == -11 and floor == -2 and direction == "west":
            wall()
        elif x == 3 and y == -11 and floor == -2 and direction == "east":
            hall()
        elif x == 3 and y == -11 and floor == -2 and direction == "south":
            hall()
        elif x == 3 and y == -10 and floor == -2 and direction == "north":
            hall_turning_left()
        elif x == 3 and y == -10 and floor == -2 and direction == "west":
            wall()
        elif x == 3 and y == -10 and floor == -2 and direction == "east":
            wall()
        elif x == 3 and y == -10 and floor == -2 and direction == "south":
            t_hall_left()
        elif x == 3 and y == -9 and floor == -2 and direction == "north":
            wall()
        elif x == 3 and y == -9 and floor == -2 and direction == "west":
            hall()
        elif x == 3 and y == -9 and floor == -2 and direction == "east":
            wall()
        elif x == 3 and y == -9 and floor == -2 and direction == "south":
            hall()
        elif x == 2 and y == -9 and floor == -2 and direction == "north":
            wall()
        elif x == 2 and y == -9 and floor == -2 and direction == "west":
            t_hall_left()
        elif x == 2 and y == -9 and floor == -2 and direction == "east":
            hall_turning_right()
        elif x == 2 and y == -9 and floor == -2 and direction == "south":
            wall()
        elif x == 1 and y == -9 and floor == -2 and direction == "north":
            wall()
        elif x == 1 and y == -9 and floor == -2 and direction == "west":
            hall()
        elif x == 1 and y == -9 and floor == -2 and direction == "east":
            hall()
        elif x == 1 and y == -9 and floor == -2 and direction == "south":
            hall()
        elif x == 1 and y == -10 and floor == -2 and direction == "north":
            t_hall()
        elif x == 1 and y == -10 and floor == -2 and direction == "west":
            wall()
        elif x == 1 and y == -10 and floor == -2 and direction == "east":
            wall()
        elif x == 1 and y == -10 and floor == -2 and direction == "south":
            hall_turning_left()
        elif x == 1 and y == -11 and floor == -2 and direction == "north":
            hall()
        elif x == 1 and y == -11 and floor == -2 and direction == "west":
            wall()
        elif x == 1 and y == -11 and floor == -2 and direction == "east":
            hall()
        elif x == 1 and y == -11 and floor == -2 and direction == "south":
            wall()
        elif x == 2 and y == -11 and floor == -2 and direction == "north":
            wall()
        elif x == 2 and y == -11 and floor == -2 and direction == "west":
            hall_turning_right()
        elif x == 2 and y == -11 and floor == -2 and direction == "east":
            wall()
        elif x == 2 and y == -11 and floor == -2 and direction == "south":
            wall()
        elif x == 4 and y == -15 and floor == -2 and direction == "north":
            wall()
        elif x == 4 and y == -15 and floor == -2 and direction == "west":
            hall_4way_split()
        elif x == 4 and y == -15 and floor == -2 and direction == "east":
            hall_turning_right()
        elif x == 4 and y == -15 and floor == -2 and direction == "south":
            wall()
        elif x == 5 and y == -15 and floor == -2 and direction == "north":
            wall()
        elif x == 5 and y == -15 and floor == -2 and direction == "west":
            hall()
        elif x == 5 and y == -15 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -15 and floor == -2 and direction == "south":
            hall_turning_right()
        elif x == 5 and y == -16 and floor == -2 and direction == "north":
            hall_turning_left()
        elif x == 5 and y == -16 and floor == -2 and direction == "west":
            hall()
        elif x == 5 and y == -16 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -16 and floor == -2 and direction == "south":
            wall()
        elif x == 4 and y == -16 and floor == -2 and direction == "north":
            wall()
        elif x == 4 and y == -16 and floor == -2 and direction == "west":
            wall()
        elif x == 4 and y == -16 and floor == -2 and direction == "east":
            hall_turning_left()
        elif x == 4 and y == -16 and floor == -2 and direction == "south":
            wall()
        elif x == 4 and y == -13 and floor == -2 and direction == "north":
            wall()
        elif x == 4 and y == -13 and floor == -2 and direction == "west":
            hall_4way_split()
        elif x == 4 and y == -13 and floor == -2 and direction == "east":
            hall_turning_left()
        elif x == 4 and y == -13 and floor == -2 and direction == "south":
            wall()
        elif x == 5 and y == -13 and floor == -2 and direction == "north":
            hall()
        elif x == 5 and y == -13 and floor == -2 and direction == "west":
            hall()
        elif x == 5 and y == -13 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -13 and floor == -2 and direction == "south":
            wall()
        elif x == 5 and y == -12 and floor == -2 and direction == "north":
            t_hall_left()
        elif x == 5 and y == -12 and floor == -2 and direction == "west":
            wall()
        elif x == 5 and y == -12 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -12 and floor == -2 and direction == "south":
            hall_turning_right()
        elif x == 4 and y == -11 and floor == -2 and direction == "north":
            wall()
        elif x == 4 and y == -11 and floor == -2 and direction == "west":
            far_wall()
        elif x == 4 and y == -11 and floor == -2 and direction == "east":
            far_wall()
        elif x == 4 and y == -11 and floor == -2 and direction == "south":
            wall()
        elif x == 5 and y == -11 and floor == -2 and direction == "north":
            hall()
        elif x == 5 and y == -11 and floor == -2 and direction == "west":
            hall()
        elif x == 5 and y == -11 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -11 and floor == -2 and direction == "south":
            hall()
        elif x == 5 and y == -10 and floor == -2 and direction == "north":
            hall()
        elif x == 5 and y == -10 and floor == -2 and direction == "west":
            wall()
        elif x == 5 and y == -10 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -10 and floor == -2 and direction == "south":
            hall()
        elif x == 5 and y == -9 and floor == -2 and direction == "north":
            hall()
        elif x == 5 and y == -9 and floor == -2 and direction == "west":
            wall()
        elif x == 5 and y == -9 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -9 and floor == -2 and direction == "south":
            hall()
        elif x == 5 and y == -8 and floor == -2 and direction == "north":
            hall()
        elif x == 5 and y == -8 and floor == -2 and direction == "west":
            wall()
        elif x == 5 and y == -8 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -8 and floor == -2 and direction == "south":
            hall()
        elif x == 5 and y == -7 and floor == -2 and direction == "north":
            t_hall_left()
        elif x == 5 and y == -7 and floor == -2 and direction == "west":
            wall()
        elif x == 5 and y == -7 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -7 and floor == -2 and direction == "south":
            hall()
        elif x == 5 and y == -6 and floor == -2 and direction == "north":
            hall()
        elif x == 5 and y == -6 and floor == -2 and direction == "west":
            hall()
        elif x == 5 and y == -6 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -6 and floor == -2 and direction == "south":
            hall()
        elif x == 5 and y == -5 and floor == -2 and direction == "north":
            hall()
        elif x == 5 and y == -5 and floor == -2 and direction == "west":
            wall()
        elif x == 5 and y == -5 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -5 and floor == -2 and direction == "south":
            t_hall_right()
        elif x == 5 and y == -4 and floor == -2 and direction == "north":
            hall_turning_left()
        elif x == 5 and y == -4 and floor == -2 and direction == "west":
            wall()
        elif x == 5 and y == -4 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -4 and floor == -2 and direction == "south":
            hall()
        elif x == 5 and y == -3 and floor == -2 and direction == "north":
            wall()
        elif x == 5 and y == -3 and floor == -2 and direction == "west":
            t_hall_right()
        elif x == 5 and y == -3 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -3 and floor == -2 and direction == "south":
            hall()
        elif x == 4 and y == -3 and floor == -2 and direction == "north":
            hall()
        elif x == 4 and y == -3 and floor == -2 and direction == "west":
            hall()
        elif x == 4 and y == -3 and floor == -2 and direction == "east":
            hall_turning_right()
        elif x == 4 and y == -3 and floor == -2 and direction == "south":
            wall()
        elif x == 4 and y == -2 and floor == -2 and direction == "north":
            hall_turning_left()
        elif x == 4 and y == -2 and floor == -2 and direction == "west":
            wall()
        elif x == 4 and y == -2 and floor == -2 and direction == "east":
            wall()
        elif x == 4 and y == -2 and floor == -2 and direction == "south":
            t_hall()
        elif x == 4 and y == -1 and floor == -2 and direction == "north":
            wall()
        elif x == 4 and y == -1 and floor == -2 and direction == "west":
            hall_4way_split()
        elif x == 4 and y == -1 and floor == -2 and direction == "east":
            wall()
        elif x == 4 and y == -1 and floor == -2 and direction == "south":
            hall()
        elif x == 3 and y == -3 and floor == -2 and direction == "north":
            hall()
        elif x == 3 and y == -3 and floor == -2 and direction == "west":
            hall_turning_right()
        elif x == 3 and y == -3 and floor == -2 and direction == "east":
            t_hall_left()
        elif x == 3 and y == -3 and floor == -2 and direction == "south":
            wall()
        elif x == 3 and y == -2 and floor == -2 and direction == "north":
            hall_4way_split()
        elif x == 3 and y == -2 and floor == -2 and direction == "west":
            wall()
        elif x == 3 and y == -2 and floor == -2 and direction == "east":
            wall()
        elif x == 3 and y == -2 and floor == -2 and direction == "south":
            far_wall()
        elif x == 3 and y == -1 and floor == -2 and direction == "north":
            hall()
        elif x == 3 and y == -1 and floor == -2 and direction == "west":
            hall()
        elif x == 3 and y == -1 and floor == -2 and direction == "east":
            hall_turning_right()
        elif x == 3 and y == -1 and floor == -2 and direction == "south":
            hall()
        elif x == 3 and y == 0 and floor == -2 and direction == "north":
            t_hall()
        elif x == 3 and y == 0 and floor == -2 and direction == "west":
            wall()
        elif x == 3 and y == 0 and floor == -2 and direction == "east":
            wall()
        elif x == 3 and y == 0 and floor == -2 and direction == "south":
            hall_4way_split()
        elif x == 3 and y == -1 and floor == -2 and direction == "north":
            wall()
        elif x == 3 and y == -1 and floor == -2 and direction == "west":
            hall()
        elif x == 3 and y == -1 and floor == -2 and direction == "east":
            hall()
        elif x == 3 and y == -1 and floor == -2 and direction == "south":
            hall()
        elif x == 4 and y == -1 and floor == -2 and direction == "north":
            wall()
        elif x == 4 and y == -1 and floor == -2 and direction == "west":
            t_hall_left()
        elif x == 4 and y == -1 and floor == -2 and direction == "east":
            hall_turning_right()
        elif x == 4 and y == -1 and floor == -2 and direction == "south":
            wall()
        elif x == 5 and y == -1 and floor == -2 and direction == "north":
            wall()
        elif x == 5 and y == -1 and floor == -2 and direction == "west":
            hall()
        elif x == 5 and y == -1 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -1 and floor == -2 and direction == "south":
            hall()
        elif x == 5 and y == 0 and floor == -2 and direction == "north":
            hall_turning_left()
        elif x == 5 and y == 0 and floor == -2 and direction == "west":
            wall()
        elif x == 5 and y == 0 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == 0 and floor == -2 and direction == "south":
            hall()
        elif x == 5 and y == -1 and floor == -2 and direction == "north":
            hall()
        elif x == 5 and y == -1 and floor == -2 and direction == "west":
            wall()
        elif x == 5 and y == -1 and floor == -2 and direction == "east":
            wall()
        elif x == 5 and y == -1 and floor == -2 and direction == "south":
            wall()
        elif x == 2 and y == 1 and floor == -2 and direction == "north":
            wall()
        elif x == 2 and y == 1 and floor == -2 and direction == "west":
            hall()
        elif x == 2 and y == 1 and floor == -2 and direction == "east":
            t_hall_right()
        elif x == 2 and y == 1 and floor == -2 and direction == "south":
            wall()
        elif x == 1 and y == 1 and floor == -2 and direction == "north":
            wall()
        elif x == 1 and y == 1 and floor == -2 and direction == "west":
            hall_turning_left()
        elif x == 1 and y == 1 and floor == -2 and direction == "east":
            hall()
        elif x == 1 and y == 1 and floor == -2 and direction == "south":
            wall()
        elif x == 0 and y == 1 and floor == -2 and direction == "north":
            hall_door_on_end()
        elif x == 0 and y == 1 and floor == -2 and direction == "west":
            wall()
        elif x == 0 and y == 1 and floor == -2 and direction == "east":
            hall()
        elif x == 0 and y == 1 and floor == -2 and direction == "south":
            wall()
        elif x == 0 and y == 2 and floor == -2 and direction == "north":
            door()
        elif x == 0 and y == 2 and floor == -2 and direction == "west":
            wall()
        elif x == 0 and y == 2 and floor == -2 and direction == "east":
            wall()
        elif x == 0 and y == 2 and floor == -2 and direction == "south":
            hall_turning_left()
        elif x == -1 and y == -13 and floor == -2 and direction == "north":
            wall()
        elif x == -1 and y == -13 and floor == -2 and direction == "west":
            hall_turning_left()
        elif x == -1 and y == -13 and floor == -2 and direction == "east":
            hall_4way_split()
        elif x == -1 and y == -13 and floor == -2 and direction == "south":
            wall()
        elif x == -2 and y == -13 and floor == -2 and direction == "north":
            wall()
        elif x == -2 and y == -13 and floor == -2 and direction == "west":
            wall()
        elif x == -2 and y == -13 and floor == -2 and direction == "east":
            hall()
        elif x == -2 and y == -13 and floor == -2 and direction == "south":
            hall()
        elif x == -2 and y == -14 and floor == -2 and direction == "north":
            hall_turning_right()
        elif x == -2 and y == -14 and floor == -2 and direction == "west":
            wall()
        elif x == -2 and y == -14 and floor == -2 and direction == "east":
            wall()
        elif x == -2 and y == -14 and floor == -2 and direction == "south":
            hall_turning_left()
        elif x == -1 and y == -14 and floor == -2 and direction == "north":
            hall()
        elif x == -1 and y == -14 and floor == -2 and direction == "west":
            hall_turning_right()
        elif x == -1 and y == -14 and floor == -2 and direction == "east":
            wall()
        elif x == -1 and y == -14 and floor == -2 and direction == "south":
            wall()
        elif x == -1 and y == -13 and floor == -2 and direction == "north":
            wall()
        elif x == -1 and y == -13 and floor == -2 and direction == "west":
            wall()
        elif x == -1 and y == -13 and floor == -2 and direction == "east":
            wall()
        elif x == -1 and y == -13 and floor == -2 and direction == "south":
            hall_turning_right()
        elif x == -1 and y == -16 and floor == -2 and direction == "north":
            wall()
        elif x == -1 and y == -16 and floor == -2 and direction == "west":
            hall()
        elif x == -1 and y == -16 and floor == -2 and direction == "east":
            wall()
        elif x == -1 and y == -16 and floor == -2 and direction == "south":
            wall()
        elif x == -2 and y == -16 and floor == -2 and direction == "north":
            wall()
        elif x == -2 and y == -16 and floor == -2 and direction == "west":
            t_hall_right()
        elif x == -2 and y == -16 and floor == -2 and direction == "east":
            hall()
        elif x == -2 and y == -16 and floor == -2 and direction == "south":
            wall()
        elif x == -3 and y == -16 and floor == -2 and direction == "north":
            hall()
        elif x == -3 and y == -16 and floor == -2 and direction == "west":
            hall()
        elif x == -3 and y == -16 and floor == -2 and direction == "east":
            hall()
        elif x == -3 and y == -16 and floor == -2 and direction == "south":
            wall()
        elif x == -4 and y == -16 and floor == -2 and direction == "north":
            wall()
        elif x == -4 and y == -16 and floor == -2 and direction == "west":
            hall_turning_right()
        elif x == -4 and y == -16 and floor == -2 and direction == "east":
            hall()
        elif x == -4 and y == -16 and floor == -2 and direction == "south":
            wall()
        elif x == -5 and y == -16 and floor == -2 and direction == "north":
            hall()
        elif x == -5 and y == -16 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == -16 and floor == -2 and direction == "east":
            hall()
        elif x == -5 and y == -16 and floor == -2 and direction == "south":
            wall()
        elif x == -5 and y == -15 and floor == -2 and direction == "north":
            hall()
        elif x == -5 and y == -15 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == -15 and floor == -2 and direction == "east":
            wall()
        elif x == -5 and y == -15 and floor == -2 and direction == "south":
            hall_turning_left()
        elif x == -5 and y == -14 and floor == -2 and direction == "north":
            hall_turning_right()
        elif x == -5 and y == -14 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == -14 and floor == -2 and direction == "east":
            wall()
        elif x == -5 and y == -14 and floor == -2 and direction == "south":
            hall()
        elif x == -5 and y == -13 and floor == -2 and direction == "north":
            wall()
        elif x == -5 and y == -13 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == -13 and floor == -2 and direction == "east":
            hall()
        elif x == -5 and y == -13 and floor == -2 and direction == "south":
            hall()
        elif x == -4 and y == -13 and floor == -2 and direction == "north":
            wall()
        elif x == -4 and y == -13 and floor == -2 and direction == "west":
            hall_turning_left()
        elif x == -4 and y == -13 and floor == -2 and direction == "east":
            t_hall()
        elif x == -4 and y == -13 and floor == -2 and direction == "south":
            wall()
        elif x == -3 and y == -15 and floor == -2 and direction == "north":
             hall()
        elif x == -3 and y == -15 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -15 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -15 and floor == -2 and direction == "south":
            t_hall()
        elif x == -3 and y == -14 and floor == -2 and direction == "north":
            t_hall_left()
        elif x == -3 and y == -14 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -14 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -14 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -13 and floor == -2 and direction == "north":
            hall()
        elif x == -3 and y == -13 and floor == -2 and direction == "west":
            hall()
        elif x == -3 and y == -13 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -13 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -12 and floor == -2 and direction == "north":
            hall()
        elif x == -3 and y == -12 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -12 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -12 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -11 and floor == -2 and direction == "north":
            hall()
        elif x == -3 and y == -11 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -11 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -11 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -10 and floor == -2 and direction == "north":
            hall_4way_split()
        elif x == -3 and y == -10 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -10 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -10 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -9 and floor == -2 and direction == "north":
            hall()
        elif x == -3 and y == -9 and floor == -2 and direction == "west":
            hall()
        elif x == -3 and y == -9 and floor == -2 and direction == "east":
            hall()
        elif x == -3 and y == -9 and floor == -2 and direction == "south":
            hall()
        elif x == -4 and y == -9 and floor == -2 and direction == "north":
            wall()
        elif x == -4 and y == -9 and floor == -2 and direction == "west":
            hall_turning_left()
        elif x == -4 and y == -9 and floor == -2 and direction == "east":
            hall_4way_split()
        elif x == -4 and y == -9 and floor == -2 and direction == "south":
            wall()
        elif x == -3 and y == -9 and floor == -2 and direction == "north":
            wall()
        elif x == -3 and y == -9 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -9 and floor == -2 and direction == "east":
            hall()
        elif x == -3 and y == -9 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -10 and floor == -2 and direction == "north":
            hall_turning_right()
        elif x == -3 and y == -10 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -10 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -10 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -11 and floor == -2 and direction == "north":
            hall()
        elif x == -3 and y == -11 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -11 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -11 and floor == -2 and direction == "south":
            wall()
        elif x == -2 and y == -9 and floor == -2 and direction == "north":
            wall()
        elif x == -2 and y == -9 and floor == -2 and direction == "west":
            hall_4way_split()
        elif x == -2 and y == -9 and floor == -2 and direction == "east":
            hall_4way_split()
        elif x == -2 and y == -9 and floor == -2 and direction == "south":
            wall()
        elif x == -1 and y == -9 and floor == -2 and direction == "north":
            hall()
        elif x == -1 and y == -9 and floor == -2 and direction == "west":
            hall()
        elif x == -1 and y == -9 and floor == -2 and direction == "east":
            hall()
        elif x == -1 and y == -9 and floor == -2 and direction == "south":
            hall()
        elif x == -1 and y == -10 and floor == -2 and direction == "north":
            hall_4way_split()
        elif x == -1 and y == -10 and floor == -2 and direction == "west":
            wall()
        elif x == -1 and y == -10 and floor == -2 and direction == "east":
            wall()
        elif x == -1 and y == -10 and floor == -2 and direction == "south":
            hall_turning_right()
        elif x == -1 and y == -11 and floor == -2 and direction == "north":
            hall()
        elif x == -1 and y == -11 and floor == -2 and direction == "west":
            chest()
        elif x == -1 and y == -11 and floor == -2 and direction == "east":
            wall()
        elif x == -1 and y == -11 and floor == -2 and direction == "south":
            wall()
        elif x == -1 and y == -8 and floor == -2 and direction == "north":
            hall()
        elif x == -1 and y == -8 and floor == -2 and direction == "west":
            wall()
        elif x == -1 and y == -8 and floor == -2 and direction == "east":
            wall()
        elif x == -1 and y == -8 and floor == -2 and direction == "south":
            hall_4way_split()
        elif x == -1 and y == -7 and floor == -2 and direction == "north":
            hall_4way_split()
        elif x == -1 and y == -7 and floor == -2 and direction == "west":
            wall()
        elif x == -1 and y == -7 and floor == -2 and direction == "east":
            wall()
        elif x == -1 and y == -7 and floor == -2 and direction == "south":
            hall()
        elif x == -1 and y == -6 and floor == -2 and direction == "north":
            hall()
        elif x == -1 and y == -6 and floor == -2 and direction == "west":
            hall()
        elif x == -1 and y == -6 and floor == -2 and direction == "east":
            hall()
        elif x == -1 and y == -6 and floor == -2 and direction == "south":
            hall()
        elif x == 0 and y == -6 and floor == -2 and direction == "north":
            wall()
        elif x == 0 and y == -6 and floor == -2 and direction == "west":
            hall_4way_split()
        elif x == 0 and y == -6 and floor == -2 and direction == "east":
            hall()
        elif x == 0 and y == -6 and floor == -2 and direction == "south":
            wall()
        elif x == 1 and y == -6 and floor == -2 and direction == "north":
            wall()
        elif x == 1 and y == -6 and floor == -2 and direction == "west":
            hall()
        elif x == 1 and y == -6 and floor == -2 and direction == "east":
            t_hall_left()
        elif x == 1 and y == -6 and floor == -2 and direction == "south":
            wall()
        elif x == 2 and y == -6 and floor == -2 and direction == "north":
            hall()
        elif x == 2 and y == -6 and floor == -2 and direction == "west":
            hall()
        elif x == 2 and y == -6 and floor == -2 and direction == "east":
            t_hall_right()
        elif x == 2 and y == -6 and floor == -2 and direction == "south":
            wall()
        elif x == 3 and y == -6 and floor == -2 and direction == "north":
            wall()
        elif x == 3 and y == -6 and floor == -2 and direction == "west":
            t_hall_right()
        elif x == 3 and y == -6 and floor == -2 and direction == "east":
            hall()
        elif x == 3 and y == -6 and floor == -2 and direction == "south":
            hall()
        elif x == 4 and y == -6 and floor == -2 and direction == "north":
            wall()
        elif x == 4 and y == -6 and floor == -2 and direction == "west":
            t_hall_left()
        elif x == 4 and y == -6 and floor == -2 and direction == "east":
            t_hall()
        elif x == 4 and y == -6 and floor == -2 and direction == "south":
            wall()
        elif x == 3 and y == -6 and floor == -2 and direction == "north":
            t_hall()
        elif x == 3 and y == -6 and floor == -2 and direction == "west":
            wall()
        elif x == 3 and y == -6 and floor == -2 and direction == "east":
            wall()
        elif x == 3 and y == -6 and floor == -2 and direction == "south":
            t_hall()
        elif x == 3 and y == -7 and floor == -2 and direction == "north":
            hall()
        elif x == 3 and y == -7 and floor == -2 and direction == "west":
            hall()
        elif x == 3 and y == -7 and floor == -2 and direction == "east":
            hall_turning_right()
        elif x == 3 and y == -7 and floor == -2 and direction == "south":
            wall()
        elif x == 2 and y == -7 and floor == -2 and direction == "north":
            wall()
        elif x == 2 and y == -7 and floor == -2 and direction == "west":
            hall()
        elif x == 2 and y == -7 and floor == -2 and direction == "east":
            t_hall_left()
        elif x == 2 and y == -7 and floor == -2 and direction == "south":
            wall()
        elif x == 1 and y == -7 and floor == -2 and direction == "north":
            wall()
        elif x == 1 and y == -7 and floor == -2 and direction == "west":
            wall()
        elif x == 1 and y == -7 and floor == -2 and direction == "east":
            hall()
        elif x == 1 and y == -7 and floor == -2 and direction == "south":
            wall()
        elif x == 4 and y == -7 and floor == -2 and direction == "north":
            wall()
        elif x == 4 and y == -7 and floor == -2 and direction == "west":
            t_hall_right()
        elif x == 4 and y == -7 and floor == -2 and direction == "east":
            wall()
        elif x == 4 and y == -7 and floor == -2 and direction == "south":
            hall()
        elif x == 4 and y == -8 and floor == -2 and direction == "north":
            right_corner()
        elif x == 4 and y == -8 and floor == -2 and direction == "west":
            wall()
        elif x == 4 and y == -8 and floor == -2 and direction == "east":
            wall()
        elif x == 4 and y == -8 and floor == -2 and direction == "south":
            chest()
        elif x == 2 and y == -5 and floor == -2 and direction == "north":
            t_hall()
        elif x == 2 and y == -5 and floor == -2 and direction == "west":
            wall()
        elif x == 2 and y == -5 and floor == -2 and direction == "east":
            wall()
        elif x == 2 and y == -5 and floor == -2 and direction == "south":
            t_hall()
        elif x == 2 and y == -4 and floor == -2 and direction == "north":
            wall()
        elif x == 2 and y == -4 and floor == -2 and direction == "west":
            hall_turning_right()
        elif x == 2 and y == -4 and floor == -2 and direction == "east":
            hall()
        elif x == 3 and y == -4 and floor == -2 and direction == "north":
            wall()
        elif x == 3 and y == -4 and floor == -2 and direction == "west":
            t_hall_left()
        elif x == 3 and y == -4 and floor == -2 and direction == "east":
            hall()
        elif x == 4 and y == -4 and floor == -2 and direction == "north":
            wall()
        elif x == 4 and y == -4 and floor == -2 and direction == "west":
            hall()
        elif x == 4 and y == -4 and floor == -2 and direction == "east":
            wall()
        elif x == 4 and y == -4 and floor == -2 and direction == "south":
            wall()
        elif x == 1 and y == -4 and floor == -2 and direction == "north":
            hall()
        elif x == 1 and y == -4 and floor == -2 and direction == "west":
            hall()
        elif x == 1 and y == -4 and floor == -2 and direction == "east":
            t_hall_right()
        elif x == 1 and y == -4 and floor == -2 and direction == "south":
            wall()
        elif x == 1 and y == -3 and floor == -2 and direction == "north":
            t_hall_right()
        elif x == 1 and y == -3 and floor == -2 and direction == "west":
            wall()
        elif x == 1 and y == -3 and floor == -2 and direction == "east":
            wall()
        elif x == 1 and y == -3 and floor == -2 and direction == "south":
            hall()
        elif x == 2 and y == -3 and floor == -2 and direction == "north":
            wall()
        elif x == 2 and y == -3 and floor == -2 and direction == "west":
            t_hall()
        elif x == 2 and y == -3 and floor == -2 and direction == "east":
            wall()
        elif x == 2 and y == -3 and floor == -2 and direction == "south":
            right_corner()
        elif x == 3 and y == -4 and floor == -2 and direction == "north":
            right_corner()
        elif x == 3 and y == -4 and floor == -2 and direction == "west":
            wall()
        elif x == 3 and y == -4 and floor == -2 and direction == "east":
            t_hall_right()
        elif x == 3 and y == -4 and floor == -2 and direction == "south":
            wall()
        elif x == 1 and y == -2 and floor == -2 and direction == "north":
            t_hall()
        elif x == 1 and y == -2 and floor == -2 and direction == "west":
            wall()
        elif x == 1 and y == -2 and floor == -2 and direction == "east":
            left_corner()
        elif x == 1 and y == -1 and floor == -2 and direction == "north":
            wall()
        elif x == 1 and y == -1 and floor == -2 and direction == "west":
            hall()
        elif x == 1 and y == -1 and floor == -2 and direction == "east":
            hall()
        elif x == 1 and y == -1 and floor == -2 and direction == "south":
            t_hall_left()
        elif x == 2 and y == -1 and floor == -2 and direction == "north":
            wall()
        elif x == 2 and y == -1 and floor == -2 and direction == "west":
            t_hall_left()
        elif x == 2 and y == -1 and floor == -2 and direction == "east":
            hall_4way_split()
        elif x == 2 and y == -1 and floor == -2 and direction == "south":
            wall()
        elif x == 0 and y == -1 and floor == -2 and direction == "north":
            wall()
        elif x == 0 and y == -1 and floor == -2 and direction == "west":
            t_hall_left()
        elif x == 0 and y == -1 and floor == -2 and direction == "east":
            t_hall_right()
        elif x == 0 and y == -1 and floor == -2 and direction == "south":
            wall()
        elif x == -1 and y == -1 and floor == -2 and direction == "north":
            wall()
        elif x == -1 and y == -1 and floor == -2 and direction == "west":
            hall()
        elif x == -1 and y == -1 and floor == -2 and direction == "east":
            hall()
        elif x == -1 and y == -1 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -8 and floor == -2 and direction == "north":
            hall_turning_left()
        elif x == -3 and y == -8 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -8 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -8 and floor == -2 and direction == "south":
            hall_4way_split()
        elif x == -3 and y == -7 and floor == -2 and direction == "north":
            wall()
        elif x == -3 and y == -7 and floor == -2 and direction == "west":
            hall()
        elif x == -3 and y == -7 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -7 and floor == -2 and direction == "south":
            hall()
        elif x == -4 and y == -7 and floor == -2 and direction == "north":
            wall()
        elif x == -4 and y == -7 and floor == -2 and direction == "west":
            hall_turning_right()
        elif x == -4 and y == -7 and floor == -2 and direction == "east":
            hall_turning_right()
        elif x == -4 and y == -7 and floor == -2 and direction == "south":
            wall()
        elif x == -5 and y == -7 and floor == -2 and direction == "north":
            hall()
        elif x == -5 and y == -7 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == -7 and floor == -2 and direction == "east":
            wall()
        elif x == -5 and y == -7 and floor == -2 and direction == "south":
            hall_turning_left()
        elif x == -5 and y == -6 and floor == -2 and direction == "north":
            hall()
        elif x == -5 and y == -6 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == -6 and floor == -2 and direction == "east":
            wall()
        elif x == -5 and y == -6 and floor == -2 and direction == "south":
            hall()
        elif x == -5 and y == -5 and floor == -2 and direction == "north":
            hall()
        elif x == -5 and y == -5 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == -5 and floor == -2 and direction == "east":
            wall()
        elif x == -5 and y == -5 and floor == -2 and direction == "south":
            hall()
        elif x == -5 and y == -4 and floor == -2 and direction == "north":
            hall()
        elif x == -5 and y == -4 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == -4 and floor == -2 and direction == "east":
            wall()
        elif x == -5 and y == -4 and floor == -2 and direction == "south":
            hall()
        elif x == -5 and y == -3 and floor == -2 and direction == "north":
            hall()
        elif x == -5 and y == -3 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == -3 and floor == -2 and direction == "east":
            wall()
        elif x == -5 and y == -3 and floor == -2 and direction == "south":
            hall()
        elif x == -5 and y == -2 and floor == -2 and direction == "north":
            hall()
        elif x == -5 and y == -2 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == -2 and floor == -2 and direction == "east":
            wall()
        elif x == -5 and y == -2 and floor == -2 and direction == "south":
            hall()
        elif x == -5 and y == -1 and floor == -2 and direction == "north":
            hall_turning_right()
        elif x == -5 and y == -1 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == -1 and floor == -2 and direction == "east":
            wall()
        elif x == -5 and y == -1 and floor == -2 and direction == "south":
            hall()
        elif x == -5 and y == 0 and floor == -2 and direction == "north":
            wall()
        elif x == -5 and y == 0 and floor == -2 and direction == "west":
            wall()
        elif x == -5 and y == 0 and floor == -2 and direction == "east":
            hall()
        elif x == -5 and y == 0 and floor == -2 and direction == "south":
            hall()
        elif x == -4 and y == 0 and floor == -2 and direction == "north":
            wall()
        elif x == -4 and y == 0 and floor == -2 and direction == "west":
            hall_turning_left()
        elif x == -4 and y == 0 and floor == -2 and direction == "east":
            t_hall_right()
        elif x == -4 and y == 0 and floor == -2 and direction == "south":
            wall()
        elif x == -3 and y == 0 and floor == -2 and direction == "north":
            wall()
        elif x == -3 and y == 0 and floor == -2 and direction == "west":
            hall()
        elif x == -3 and y == 0 and floor == -2 and direction == "east":
            hall()
        elif x == -3 and y == 0 and floor == -2 and direction == "south":
            t_hall_left()
        elif x == -2 and y == 0 and floor == -2 and direction == "north":
            wall()
        elif x == -2 and y == 0 and floor == -2 and direction == "west":
            t_hall_left()
        elif x == -2 and y == 0 and floor == -2 and direction == "east":
            hall()
        elif x == -2 and y == 0 and floor == -2 and direction == "south":
            wall()
        elif x == -1 and y == 0 and floor == -2 and direction == "north":
            wall()
        elif x == -1 and y == 0 and floor == -2 and direction == "west":
            hall()
        elif x == -1 and y == 0 and floor == -2 and direction == "east":
            hall()
        elif x == -1 and y == 0 and floor == -2 and direction == "south":
            wall()
        elif x == 0 and y == 0 and floor == -2 and direction == "north":
            wall()
        elif x == 0 and y == 0 and floor == -2 and direction == "west":
            hall()
        elif x == 0 and y == 0 and floor == -2 and direction == "east":
            hall()
        elif x == 0 and y == 0 and floor == -2 and direction == "south":
            wall()
        elif x == 0 and y == -1 and floor == -2 and direction == "north":
            wall()
        elif x == 0 and y == -1 and floor == -2 and direction == "west":
            hall()
        elif x == 0 and y == -1 and floor == -2 and direction == "east":
            chest()
        elif x == 0 and y == -1 and floor == -2 and direction == "south":
            wall()
        elif x == -1 and y == -6 and floor == -2 and direction == "north":
            hall()
        elif x == -1 and y == -6 and floor == -2 and direction == "west":
            hall()
        elif x == -1 and y == -6 and floor == -2 and direction == "east":
            hall()
        elif x == -1 and y == -6 and floor == -2 and direction == "south":
            hall()
        elif x == -1 and y == -5 and floor == -2 and direction == "north":
            t_hall_right()
        elif x == -1 and y == -5 and floor == -2 and direction == "west":
            wall()
        elif x == -1 and y == -5 and floor == -2 and direction == "east":
            wall()
        elif x == -1 and y == -5 and floor == -2 and direction == "south":
            hall_4way_split()
        elif x == -1 and y == -4 and floor == -2 and direction == "north":
            hall()
        elif x == -1 and y == -4 and floor == -2 and direction == "west":
            wall()
        elif x == -1 and y == -4 and floor == -2 and direction == "east":
            hall()
        elif x == -1 and y == -4 and floor == -2 and direction == "south":
            hall()
        elif x == -1 and y == -3 and floor == -2 and direction == "north":
            wall()
        elif x == -1 and y == -3 and floor == -2 and direction == "west":
            wall()
        elif x == -1 and y == -3 and floor == -2 and direction == "east":
            wall()
        elif x == -1 and y == -3 and floor == -2 and direction == "south":
            t_hall_left()
        elif x == -1 and y == -2 and floor == -2 and direction == "north":
            t_hall()
        elif x == -1 and y == -2 and floor == -2 and direction == "west":
            wall()
        elif x == -1 and y == -2 and floor == -2 and direction == "east":
            wall()
        elif x == -1 and y == -2 and floor == -2 and direction == "south":
            hall()
        elif x == -1 and y == -1 and floor == -2 and direction == "north":
            wall()
        elif x == -1 and y == -1 and floor == -2 and direction == "west":
            hall()
        elif x == -1 and y == -1 and floor == -2 and direction == "east":
            hall()
        elif x == -1 and y == -1 and floor == -2 and direction == "south":
            hall()
        elif x == -2 and y == -1 and floor == -2 and direction == "north":
            wall()
        elif x == -2 and y == -1 and floor == -2 and direction == "west":
            t_hall()
        elif x == -2 and y == -1 and floor == -2 and direction == "east":
            t_hall_right()
        elif x == -2 and y == -1 and floor == -2 and direction == "south":
            wall()
        elif x == -3 and y == -1 and floor == -2 and direction == "north":
            t_hall()
        elif x == -3 and y == -1 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -1 and floor == -2 and direction == "east":
            hall()
        elif x == -3 and y == -1 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -2 and floor == -2 and direction == "north":
            t_hall_right()
        elif x == -3 and y == -2 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -2 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -2 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -3 and floor == -2 and direction == "north":
            hall()
        elif x == -3 and y == -3 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -3 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -3 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -4 and floor == -2 and direction == "north":
            hall()
        elif x == -3 and y == -4 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -4 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -4 and floor == -2 and direction == "south":
            hall()
        elif x == -3 and y == -5 and floor == -2 and direction == "north":
            hall()
        elif x == -3 and y == -5 and floor == -2 and direction == "west":
            wall()
        elif x == -3 and y == -5 and floor == -2 and direction == "east":
            wall()
        elif x == -3 and y == -5 and floor == -2 and direction == "south":
            t_hall()
        elif x == -3 and y == -6 and floor == -2 and direction == "north":
            hall()
        elif x == -3 and y == -6 and floor == -2 and direction == "west":
            hall_turning_right()
        elif x == -3 and y == -6 and floor == -2 and direction == "east":
            hall()
        elif x == -3 and y == -6 and floor == -2 and direction == "south":
            wall()
        elif x == -4 and y == -6 and floor == -2 and direction == "north":
            hall()
        elif x == -4 and y == -6 and floor == -2 and direction == "west":
            wall()
        elif x == -4 and y == -6 and floor == -2 and direction == "east":
            t_hall_left()
        elif x == -4 and y == -6 and floor == -2 and direction == "south":
            wall()
        elif x == -4 and y == -5 and floor == -2 and direction == "north":
            wall()
        elif x == -4 and y == -6 and floor == -2 and direction == "west":
            wall()
        elif x == -4 and y == -6 and floor == -2 and direction == "east":
            wall()
        elif x == -4 and y == -6 and floor == -2 and direction == "south":
            hall_turning_left()
        elif x == 0 and y == 3 and floor == -2 and direction == "north":
            hall()
        elif x == 0 and y == 3 and floor == -2 and direction == "west":
            wall()
        elif x == 0 and y == 3 and floor == -2 and direction == "east":
            wall()
        elif x == 0 and y == 3 and floor == -2 and direction == "south":
            door()
        elif x == 0 and y == 4 and floor == -2 and direction == "north":
            stairs()
        elif x == 0 and y == 4 and floor == -2 and direction == "west":
            wall()
        elif x == 0 and y == 4 and floor == -2 and direction == "east":
            wall()
        elif x == 0 and y == 4 and floor == -2 and direction == "south":
            hall_door_on_end()
        elif x == 0 and y == 5 and floor == -2 and direction == "north":
            if level2boss_alive == True:
                x = 0
                y = 5
                direction = "north"
                floor -= 1
                level2boss()
            else:
                x = 0
                y = 5
                direction = "north"
                floor -= 1
                print_area()
        elif x == 0 and y == 6 and floor == -3 and direction == "north":
            hall_door_on_end()
        elif x == 0 and y == 6 and floor == -2 and direction == "west":
            wall()
        elif x == 0 and y == 6 and floor == -3 and direction == "east":
            wall()
        elif x == 0 and y == 6 and floor == -3 and direction == "south":
            up_stairs()
        elif x == 0 and y == 7 and floor == -3 and direction == "north":
            last_door()
        elif x == 0 and y == 7 and floor == -3 and direction == "west":
            wall()
        elif x == 0 and y == 7 and floor == -3 and direction == "east":
            wall()
        elif x == 0 and y == 7 and floor == -3 and direction == "south":
            hall()
        else:
            print("ERROR")

def south_entrance_room_facingwest():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                                                     |          name: {player1.name}")
    print(f"         |                                                                                     |                                              {player1.gold} gold")
    print(f"         |                                                                                     |          class: {player1.Class}")                                                
    print(f"         |                                                       ____________                  |                                              {inventory[0]}")
    print(f"         |                                                      |            |                 |          level: {player1.level}")
    print(f"         |                                                      |   |      | |                 |                                              {inventory[1]}")
    print(f"         |                                                      |   |        |                 |          health: {player1.health}")
    print(f"         |                                                      |            |                 |                                              {inventory[2]}")
    print(f"         |                                                      |     |    O |                 |          strength: {player1.strength}")
    print(f"         |                                                      |     |      |                 |                                              {inventory[3]}")
    print(f"         |                                                      | |        | |                 |          endurance: {player1.endurance}")
    print(f"         |______________________________________________________|____________|_________________|                                              {inventory[4]}")
    print(f"         |                                                                                     |          dexterity: {player1.dexterity}")
    print(f"         |    ️                                                                               |                                              {inventory[5]}")
    print(f"         |                                                                                     |          magic: {player1.magic}")
    print(f"         |                                       ️                                            |                                              {inventory[6]}")
    print(f"         |                                                                                     |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                                                     |                                              {inventory[7]}")
    print(f"         |        ️                                                                           |          condition: {player1.condition}")
    print(f"         |                                                                                     |                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                            ️                                       |                                              {inventory[9]}")
    print(f"         |                                                                     ️              |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    if just_entered == True:
        print("You turn and see another door in the large room. As you look around, you feel an eerie presence lurking in the shadows.")
        just_entered = False
    else:
        print("You see a door.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def south_entrance_room_facingeast():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                                                     |          name: {player1.name}")
    print(f"         |                                                                                     |                                              {player1.gold} gold")
    print(f"         |                                                                                     |          class: {player1.Class}")                                                
    print(f"         |                  ____________                                                       |                                              {inventory[0]}")
    print(f"         |                 |            |                                                      |          level: {player1.level}")
    print(f"         |                 |   |      | |                                                      |                                              {inventory[1]}")
    print(f"         |                 |   |        |                                                      |          health: {player1.health}")
    print(f"         |                 |            |                                                      |                                              {inventory[2]}")
    print(f"         |                 |     |    O |                                                      |          strength: {player1.strength}")
    print(f"         |                 |     |      |                                                      |                                              {inventory[3]}")
    print(f"         |                 | |        | |                                                      |          endurance: {player1.endurance}")
    print(f"         |_________________|____________|______________________________________________________|                                              {inventory[4]}")
    print(f"         |                                                                                     |          dexterity: {player1.dexterity}")
    print(f"         |    ️                                                                               |                                              {inventory[5]}")
    print(f"         |                                                                                     |          magic: {player1.magic}")
    print(f"         |                                       ️                                            |                                              {inventory[6]}")
    print(f"         |                                                                                     |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                                                     |                                              {inventory[7]}")
    print(f"         |        ️                                                                           |          condition: {player1.condition}")
    print(f"         |                                                                                     |                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                            ️                                       |                                              {inventory[9]}")
    print(f"         |                                                                     ️              |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    if just_entered == True:
        print("You turn and see another door in the large room. As you look around, you feel an eerie presence lurking in the shadows.")
        just_entered = False
    else:
        print("You see a door.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def twodoors():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                      |                              |          name: {player1.name}")
    print(f"         |                                                      |                              |                                              {player1.gold} gold")
    print(f"         |                                                      |                              |          class: {player1.Class}")                                                
    print(f"         |                  ____________                        |                              |                                              {inventory[0]}")
    print(f"         |                 |            |                       |                              |          level: {player1.level}")
    print(f"         |                 |   |      | |                       |          /\\                  |                                              {inventory[1]}")
    print(f"         |                 |   |        |                       |         /  \\                 |          health: {player1.health}")
    print(f"         |                 |            |                       |        / /  \\                |                                              {inventory[2]}")
    print(f"         |                 |     |    O |                       |       /      \\               |          strength: {player1.strength}")
    print(f"         |                 |     |      |                       |      /        \\              |                                              {inventory[3]}")
    print(f"         |                 | |        | |                       |     /    /  /  \\             |          endurance: {player1.endurance}")
    print(f"         |_________________|____________|_______________________|    /    /       /            |                                              {inventory[4]}")
    print(f"         |                                                      L   / /  /       /             |          dexterity: {player1.dexterity}")
    print(f"         |    ️                                                 L / /          /              |                                              {inventory[5]}")
    print(f"         |                                                         L       O   /               |          magic: {player1.magic}")
    print(f"         |                                       ️                L    /    /                 |                                              {inventory[6]}")
    print(f"         |                                                          L  /    /                  |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                           L     /                   |                                              {inventory[7]}")
    print(f"         |        ️                                                  L   /                    |          condition: {player1.condition}")
    print(f"         |                                                              L/                     |                                              {inventory[8]}")
    print(f"         |                                                               L                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                            ️                   L                  |                                               {inventory[9]}")
    print(f"         |                                                                 L                   |          armor equiped: {player1.armor}")
    print("         |                                                                   L                 |")
    print(f"         |                                                                    L                |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see two doors.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def twodoors2():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                              |                                                      |          name: {player1.name}")
    print(f"         |                              |                                                      |                                              {player1.gold} gold")
    print(f"         |                              |                                                      |          class: {player1.Class}")                                                
    print(f"         |                              |                 ____________                         |                                              {inventory[0]}")
    print(f"         |                              |                |            |                        |          level: {player1.level}")
    print(f"         |                   /\\         |                |   |      | |                        |                                              {inventory[1]}")
    print(f"         |                  /  \\        |                |   |        |                        |          health: {player1.health}")
    print(f"         |                 /  \\ \\       |                |            |                        |                                              {inventory[2]}")
    print(f"         |                /    \\ \\      |                |     |    O |                        |          strength: {player1.strength}")
    print(f"         |               /        \\     |                |     |      |                        |                                              {inventory[3]}")
    print(f"         |              /          \\    |                | |        | |                        |          endurance: {player1.endurance}")
    print(f"         |             \\  \\       O \\   |________________|____________|________________________|                                              {inventory[4]}")
    print(f"         |              \\  \\         \\  L                                                      |          dexterity: {player1.dexterity}")
    print(f"         |     ️        \\       \\    \L                                                       |                                              {inventory[5]}")
    print(f"         |                \\       \\   L                                                        |          magic: {player1.magic}")
    print(f"         |                 \\         L                       ️                                |                                              {inventory[6]}")
    print(f"         |                  \\       L                                                          |           hunger: {round_to(player1.hunger)}")
    print(f"         |                   \\     L                                                           |                                              {inventory[7]}")
    print(f"         |                    \\  L                                                             |          condition: {player1.condition}")
    print(f"         |                     \\L                                                              |                                              {inventory[8]}")
    print(f"         |                     L                                                               |          weapon equiped: {player1.weapon}")
    print(f"         |                    L                                      ️                        |                                              {inventory[9]}")
    print(f"         |                  L                                                                  |          armor equiped: {player1.armor}")
    print("         |                  L                                                                  |")
    print(f"         |                L                                                                    |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see two doors.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def northwest_entrance_room_facingsouth():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |________________|                                     |                              |          name: {player1.name}")
    print(f"         |________________|                                     |                              |                                              {player1.gold} gold")
    print(f"         |                |                                     |                              |          Class: {player1.Class}")                                                
    print(f"         |________________|                                     |                              |                                              {inventory[0]}")
    print(f"         |________________|                                     |                              |          level: {player1.level}")
    print(f"         |                |                                     |                              |                                              {inventory[1]}")
    print(f"         |________________|                                     |                              |          health: {player1.health}")
    print(f"         |________________|                                     |                              |                                              {inventory[2]}")
    print(f"         |                |   *??*                              |                              |          strength: {player1.strength}")
    print(f"         |________________|    ||                               |                              |                                              {inventory[3]}")
    print(f"         |________________|    --                               |                              |          endurance: {player1.endurance}")
    print(f"         |                |                                     |                              |                                              {inventory[4]}")
    print(f"         |________________|_____________________________________|                              |          dexterity: {player1.dexterity}")
    print(f"         |    ️                                                L                              |                                              {inventory[5]}")
    print(f"         |                                                       L                             |          magic: {player1.magic}")
    print(f"         |                                                        L                            |                                              {inventory[6]}")
    print(f"         |                                                         L                           |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                          L                          |                                              {inventory[7]}")
    print(f"         |        ️                                                L                          |          condition: {player1.condition}")
    print(f"         |                                                           L                         |                                              {inventory[8]}")
    print(f"         |                                                            L                        |          weapon equiped: {player1.weapon}")
    print(f"         |                                                    ️      L                        |                                              {inventory[9]}")
    print(f"         |                                                             L               ️      |          armor equiped: {player1.armor}")
    print("         |                                                               L                     |")
    print(f"         |                                                               L                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see the staircase leading out of the dungeon.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def northeast_entrance_room_facingsouth():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                      |             stats                            inventory")
    print("         |                                                                                      |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                              |                                      |_______________|          name: {player1.name}")
    print(f"         |                              |                                      |_______________|                                              {player1.gold} gold")
    print(f"         |                              |                                      |               |          Class: {player1.Class}")                                                
    print(f"         |                              |                                      |_______________|                                              {inventory[0]}")
    print(f"         |                              |                                      |_______________|          level: {player1.level}")
    print(f"         |                              |                                      |               |                                              {inventory[1]}")
    print(f"         |                              |                                      |_______________|          health: {player1.health}")
    print(f"         |                              |                                      |_______________|                                              {inventory[2]}")
    print(f"         |                              |                               *??*   |               |          strength: {player1.strength}")
    print(f"         |                              |                                ||    |_______________|                                              {inventory[3]}")
    print(f"         |                              |                                --    |_______________|          endurance: {player1.endurance}")
    print(f"         |                              |                                      |               |                                              {inventory[4]}")
    print(f"         |                              |______________________________________|_______________|          dexterity: {player1.dexterity}")
    print(f"         |    ️                       L                                                       |                                              {inventory[5]}")
    print(f"         |                            L                                                        |          magic: {player1.magic}")
    print(f"         |                           L                                                         |                                              {inventory[6]}")
    print(f"         |                          L                                                          |          hunger: {round_to(player1.hunger)}")
    print(f"         |                         L                                                           |                                              {inventory[7]}")
    print(f"         |        ️              L                                                            |          condition: {player1.condition}")
    print(f"         |                       L                                                             |                                              {inventory[8]}")
    print(f"         |                      L                                                              |          weapon equiped: {player1.weapon}")
    print(f"         |                     L                              ️                               |                                              {inventory[9]}")
    print(f"         |                    L                                                        ️      |          armor equiped: {player1.armor}")
    print("         |                    L                                                                |")
    print(f"         |                  L                                                                  |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see the staircase leading out of the dungeon.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def entrance_stairs():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                        |__________________________________|                         |          name: {player1.name}")
    print(f"         |                        |__________________________________|                         |                                              {player1.gold} gold")
    print(f"         |                        |                                  |                         |          class: {player1.Class}")                                                
    print(f"         |                        |__________________________________|                         |                                              {inventory[0]}")
    print(f"         |                        |__________________________________|                         |          level: {player1.level}")
    print(f"         |                        |                                  |                         |                                              {inventory[1]}")
    print(f"         |                        |__________________________________|                         |          health: {player1.health}")
    print(f"         |                        |__________________________________|                         |                                              {inventory[2]}")
    print(f"         |                 *??*   |                                  |   *??*                  |          strength: {player1.strength}")
    print(f"         |                  ||    |__________________________________|    ||                   |                                              {inventory[3]}")
    print(f"         |                  --    |__________________________________|    --                   |          endurance: {player1.endurance}")
    print(f"         |                        |                                  |                         |                                              {inventory[4]}")
    print(f"         |                        |__________________________________|                         |          dexterity: {player1.dexterity}")
    print(f"         |    ️                  |__________________________________|                         |                                              {inventory[5]}")
    print(f"         |                        |                                  |                         |          magic: {player1.magic}")
    print(f"         |                        |__________________________________|                         |                                              {inventory[6]}")
    print(f"         |                        |__________________________________|                         |          hunger: {round_to(player1.hunger)}")
    print(f"         |                        |                                  |                         |                                              {inventory[7]}")
    print(f"         |        ️              |                                  |                         |          condition: {player1.condition}")
    print(f"         |________________________|__________________________________|_________________________|                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                                    ️                               |                                              {inventory[9]}")
    print(f"         |                                                                             ️      |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see the staircase leading out of the dungeon.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "walk":
        print("You can't do that!")
        answer = input("Type 'left', 'right', 'items', 'rest', or 'search'.")
        while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "search":
            answer = input("Type 'left','right', 'items','rest', or 'search'.")
        just_entered = False
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def entrance_stairs2():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                          |________________________________|                         |          name: {player1.name}")
    print(f"         |                          |________________________________|                         |                                              {player1.gold} gold")
    print(f"         |                          |                                |                         |          Class: {player1.Class}")                                                
    print(f"         |                          |________________________________|                         |                                              {inventory[0]}")
    print(f"         |                          |________________________________|                         |          level: {player1.level}")
    print(f"         |                          |                                |                         |                                              {inventory[1]}")
    print(f"         |                          |________________________________|                         |          health: {player1.health}")
    print(f"         |                          |________________________________|                         |                                              {inventory[2]}")
    print(f"         |                   *??*   |                                |   *??*                  |          strength: {player1.strength}")
    print(f"         |                    ||    |________________________________|    ||                   |                                              {inventory[3]}")
    print(f"         |                    --    |________________________________|    --                   |          endurance: {player1.endurance}")
    print(f"         |                          |                                |                         |                                              {inventory[4]}")
    print(f"         |__________________________|________________________________|_________________________|          dexterity: {player1.dexterity}")
    print(f"         |    ️                                                                               |                                              {inventory[5]}")
    print(f"         |                                                                                     |          magic: {player1.magic}")
    print(f"         |                                                                                     |                                              {inventory[6]}")
    print(f"         |                                                                                     |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                                                     |                                              {inventory[7]}")
    print(f"         |        ️                                                                           |          condition: {player1.condition}")
    print(f"         |                                                                                     |                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                                    ️                               |                                              {inventory[9]}")
    print(f"         |                                                                             ️      |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a staircase leading up.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left', 'right', 'items', 'rest', or 'search'.")
    just_entered = False
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def up_stairs():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                        |__________________________________|                         |          name: {player1.name}")
    print(f"         |                        |__________________________________|                         |                                              {player1.gold} gold")
    print(f"         |                        |                                  |                         |          class: {player1.Class}")                                                
    print(f"         |                        |__________________________________|                         |                                              {inventory[0]}")
    print(f"         |                        |__________________________________|                         |          level: {player1.level}")
    print(f"         |                        |                                  |                         |                                              {inventory[1]}")
    print(f"         |                        |__________________________________|                         |          health: {player1.health}")
    print(f"         |                        |__________________________________|                         |                                              {inventory[2]}")
    print(f"         |                 *??*   |                                  |   *??*                  |          strength: {player1.strength}")
    print(f"         |                  ||    |__________________________________|    ||                   |                                              {inventory[3]}")
    print(f"         |                  --    |__________________________________|    --                   |          endurance: {player1.endurance}")
    print(f"         |                        |                                  |                         |                                              {inventory[4]}")
    print(f"         |                        |__________________________________|                         |          dexterity: {player1.dexterity}")
    print(f"         |    ️                  |__________________________________|                         |                                              {inventory[5]}")
    print(f"         |                        |                                  |                         |          magic: {player1.magic}")
    print(f"         |                        |__________________________________|                         |                                              {inventory[6]}")
    print(f"         |                        |__________________________________|                         |          hunger: {round_to(player1.hunger)}")
    print(f"         |                        |                                  |                         |                                              {inventory[7]}")
    print(f"         |        ️              |                                  |                         |          condition: {player1.condition}")
    print(f"         |________________________|__________________________________|_________________________|                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                                    ️                               |                                              {inventory[9]}")
    print(f"         |                                                                             ️      |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You a the staircase leading up.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        floor += 1
        print_area()
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def stairs():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                        |                                  |                         |          name: {player1.name}")
    print(f"         |                        |                                  |                         |                                              {player1.gold} gold")
    print(f"         |                        |                                  |                         |          class: {player1.Class}")                                                
    print(f"         |                        |                                  |                         |                                              {inventory[0]}")
    print(f"         |                        |                                  |                         |          level: {player1.level}")
    print(f"         |                        |                                  |                         |                                              {inventory[1]}")
    print(f"         |                        |                                  |                         |          health: {player1.health}")
    print(f"         |                        |                                  |                         |                                              {inventory[2]}")
    print(f"         |                 *??*   |                                  |   *??*                  |          strength: {player1.strength}")
    print(f"         |                  ||    |                                  |    ||                   |                                              {inventory[3]}")
    print(f"         |                  --    |                                  |    --                   |          endurance: {player1.endurance}")
    print(f"         |                        |                                  |                         |                                              {inventory[4]}")
    print(f"         |                        |                                  |                         |          dexterity: {player1.dexterity}")
    print(f"         |    ️                  |                                  |                         |                                              {inventory[5]}")
    print(f"         |                        |                                  |                         |          magic: {player1.magic}")
    print(f"         |                        |__________________________________|                         |                                              {inventory[6]}")
    print(f"         |                        |__________________________________|                         |          hunger: {round_to(player1.hunger)}")
    print(f"         |                        |                                  |                         |                                              {inventory[7]}")
    print(f"         |        ️              |                                  |                         |          condition: {player1.condition}")
    print(f"         |________________________|__________________________________|_________________________|                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                                    ️                               |                                              {inventory[9]}")
    print(f"         |                                                                             ️      |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a staircase going down to the next level.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def far_stairs():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                          |                                |                         |          name: {player1.name}")
    print(f"         |                          |                                |                         |                                              {player1.gold} gold")
    print(f"         |                          |                                |                         |          Class: {player1.Class}")                                                
    print(f"         |                          |                                |                         |                                              {inventory[0]}")
    print(f"         |                          |                                |                         |          level: {player1.level}")
    print(f"         |                          |                                |                         |                                              {inventory[1]}")
    print(f"         |                          |                                |                         |          health: {player1.health}")
    print(f"         |                          |                                |                         |                                              {inventory[2]}")
    print(f"         |                          |                                |                         |          strength: {player1.strength}")
    print(f"         |                          |________________________________|                         |                                              {inventory[3]}")
    print(f"         |                          |________________________________|                         |          endurance: {player1.endurance}")
    print(f"         |                          |                                |                         |                                              {inventory[4]}")
    print(f"         |__________________________|________________________________|_________________________|          dexterity: {player1.dexterity}")
    print(f"         |    ️                                                                               |                                              {inventory[5]}")
    print(f"         |                                                                                     |          magic: {player1.magic}")
    print(f"         |                                                                                     |                                              {inventory[6]}")
    print(f"         |                                                                                     |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                                                     |                                              {inventory[7]}")
    print(f"         |        ️                                                                           |          condition: {player1.condition}")
    print(f"         |                                                                                     |                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                                    ️                               |                                              {inventory[9]}")
    print(f"         |                                                                             ️      |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a staircase going down to the next level.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left', 'right', 'items', 'rest', or 'search'.")
    just_entered = False
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def wall():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                                                     |          name: {player1.name}")
    print(f"         |                                                                                     |                                              {player1.gold} gold")
    print(f"         |                                                                                     |          class: {player1.Class}")                                                
    print(f"         |                                                                                     |                                              {inventory[0]}")
    print(f"         |                                                                                     |          level: {player1.level}")
    print(f"         |                                                                                     |                                              {inventory[1]}")
    print(f"         |                                                                                     |          health: {player1.health}")
    print(f"         |                                                                                     |                                              {inventory[2]}")
    print(f"         |        ️                                                                           |          strength: {player1.strength}")
    print(f"         |                                                                                     |                                              {inventory[3]}")
    print(f"         |                                                                                     |          endurance: {player1.endurance}")
    print(f"         |                                                                                     |                                              {inventory[4]}")
    print(f"         |                                                                                     |          dexterity: {player1.dexterity}")
    print(f"         |    ️                                                                               |                                              {inventory[5]}")
    print(f"         |                                                                                     |          magic: {player1.magic}")
    print(f"         |                                                                                     |                                              {inventory[6]}")
    print(f"         |                                                                                     |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                                                     |                                              {inventory[7]}")
    print(f"         |        ️                                                                           |          condition: {player1.condition}")
    print(f"         |_____________________________________________________________________________________|                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |        ️                                                                           |                                              {inventory[9]}")
    print(f"         |        ️                                                                           |          armor equiped: {player1.armor}")
    print("         |        ️                                                                           |")
    print(f"         |        ️                                                                           |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You stare at the dungeon wall, encaptivated by its beauty.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "walk":
        print("You slam into the thick dungeon wall to no avail.")
        answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
        while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "search":
            answer = input("Type 'left','right','items','rest', or 'search'.")
    elif answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def far_wall():
    global x
    global y
    global direction
    global just_entered
    global play
    if player1.health < 1:
        player1.health = 10
        return
    else:
        if play == "no":
            return
        for lines in range (5):
            print("")
        print("          _____________________________________________________________________________________ ")
        print("         |                                                                                     |             stats                            inventory")
        print("         |                                                                                     |             -----                            ---------")
        print("         |_____________________________________________________________________________________|")
        print(f"         |                                                                                     |          name: {player1.name}")
        print(f"         |                                                                                     |                                              {player1.gold} gold")
        print(f"         |                                                                                     |          class: {player1.Class}")                                                
        print(f"         |                                                                                     |                                              {inventory[0]}")
        print(f"         |                                                                                     |          level: {player1.level}")
        print(f"         |                                                                                     |                                              {inventory[1]}")
        print(f"         |                                                                                     |          health: {player1.health}")
        print(f"         |                                                                                     |                                              {inventory[2]}")
        print(f"         |                                                                                     |          strength: {player1.strength}")
        print(f"         |                                                                                     |                                              {inventory[3]}")
        print(f"         |                                                                                     |          endurance: {player1.endurance}")
        print(f"         |_____________________________________________________________________________________|                                              {inventory[4]}")
        print(f"         |                                                                                     |          dexterity: {player1.dexterity}")
        print(f"         |     ️                                                                              |                                              {inventory[5]}")
        print(f"         |                                                                                     |          magic: {player1.magic}")
        print(f"         |                                    ️                                               |                                              {inventory[6]}")
        print(f"         |                                                                                     |          hunger: {round_to(player1.hunger)}")
        print(f"         |                                                                                     |                                              {inventory[7]}")
        print(f"         |         ️                                                                          |          condition: {player1.condition}")
        print(f"         |                                                                                     |                                              {inventory[8]}")
        print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
        print(f"         |                                             ️                                      |                                              {inventory[9]}")
        print(f"         |                                                                      ️             |          armor equiped: {player1.armor}")
        print("         |                                                                                     |")
        print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
        print("         |_____________________________________________________________________________________|")
        print("")
        print("")
        print("")
        print("You see nothing but bodies in this room.")
        answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
        while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
            answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
        if answer == "left":
            if direction == "north":
                direction = "west"
            elif direction == "west":
                direction = "south"
            elif direction == "south":
                direction = "east"
            elif direction == "east":
                direction = "north"
            print_area()
        elif answer == "right":
            if direction == "north":
                direction = "east"
            elif direction == "east":
                direction = "south"
            elif direction == "south":
                direction = "west"
            elif direction == "west":
                direction = "north"
            print_area()
        elif answer == "walk":
            if direction == "north":
                y += 1
            elif direction == "west":
                x -= 1
            elif direction == "south":
                y -= 1
            elif direction == "east":
                x += 1
            print_area()
        elif answer == "items":
            items()
        elif answer == "rest":
            rest()
        elif answer == "search":
            search()
        if play == "no":
            return

def door():
    global x
    global y
    global just_entered
    global direction
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                                                     |          name: {player1.name}")
    print(f"         |                                                                                     |                                              {player1.gold} gold")
    print(f"         |                         ___________________________________                         |          class: {player1.Class}")                                                
    print(f"         |                         |                                 |                         |                                              {inventory[0]}")
    print(f"         |                         |            |            |       |                         |          level: {player1.level}")
    print(f"         |                         |   |        |            |       |                         |                                              {inventory[1]}")
    print(f"         |                         |   |        |                    |                         |          health: {player1.health}")
    print(f"         |                         |   |        |                    |                         |                                              {inventory[2]}")
    print(f"         |        ️               |                                 |                         |          strength: {player1.strength}")
    print(f"         |                         |                                 |                         |                                              {inventory[3]}")
    print(f"         |                         |                                 |                         |          endurance: {player1.endurance}")
    print(f"         |                         |                  |              |                         |                                              {inventory[4]}")
    print(f"         |                         |                  |         O    |                         |          dexterity: {player1.dexterity}")
    print(f"         |    ️                   |        |                        |                         |                                              {inventory[5]}")
    print(f"         |                         |        |                        |                         |          magic: {player1.magic}")
    print(f"         |                         |        |             |          |                         |                                              {inventory[6]}")
    print(f"         |                         |        |             |          |                         |          hunger: {round_to(player1.hunger)}")
    print(f"         |                         |                      |          |                         |                                              {inventory[7]}")
    print(f"         |        ️               |                                 |                         |          condition: {player1.condition}")
    print(f"         |_________________________|_________________________________|_________________________|                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |        ️                                                                           |                                              {inventory[9]}")
    print(f"         |        ️                                                                           |          armor equiped: {player1.armor}")
    print("         |        ️                                                                           |")
    print(f"         |        ️                                                                           |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    if just_entered == False:
        print("You see a door.")
    else:
        print("You walk farther into the dungeon and see an door.")
        just_entered = False
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to open the door. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def locked_door():
    global x
    global y
    global just_entered
    global direction
    global play
    global east_fountain_room_door, west_fountain_room_door
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                                                     |          name: {player1.name}")
    print(f"         |                                                                                     |                                              {player1.gold} gold")
    print(f"         |                         ___________________________________                         |          class: {player1.Class}")                                                
    print(f"         |                         |                                 |                         |                                              {inventory[0]}")
    print(f"         |                         |            |            |       |                         |          level: {player1.level}")
    print(f"         |                         |   |        |            |       |                         |                                              {inventory[1]}")
    print(f"         |                         |   |        |                    |                         |          health: {player1.health}")
    print(f"         |                         |   |        |                    |                         |                                              {inventory[2]}")
    print(f"         |        ️               |                                 |                         |          strength: {player1.strength}")
    print(f"         |                         |                                 |                         |                                              {inventory[3]}")
    print(f"         |                         |                                 |                         |          endurance: {player1.endurance}")
    print(f"         |                         |                  |              |                         |                                              {inventory[4]}")
    print(f"         |                         |                  |         O    |                         |          dexterity: {player1.dexterity}")
    print(f"         |    ️                   |        |                        |                         |                                              {inventory[5]}")
    print(f"         |                         |        |                        |                         |          magic: {player1.magic}")
    print(f"         |                         |        |             |          |                         |                                              {inventory[6]}")
    print(f"         |                         |        |             |          |                         |          hunger: {round_to(player1.hunger)}")
    print(f"         |                         |                      |          |                         |                                              {inventory[7]}")
    print(f"         |        ️               |                                 |                         |          condition: {player1.condition}")
    print(f"         |_________________________|_________________________________|_________________________|                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |        ️                                                                           |                                              {inventory[9]}")
    print(f"         |        ️                                                                           |          armor equiped: {player1.armor}")
    print("         |        ️                                                                           |")
    print(f"         |        ️                                                                           |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a door.")
    just_entered = False
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to open the door. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    if answer == "walk":
        if x == 2 and y == -3:
            if east_fountain_room_door == "locked":
                print("You try to open the door, but it's locked.")
                if player1.Class != "thief":
                    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items (like a key). Type 'rest' to rest.")
                    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest":
                        answer = input("Type 'left','right', 'walk','items', or 'rest'.")
                else:
                    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items (like a key). Type 'rest' to rest. Type 'pick' to pick the lock.")
                    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "pick":
                        answer = input("Type 'left','right', 'walk','items','rest', or 'pick'.")
            else:
                x -= 1
                print_area()
        if x == -2 and y == -3:
            if west_fountain_room_door == "locked":
                print("You try to open the door, but it's locked.")
                if player1.Class != "thief":
                    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items (like a key). Type 'rest' to rest.")
                    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest":
                        answer = input("Type 'left','right', 'walk','items', or 'rest'.")
                else:
                    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items (like a key). Type 'rest' to rest. Type 'pick' to pick the lock.")
                    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "pick":
                        answer = input("Type 'left','right', 'walk','items','rest', or 'pick'.")
            else:
                x += 1
                print_area()
    if answer == "pick":
        if player1.dexterity == "infinite":
            if x == 2 and y == -3:
                east_fountain_room_door = "unlocked"
            elif x == -2 and y == -3:
                west_fountain_room_door = "unlocked"
            print("You picked the lock!")
            input("Press ENTER to continue.")
            print_area()
        else:
            if player1.dexterity > abs(floor) * 10 + 8:
                if x == 2 and y == -3:
                    east_fountain_room_door = "unlocked"
                elif x == -2 and y == -3:
                    west_fountain_room_door = "unlocked"
                print("You picked the lock!")
                input("Press ENTER to continue.")
                print_area()
            else:
                print("You try to pick the lock, but you can't.")
                input("Press ENTER to continue.")
                print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def last_door():
    global x
    global y
    global just_entered
    global direction
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                                                     |          name: {player1.name}")
    print(f"         |                                                                                     |                                              {player1.gold} gold")
    print(f"         |                         ___________________________________                         |          class: {player1.Class}")                                                
    print(f"         |                         |                                 |                         |                                              {inventory[0]}")
    print(f"         |                         |            |            |       |                         |          level: {player1.level}")
    print(f"         |                         |   |        |            |       |                         |                                              {inventory[1]}")
    print(f"         |                         |   |        |                    |                         |          health: {player1.health}")
    print(f"         |                         |   |        |                    |                         |                                              {inventory[2]}")
    print(f"         |        ️               |                                 |                         |          strength: {player1.strength}")
    print(f"         |                         |                                 |                         |                                              {inventory[3]}")
    print(f"         |                         |                                 |                         |          endurance: {player1.endurance}")
    print(f"         |                         |                  |              |                         |                                              {inventory[4]}")
    print(f"         |                         |                  |         =[]  |                         |          dexterity: {player1.dexterity}")
    print(f"         |    ️                   |        |                        |                         |                                              {inventory[5]}")
    print(f"         |                         |        |                        |                         |          magic: {player1.magic}")
    print(f"         |                         |        |             |          |                         |                                              {inventory[6]}")
    print(f"         |                         |        |             |          |                         |          hunger: {round_to(player1.hunger)}")
    print(f"         |                         |                      |          |                         |                                              {inventory[7]}")
    print(f"         |        ️               |                                 |                         |          condition: {player1.condition}")
    print(f"         |_________________________|_________________________________|_________________________|                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |        ️                                                                           |                                              {inventory[9]}")
    print(f"         |        ️                                                                           |          armor equiped: {player1.armor}")
    print("         |        ️                                                                           |")
    print(f"         |        ️                                                                           |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a giant door and hear strange magical sounds behind it.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to open the door. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        answer = input("Are you sure? The lich may be just beyond this door. y/n")
        while answer != "y" and answer != "yes" and answer != "n" and answer != "no":
            answer = input("Will you enter the room? y/n")
        if answer == "yes" or answer == "y":
            final_boss_battle()
        elif answer == "no":
            print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def hall():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |               ______________________________________________________                |          name: {player1.name}")
    print(f"         |               |                                                     |               |                                              {player1.gold} gold")
    print(f"         |               |                                                     |               |          class: {player1.Class}")                                                
    print(f"         |               |                                                     |               |                                              {inventory[0]}")
    print(f"         |               |                                                     |               |          level: {player1.level}")
    print(f"         |               |                                                     |               |                                              {inventory[1]}")
    print(f"         |               |                                                     |               |          health: {player1.health}")
    print(f"         |               |            ________________________________         |               |                                              {inventory[2]}")
    print(f"         |        ️     |           |                               |         |               |          strength: {player1.strength}")
    print(f"         |               |           |                               |         |               |                                              {inventory[3]}")
    print(f"         |               |           |                               |         |               |          endurance: {player1.endurance}")
    print(f"         |               |           |      ____________________     |         |               |                                              {inventory[4]}")
    print(f"         |               |           |     |                   |     |         |               |          dexterity: {player1.dexterity}")
    print(f"         |    ️         |           |     |                   |     |         |               |                                              {inventory[5]}")
    print(f"         |               |           |     |                   |     |         |               |          magic: {player1.magic}")
    print(f"         |               |           |     |                   |     |         |               |                                              {inventory[6]}")
    print(f"         |               |           |     |                   |     |         |               |          hunger: {round_to(player1.hunger)}")
    print(f"         |               |           |     |                   |     |         |               |                                              {inventory[7]}")
    print(f"         |               |        ️ |     |                   |     |         |               |          condition: {player1.condition}")
    print(f"         |               |           |     |                   |     |         |               |                                              {inventory[8]}")
    print(f"         |               |           |     |___________________|     |         |               |          weapon equiped: {player1.weapon}")
    print(f"         |        ️     |           |                               |         |               |                                              {inventory[9]}")
    print(f"         |        ️     |           |_______________________________|         |               |          armor equiped: {player1.armor}")
    print("         |        ️     |                                                     |               |")
    print(f"         |        ️     |                                                     |               |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You look down a dark corridor, but see no end.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def hall_door_on_end():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |               ______________________________________________________                |          name: {player1.name}")
    print(f"         |               |                                                     |               |                                              {player1.gold} gold")
    print(f"         |               |                                                     |               |          class: {player1.Class}")                                                
    print(f"         |               |                                                     |               |                                              {inventory[0]}")
    print(f"         |               |                                                     |               |          level: {player1.level}")
    print(f"         |               |                                                     |               |                                              {inventory[1]}")
    print(f"         |               |                                                     |               |          health: {player1.health}")
    print(f"         |               |            ________________________________         |               |                                              {inventory[2]}")
    print(f"         |        ️     |           |                               |         |               |          strength: {player1.strength}")
    print(f"         |               |           |                               |         |               |                                              {inventory[3]}")
    print(f"         |               |           |                               |         |               |          endurance: {player1.endurance}")
    print(f"         |               |           |                               |         |               |                                              {inventory[4]}")
    print(f"         |               |           |                               |         |               |          dexterity: {player1.dexterity}")
    print(f"         |    ️         |           |                               |         |               |                                              {inventory[5]}")
    print(f"         |               |           |                               |         |               |          magic: {player1.magic}")
    print(f"         |               |           |          ____________         |         |               |                                              {inventory[6]}")
    print(f"         |               |           |         |            |        |         |               |          hunger: {round_to(player1.hunger)}")
    print(f"         |               |           |         |   |     |  |        |         |               |                                              {inventory[7]}")
    print(f"         |               |        ️ |         |   |     |  |        |         |               |          condition: {player1.condition}")
    print(f"         |               |           |         |   |        |        |         |               |                                              {inventory[8]}")
    print(f"         |               |           |         |     |   O  |        |         |               |          weapon equiped: {player1.weapon}")
    print(f"         |        ️     |           |         |     |      |        |         |               |                                              {inventory[9]}")
    print(f"         |        ️     |           |_________|____________|________|         |               |          armor equiped: {player1.armor}")
    print("         |        ️      |                                                     |              |")
    print(f"         |        ️      |                                                     |              |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You look down a dark corridor, and see a door at the end.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def hall_turning_right():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |               ______________________________________________________                |          name: {player1.name}")
    print(f"         |               |                                                     |               |                                              {player1.gold} gold")
    print(f"         |               |                                                     |               |          class: {player1.Class}")                                                
    print(f"         |               |                                                     |               |                                              {inventory[0]}")
    print(f"         |               |                                                     |               |          level: {player1.level}")
    print(f"         |               |                                                     |               |                                              {inventory[1]}")
    print(f"         |               |                                                     |               |          health: {player1.health}")
    print(f"         |               |            ________________________________         |               |                                              {inventory[2]}")
    print(f"         |        ️     |           |                               |         |               |          strength: {player1.strength}")
    print(f"         |               |           |                               |         |               |                                              {inventory[3]}")
    print(f"         |               |           |                               |         |               |          endurance: {player1.endurance}")
    print(f"         |               |           |                          _____|         |               |                                              {inventory[4]}")
    print(f"         |               |           |                         |     |         |               |          dexterity: {player1.dexterity}")
    print(f"         |    ️         |           |                         |     |         |               |                                              {inventory[5]}")
    print(f"         |               |           |                         |     |         |               |          magic: {player1.magic}")
    print(f"         |               |           |                         |     |         |               |                                              {inventory[6]}")
    print(f"         |               |           |                         |     |         |               |          hunger: {round_to(player1.hunger)}")
    print(f"         |               |           |                         |     |         |               |                                              {inventory[7]}")
    print(f"         |               |        ️ |                         |     |         |               |          condition: {player1.condition}")
    print(f"         |               |           |                         |     |         |               |                                              {inventory[8]}")
    print(f"         |               |           |                         |     |         |               |          weapon equiped: {player1.weapon}")
    print(f"         |        ️     |           |                         |_____|         |               |                                              {inventory[9]}")
    print(f"         |        ️     |           |_______________________________|         |               |          armor equiped: {player1.armor}")
    print("         |        ️      |                                                     |              |")
    print(f"         |        ️      |                                                     |              |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("The corridor turns right in front of you.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def hall_turning_left():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |               ______________________________________________________                |          name: {player1.name}")
    print(f"         |               |                                                     |               |                                              {player1.gold} gold")
    print(f"         |               |                                                     |               |          class: {player1.Class}")                                                
    print(f"         |               |                                                     |               |                                              {inventory[0]}")
    print(f"         |               |                                                     |               |          level: {player1.level}")
    print(f"         |               |                                                     |               |                                              {inventory[1]}")
    print(f"         |               |                                                     |               |          health: {player1.health}")
    print(f"         |               |            _______________________________          |               |                                              {inventory[2]}")
    print(f"         |        ️     |           |                               |         |               |          strength: {player1.strength}")
    print(f"         |               |           |                               |         |               |                                              {inventory[3]}")
    print(f"         |               |           |____                           |         |               |          endurance: {player1.endurance}")
    print(f"         |               |           |    |                          |         |               |                                              {inventory[4]}")
    print(f"         |               |           |    |                          |         |               |          dexterity: {player1.dexterity}")
    print(f"         |    ️         |           |    |                          |         |               |                                              {inventory[5]}")
    print(f"         |               |           |    |                          |         |               |          magic: {player1.magic}")
    print(f"         |               |           |    |                          |         |               |                                              {inventory[6]}")
    print(f"         |               |           |    |                          |         |               |          hunger: {round_to(player1.hunger)}")
    print(f"         |               |           |    |                          |         |               |                                              {inventory[7]}")
    print(f"         |               |        ️ |    |                          |         |               |          condition: {player1.condition}")
    print(f"         |               |           |    |                          |         |               |                                              {inventory[8]}")
    print(f"         |               |           |    |                          |         |               |          weapon equiped: {player1.weapon}")
    print(f"         |        ️     |           |____|                          |         |               |                                              {inventory[9]}")
    print(f"         |        ️     |           |_______________________________|         |               |          armor equiped: {player1.armor}")
    print("         |        ️      |          /                                \\         |              |")
    print(f"         |        ️      |        /                                  \\         |              |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("The corridor turns left in front of you.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def hall_4way_split():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |               ______________________________________________________                |          name: {player1.name}")
    print(f"         |               |                                                     |               |                                              {player1.gold} gold")
    print(f"         |               |                                                     |               |          class: {player1.Class}")                                                
    print(f"         |               |                                                     |               |                                              {inventory[0]}")
    print(f"         |               |                                                     |               |          level: {player1.level}")
    print(f"         |               |                                                     |               |                                              {inventory[1]}")
    print(f"         |               |                                                     |               |          health: {player1.health}")
    print(f"         |               |_____________________________________________________|               |                                              {inventory[2]}")
    print(f"         |        ️     |           |                               |         |               |          strength: {player1.strength}")
    print(f"         |               |__         |                               |       __|               |                                              {inventory[3]}")
    print(f"         |               |  |        |                               |      |  |               |          endurance: {player1.endurance}")
    print(f"         |               |  |        |      ____________________     |      |  |               |                                              {inventory[4]}")
    print(f"         |               |  |        |     |                   |     |      |  |               |          dexterity: {player1.dexterity}")
    print(f"         |    ️         |  |        |     |                   |     |      |  |               |                                              {inventory[5]}")
    print(f"         |               |  |        |     |                   |     |      |  |               |          magic: {player1.magic}")
    print(f"         |               |  |        |     |                   |     |      |  |               |                                              {inventory[6]}")
    print(f"         |               |  |        |     |                   |     |      |  |               |          hunger: {round_to(player1.hunger)}")
    print(f"         |               |  |        |     |                   |     |      |  |               |                                              {inventory[7]}")
    print(f"         |               |  |     ️ |     |                   |     |      |  |               |          condition: {player1.condition}")
    print(f"         |               |  |        |     |                   |     |      |  |               |                                              {inventory[8]}")
    print(f"         |               |  |        |     |___________________|     |      |  |               |          weapon equiped: {player1.weapon}")
    print(f"         |        ️     |  |        |                               |      |  |               |                                              {inventory[9]}")
    print(f"         |        ️     |__|        |_______________________________|      |__|               |          armor equiped: {player1.armor}")
    print("         |        ️      |          /                                \         |              |")
    print(f"         |        ️      |        /                                  \         |              |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("The corridor branches off into 4 paths in front of you.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def t_hall():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |               ______________________________________________________                |          name: {player1.name}")
    print(f"         |               |                                                     |               |                                              {player1.gold} gold")
    print(f"         |               |                                                     |               |          class: {player1.Class}")                                                
    print(f"         |               |                                                     |               |                                              {inventory[0]}")
    print(f"         |               |                                                     |               |          level: {player1.level}")
    print(f"         |               |                                                     |               |                                              {inventory[1]}")
    print(f"         |               |                                                     |               |          health: {player1.health}")
    print(f"         |               |_____________________________________________________|               |                                              {inventory[2]}")
    print(f"         |        ️     |           |                               |         |               |          strength: {player1.strength}")
    print(f"         |               |__         |                               |       __|               |                                              {inventory[3]}")
    print(f"         |               |  |        |                               |      |  |               |          endurance: {player1.endurance}")
    print(f"         |               |  |        |                               |      |  |               |                                              {inventory[4]}")
    print(f"         |               |  |        |                               |      |  |               |          dexterity: {player1.dexterity}")
    print(f"         |    ️         |  |        |                               |      |  |               |                                              {inventory[5]}")
    print(f"         |               |  |        |                               |      |  |               |          magic: {player1.magic}")
    print(f"         |               |  |        |                               |      |  |               |                                              {inventory[6]}")
    print(f"         |               |  |        |                               |      |  |               |          hunger: {round_to(player1.hunger)}")
    print(f"         |               |  |        |                               |      |  |               |                                              {inventory[7]}")
    print(f"         |               |  |     ️ |                               |      |  |               |          condition: {player1.condition}")
    print(f"         |               |  |        |                               |      |  |               |                                              {inventory[8]}")
    print(f"         |               |  |        |                               |      |  |               |          weapon equiped: {player1.weapon}")
    print(f"         |        ️     |  |        |                               |      |  |               |                                              {inventory[9]}")
    print(f"         |        ️     |__|        |_______________________________|      |__|               |          armor equiped: {player1.armor}")
    print("         |        ️      |          /                                \         |              |")
    print(f"         |        ️      |        /                                  \         |              |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("The corridor branches off into 2 paths in front of you.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def t_hall_right():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |               ______________________________________________________                |          name: {player1.name}")
    print(f"         |               |                                                     |               |                                              {player1.gold} gold")
    print(f"         |               |                                                     |               |          class: {player1.Class}")                                                
    print(f"         |               |                                                     |               |                                              {inventory[0]}")
    print(f"         |               |                                                     |               |          level: {player1.level}")
    print(f"         |               |                                                     |               |                                              {inventory[1]}")
    print(f"         |               |                                                     |               |          health: {player1.health}")
    print(f"         |               |_____________________________________________________|               |                                              {inventory[2]}")
    print(f"         |        ️     |           |                               |         |               |          strength: {player1.strength}")
    print(f"         |               |           |                               |       __|               |                                              {inventory[3]}")
    print(f"         |               |           |                               |      |  |               |          endurance: {player1.endurance}")
    print(f"         |               |           |      ____________________     |      |  |               |                                              {inventory[4]}")
    print(f"         |               |           |     |                   |     |      |  |               |          dexterity: {player1.dexterity}")
    print(f"         |    ️         |           |     |                   |     |      |  |               |                                              {inventory[5]}")
    print(f"         |               |           |     |                   |     |      |  |               |          magic: {player1.magic}")
    print(f"         |               |           |     |                   |     |      |  |               |                                              {inventory[6]}")
    print(f"         |               |           |     |                   |     |      |  |               |          hunger: {round_to(player1.hunger)}")
    print(f"         |               |           |     |                   |     |      |  |               |                                              {inventory[7]}")
    print(f"         |               |        ️ |     |                   |     |      |  |               |          condition: {player1.condition}")
    print(f"         |               |           |     |                   |     |      |  |               |                                              {inventory[8]}")
    print(f"         |               |           |     |___________________|     |      |  |               |          weapon equiped: {player1.weapon}")
    print(f"         |        ️     |           |                               |      |  |               |                                              {inventory[9]}")
    print(f"         |        ️     |           |_______________________________|      |__|               |          armor equiped: {player1.armor}")
    print("         |        ️      |          /                                \         |              |")
    print(f"         |        ️      |        /                                  \         |              |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("The corridor branches off into 2 paths in front of you.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def t_hall_left():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |               ______________________________________________________                |          name: {player1.name}")
    print(f"         |               |                                                     |               |                                              {player1.gold} gold")
    print(f"         |               |                                                     |               |          class: {player1.Class}")                                                
    print(f"         |               |                                                     |               |                                              {inventory[0]}")
    print(f"         |               |                                                     |               |          level: {player1.level}")
    print(f"         |               |                                                     |               |                                              {inventory[1]}")
    print(f"         |               |                                                     |               |          health: {player1.health}")
    print(f"         |               |_____________________________________________________|               |                                              {inventory[2]}")
    print(f"         |        ️     |           |                               |         |               |          strength: {player1.strength}")
    print(f"         |               |__         |                               |         |               |                                              {inventory[3]}")
    print(f"         |               |  |        |                               |         |               |          endurance: {player1.endurance}")
    print(f"         |               |  |        |      ____________________     |         |               |                                              {inventory[4]}")
    print(f"         |               |  |        |     |                   |     |         |               |          dexterity: {player1.dexterity}")
    print(f"         |    ️         |  |        |     |                   |     |         |               |                                              {inventory[5]}")
    print(f"         |               |  |        |     |                   |     |         |               |          magic: {player1.magic}")
    print(f"         |               |  |        |     |                   |     |         |               |                                              {inventory[6]}")
    print(f"         |               |  |        |     |                   |     |         |               |          hunger: {round_to(player1.hunger)}")
    print(f"         |               |  |        |     |                   |     |         |               |                                              {inventory[7]}")
    print(f"         |               |  |     ️ |     |                   |     |         |               |          condition: {player1.condition}")
    print(f"         |               |  |        |     |                   |     |         |               |                                              {inventory[8]}")
    print(f"         |               |  |        |     |___________________|     |         |               |          weapon equiped: {player1.weapon}")
    print(f"         |        ️     |  |        |                               |         |               |                                              {inventory[9]}")
    print(f"         |        ️     |__|        |_______________________________|         |               |          armor equiped: {player1.armor}")
    print("         |        ️      |          /                                \         |              |")
    print(f"         |        ️      |        /                                  \         |              |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("The corridor branches off into 2 paths in front of you.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def hall_door_on_right():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |               ______________________________________________________                |          name: {player1.name}")
    print(f"         |               |                                                     |               |                                              {player1.gold} gold")
    print(f"         |               |                                                     |               |          class: {player1.Class}")                                                
    print(f"         |               |                                                     |               |                                              {inventory[0]}")
    print(f"         |               |                                                     |               |          level: {player1.level}")
    print(f"         |               |                                                     |               |                                              {inventory[1]}")
    print(f"         |               |                                                     |               |          health: {player1.health}")
    print(f"         |               |            ________________________________         |               |                                              {inventory[2]}")
    print(f"         |        ️     |           |                               |         |               |          strength: {player1.strength}")
    print(f"         |               |           |                               |         |               |                                              {inventory[3]}")
    print(f"         |               |           |                               |         |               |          endurance: {player1.endurance}")
    print(f"         |               |           |      ____________________     |         |               |                                              {inventory[4]}")
    print(f"         |               |           |     |                   |     |_________|               |          dexterity: {player1.dexterity}")
    print(f"         |    ️         |           |     |                   |     |         |               |                                              {inventory[5]}")
    print(f"         |               |           |     |                   |     |       | |               |          magic: {player1.magic}")
    print(f"         |               |           |     |                   |     |  |    | |               |                                              {inventory[6]}")
    print(f"         |               |           |     |                   |     |  |      |               |          hunger: {round_to(player1.hunger)}")
    print(f"         |               |           |     |                   |     |  |      |               |                                              {inventory[7]}")
    print(f"         |               |        ️ |     |                   |     |         |               |          condition: {player1.condition}")
    print(f"         |               |           |     |                   |     |      O  |               |                                              {inventory[8]}")
    print(f"         |               |           |     |___________________|     |         |               |          weapon equiped: {player1.weapon}")
    print(f"         |        ️     |           |                               |    |    |               |                                              {inventory[9]}")
    print(f"         |        ️     |           |_______________________________|    |    |               |          armor equiped: {player1.armor}")
    print("         |        ️     |                                            \\   |     |              |")
    print(f"         |        ️     |                                             \\         |             |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You look down a dark corridor and see a door on one side.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def hall_door_on_left():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |               ______________________________________________________                |          name: {player1.name}")
    print(f"         |               |                                                     |               |                                              {player1.gold} gold")
    print(f"         |               |                                                     |               |          class: {player1.Class}")                                                
    print(f"         |               |                                                     |               |                                              {inventory[0]}")
    print(f"         |               |                                                     |               |          level: {player1.level}")
    print(f"         |               |                                                     |               |                                              {inventory[1]}")
    print(f"         |               |                                                     |               |          health: {player1.health}")
    print(f"         |               |            ________________________________         |               |                                              {inventory[2]}")
    print(f"         |        ️     |           |                               |         |               |          strength: {player1.strength}")
    print(f"         |               |           |                               |         |               |                                              {inventory[3]}")
    print(f"         |               |           |                               |         |               |          endurance: {player1.endurance}")
    print(f"         |               |           |      ____________________     |         |               |                                              {inventory[4]}")
    print(f"         |               |___________|     |                   |     |         |               |          dexterity: {player1.dexterity}")
    print(f"         |    ️         |           |     |                   |     |         |               |                                              {inventory[5]}")
    print(f"         |               |   |     | |     |                   |     |         |               |          magic: {player1.magic}")
    print(f"         |               |   |       |     |                   |     |         |               |                                              {inventory[6]}")
    print(f"         |               |   |       |     |                   |     |         |               |          hunger: {round_to(player1.hunger)}")
    print(f"         |               |   |   |   |     |                   |     |         |               |                                              {inventory[7]}")
    print(f"         |               |       |️ |     |                   |     |         |               |          condition: {player1.condition}")
    print(f"         |               |         O |     |                   |     |         |               |                                              {inventory[8]}")
    print(f"         |               |     |     |     |___________________|     |         |               |          weapon equiped: {player1.weapon}")
    print(f"         |        ️     |           |                               |         |               |                                              {inventory[9]}")
    print(f"         |        ️     |    |   |  |_______________________________|         |               |          armor equiped: {player1.armor}")
    print("         |        ️     |    |     /                                          |               |")
    print(f"         |        ️     |        /                                            |               |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You look down a dark corridor, and see a door on one side.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def hall_2doors():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |               ______________________________________________________                |          name: {player1.name}")
    print(f"         |               |                                                     |               |                                              {player1.gold} gold")
    print(f"         |               |                                                     |               |          class: {player1.Class}")                                                
    print(f"         |               |                                                     |               |                                              {inventory[0]}")
    print(f"         |               |                                                     |               |          level: {player1.level}")
    print(f"         |               |                                                     |               |                                              {inventory[1]}")
    print(f"         |               |                                                     |               |          health: {player1.health}")
    print(f"         |               |            ________________________________         |               |                                              {inventory[2]}")
    print(f"         |        ️     |           |                               |         |               |          strength: {player1.strength}")
    print(f"         |               |           |                               |         |               |                                              {inventory[3]}")
    print(f"         |               |           |                               |         |               |          endurance: {player1.endurance}")
    print(f"         |               |           |      ____________________     |         |               |                                              {inventory[4]}")
    print(f"         |               |___________|     |                   |     |_________|               |          dexterity: {player1.dexterity}")
    print(f"         |    ️         |           |     |                   |     |         |               |                                              {inventory[5]}")
    print(f"         |               |   |     | |     |                   |     |       | |               |          magic: {player1.magic}")
    print(f"         |               |   |       |     |                   |     |   |   | |               |                                              {inventory[6]}")
    print(f"         |               |   |       |     |                   |     |   |     |               |          hunger: {round_to(player1.hunger)}")
    print(f"         |               |   |   |   |     |                   |     |   |     |               |                                              {inventory[7]}")
    print(f"         |               |       |️ |     |                   |     |         |               |          condition: {player1.condition}")
    print(f"         |               |         O |     |                   |     |       O |               |                                              {inventory[8]}")
    print(f"         |               |     |     |     |___________________|     |         |               |          weapon equiped: {player1.weapon}")
    print(f"         |        ️      |           |                               |    |    |              |                                              {inventory[9]}")
    print(f"         |        ️     |    |   |  |_______________________________|     |   |               |          armor equiped: {player1.armor}")
    print("         |        ️      |    |     /                                \\     |   |              |")
    print(f"         |        ️      |        /                                  \\         |              |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You look down a dark corridor, and see two doors; one on each side.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    just_entered = False
    if answer == "search":
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return
        
def south_entrance_room_facingnorth():
    global x
    global y
    global direction
    global just_entered
    global play
    if player1.health != "infinite":
        if player1.health < 1:
            return
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                                                     |          name: {player1.name}")
    print(f"         |                                                                                     |                                              {player1.gold} gold")
    print(f"         |                                                                                     |          class: {player1.Class}")                                                
    print(f"         |                                     ____________                                    |                                              {inventory[0]}")
    print(f"         |                                    |            |                                   |          level: {player1.level}")
    print(f"         |                                    |   |      | |                                   |                                              {inventory[1]}")
    print(f"         |                                    |   |        |                                   |          health: {player1.health}")
    print(f"         |                                    |            |                                   |                                              {inventory[2]}")
    print(f"         |                                    |     |    O |                                   |          strength: {player1.strength}")
    print(f"         |                                    |     |      |                                   |                                              {inventory[3]}")
    print(f"         |                                    | |        | |                                   |          endurance: {player1.endurance}")
    print(f"         |____________________________________|____________|___________________________________|                                              {inventory[4]}")
    print(f"         |                                                                                     |          dexterity: {player1.dexterity}")
    print(f"         |     ️                                                                              |                                              {inventory[5]}")
    print(f"         |                                                                                     |          magic: {player1.magic}")
    print(f"         |                                    ️                                               |                                              {inventory[6]}")
    print(f"         |                                                                                     |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                                                     |                                              {inventory[7]}")
    print(f"         |         ️                                                                          |          condition: {player1.condition}")
    print(f"         |                                                                                     |                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                             ️                                      |                                              {inventory[9]}")
    print(f"         |                                                                      ️             |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    if just_entered == True:
        print("You enter a dark underground room with bones scattered all over the floor. It has obviously been abandoned for years, yet you feel like someone, or something, is watching you.")
        just_entered = False
    else:
        print("You see a door on the other side of the room.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def southeast_entrance_room_facingwest():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |      /    /   \\                 |                                                   |          name: {player1.name}")
    print(f"         |     /    /     \\                |                                       __________  |                                              {player1.gold} gold")
    print(f"         |    /    /      /\\               |                                      |          | |          class: {player1.Class}")                                                
    print(f"         |   /    /      /  \\              |                                      |   |      | |                                              {inventory[0]}")
    print(f"         |  /    /      /    \\             |                                      |   |      | |          level: {player1.level}")
    print(f"         | /    /      /    / \\            |                                      |   |    O | |                                              {inventory[1]}")
    print(f"         |/    /      /    /   \\           |                                      |      |   | |          health: {player1.health}")
    print(f"         |\\   /      /    /     \\          |                                      |      |   | |                                              {inventory[2]}")
    print(f"         | \\ /      /    /       \\         |______________________________________|__________|_|          strength: {player1.strength}")
    print(f"         |  \\      /    /        /\\        L                                                   |                                              {inventory[3]}")
    print(f"         |   \\    /    /        /  \\      L                                                    |          endurance: {player1.endurance}")
    print(f"         |    \\  /    /        /   /\\    L                                                     |                                              {inventory[4]}")
    print(f"         |     \\/    /        /   /  \\  L                                                     |          dexterity: {player1.dexterity}")
    print(f"         |      \\   /        /   /    \\L                                                       |                                              {inventory[5]}")
    print(f"         |       \\ /        /   /     L                                                        |          magic: {player1.magic}")
    print(f"         |        \\        /   /     L                       ️                                |                                              {inventory[6]}")
    print(f"         |         \\      /   /     L                                                          |          hunger: {round_to(player1.hunger)}")
    print(f"         |          \\    /   /     L                                                           |                                              {inventory[7]}")
    print(f"         |           \\  /   /     L                                                              |          condition: {player1.condition}")
    print(f"         |            \\/   /     L                                                             |                                              {inventory[8]}")
    print(f"         |             \\  /     L                                                              |          weapon equiped: {player1.weapon}")
    print(f"         |              \\/    L                                     ️                         |                                              {inventory[9]}")
    print(f"         |               \\   L                                                                 |          armor equiped: {player1.armor}")
    print("         |                \\L                                                                |")
    print(f"         |                 L                                                                   |           accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a door and stairs going up.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def southwest_entrance_room_facingeast():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                      |             stats                            inventory")
    print("         |                                                                                      |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                   |                 /\\   \\       \\  |          name: {player1.name}")
    print(f"         |  __________                                       |                /  \\   \\       \\ |                                              {player1.gold} gold")
    print(f"         | |          |                                      |               /    \\   \\       \\|          class: {player1.Class}")                                                
    print(f"         | | |    |   |                                      |              /\\     \\   \\       |                                              {inventory[0]}")
    print(f"         | | |        |                                      |             /  \\     \\   \\      |          level: {player1.level}")
    print(f"         | | |        |                                      |            /\\   \\     \\   \\    /|                                              {inventory[1]}")
    print(f"         | |    |   O |                                      |           /  \\   \\     \\   \\  / |          health: {player1.health}")
    print(f"         | |    |     |                                      |          /    \\   \\     \\   \\/  |                                              {inventory[2]}")
    print(f"         |_|__________|______________________________________|         /      \\   \\     \\  /   |          strength: {player1.strength}")
    print(f"         |                                                   L        /        \\   \\     \\/    |                                              {inventory[3]}")
    print(f"         |                                                    L      /\\         \\   \\    /     |          endurance: {player1.endurance}")
    print(f"         |                                                     L    /  \\         \\   \\  /      |                                              {inventory[4]}")
    print(f"         |                                                      L  /\\   \\         \\   \\/       |          dexterity: {player1.dexterity}")
    print(f"         |     ️                                                L/  \\   \\         \\  /        |                                              {inventory[5]}")
    print(f"         |                                                        L   \\   \\         \\/         |          magic: {player1.magic}")
    print(f"         |                                                   ️    L   \\   \\        /          |                                              {inventory[6]}")
    print(f"         |                                                          L   \\   \\      /           |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                           L   \\   \\    /            |                                              {inventory[7]}")
    print(f"         |                                                            L   \\   \\  /             |          condition: {player1.condition}")
    print(f"         |                                                             L   \\   \\/              |                                              {inventory[8]}")
    print(f"         |                                                              L   \\  /               |          weapon equiped: {player1.weapon}")
    print(f"         |                                                           ️  L   \\/                |                                               {inventory[9]}")
    print(f"         |                                                                L  /                 |          armor equiped: {player1.armor}")
    print("         |                                                                 L/                  |")
    print(f"         |                                                                  L                  |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a door and stairs going up.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def threedoors():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                                                     |          name: {player1.name}")
    print(f"         |                                                                                     |                                              {player1.gold} gold")
    print(f"         |                                                                                     |          class: {player1.Class}")                                                
    print(f"         |_____                                ____________                               _____|                                              {inventory[0]}")
    print(f"         |     |                              |            |                             |     |          level: {player1.level}")
    print(f"         | |   |                              |   |      | |                             |   | |                                              {inventory[1]}")
    print(f"         | |   |                              |   |        |                             |   | |          health: {player1.health}")
    print(f"         | |   |                              |            |                             |     |                                              {inventory[2]}")
    print(f"         |   O |                              |     |    O |                             | |   |          strength: {player1.strength}")
    print(f"         |  |  |                              |     |      |                             | |  ||                                              {inventory[3]}")
    print(f"         |  |  |                              | |        | |                             | |   |          endurance: {player1.endurance}")
    print(f"         |_____|______________________________|____________|_____________________________|_____|                                              {inventory[4]}")
    print(f"         |                                                                                     |          dexterity: {player1.dexterity}")
    print(f"         |     ️                                                                              |                                              {inventory[5]}")
    print(f"         |                                                                                     |          magic: {player1.magic}")
    print(f"         |                                    ️                                               |                                              {inventory[6]}")
    print(f"         |                                                                                     |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                                                     |                                              {inventory[7]}")
    print(f"         |         ️                                                                          |          condition: {player1.condition}")
    print(f"         |                                                                                     |                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                             ️                                      |                                              {inventory[9]}")
    print(f"         |                                                                      ️             |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see 3 doors on the other side of the room.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def door2():
    global x
    global y
    global just_entered
    global direction
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                        |                            |          name: {player1.name}")
    print(f"         |                                                        |                            |                                              {player1.gold} gold")
    print(f"         |                                                        |                            |          class: {player1.Class}")                                                
    print(f"         |                           ____________                 |                            |                                              {inventory[0]}")
    print(f"         |                          |            |                |                            |          level: {player1.level}")
    print(f"         |                          |   |      | |                |                            |                                              {inventory[1]}")
    print(f"         |                          |   |        |                |                            |          health: {player1.health}")
    print(f"         |                          |            |                |                            |                                              {inventory[2]}")
    print(f"         |                          |     |    O |                |                            |          strength: {player1.strength}")
    print(f"         |                          |     |      |                |                            |                                              {inventory[3]}")
    print(f"         |                          | |        | |                |                            |          endurance: {player1.endurance}")
    print(f"         |__________________________|____________|________________|                            |                                              {inventory[4]}")
    print(f"         |                                                        L                            |          dexterity: {player1.dexterity}")
    print(f"         |     ️                                                  L                           |                                              {inventory[5]}")
    print(f"         |                                                          L                          |          magic: {player1.magic}")
    print(f"         |                                    ️                     L                         |                                              {inventory[6]}")
    print(f"         |                                                            L                        |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                             L                       |                                              {inventory[7]}")
    print(f"         |         ️                                                   L                      |          condition: {player1.condition}")
    print(f"         |                                                                L                    |                                              {inventory[8]}")
    print(f"         |                                                                 L                   |          weapon equiped: {player1.weapon}")
    print(f"         |                                             ️                     L                |                                              {inventory[9]}")
    print(f"         |                                                                    L  ️            |          armor equiped: {player1.armor}")
    print("         |                                                                      L              |")
    print(f"         |                                                                       L             |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a door.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def door3():
    global x
    global y
    global just_entered
    global direction
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |              stats                            inventory")
    print("         |                                                                                     |              -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                              |                                                      |          name: {player1.name}")
    print(f"         |                              |                                                      |                                              {player1.gold} gold")
    print(f"         |                              |                                                      |          class: {player1.Class}")                                                
    print(f"         |                              |                 ____________                         |                                              {inventory[0]}")
    print(f"         |                              |                |            |                        |          level: {player1.level}")
    print(f"         |                              |                |   |      | |                        |                                              {inventory[1]}")
    print(f"         |                              |                |   |        |                        |          health: {player1.health}")
    print(f"         |                              |                |            |                        |                                              {inventory[2]}")
    print(f"         |                              |                |     |    O |                        |          strength: {player1.strength}")
    print(f"         |                              |                |     |      |                        |                                              {inventory[3]}")
    print(f"         |                              |                | |        | |                        |          endurance: {player1.endurance}")
    print(f"         |                              |________________|____________|________________________|                                              {inventory[4]}")
    print(f"         |                              L                                                      |          dexterity: {player1.dexterity}")
    print(f"         |     ️                      L                                                       |                                              {inventory[5]}")
    print(f"         |                            L                                                        |          magic: {player1.magic}")
    print(f"         |                           L                       ️                                |                                              {inventory[6]}")
    print(f"         |                          L                                                          |          hunger: {round_to(player1.hunger)}")
    print(f"         |                         L                                                           |                                              {inventory[7]}")
    print(f"         |                       L                                                             |          condition: {player1.condition}")
    print(f"         |                      L                                                              |                                              {inventory[8]}")
    print(f"         |                     L                                                               |          weapon equiped: {player1.weapon}")
    print(f"         |                    L                                                                |                                              {inventory[9]}")
    print(f"         |                  L                                                                  |          armor equiped: {player1.armor}")
    print("         |                  L                                                                  |")
    print(f"         |                L                                                                    |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a door.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def left_corner():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                      |             stats                            inventory")
    print("         |                                                                                      |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                              |                                                      |          name: {player1.name}")
    print(f"         |                              |                                                      |                                              {player1.gold} gold")
    print(f"         |                              |                                                      |          class: {player1.Class}")                                                
    print(f"         |                              |                                                      |                                              {inventory[0]}")
    print(f"         |                              |                                                      |          level: {player1.level}")
    print(f"         |                              |                                                      |                                              {inventory[1]}")
    print(f"         |                              |                                                      |          health: {player1.health}")
    print(f"         |                              |                                                      |                                              {inventory[2]}")
    print(f"         |                              |                                                      |          strength: {player1.strength}")
    print(f"         |                              |                                                      |                                              {inventory[3]}")
    print(f"         |                              |                                                      |          endurance: {player1.endurance}")
    print(f"         |                              |______________________________________________________|                                              {inventory[4]}")
    print(f"         |                              L                                                      |          dexterity: {player1.dexterity}")
    print(f"         |     ️                      L                                                       |                                              {inventory[5]}")
    print(f"         |                            L                                                        |          magic: {player1.magic}")
    print(f"         |                           L                       ️                                |                                              {inventory[6]}")
    print(f"         |                          L                                                          |          hunger: {round_to(player1.hunger)}")
    print(f"         |                         L                                                           |                                              {inventory[7]}")
    print(f"         |                       L                                                             |          condition: {player1.condition}")
    print(f"         |                      L                                                              |                                              {inventory[8]}")
    print(f"         |                     L                                                               |          weapon equiped: {player1.weapon}")
    print(f"         |                    L                                      ️                        |                                              {inventory[9]}")
    print(f"         |                  L                                                                  |          armor equiped: {player1.armor}")
    print("         |                  L                                                                  |")
    print(f"         |                L                                                                    |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see nothing in that corner.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def right_corner():
    global x
    global y
    global just_entered
    global direction
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                        |                            |          name: {player1.name}")
    print(f"         |                                                        |                            |                                              {player1.gold} gold")
    print(f"         |                                                        |                            |          class: {player1.Class}")                                                
    print(f"         |                                                        |                            |                                              {inventory[0]}")
    print(f"         |                                                        |                            |          level: {player1.level}")
    print(f"         |                                                        |                            |                                              {inventory[1]}")
    print(f"         |                                                        |                            |          health: {player1.health}")
    print(f"         |                                                        |                            |                                              {inventory[2]}")
    print(f"         |                                                        |                            |          strength: {player1.strength}")
    print(f"         |                                                        |                            |                                              {inventory[3]}")
    print(f"         |                                                        |                            |          endurance: {player1.endurance}")
    print(f"         |________________________________________________________|                            |                                              {inventory[4]}")
    print(f"         |                                                        L                            |          dexterity: {player1.dexterity}")
    print(f"         |     ️                                                  L                           |                                              {inventory[5]}")
    print(f"         |                                                          L                          |          magic: {player1.magic}")
    print(f"         |                                    ️                     L                         |                                              {inventory[6]}")
    print(f"         |                                                            L                        |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                             L                       |                                              {inventory[7]}")
    print(f"         |         ️                                                   L                      |          condition: {player1.condition}")
    print(f"         |                                                                L                    |                                              {inventory[8]}")
    print(f"         |                                                                 L                   |          weapon equiped: {player1.weapon}")
    print(f"         |                                             ️                    L                 |                                              {inventory[9]}")
    print(f"         |                                                                    L  ️            |          armor equiped: {player1.armor}")
    print("         |                                                                      L              |")
    print(f"         |                                                                       L             |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see nothing in that corner.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def far_right_corner():
    global x
    global y
    global just_entered
    global direction
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                |                                    |          name: {player1.name}")
    print(f"         |                                                |                                    |                                              {player1.gold} gold")
    print(f"         |                                                |                                    |          class: {player1.Class}")                                                
    print(f"         |________________________________________________|                                    |                                              {inventory[0]}")
    print(f"         |                                                L                                    |          level: {player1.level}")
    print(f"         |                                                 L                                   |                                              {inventory[1]}")
    print(f"         |                                                  L                                  |          health: {player1.health}")
    print(f"         |                                                   L                                 |                                              {inventory[2]}")
    print(f"         |                                                    L                                |          strength: {player1.strength}")
    print(f"         |                                                     L                               |                                              {inventory[3]}")
    print(f"         |                                                      L                              |          endurance: {player1.endurance}")
    print(f"         |                                                       L                             |                                              {inventory[4]}")
    print(f"         |                                                        L                            |          dexterity: {player1.dexterity}")
    print(f"         |     ️                                                  L                           |                                              {inventory[5]}")
    print(f"         |                                                          L                          |          magic: {player1.magic}")
    print(f"         |                                    ️                     L                         |                                              {inventory[6]}")
    print(f"         |                                                            L                        |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                             L                       |                                              {inventory[7]}")
    print(f"         |         ️                                                   L                      |          condition: {player1.condition}")
    print(f"         |                                                                L                    |                                              {inventory[8]}")
    print(f"         |                                                                 L                   |          weapon equiped: {player1.weapon}")
    print(f"         |                                             ️                   L                  |                                              {inventory[9]}")
    print(f"         |                                                                    L  ️            |          armor equiped: {player1.armor}")
    print("         |                                                                      L              |")
    print(f"         |                                                                       L             |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see nothing in that corner.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def far_left_corner():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                      |             stats                            inventory")
    print("         |                                                                                      |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                      |                                              |          name: {player1.name}")
    print(f"         |                                      |                                              |                                              {player1.gold} gold")
    print(f"         |                                      |                                              |          class: {player1.Class}")                                                
    print(f"         |                                      |______________________________________________|                                              {inventory[0]}")
    print(f"         |                                      L                                              |          level: {player1.level}")
    print(f"         |                                     L                                               |                                              {inventory[1]}")
    print(f"         |                                    L                                                |          health: {player1.health}")
    print(f"         |                                   L                                                 |                                              {inventory[2]}")
    print(f"         |                                  L                                                  |          strength: {player1.strength}")
    print(f"         |                                 L                                                   |                                              {inventory[3]}")
    print(f"         |                                L                                                    |          endurance: {player1.endurance}")
    print(f"         |                               L                                                     |                                              {inventory[4]}")
    print(f"         |                              L                                                      |          dexterity: {player1.dexterity}")
    print(f"         |     ️                      L                                                       |                                              {inventory[5]}")
    print(f"         |                            L                                                        |          magic: {player1.magic}")
    print(f"         |                           L                       ️                                |                                              {inventory[6]}")
    print(f"         |                          L                                                          |          hunger: {round_to(player1.hunger)}")
    print(f"         |                         L                                                           |                                              {inventory[7]}")
    print(f"         |                       L                                                             |          condition: {player1.condition}")
    print(f"         |                      L                                                              |                                              {inventory[8]}")
    print(f"         |                     L                                                               |          weapon equiped: {player1.weapon}")
    print(f"         |                    L                                      ️                        |                                              {inventory[9]}")
    print(f"         |                  L                                                                  |          armor equiped: {player1.armor}")
    print("         |                  L                                                                  |")
    print(f"         |                L                                                                    |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see nothing in that corner.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def door_left_corner():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                      |             stats                            inventory")
    print("         |                                                                                      |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                              |                                                      |          name: {player1.name}")
    print(f"         |                              |                                                      |                                              {player1.gold} gold")
    print(f"         |                              |                                                      |          class: {player1.Class}")                                                
    print(f"         |                              |                                                      |                                              {inventory[0]}")
    print(f"         |                              |                                                      |          level: {player1.level}")
    print(f"         |                              |                                                      |                                              {inventory[1]}")
    print(f"         |                 /\\           |                                                      |          health: {player1.health}")
    print(f"         |                /  \\          |                                                      |                                              {inventory[2]}")
    print(f"         |               /    \\         |                                                      |          strength: {player1.strength}")
    print(f"         |              /      \\        |                                                      |                                              {inventory[3]}")
    print(f"         |             /        \\       |                                                      |          endurance: {player1.endurance}")
    print(f"         |            /  \\       \\      |______________________________________________________|                                              {inventory[4]}")
    print(f"         |           /    \\    O  \\     L                                                      |          dexterity: {player1.dexterity}")
    print(f"         |     ️    \\             \\   L                                                       |                                              {inventory[5]}")
    print(f"         |            \\   \\      \\   \\L                                                        |          magic: {player1.magic}")
    print(f"         |             \\   \\      \\  L                       ️                                |                                              {inventory[6]}")
    print(f"         |              \\   \\       L                                                          |          hunger: {round_to(player1.hunger)}")
    print(f"         |               \\     \\   L                                                           |                                              {inventory[7]}")
    print(f"         |                \\      L                                                             |          condition: {player1.condition}")
    print(f"         |                 \\    L                                                              |                                              {inventory[8]}")
    print(f"         |                  \\  L                                                               |          weapon equiped: {player1.weapon}")
    print(f"         |                   \\L                                      ️                        |                                              {inventory[9]}")
    print(f"         |                  L                                                                  |          armor equiped: {player1.armor}")
    print("         |                  L                                                                  |")
    print(f"         |                L                                                                    |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a door in that corner.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def door_right_corner():
    global x
    global y
    global just_entered
    global direction
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                        |                            |          name: {player1.name}")
    print(f"         |                                                        |                            |                                              {player1.gold} gold")
    print(f"         |                                                        |                            |          class: {player1.Class}")                                                
    print(f"         |                                                        |                            |                                              {inventory[0]}")
    print(f"         |                                                        |                            |          level: {player1.level}")
    print(f"         |                                                        |                            |                                              {inventory[1]}")
    print(f"         |                                                        |          /\\                |          health: {player1.health}")
    print(f"         |                                                        |         /  \\               |                                              {inventory[2]}")
    print(f"         |                                                        |        /    \\              |          strength: {player1.strength}")
    print(f"         |                                                        |       /      \\             |                                              {inventory[3]}")
    print(f"         |                                                        |      /    /   \\            |          endurance: {player1.endurance}")
    print(f"         |________________________________________________________|     /    /     \\           |                                              {inventory[4]}")
    print(f"         |                                                        L    /    /   /   \\          |          dexterity: {player1.dexterity}")
    print(f"         |     ️                                                  L  /            /           |                                              {inventory[5]}")
    print(f"         |                                                          L/ /   /      /            |          magic: {player1.magic}")
    print(f"         |                                    ️                     L    /  O   /             |                                              {inventory[6]}")
    print(f"         |                                                            L         /              |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                             L       /               |                                              {inventory[7]}")
    print(f"         |         ️                                                   L    /                 |          condition: {player1.condition}")
    print(f"         |                                                                L /                  |                                              {inventory[8]}")
    print(f"         |                                                                 L                   |          weapon equiped: {player1.weapon}")
    print(f"         |                                             ️                     L                |                                              {inventory[9]}")
    print(f"         |                                                                    L  ️            |          armor equiped: {player1.armor}")
    print("         |                                                                      L              |")
    print(f"         |                                                                       L             |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a door in that corner.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def door_far_left_corner():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                      |             stats                            inventory")
    print("         |                                                                                      |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                              /\\      |                                              |          name: {player1.name}")
    print(f"         |                             /  \\     |                                              |                                              {player1.gold} gold")
    print(f"         |                            /    \\    |                                              |          class: {player1.Class}")                                                
    print(f"         |                           /  \\   \\   |______________________________________________|                                              {inventory[0]}")
    print(f"         |                           \\   \\ O \\  L                                              |          level: {player1.level}")
    print(f"         |                            \\ \\    \\\\L                                               |                                              {inventory[1]}")
    print(f"         |                             \\ \\    L                                                |            health: {player1.health}")
    print(f"         |                              \\ \\  L                                                 |                                              {inventory[2]}")
    print(f"         |                               \\  L                                                  |          strength: {player1.strength}")
    print(f"         |                                \\L                                                   |                                              {inventory[3]}")
    print(f"         |                                L                                                    |          endurance: {player1.endurance}")
    print(f"         |                               L                                                     |                                              {inventory[4]}")
    print(f"         |                              L                                                      |          dexterity: {player1.dexterity}")
    print(f"         |     ️                      L                                                       |                                              {inventory[5]}")
    print(f"         |                            L                                                        |          magic: {player1.magic}")
    print(f"         |                           L                       ️                                |                                              {inventory[6]}")
    print(f"         |                          L                                                          |          hunger: {round_to(player1.hunger)}")
    print(f"         |                         L                                                           |                                              {inventory[7]}")
    print(f"         |                       L                                                             |          condition: {player1.condition}")
    print(f"         |                      L                                                              |                                              {inventory[8]}")
    print(f"         |                     L                                                               |          weapon equiped: {player1.weapon}")
    print(f"         |                    L                                      ️                        |                                              {inventory[9]}")
    print(f"         |                  L                                                                  |          armor equiped: {player1.armor}")
    print("         |                  L                                                                  |")
    print(f"         |                L                                                                    |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a door in that corner.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return
    
def door_far_right_corner():
    global x
    global y
    global just_entered
    global direction
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                |      /\\                            |          name: {player1.name}")
    print(f"         |                                                |     /  \\                           |                                              {player1.gold} gold")
    print(f"         |                                                |    /    \\                          |          class: {player1.Class}")                                                
    print(f"         |________________________________________________|   /   /  \\                         |                                              {inventory[0]}")
    print(f"         |                                                L  / / /   /                         |          level: {player1.level}")
    print(f"         |                                                 L/ /     /                          |                                              {inventory[1]}")
    print(f"         |                                                L    O /                           |          health: {player1.health}")
    print(f"         |                                                   L  / /                            |                                              {inventory[2]}")
    print(f"         |                                                    L  /                             |          strength: {player1.strength}")
    print(f"         |                                                     L/                              |                                              {inventory[3]}")
    print(f"         |                                                      L                              |          endurance: {player1.endurance}")
    print(f"         |                                                       L                             |                                              {inventory[4]}")
    print(f"         |                                                        L                            |          dexterity: {player1.dexterity}")
    print(f"         |     ️                                                  L                           |                                              {inventory[5]}")
    print(f"         |                                                          L                          |          magic: {player1.magic}")
    print(f"         |                                    ️                     L                         |                                              {inventory[6]}")
    print(f"         |                                                            L                        |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                             L                       |                                              {inventory[7]}")
    print(f"         |         ️                                                   L                      |          condition: {player1.condition}")
    print(f"         |                                                              L                    |                                              {inventory[8]}")
    print(f"         |                                                                 L                   |          weapon equiped: {player1.weapon}")
    print(f"         |                                             ️                   L                  |                                              {inventory[9]}")
    print(f"         |                                                                    L  ️            |          armor equiped: {player1.armor}")
    print("         |                                                                      L              |")
    print(f"         |                                                                       L             |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a door in that corner.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def twodoors_far_left_corner():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                      |             stats                            inventory")
    print("         |                                                                                      |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                              /\\      |                                              |          name: {player1.name}")
    print(f"         |                             /  \\     |                                              |                                              {player1.gold} gold")
    print(f"         |                            /    \\    |                                              |          class: {player1.Class}")                                                
    print(f"         |                           /  \\   \\   |______________________________________________|                                              {inventory[0]}")
    print(f"         |                           \\   \\ O \\  L                                              |          level: {player1.level}")
    print(f"         |                            \\ \\    \\\\L                                               |                                              {inventory[1]}")
    print(f"         |                             \\ \\    L                                                |          health: {player1.health}")
    print(f"         |                              \\ \\  L                                                 |                                              {inventory[2]}")
    print(f"         |                               \\  L                                                  |          strength: {player1.strength}")
    print(f"         |                     /\\         \\L                                                   |                                              {inventory[3]}")
    print(f"         |                    /  \\        L                                                    |          endurance: {player1.endurance}")
    print(f"         |                   /    \\      L                                                     |                                              {inventory[4]}")
    print(f"         |                  /      \\    L                                                      |          dexterity: {player1.dexterity}")
    print(f"         |     ️           \\  \\ O  \\  L                                                       |                                              {inventory[5]}")
    print(f"         |                   \\  \\  \\ \\L                                                        |          magic: {player1.magic}")
    print(f"         |                    \\      L                       ️                                |                                              {inventory[6]}")
    print(f"         |                     \\ \\  L                                                          |          hunger: {round_to(player1.hunger)}")
    print(f"         |                      \\  L                                                           |                                              {inventory[7]}")
    print(f"         |                       L                                                             |          condition: {player1.condition}")
    print(f"         |                      L                                                              |                                              {inventory[8]}")
    print(f"         |                     L                                                               |          weapon equiped: {player1.weapon}")
    print(f"         |                    L                                      ️                        |                                              {inventory[9]}")
    print(f"         |                  L                                                                  |          armor equiped: {player1.armor}")
    print("         |                  L                                                                  |")
    print(f"         |                L                                                                    |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see two doors in that corner.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def twodoors_far_right_corner():
    global x
    global y
    global just_entered
    global direction
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                |      /\\                            |          name: {player1.name}")
    print(f"         |                                                |     /  \\                           |                                              {player1.gold} gold")
    print(f"         |                                                |    /    \\                          |          class: {player1.Class}")                                                
    print(f"         |________________________________________________|   /   /  \\                         |                                              {inventory[0]}")
    print(f"         |                                                L  / / /   /                         |          level: {player1.level}")
    print(f"         |                                                 L/ /     /                          |                                              {inventory[1]}")
    print(f"         |                                                  L    O /                           |          health: {player1.health}")
    print(f"         |                                                   L  / /                            |                                              {inventory[2]}")
    print(f"         |                                                    L  /                             |          strength: {player1.strength}")
    print(f"         |                                                     L/                              |                                              {inventory[3]}")
    print(f"         |                                                      L           /\\                 |          endurance: {player1.endurance}")
    print(f"         |                                                       L         /  \\                |                                              {inventory[4]}")
    print(f"         |                                                        L       /    \\               |          dexterity: {player1.dexterity}")
    print(f"         |     ️                                                  L    /  /   \\               |                                              {inventory[5]}")
    print(f"         |                                                          L  /  /  / /               |          magic: {player1.magic}")
    print(f"         |                                    ️                     L/       /                |                                              {inventory[6]}")
    print(f"         |                                                            L    O /                 |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                             L /  /                  |                                              {inventory[7]}")
    print(f"         |         ️                                                   L /                    |          condition: {player1.condition}")
    print(f"         |                                                                L                    |                                              {inventory[8]}")
    print(f"         |                                                                 L                   |          weapon equiped: {player1.weapon}")
    print(f"         |                                             ️                   L                  |                                              {inventory[9]}")
    print(f"         |                                                                    L  ️            |          armor equiped: {player1.armor}")
    print("         |                                                                      L              |")
    print(f"         |                                                                       L             |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see two doors in that corner.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def fountain():
    global x
    global y
    global direction
    global just_entered
    global searched_fountain
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                     /\\\\\\\\\\\\\////////\\                               |          name: {player1.name}")
    print(f"         |                                    ///\\\\\\\\\\\\///////\\\\\\\                             |                                              {player1.gold} gold")
    print(f"         |                                   ////\\\\\\\\\\\\///////\\\\\\\\                             |          class: {player1.Class}")                                                
    print(f"         |                                  ////  \\\\\\\\\\\//////  \\\\\\\\                           |                                              {inventory[0]}")
    print(f"         |                                 ////  | \\\\\\\\\\/////    \\\\\\\\                          |          level: {player1.level}")
    print(f"         |                                ||||  |   |||||||| ||   ||||                         |                                              {inventory[1]}")
    print(f"         |                                ||||  |||| ||||||    |  ||||                         |          health: {player1.health}")
    print(f"         |                           |    |||| ||     ||||  ||    ||||  |                      |                                              {inventory[2]}")
    print(f"         |                           |   ||||||   ||  ||||       |||||| |                      |          strength: {player1.strength}")
    print(f"         |                           |   |||||| |     ||||   ||| |||||| |                      |                                              {inventory[3]}")
    print(f"         |                           |   |||||| ||    |||| |     |||||| |                      |          endurance: {player1.endurance}")
    print(f"         |___________________________|  ||||||||   |  ||||   |  |||||||||______________________|                                              {inventory[4]}")
    print(f"         |                           |\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/|                      |          dexterity: {player1.dexterity}")
    print(f"         |    ️                     | \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/ |                      |                                              {inventory[5]}")
    print(f"         |                           |  \____________________________/  |                      |          magic: {player1.magic}")
    print(f"         |                           |           ️                     |                      |                                              {inventory[6]}")
    print(f"         |                           |                                  |                      |          hunger: {round_to(player1.hunger)}")
    print(f"         |                           |                                  |                      |                                              {inventory[7]}")
    print(f"         |        ️                 |                                  |                      |          condition: {player1.condition}")
    print(f"         |                           |__________________________________|                      |                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                            ️                                       |                                               {inventory[9]}")
    print(f"         |                                                                     ️              |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a giant fountain spewing eerie, unnatural-looking water.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room. Type 'drink' to drink from the fountain")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search" and answer != "drink":
        answer = input("Type 'left','right', 'walk','items','rest', 'search', or 'drink'.")
    just_entered = False
    if answer == "walk":
        print("You can't do that!")
        answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room. Type 'drink' to drink from the fountain")
        while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "search" and answer != "drink":
            answer = input("Type 'left','right', 'items','rest', 'search', or 'drink'.")
    elif answer == "search":
        if searched_fountain == False:
            player1.gold += 5
            searched_fountain = True
            print("You find 5 gold in the fountain.")
            answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'items' to use items. Type 'rest' to rest. Type 'drink' to drink from the fountain")
            while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "drink":
                answer = input("Type 'left','right', 'items','rest', or 'drink'.")
        else:
            print("There's nothing here.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "drink":
        player1.health = player1.max_health
        battle_end = True
        print("You drink from the fountain and instantly all of your wounds heal.")
        input("press ENTER to continue.")
        print_area()
    if play == "no":
        return
def chest():
    global x
    global y
    global direction
    global just_entered
    global play
    global chest1, chest2, chest3, chest4, chest5, chest6, chest7, chest8, chest9, chest10, chest11
    gold_in_chest = 0
    item_in_chest = "none"
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                                                                     |          name: {player1.name}")
    print(f"         |                                                                                     |                                              {player1.gold} gold")
    print(f"         |                                                                                     |          class: {player1.Class}")                                                
    print(f"         |                                                                                     |                                              {inventory[0]}")
    print(f"         |                                                                                     |          level: {player1.level}")
    print(f"         |                                                                                     |                                              {inventory[1]}")
    print(f"         |                                                                                     |          health: {player1.health}")
    print(f"         |                                                                                     |                                              {inventory[2]}")
    print(f"         |        ️                ______________________________________                     |          strength: {player1.strength}")
    print(f"         |                         /                                     /|                    |                                              {inventory[3]}")
    print(f"         |                        /____________________________________ / |                    |          endurance: {player1.endurance}")
    print(f"         |                       |                                     |  |                    |                                              {inventory[4]}")
    print(f"         |                       |                                     | /|                    |          dexterity: {player1.dexterity}")
    print(f"         |    ️                 |_____________________________________|/ |                    |                                              {inventory[5]}")
    print(f"         |                       |                                     |  |                    |          magic: {player1.magic}")
    print(f"         |                       |                  O                  |  |                    |                                              {inventory[6]}")
    print(f"         |_______________________|                                     |  |____________________|          hunger: {round_to(player1.hunger)}")
    print(f"         |                       |                                     |  |                    |                                              {inventory[7]}")
    print(f"         |        ️             |                                     | /                     |          condition: {player1.condition}")
    print(f"         |                       |_____________________________________|/                      |                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |        ️                                                                           |                                              {inventory[9]}")
    print(f"         |        ️                                                                           |          armor equiped: {player1.armor}")
    print("         |        ️                                                                           |")
    print(f"         |        ️                                                                           |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You find a chest.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search. Type 'chest' to open the chest.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "chest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', 'search', or 'chest'.")
    just_entered = False
    if answer == "search":
        print("You found a chest!")
        answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'chest' to open the chest.")
        while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "chest":
            answer = input("Type 'left','right', 'walk','items','rest', or 'chest'.")
    if answer == "walk":
        print("You can't walk into a chest that small.")
        answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'chest' to open the chest.")
        while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "chest":
            answer = input("Type 'left','right','items','rest', or 'chest'.")
    if answer == "chest":
        if x == 4 and y == -8 and floor == -1 or x == 3 and y == -9 and floor == -1:
            item_in_chest = "leather armor"# endurance + 3
            gold_in_chest = 5
            if chest1 == False:
                print("The chest is empty.")
                input("Press ENTER to continue.")
                print_area()
                return
            else:
                chest1 = False
            if answer == "walk":
                print("You can't walk into a chest that small.")
                answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'chest' to open the chest.")
                while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "chest":
                    answer = input("Type 'left','right','items','rest', or 'chest'.")
            if answer == "left":
                if direction == "north":
                    direction = "west"
                elif direction == "west":
                    direction = "south"
                elif direction == "south":
                    direction = "east"
                elif direction == "east":
                    direction = "north"
                print_area()
            elif answer == "right":
                if direction == "north":
                    direction = "east"
                elif direction == "east":
                    direction = "south"
                elif direction == "south":
                    direction = "west"
                elif direction == "west":
                    direction = "north"
                print_area()
            elif answer == "items":
                items()
            elif answer == "rest":
                rest()
        elif x == 3 and y == 3 and floor == -1 or x == 4 and y == 4 and floor == -1:
            item_in_chest = "key"
            gold_in_chest = 6
            if chest4 == False:
                print("The chest is empty.")
                input("Press ENTER to continue.")
                print_area()
                return
            else:
                chest4 = False
            if answer == "walk":
                print("You can't walk into a chest that small.")
                answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'chest' to open the chest.")
                while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "chest":
                    answer = input("Type 'left','right','items','rest', or 'chest'.")
                if answer == "left":
                    if direction == "north":
                        direction = "west"
                    elif direction == "west":
                        direction = "south"
                    elif direction == "south":
                        direction = "east"
                    elif direction == "east":
                        direction = "north"
                    print_area()
                elif answer == "right":
                    if direction == "north":
                        direction = "east"
                    elif direction == "east":
                        direction = "south"
                    elif direction == "south":
                        direction = "west"
                    elif direction == "west":
                        direction = "north"
                    print_area()
                elif answer == "items":
                    items()
                elif answer == "rest":
                    rest()
        elif x == 3 and y == 0 and floor == -1 or x == 4 and y == -1 and floor == -1:
            item_in_chest = "dagger" # attack + 1
            gold_in_chest = 2
            if chest3 == False:
                print("The chest is empty.")
                input("Press ENTER to continue.")
                print_area()
                return
            else:
                chest3 = False
            if answer == "walk":
                print("You can't walk into a chest that small.")
                answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'chest' to open the chest.")
                while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "chest":
                    answer = input("Type 'left','right','items','rest', or 'chest'.")
                if answer == "left":
                    if direction == "north":
                        direction = "west"
                    elif direction == "west":
                        direction = "south"
                    elif direction == "south":
                        direction = "east"
                    elif direction == "east":
                        direction = "north"
                    print_area()
                elif answer == "right":
                    if direction == "north":
                        direction = "east"
                    elif direction == "east":
                        direction = "south"
                    elif direction == "south":
                        direction = "west"
                    elif direction == "west":
                        direction = "north"
                    print_area()
                elif answer == "items":
                    items()
                elif answer == "rest":
                    rest()
        elif x == -3 and y == 3 and floor == -1 or x == -4 and y == 4 and floor == -1:
            item_in_chest = "ration"
            gold_in_chest = 3
            if chest6 == False:
                print("The chest is empty.")
                input("Press ENTER to continue.")
                print_area()
                return
            else:
                chest6 = False
            if answer == "walk":
                print("You can't walk into a chest that small.")
                answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'chest' to open the chest.")
                while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "chest":
                    answer = input("Type 'left','right','items','rest', or 'chest'.")
                if answer == "left":
                    if direction == "north":
                        direction = "west"
                    elif direction == "west":
                        direction = "south"
                    elif direction == "south":
                        direction = "east"
                    elif direction == "east":
                        direction = "north"
                    print_area()
                elif answer == "right":
                    if direction == "north":
                        direction = "east"
                    elif direction == "east":
                        direction = "south"
                    elif direction == "south":
                        direction = "west"
                    elif direction == "west":
                        direction = "north"
                    print_area()
                elif answer == "items":
                    items()
                elif answer == "rest":
                    rest()
        elif x == -4 and y == 0 and floor == -1 or x == -3 and y == -1 and floor == -1:
            item_in_chest = "spear"# attack + 5
            gold_in_chest = 3
            if chest7 == False:
                print("The chest is empty.")
                input("Press ENTER to continue.")
                print_area()
                return
            else:
                chest7 = False
            if answer == "walk":
                print("You can't walk into a chest that small.")
                answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'chest' to open the chest.")
                while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "chest":
                    answer = input("Type 'left','right','items','rest', or 'chest'.")
                if answer == "left":
                    if direction == "north":
                        direction = "west"
                    elif direction == "west":
                        direction = "south"
                    elif direction == "south":
                        direction = "east"
                    elif direction == "east":
                        direction = "north"
                    print_area()
                elif answer == "right":
                    if direction == "north":
                        direction = "east"
                    elif direction == "east":
                        direction = "south"
                    elif direction == "south":
                        direction = "west"
                    elif direction == "west":
                        direction = "north"
                    print_area()
                elif answer == "items":
                    items()
                elif answer == "rest":
                    rest()
        elif x == -1 and y == -12 and floor == -2:
            item_in_chest = "ration"# +5 hunger
            gold_in_chest = 5
            if chest9 == False:
                print("The chest is empty.")
                input("Press ENTER to continue.")
                print_area()
                return
            else:
                chest9 = False
            if answer == "walk":
                print("You can't walk into a chest that small.")
                answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'chest' to open the chest.")
                while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "chest":
                    answer = input("Type 'left','right','items','rest', or 'chest'.")
                if answer == "left":
                    if direction == "north":
                        direction = "west"
                    elif direction == "west":
                        direction = "south"
                    elif direction == "south":
                        direction = "east"
                    elif direction == "east":
                        direction = "north"
                    print_area()
                elif answer == "right":
                    if direction == "north":
                        direction = "east"
                    elif direction == "east":
                        direction = "south"
                    elif direction == "south":
                        direction = "west"
                    elif direction == "west":
                        direction = "north"
                    print_area()
                elif answer == "items":
                    items()
                elif answer == "rest":
                    rest()
        elif x == 1 and y == 0 and floor == -2:
            item_in_chest = "golden apple"# +10 hunger, +1 strength, +1 endurance, +1 magic, +1 dexterity
            gold_in_chest = 10
            if chest11 == False:
                print("The chest is empty.")
                input("Press ENTER to continue.")
                print_area()
                return
            else:
                chest11 = False
            if answer == "walk":
                print("You can't walk into a chest that small.")
                answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'chest' to open the chest.")
                while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "chest":
                    answer = input("Type 'left','right','items','rest', or 'chest'.")
                if answer == "left":
                    if direction == "north":
                        direction = "west"
                    elif direction == "west":
                        direction = "south"
                    elif direction == "south":
                        direction = "east"
                    elif direction == "east":
                        direction = "north"
                    print_area()
                elif answer == "right":
                    if direction == "north":
                        direction = "east"
                    elif direction == "east":
                        direction = "south"
                    elif direction == "south":
                        direction = "west"
                    elif direction == "west":
                        direction = "north"
                    print_area()
                elif answer == "items":
                    items()
                elif answer == "rest":
                    rest()
        if (x == 4 and y == -6 and floor == -1) or (x == 3 and y == -7 and floor == -1) or (x == 1 and y == 7 and floor == -1) or (x == 0 and y == 6 and floor == -1) or (x == -1 and y == 7 and floor == -1) or (x == -4 and y == -8 and floor == -1) or (x == -3 and y == -8 and floor == -1) or (x == 4 and y == -9 and floor == -2) or (x == 4 and y == -9 and floor == -2):
            print(f"The chest is trapped! You take {abs(floor) * 5} damage!")
            if player1.health != "infinite":
                player1.health -= abs(floor) * 5
                if player1.health < 1:
                    play = "no"
                    time.sleep(3)
                    game_over()
        else:
            player1.gold += gold_in_chest
            if "" in inventory:
                inventory.remove("")
                inventory.insert(0, item_in_chest)
                print(f"The chest is not locked. You open it and find {gold_in_chest} gold and {item_in_chest}.")
            else:
                answer = input(f"The chest is not locked. You open it and find {gold_in_chest} gold and {item_in_chest}. You take the gold but there is no space left in your inventory for more items. Will you descard something to make room for more items? y/n")
                while answer != "y" and answer != "yes" and answer != "n" and answer != "no":
                    answer = input("Will you discard something to make room for more items? y/n")
                if answer == "yes" or answer == "y":
                    answer == input("What will you discard? Type back if you don't want to discard anything.")
                    while answer not in inventory and answer != "back":
                        answer = input("What will you discard? Type back if you don't want to discard anything.")
                    if answer == "back":
                        chest()
                    else:
                        inventory.remove(answer)
                        inventory.insert(0, "leather armor")
                        print(f"You discarded your {answer} and took the {item_in_chest}.")
        item_in_chest = "nothing"
        gold_in_chest = 0
        input("Press ENTER to continue.")
        print_area()
        return
        if answer == "walk":
            print("You can't walk into a chest that small.")
            answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'chest' to open the chest.")
            while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "chest":
                answer = input("Type 'left','right','items','rest', or 'chest'.")
        elif answer == "left":
            if direction == "north":
                direction = "west"
            elif direction == "west":
                direction = "south"
            elif direction == "south":
                direction = "east"
            elif direction == "east":
                direction = "north"
            print_area()
        elif answer == "right":
            if direction == "north":
                direction = "east"
            elif direction == "east":
                direction = "south"
            elif direction == "south":
                direction = "west"
            elif direction == "west":
                direction = "north"
            print_area()
        elif answer == "items":
            items()
        elif answer == "rest":
            rest()
    if answer == "walk":
        print("You can't walk into a chest that small.")
        answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'chest' to open the chest.")
        while answer != "left" and answer != "right" and answer != "items" and answer != "rest" and answer != "chest":
            answer = input("Type 'left','right','items','rest', or 'chest'.")
    elif answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    if play == "no":
        return

def far_chest_left_corner():
    global x
    global y
    global direction
    global just_entered
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                      |             stats                            inventory")
    print("         |                                                                                      |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                                      |        ____________________________          |          name: {player1.name}")
    print(f"         |                                      |       /                           /|         |                                              {player1.gold} gold")
    print(f"         |                                      |      /__________________________ / |         |          class: {player1.Class}")                                                
    print(f"         |                                      |_____|                           | /|_________|                                              {inventory[0]}")
    print(f"         |                                      L     |___________________________|/ |         |          level: {player1.level}")
    print(f"         |                                     L      |                           |  |         |                                              {inventory[1]}")
    print(f"         |                                    L       |             O             |  |         |          health: {player1.health}")
    print(f"         |                                   L        |                           | /          |                                              {inventory[2]}")
    print(f"         |                                  L         |___________________________|/           |          strength: {player1.strength}")
    print(f"         |                                 L                                                   |                                              {inventory[3]}")
    print(f"         |                                L                                                    |          endurance: {player1.endurance}")
    print(f"         |                               L                                                     |                                              {inventory[4]}")
    print(f"         |                              L                                                      |          dexterity: {player1.dexterity}")
    print(f"         |     ️                      L                                                       |                                              {inventory[5]}")
    print(f"         |                            L                                                        |          magic: {player1.magic}")
    print(f"         |                           L                       ️                                |                                              {inventory[6]}")
    print(f"         |                          L                                                          |          hunger: {round_to(player1.hunger)}")
    print(f"         |                         L                                                           |                                              {inventory[7]}")
    print(f"         |                       L                                                             |          condition: {player1.condition}")
    print(f"         |                      L                                                              |                                              {inventory[8]}")
    print(f"         |                     L                                                               |          weapon equiped: {player1.weapon}")
    print(f"         |                    L                                      ️                        |                                              {inventory[9]}")
    print(f"         |                  L                                                                  |          armor equiped: {player1.armor}")
    print("         |                  L                                                                  |")
    print(f"         |                L                                                                    |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a chest.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def far_chest_right_corner():
    global x
    global y
    global just_entered
    global direction
    global play
    if play == "no":
        return
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |_____________________________________________________________________________________|")
    print(f"         |                 ____________________________   |                                    |          name: {player1.name}")
    print(f"         |                /                           /|  |                                    |                                              {player1.gold} gold")
    print(f"         |               /__________________________ / |  |                                    |          class: {player1.Class}")                                                
    print(f"         |______________|                           | /|  |                                    |                                              {inventory[0]}")
    print(f"         |              |___________________________|/ |  L                                    |          level: {player1.level}")
    print(f"         |              |                           |  |   L                                   |                                              {inventory[1]}")
    print(f"         |              |             O             |  |    L                                  |          health: {player1.health}")
    print(f"         |              |                           | /      L                                 |                                              {inventory[2]}")
    print(f"         |              |___________________________|/        L                                |          strength: {player1.strength}")
    print(f"         |                                                     L                               |                                              {inventory[3]}")
    print(f"         |                                                      L                              |          endurance: {player1.endurance}")
    print(f"         |                                                       L                             |                                              {inventory[4]}")
    print(f"         |                                                        L                            |          dexterity: {player1.dexterity}")
    print(f"         |     ️                                                  L                           |                                              {inventory[5]}")
    print(f"         |                                                          L                          |          magic: {player1.magic}")
    print(f"         |                                    ️                     L                         |                                              {inventory[6]}")
    print(f"         |                                                            L                        |          hunger: {round_to(player1.hunger)}")
    print(f"         |                                                             L                       |                                              {inventory[7]}")
    print(f"         |         ️                                                   L                      |          condition: {player1.condition}")
    print(f"         |                                                                L                    |                                              {inventory[8]}")
    print(f"         |                                                                 L                   |          weapon equiped: {player1.weapon}")
    print(f"         |                                             ️                   L                  |                                              {inventory[9]}")
    print(f"         |                                                                    L  ️            |          armor equiped: {player1.armor}")
    print("         |                                                                      L              |")
    print(f"         |                                                                       L             |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You see a chest.")
    answer = input("Type 'left' to turn left. Type 'right' to turn right. Type 'walk' to move forward. Type 'items' to use items. Type 'rest' to rest. Type 'search' to search the room.")
    while answer != "left" and answer != "right" and answer != "walk" and answer != "items" and answer != "rest" and answer != "search":
        answer = input("Type 'left','right', 'walk','items','rest', or 'search'.")
    if answer == "left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print_area()
    elif answer == "right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print_area()
    elif answer == "walk":
        if direction == "north":
            y += 1
        elif direction == "west":
            x -= 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        print_area()
    elif answer == "items":
        items()
    elif answer == "rest":
        rest()
    elif answer == "search":
        search()
    if play == "no":
        return

def fight():
    global play
    if play == "no":
        return
    if floor == -1:
        number = random.randint(1,5)
        if number == 1 or number == 2:
            rat()
        elif number == 3 or number == 4:
            bat()
        elif number == 5:
            slime()
    elif floor == -2:
        number = random.randint(1, 10)
        if number == 1:
            rat()
        elif number == 2:
            bat()
        elif number == 3 or number == 4:
            slime()
        elif number > 4 and number < 8:
            zombie()
        elif number > 7 and number < 11:
            ghost()
    elif floor == -3:
        number = random.randint(1, 10)
        if number == 1 or number == 2:
            slime()
        elif number > 2 and number < 5:
            zombie()
        elif number > 4 and number < 7:
            ghost()
        elif number > 6 and number < 11:
            salamander()

def rat():
    global enemy
    global enemy_attack
    global enemy_health
    global enemy_avoidance
    global enemy_defence
    global enemy_accuracy
    global enemy_XP
    global enemy_gold
    global enemy_condition
    global play
    global answer
    if play == "no":
        return
    enemy = "rat"
    enemy_attack = 16
    enemy_health = 10
    enemy_avoidance = 2
    enemy_defence = 6
    enemy_accuracy = 15
    enemy_XP = 5
    enemy_gold = 0
    enemy_condition = "none"
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          name: {player1.name}")
    print(f"         |                                                                                     |                                              {player1.gold} gold")
    print(f"         |                          /\\                         /\\                              |          class: {player1.Class}")                                                
    print(f"         |                          | \\                       /  |                             |                                              {inventory[0]}")
    print(f"         |                          |  \\_____________________/   |             ?               |          level: {player1.level}")
    print(f"         |                          |  /                      \\  |            /                |                                              {inventory[1]}")
    print(f"         |                          | /                        \\ |           /                 |          health: {player1.health}")
    print(f"         |                          |/          O      O        \\|          /                  |                                              {inventory[2]}")
    print(f"         |                          |                            |         /                   |          strength: {player1.strength}")
    print(f"         |                          |     __________________     |      __/                    |                                              {inventory[3]}")
    print(f"         |                          |    |\\    /\\    /\\    /|    |     /                       |          endurance: {player1.endurance}")
    print(f"         |                          |    | \\  /  \\  /  \\  / |    |    /                        |                                              {inventory[4]}")
    print(f"         |                          |    |  \\/    \\/    \\/  |    |   /                         |          dexterity: {player1.dexterity}")
    print(f"         |     ️                   |    |\\    /\\    /\\    /|    |  /                          |                                              {inventory[5]}")
    print(f"         |                          |    | \\  /  \\  /  \\  / |    | /                           |          magic: {player1.magic}")
    print(f"         |                          |    |__\\/____\\/____\\/__|️  |/                            |                                              {inventory[6]}")
    print(f"         |                          |                            |                             |          hunger: {round_to(player1.hunger)}")
    print(f"         |                  \\_\\_\\_|  \\                          /  |_/_/_/                     |                                              {inventory[7]}")
    print(f"         |                   \\_   |   \\________________________/   |   _/                      |          condition: {player1.condition}")
    print(f"         |                     \\  |   |                        |   |  /                        |                                              {inventory[8]}")
    print(f"         |                      \\  \\  |                        |  /  /                         |          weapon equiped: {player1.weapon}")
    print(f"         |                       \\  \\/                          \\/  / ️                       |                                              {inventory[9]}")
    print(f"         |                        \\                                /                           |          armor equiped: {player1.armor}")
    print("         |                        |                                |                           |")
    print(f"         |                        |                                |                           |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("A giant rat attacks!")
    if player1.Class == "mage":
        answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "magic" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
    else:
        answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
    if answer == "attack":
        attack()
    elif answer == "magic":
        magic_spell()
    elif answer == "items":
        items()
    elif answer == "flee":
        flee()

def bat():
    global enemy
    global enemy_attack
    global enemy_health
    global enemy_avoidance
    global enemy_defence
    global enemy_accuracy
    global enemy_XP
    global enemy_gold
    global enemy_condition
    global play
    global answer
    if play == "no":
        return
    enemy = "bat"
    enemy_attack = 17
    enemy_health = 10
    enemy_avoidance = 5
    enemy_defence = 4
    enemy_accuracy = 14
    enemy_XP = 2
    enemy_gold = 0
    enemy_condition = "none"
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                   /\\              /\\                                |              stats                            inventory")
    print("         |                                  |  \\____________/ |                                |              -----                            ---------")
    print("         |                                  |  /            \ |                                |")
    print(f"         |                                  \\|    _     _   |/                                 |          name: {player1.name}")
    print(f"         |                                   |       |      |                                  |                                              {player1.gold} gold")
    print(f"         |                                    \\    _____   /                                   |          class: {player1.Class}")                                                
    print(f"         |                                     \\   V   V  /                                    |                                              {inventory[0]}")
    print(f"         |                                      |        |                                     |          level: {player1.level}")
    print(f"         |                  ____________________|        |___________________                  |                                              {inventory[1]}")
    print(f"         |                  |                   |        |                   |                 |          health: {player1.health}")
    print(f"         |                  |                   |        |                   |                 |                                              {inventory[2]}")
    print(f"         |                  |                   |        |                   |                 |          strength: {player1.strength}")
    print(f"         |                  |                   |        |                   |                 |                                              {inventory[3]}")
    print(f"         |                  |            _______|        |_____              |                 |          endurance: {player1.endurance}")
    print(f"         |                  |           /       |        |     \\             |                 |                                              {inventory[4]}")
    print(f"         |                  |          /        |        |      \\            |                 |          dexterity: {player1.dexterity}")
    print(f"         |     ️           |         /         |        |       \\           |                 |                                              {inventory[5]}")
    print(f"         |                  |        /          |        |         \\         |                 |          magic: {player1.magic}")
    print(f"         |                  |       /           |  ____  |      ️  \\        |                 |                                             {inventory[6]}")
    print(f"         |                  |      /            / /    \\ \\            \\      |                 |          hunger: {round_to(player1.hunger)}")
    print(f"         |                  |     /            / /      \\ \\            \\     |                 |                                              {inventory[7]}")
    print(f"         |                  |    /            / /        \\ \\            \\    |                 |          condition: {player1.condition}")
    print(f"         |                  |   /            /_/          \\_\\            \\   |                 |                                              {inventory[8]}")
    print(f"         |                  |  /                                          \\  |                 |          weapon equiped: {player1.weapon}")
    print(f"         |                  | /                                          ️\\ |                 |                                              {inventory[9]}")
    print(f"         |                  |/                                              \\|                 |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("A bat attacks!")
    if player1.Class == "mage":
        answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "magic" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
    else:
        answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
    if answer == "attack":
        attack()
    elif answer == "magic":
        magic_spell()
    elif answer == "items":
        items()
    elif answer == "flee":
        flee()

def slime():
    global enemy
    global enemy_attack
    global enemy_health
    global enemy_avoidance
    global enemy_defence
    global enemy_accuracy
    global enemy_XP
    global enemy_gold
    global enemy_condition
    global play
    global answer
    if play == "no":
        return
    enemy = "slime"
    enemy_attack = 20
    enemy_health = 10
    enemy_avoidance = 1
    enemy_defence = 10
    enemy_accuracy = 20
    enemy_XP = 5
    enemy_gold = random.randint(0, 2)
    enemy_condition = "none"
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |                                                                                     |             -----                            ---------")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          name: {player1.name}")
    print(f"         |                                                                                     |                                              {player1.gold} gold")
    print(f"         |                                                                                     |          class: {player1.Class}")                                                
    print(f"         |                                                                                     |                                              {inventory[0]}")
    print(f"         |                                                                                     |          level: {player1.level}")
    print(f"         |                                                                                     |                                              {inventory[1]}")
    print(f"         |                                                                                     |          health: {player1.health}")
    print(f"         |                                                                                     |                                              {inventory[2]}")
    print(f"         |                                                                                     |          strength: {player1.strength}")
    print(f"         |                                                                                     |                                              {inventory[3]}")
    print(f"         |                                                                                     |          endurance: {player1.endurance}")
    print(f"         |                               OO~~~OOOOOOOOOO0OOOO                                  |                                              {inventory[4]}")
    print(f"         |                               OOOOOO0OOOOOOOOOOOOOOO                                |          dexterity: {player1.dexterity}")
    print(f"         |     ️                      0   OOOOOOO0OOOOO0OOOOOOOO  0                           |                                              {inventory[5]}")
    print(f"         |                                OOOOOOOOOOOOOOOOOOOOOOOOO 0 0                        |          magic: {player1.magic}")
    print(f"         |______________________________OOO0OOOOOOOOOOO0OOOO0OOOOOOOO__________________________|                                             {inventory[6]}")
    print(f"         |                            OO0OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO                        |          hunger: {round_to(player1.hunger)}")
    print(f"         |                           OOOOOOOOOO0OOOOOOOOOOOOOOOOOOOOOOOO                       |                                              {inventory[7]}")
    print(f"         |                         O0OOOOOOO0OOOOOOOO0OOOOOOOOOOOOOO0OOOOO                     |          condition: {player1.condition}")
    print(f"         |                                                                                     |                                              {inventory[8]}")
    print(f"         |                                                                                     |          weapon equiped: {player1.weapon}")
    print(f"         |                                                               ️                    |                                              {inventory[9]}")
    print(f"         |                                                                                     |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("A slime attacks!")
    if player1.Class == "mage":
        answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "magic" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
    else:
        answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
    if answer == "attack":
        attack()
    elif answer == "magic":
        magic_spell()
    elif answer == "items":
        items()
    elif answer == "flee":
        flee()

def level1boss():
    global enemy
    global enemy_attack
    global enemy_health
    global enemy_avoidance
    global enemy_defence
    global enemy_accuracy
    global enemy_XP
    global enemy_gold
    global enemy_condition
    global play
    global answer
    if play == "no":
        return
    enemy = "orc warrior"
    enemy_attack = 30
    enemy_health = 20
    enemy_avoidance = 5
    enemy_defence = 15
    enemy_accuracy = 20
    enemy_XP = 100
    enemy_gold = 20
    enemy_condition = "none"
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |           ____________           _______________________                            |             stats                            inventory")
    print("         |           \\          /         /      \\       /        \\         ______             |             -----                            ---------")
    print("         |            \\        /_________|       O       O         |_______|      |____________|")
    print(f"         |           /                   |                         |       |      |            |          name: {player1.name}")
    print(f"         |           \\        ___________|                         |_______|      |____________|                                              {player1.gold} gold")
    print(f"         |           /        \\          |         (O  O)          |       |      |            |          class: {player1.Class}")                                                
    print(f"         |          /__________\\     ____|                         |___    |      |            |                                              {inventory[0]}")
    print(f"         |                          /    \\         ______          /   \\  /\\     /             |          level: {player1.level}")
    print(f"         |                         /      \\       /      \\        /     \\/  \\   /              |                                              {inventory[1]}")
    print(f"         |                        /        \\     /        \\      /           \\ /               |          health: {player1.health}")
    print(f"         |                       /          \\___________________/             /                |                                              {inventory[2]}")
    print(f"         |                      /                                            /                 |          strength: {player1.strength}")
    print(f"         |                     |\\ /|                                        |                  |                                              {inventory[3]}")
    print(f"         |                     | | |                                        |                  |          endurance: {player1.endurance}")
    print(f"         |                     | | |                                        |                  |                                              {inventory[4]}")
    print(f"         |                     | | |                                        |                  |          dexterity: {player1.dexterity}")
    print(f"         |     ️              | | |                                        |                  |                                              {inventory[5]}")
    print(f"         |                     | | |                                        |                  |          magic: {player1.magic}")
    print(f"         |_____________________| |_|                                        |__________________|                                             {inventory[6]}")
    print(f"         |                     | | |                                        |                  |          hunger: {round_to(player1.hunger)}")
    print(f"         |                     | | |                                        |                  |                                              {inventory[7]}")
    print(f"         |                     | | |                                        |                  |          condition: {player1.condition}")
    print(f"         |                    /|||\\|                                        |                  |                                              {inventory[8]}")
    print(f"         |                         |                                        |                  |          weapon equiped: {player1.weapon}")
    print(f"         |                         |            _________________       ️  |                  |                                              {inventory[9]}")
    print(f"         |                         |           |                 |          |                  |          armor equiped: {player1.armor}")
    print("         |                         |           |                 |          |                  |")
    print(f"         |                         |           |                 |          |                  |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You are about to go down the stairs, when a giant orc warrior jumps out of the shadows and attacks!")
    if player1.Class == "mage":
        answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "magic" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
    else:
        answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
    if answer == "attack":
        attack()
    elif answer == "magic":
        magic_spell()
    elif answer == "items":
        items()
    elif answer == "flee":
        flee()

def zombie():
    global enemy
    global enemy_attack
    global enemy_health
    global enemy_avoidance
    global enemy_defence
    global enemy_accuracy
    global enemy_XP
    global enemy_gold
    global enemy_condition
    global play
    global answer
    if play == "no":
        return
    enemy = "zombie"
    enemy_attack = 23
    enemy_health = 15
    enemy_avoidance = 5
    enemy_defence = 8
    enemy_accuracy = 20
    enemy_XP = 10
    enemy_gold = random.randint(0, 3)
    enemy_condition = "none"
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                    __________                                       |             stats                            inventory")
    print("         |                                   /          \\                                      |             -----                            ---------")
    print("         |                                  |   O   O    |                                     |")
    print(f"         |                                  |    ___     |                                     |          name: {player1.name}")
    print(f"         |                               ___|   /___\\    |____                                 |                                              {player1.gold} gold")
    print(f"         |                              /                     \\                                |          class: {player1.Class}")                                                
    print(f"         |                             /   /                /  \\                               |                                              {inventory[0]}")
    print(f"         |                            /   /                /   /|                              |          level: {player1.level}")
    print(f"         |                           /   /                /   / |                              |                                              {inventory[1]}")
    print(f"         |                          /   /                /   /  |                              |          health: {player1.health}")
    print(f"         |                         /   /                /   /   |                              |                                              {inventory[2]}")
    print(f"         |                        /   /                /   /    |                              |          strength: {player1.strength}")
    print(f"         |                       /   /|               /   /     |                              |                                              {inventory[3]}")
    print(f"         |                      |   | |              |   |      |                              |          endurance: {player1.endurance}")
    print(f"         |                      |___| |              |___|      |                              |                                              {inventory[4]}")
    print(f"         |                            |                         |                              |          dexterity: {player1.dexterity}")
    print(f"         |     ️                     |  _____________________  |                              |                                              {inventory[5]}")
    print(f"         |                            | |                     | |                              |          magic: {player1.magic}")
    print(f"         |____________________________| |_____________________| |______________________________|                                             {inventory[6]}")
    print(f"         |                            | |                     | |                              |          hunger: {round_to(player1.hunger)}")
    print(f"         |                            | |                     | |                              |                                              {inventory[7]}")
    print(f"         |                            | |                     | |                              |          condition: {player1.condition}")
    print(f"         |                            | |                     | |                              |                                              {inventory[8]}")
    print(f"         |                            | |                     | |                              |          weapon equiped: {player1.weapon}")
    print(f"         |                            / /                    / /         ️                    |                                              {inventory[9]}")
    print(f"         |                           /_/                    /_/                                |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("A zombie attacks!")
    if player1.Class == "mage":
        answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "magic" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
    else:
        answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
    if answer == "attack":
        attack()
    elif answer == "magic":
        magic_spell()
    elif answer == "items":
        items()
    elif answer == "flee":
        flee()

def ghost():
    global enemy
    global enemy_attack
    global enemy_health
    global enemy_avoidance
    global enemy_defence
    global enemy_accuracy
    global enemy_XP
    global enemy_gold
    global enemy_condition
    global play
    global answer
    if play == "no":
        return
    enemy = "ghost"
    enemy_attack = 20
    enemy_health = 15
    enemy_avoidance = 7
    enemy_defence = 7
    enemy_accuracy = 25
    enemy_XP = 10
    enemy_gold = random.randint(0, 3)
    enemy_condition = "none"
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                      |             stats                            inventory")
    print("         |                                ^                       ^                             |             -----                            ---------")
    print("         |                               /                         \\                           |")
    print(f"         |                             /                           \\                           |          name: {player1.name}")
    print(f"         |                             \\                           /                           |                                              {player1.gold} gold")
    print(f"         |                              \\  _____________________  /                            |          class: {player1.Class}")                                                
    print(f"         |                               \\/                     \\/                             |                                              {inventory[0]}")
    print(f"         |                               /                       \\                             |          level: {player1.level}")
    print(f"         |                              /    \\              /     \\                            |                                              {inventory[1]}")
    print(f"         |                             /      O            O       \\                           |          health: {player1.health}")
    print(f"         |                            |                             |                          |                                              {inventory[2]}")
    print(f"         |                            |                             |                          |          strength: {player1.strength}")
    print(f"         |                            |                             |                          |                                              {inventory[3]}")
    print(f"         |                            |                             |                          |          endurance: {player1.endurance}")
    print(f"         |                            |                             |                          |                                              {inventory[4]}")
    print(f"         |                            |      ________________       |                          |          dexterity: {player1.dexterity}")
    print(f"         |     ️                     |                             |                          |                                              {inventory[5]}")
    print(f"         |                            |                             |                          |          magic: {player1.magic}")
    print(f"         |____________________________|_____________________________|__________________________|                                             {inventory[6]}")
    print(f"         |                            |                             |                          |          hunger: {round_to(player1.hunger)}")
    print(f"         |                            |                             |                          |                                              {inventory[7]}")
    print(f"         |                            |                             |                          |          condition: {player1.condition}")
    print(f"         |                            |                             |                          |                                              {inventory[8]}")
    print(f"         |                            |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|                          |          weapon equiped: {player1.weapon}")
    print(f"         |                                                               ️                    |                                              {inventory[9]}")
    print(f"         |                                                                                     |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("A ghost attacks!")
    if player1.Class == "mage":
        answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "magic" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
    else:
        answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
    if answer == "attack":
        attack()
    elif answer == "magic":
        magic_spell()
    elif answer == "items":
        items()
    elif answer == "flee":
        flee()


def level2boss():
    global enemy
    global enemy_attack
    global enemy_health
    global enemy_avoidance
    global enemy_defence
    global enemy_accuracy
    global enemy_XP
    global enemy_gold
    global enemy_condition
    global play
    global answer
    if play == "no":
        return
    enemy = "skeleton king"
    enemy_attack = 35
    enemy_health = 20
    enemy_avoidance = 25
    enemy_defence = 30
    enemy_accuracy = 37
    enemy_XP = 200
    enemy_gold = 30
    enemy_condition = "none"
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                     _____________                                    |             stats                            inventory")
    print("         |                                    /              \\                                  |             -----                            ---------")
    print("         |                                   |     O     O    |                                |")
    print(f"         |                                  |        |       |                                 |          name: {player1.name}")
    print(f"         |                                   \\              /                                  |                                              {player1.gold} gold")
    print(f"         |                                    \\     ___    /                               /\\  |          class: {player1.Class}")                                                
    print(f"         |                                     |   /   \  |                               / /  |                                              {inventory[0]}")
    print(f"         |                                     |          |                              / /   |          level: {player1.level}")
    print(f"         |                              _______|__________|________                     / /    |                                              {inventory[1]}")
    print(f"         |                             /___________________________\\                   / /     |          health: {player1.health}")
    print(f"         |                            / ___________________________ \\                 / /      |                                              {inventory[2]}")
    print(f"         |                           /  ___________________________  \\               / /       |          strength: {player1.strength}")
    print(f"         |                          /  /___________________________\\  \\             / /        |                                              {inventory[3]}")
    print(f"         |                         /  / ___________________________ \\  \\           / /         |          endurance: {player1.endurance}")
    print(f"         |                        /  /  ___________________________  \\  \\         / /          |                                              {inventory[4]}")
    print(f"         |                       /  /   ___________________________   \\  \\     \\ / /           |          dexterity: {player1.dexterity}")
    print(f"         |     ️               /  /   ____________________________    \\  \\    /\\ /            |                                              {inventory[5]}")
    print(f"         |                     /  /    |     |               |     |    \\  \\  / /\\             |          magic: {player1.magic}")
    print(f"         |____________________/__/_____|     |_______________|     |____/_|\\\\/_/_______________|                                              {inventory[6]}")
    print(f"         |                   //|\\      |     |               |     |   /  | \\\\/                |          hunger: {round_to(player1.hunger)}")
    print(f"         |                  // | \\     |     |               |     |                           |                                              {inventory[7]}")
    print(f"         |                             |     |               |     |                           |          condition: {player1.condition}")
    print(f"         |                             |     |               |     |                           |                                              {inventory[8]}")
    print(f"         |                             |     |               |     |                           |          weapon equiped: {player1.weapon}")
    print(f"         |                             |     |               |     |    ️                     |                                              {inventory[9]}")
    print(f"         |                             |     |               |     |                           |          armor equiped: {player1.armor}")
    print("         |                              |     |               |     |                          |")
    print(f"         |                              \\___/                 \\___/                            |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You are about to go down the stairs, when a giant skeleton king jumps out of the shadows and attacks!")
    if player1.Class == "mage":
        answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "magic" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
    else:
        answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
    if answer == "attack":
        attack()
    elif answer == "magic":
        magic_spell()
    elif answer == "items":
        items()
    elif answer == "flee":
        flee()

def salamander():
    global enemy
    global enemy_attack
    global enemy_health
    global enemy_avoidance
    global enemy_defence
    global enemy_accuracy
    global enemy_XP
    global enemy_gold
    global enemy_condition
    global play
    global answer
    if play == "no":
        return
    enemy = "salamander"
    enemy_attack = 27
    enemy_health = 20
    enemy_avoidance = 10
    enemy_defence = 13
    enemy_accuracy = 30
    enemy_XP = 20
    enemy_gold = random.randint(5, 10)
    enemy_condition = "none"
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                       _________                                     |             stats                            inventory")
    print("         |                                      /         \\                                    |             -----                            ---------")
    print("         |                                     |   O  O    |                                   |")
    print(f"         |                                     \\  \\____/  /                                    |          name: {player1.name}")
    print(f"         |                                      \\   |||  /                                     |                                              {player1.gold} gold")
    print(f"         |                                 ______|  ||| |______                                |          class: {player1.Class}")                                                
    print(f"         |                                /         |\\\\\       \\                               |                                              {inventory[0]}")
    print(f"         |                               /           \\\\\\        \\                              |          level: {player1.level}")
    print(f"         |                              /             \\\\\\        \\                             |                                              {inventory[1]}")
    print(f"         |                             /               \\/         \\                            |          health: {player1.health}")
    print(f"         |                            / /|                      |\\ \\                           |                                              {inventory[2]}")
    print(f"         |                           / / |                      | \\ \\                          |          strength: {player1.strength}")
    print(f"         |                           |/  |                      |  \\|                          |                                              {inventory[3]}")
    print(f"         |                           |   |                      |   |                          |          endurance: {player1.endurance}")
    print(f"         |                           |   |                      |   |                          |                                              {inventory[4]}")
    print(f"         |                           |   |                      |   |                          |          dexterity: {player1.dexterity}")
    print(f"         |     ️                    |   |                      |   |                          |                                              {inventory[5]}")
    print(f"         |                           |   |                      |   |                          |          magic: {player1.magic}")
    print(f"         |___________________________|___|                      |___|__________________________|                                             {inventory[6]}")
    print(f"         |                           |   |  __________________  |   |  _____                   |          hunger: {round_to(player1.hunger)}")
    print(f"         |                          /|\\  | |                  | |\\ /|\\/     \\                  |                                              {inventory[7]}")
    print(f"         |                         /_|_\\ | |\\                 | | /_|_\\      \\                 |          condition: {player1.condition}")
    print(f"         |                               | | \\                | |   \\        /                 |                                              {inventory[8]}")
    print(f"         |                               | |  \\               | |    \\      /                  |          weapon equiped: {player1.weapon}")
    print(f"         |                               | |   \\              | |     \\    /  ️               |                                              {inventory[9]}")
    print(f"         |                               | |    \\             | |      \\  /                    |          armor equiped: {player1.armor}")
    print("         |                               /|\\     \\____________/|\\_______|/                    |")
    print(f"         |                              /_|_\\                /_|_\\                             |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("A salamander attacks!")
    if player1.Class == "mage":
        answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "magic" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
    else:
        answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
    if answer == "attack":
        attack()
    elif answer == "magic":
        magic_spell()
    elif answer == "items":
        items()
    elif answer == "flee":
        flee()

def final_boss_battle():
    global enemy
    global enemy_attack
    global enemy_health
    global enemy_avoidance
    global enemy_defence
    global enemy_accuracy
    global enemy_XP
    global enemy_gold
    global enemy_condition
    global play
    global answer
    if play == "no":
        return
    enemy = "lich"
    enemy_attack = 50
    enemy_health = 100
    enemy_avoidance = 30
    enemy_defence = 45
    enemy_accuracy = 50
    enemy_XP = 1000
    enemy_gold = 1000000000
    enemy_condition = "none"
    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |      ____                              |_______|                                    |             stats                            inventory")
    print("         |  \\  /OOOO\\   /                       __|_______|__                                  |             -----                            ---------")
    print("         |    /OOOOOO\\                   \\     /    \\   /    \\    /                           |")
    print(f"         |_ |OOOOOOOO| __                    |     O   O     |                                 |          name: {player1.name}")
    print(f"         |   \\OOOOOO/                         \\     | |     /                                  |                                              {player1.gold} gold")
    print(f"         |    \\OOOO/              \\           |            |        /                          |          class: {player1.Class}")                                                
    print(f"         | /   |  |  \                        |   _______  |                                   |                                              {inventory[0]}")
    print(f"         |     |  |           \\              /   /_______\\  \\               /                  |          level: {player1.level}")
    print(f"         |     |  |_________________________/                \\_________                        |                                              {inventory[1]}")
    print(f"         |     |  |                  |      \\________________/         \\                       |          health: {player1.health}")
    print(f"         |     |__|__________________|                                  \\                      |                                              {inventory[2]}")
    print(f"         |     |  |                   |                              |\\  \\                     |          strength: {player1.strength}")
    print(f"         |     |  |                   |                              | \\/ \\                    |                                              {inventory[3]}")
    print(f"         |     |  |           __      |                              |  \\  \\     __            |          endurance: {player1.endurance}")
    print(f"         |     |  |                   |                              |   \\  \\                  |                                              {inventory[4]}")
    print(f"         |     |  |                   |                              |    \\  |                 |          dexterity: {player1.dexterity}")
    print(f"         |     |  |           __      |                              |     | |   __            |                                              {inventory[5]}")
    print(f"         |     |  |                   |______________________________|     | |                 |          magic: {player1.magic}")
    print(f"         |_____|  |___________________| U    U    U        U     U   |_____| |_________________|                                             {inventory[6]}")
    print(f"         |     |  |                   |     U  U     U    U    U   U |     | |                 |          hunger: {round_to(player1.hunger)}")
    print(f"         |     |  |                   |  U        U     U   U     U  |     | |                 |                                              {inventory[7]}")
    print(f"         |     |  |                   |        U             U       |    /|||\                |          condition: {player1.condition}")
    print(f"         |     |  |                   |    U        U    U         U |                         |                                              {inventory[8]}")
    print(f"         |     |  |                   | U        U   U     U    U    |                         |          weapon equiped: {player1.weapon}")
    print(f"         |     |  |                   |  U   U     U   U    U       U|   ️                    |                                              {inventory[9]}")
    print(f"         |     |__|                   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|                         |          armor equiped: {player1.armor}")
    print("         |                                                                                     |")
    print(f"         |                                                                                     |          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You open the door and enter into a giant throne room, with eerie blue torches all around. The lich gets up from his throne and attacks!")
    if player1.Class == "mage":
        answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "magic" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
    else:
        answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "items" and answer != "flee":
            answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
    if answer == "attack":
        attack()
    elif answer == "magic":
        magic_spell()
    elif answer == "items":
        items()
    elif answer == "flee":
        flee()

def rest():
    global health
    global hunger
    global play
    if play == "no":
        return
    health == 10
    hunger -= 3
    for lines in range(7):
        print("\n")
    input("You are all rested. Press ENTER to continue.")
    print_area()

def items():
    global inventory
    global play
    global x
    global y
    global direction
    global east_fountain_room_door
    global west_fountain_room_door
    if play == "no":
        return
    item_used = input("which item would you like to use? Type the name of the item you want to use or type 'back' if you don't want to use an item.")
    if item_used == "back":
        if enemy != "none":
            if player1.Class == "mage":
                answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'flee' to run away.")
            else:
                answer = input("Type 'attack' to attack. Type 'flee' to run away.")
            if answer == "attack":
                attack()
            elif answer == "magic":
                magic_spell()
            elif answer == "flee":
                flee()
        else:
            print_area()
    while item_used != inventory [0] and item_used != inventory [1] and item_used != inventory [2] and item_used != inventory [3] and item_used != inventory [4] and item_used != inventory [5] and item_used != inventory [6] and item_used != inventory [7] and item_used != inventory [8] and item_used != inventory [9] and item_used != "back":
        print("You don't have that item.")
        item_used = input("which item would you like to use? Type the name of the item you want to use or type 'back'.")
    if item_used == "back":
        if enemy != "none":
            if player1.Class == "mage":
                answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'flee' to run away.")
            else:
                answer = input("Type 'attack' to attack. Type 'flee' to run away.")
                if answer == "attack":
                    attack()
                elif answer == "magic":
                    magic_spell()
                elif answer == "flee":
                    flee()
    elif item_used == "key":
        if enemy == "none":
            if x == 2 and y == -3 and direction == "west":
                east_fountain_room_door = "unlocked"
                inventory.remove("key")
                inventory.append("")
                print("You unlocked the door!")
            elif x == -2 and y == -3 and direction == "east":
                west_fountain_room_door = "unlocked"
                inventory.remove("key")
                inventory.append("")
                print("You unlocked the door!")
            else:
                print("You can't use this right now.")
            input("Press ENTER to continue.")
            print_area()
        battle_end = True
        print_area()
    else:
        answer = input("What would you like to do with it? Type 'eat' to eat it. Type 'equip' to equip it. Type 'discard' to drop it. Type 'back' if you don't want to do anything with it.")
        if answer == "back":
            if enemy != "none":
                if player1.Class == "mage":
                    answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'flee' to run away.")
                else:
                    answer = input("Type 'attack' to attack. Type 'flee' to run away.")
                    if answer == "attack":
                        attack()
                    elif answer == "magic":
                        magic_spell()
                    elif answer == "flee":
                        flee()
            else:
                battle_end = True
                print_area()
        elif answer == "eat":
            if item_used == "ration" or item_used == "golden apple":
                inventory.remove(item_used)
                inventory.append("")
                if player1.condition != "invincible":
                    if item_used == "ration":
                        player1.hunger += 5
                    elif item_used == "golden apple":
                        if player1.condition != "invincible":
                            player1.hunger += 10
                            player1.magic += 1
                            player1.strength += 1
                            player1.endurance += 1
                            player1.dexterity += 1
                if player1.hunger != "full":
                    if player1.hunger > 10:
                        player1.hunger = 10
                print(f"You gobble up the discusting {item_used} within seconds.")
            else:
                print("You can't eat that!")
        elif answer == "discard":
            inventory.remove(item_used)
            inventory.append("")
            print(f"You throw away the {item_used}.")
        elif answer == "equip":
            if item_used == "shortsword" or item_used == "spear" or item_used == "dagger":
                if player1.weapon == item_used:
                    print(f"The {item_used} is already equiped.")
                else:
                    player1.weapon = item_used
                    print("You equiped the {item_used}.")
                    items()
            elif item_used == "dexterity ring" or item_used == "magic amulet" or item_used == "endurance ring" or item_used == "bracer of strength" or item_used == "magic sock of power" or item_used == "cursed life-sucking amulet":
                if player1.accessory == item_used:
                    print(f"The {item_used} is already equiped.")
                elif player1.accessory == "cursed life-sucking amulet":
                    print("You can't equip anything there because you can't get the {player1.accessory} off.")
                else:
                    if player1.condition != "invincible":
                        if player1.accessory == "dexterity ring":
                            player1.dexterity -= 5
                        elif player1.accessory == "magic amulet":
                            player1.magic -= 5
                        elif player1.accessory == "endurance ring":
                            player1.endurance -= 5
                        elif player1.accessory == "bracer of strength":
                            player1.strength -= 5
                        elif player1.accessory == "magic sock of power":
                            player1.dexterity -= 5
                            player1.magic -= 10
                            player1.endurance -= 5
                            player1.strength -= 5
                    player1.accessory = item_used
                    if player1.condition != "invincible":
                        if item_used == "dexterity_ring":
                            player1.dexterity += 5
                        elif item_used == "magic amulet":
                            player1.magic += 5
                        elif item_used == "endurance ring":
                            player1.endurance += 5
                        elif item_used == "bracer of strength":
                            player1.strength += 5
                        elif item_used == "magic sock of power":
                            player1.dexterity += 5
                            player1.magic += 10
                            player1.endurance += 5
                            player1.strength += 5
                    print("You equiped the {item_used}.")
            else:
                print("You can't equip that!")
        if enemy != "none":
            if player1.Class == "mage":
                answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'flee' to run away.")
            else:
                answer = input("Type 'attack' to attack. Type 'flee' to run away.")
            if answer == "attack":
                attack()
            elif answer == "magic":
                magic_spell()
            elif answer == "flee":
                flee()
        else:
            input("Press ENTER to continue.")
            clear_screen()
            print_area()

def attack():
    global enemy
    global enemy_attack
    global enemy_health
    global enemy_avoidance
    global enemy_defence
    global enemy_accuracy
    global enemy_XP
    global enemy_gold
    global enemy_condition
    global battle_end
    global play
    global weather
    global magic
    if play == "no":
        return
    while enemy_health > 0 and more_than(player1.health, 0) == True and play == "yes":
        if enemy_health < 0 or more_than(player1.health, -1) == False:
            break
        if enemy_health > 0:
            answer = input("How will you attack? Type 'swing' to swing. Type 'thrust' to thrust.")
            while answer != "swing" and answer != "thrust":
                answer = input("Type 'swing' or 'thrust'.")
            if player1.condition == "invincible":
                enemy_health = 0
            else:
                if answer == "swing":
                    if player1.weapon == "shortsword":
                        weapon_bonus = 3
                    elif player1.weapon == "dagger":
                        weapon_bonus = 1
                    elif player1.weapon == "spear":
                        weapon_bonus = 5
                    else:
                        weapon_bonus = 0
                    number = random.randint(1, enemy_avoidance)
                    bonus = random.randint(-1, 1)
                    if number > 1 and number < player1.dexterity + 3:
                        if round(player1.strength*.75) - enemy_defence + bonus < 0:
                            print(f"You dealt 0 damage to the {enemy}!")
                        else:
                            enemy_health -= round(player1.strength*.75) - enemy_defence + bonus + weapon_bonus
                            print(f"You dealt {round(player1.strength*.75) - enemy_defence + bonus + weapon_bonus} damage to the {enemy}!")
                    else:
                        print("You missed.")
                elif answer == "thrust":
                    if player1.weapon == "shortsword":
                        weapon_bonus = 3
                    elif player1.weapon == "dagger":
                        weapon_bonus = 1
                    number = random.randint(1, enemy_avoidance)
                    bonus = random.randint(-1, 1)
                    if number > 4 and number < player1.dexterity + 3:
                        if player1.strength - enemy_defence + bonus + weapon_bonus < 0:
                            print(f"You dealt 0 damage to the {enemy}!")
                        else:
                            enemy_health -= player1.strength - enemy_defence + bonus
                            print(f"You dealt {player1.strength - enemy_defence + bonus + weapon_bonus} damage to the {enemy}!")
                    else:
                        print("You missed.")
        if enemy_health > 0:
            if enemy_condition == "burned" or enemy_condition == "poisoned":
                number = random.randint(1, 2)
                print(f"The {enemy} takes {number} damage from its {enemy_condition}.")
                enemy_health -= number
                number = random.randint(1, 2)
                if number == 1:
                    enemy_condition = "none"
            if weather != "none":
                number = random.randint(2, 4)
                print(f"The {enemy} takes {number} damage from the {weather}.")
                enemy_health -= number
            if enemy_condition == "paralysed" or enemy_condition == "stoned":
                print("The {enemy} can't attack because it's {enemy_condition}.")
                enemy_condition = "none"
            else:
                if player1.armor == "leather armor":
                    armor_bonus = 3
                else:
                    armor_bonus = 0
                number = random.randint(1, player1.dexterity)
                bonus = random.randint(-2, 2)
                if number > 1 and number < enemy_accuracy:
                    if enemy_attack + bonus - player1.endurance - armor_bonus > 0:
                        player1.health -= enemy_attack + bonus - player1.endurance - armor_bonus
                        if player1.health < 0:
                            player1.health = 0
                    if enemy_attack + bonus - player1.endurance - armor_bonus < 0:
                        print(f"The {enemy} attacks and deals 0 damage! You have {player1.health} health left.")
                    else:
                        print(f"The {enemy} attacks and deals {enemy_attack + bonus - player1.endurance - armor_bonus} damage! You have {player1.health} health left.")
                    if play == "no":
                        return
                    elif more_than(player1.health, 0) == False:
                        play = "no"
                        time.sleep(3)
                        game_over()
                        return
                else:
                    print(f"The {enemy} attacks and misses.")
        if enemy_health > 0:
            if player1.Class == "mage":
                answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
                while answer != "attack" and answer != "items" and answer != "flee" and answer != "magic":
                    answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
            else:
                answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
                while answer != "attack" and answer != "items" and answer != "flee":
                    answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'flee' to run away.")
            if answer == "attack":
                attack()
                return
            elif answer == "magic":
                magic()
                return
            elif answer == "items":
                items()
                return
            elif answer == "flee":
                flee()
                return
    if enemy_health < 1:
        print(f"You defeated the {enemy}! You gained {enemy_XP} XP and {enemy_gold} gold!")
        if enemy == "lich":
            end_cutscene()
            return
        player1.gold += enemy_gold
        player1.XP += enemy_XP
        enemy_XP = 0
        enemy_gold = 0
        if player1.level < 100:
            if player1.XP > player1.level * 10:
                player1.XP = 0
                player1.level += 1
                player1.max_health += 1
                if player1.condition != "invicible":
                    if player1.Class == "mage":
                        answer = input(f"Level up! You are now level {player1.level}! Which stat would you like to improve? Type 'strength', 'endurance', 'magic', or 'dexterity'.")
                        while answer != "strength" and answer != "endurance" and answer != "magic" and answer != "dexterity":
                            answer = input("Which stat would you like to improve? Type 'strength', 'endurance', 'magic', or 'dexterity'.")
                    else:
                        answer = input(f"Level up! You are now level {player1.level}! Which stat would you like to improve? Type 'strength', 'endurance', or 'dexterity'.")
                        while answer != "strength" and answer != "endurance" and answer != "dexterity":
                            answer = input("Which stat would you like to improve? Type 'strength', 'endurance', or 'dexterity'.")
                    if answer == "strength":
                        player1.strength += 1
                        print("You are now stronger!")
                    elif answer == "endurance":
                        player1.endurance += 1
                        print("You now have more endurance!")
                    elif answer == "magic":
                        player1.magic += 1
                        print("You now have more powerful magic!")
                    elif answer == "dexterity":
                        player1.dexterity += 1
                        print("You are now more dexterous!")
            if player1.magic != "infinite":
                if player1.Class == "mage":
                    if player1.level == 2:
                        if magic == "fire":
                            spells.append("inferno")# attack + 3
                            print("You learned a new spell! You can now cast inferno!")
                        elif magic == "water":
                            spells.append("ice")# attack + 3
                            print("You learned a new spell! You can now cast ice!")
                        elif magic == "earth":
                            spells.append("rockslide")# attack + 3
                            print("You learned a new spell! You can now cast rockslide!")
                        elif magic == "air":
                            spells.append("twister")# attack + 3
                            print("You learned a new spell! You can now cast twister!")
                    elif player1.level == 5:
                        if magic == "fire":
                            spells.append("courage")# strength + 5
                            print("You learned a new spell! You can now cast courage!")
                        elif magic == "water":
                            spells.append("healing water")# health + 5
                            print("You learned a new spell! You can now cast healing water!") 
                        elif magic == "earth":
                            spells.append("stone skin")# endurance + 5
                            print("You learned a new spell! You can now cast stone skin!") 
                        elif magic == "air":
                            spells.append("escape")#end battle
                            print("You learned a new spell! You can now cast escape!")
                    elif player1.level == 10:
                        if magic == "fire":
                            spells.append("blaze of death")# attack + 5
                            print("You learned a new spell! You can now cast blaze of death!")
                        elif magic == "water":
                            spells.append("acid")# attack + 5
                            print("You learned a new spell! You can now cast acid!")
                        elif magic == "earth":
                            spells.append("nature's power")# magic + 5
                            print("You learned a new spell! You can now cast nature's power!")
                        elif magic == "air":
                            spells.append("lightning")# attack + 5
                            print("You learned a new spell! You can now cast lightning!")
                    elif player1.level == 15:
                        spells.append("teleport")#teleport to entrance
                        print("You learned a new spell! You can now cast teleport!")
                    elif player1.level == 20:
                        if magic == "fire":
                            spells.append("burn")#enemy takes 1-2 damage every turn
                            print("You learned a new spell! You can now cast burn!")
                        elif magic == "water":
                            spells.append("poison")#enemy takes 1-2 damage every turn
                            print("You learned a new spell! You can now cast poison!")
                        elif magic == "earth":
                            spells.append("stone")#enemy can't move
                            print("You learned a new spell! You can now cast stone!")
                        elif magic == "air":
                            spells.append("paralysis")#enemy can't move
                            print("You learned a new spell! You can now cast paralysis!")
                    elif player1.level == 25:
                        spells.append("heal")#health + 10
                        print("You learned a new spell! You can now cast heal!")
                    elif player1.level == 30:
                        if magic == "fire":
                            spells.append("rain of fire")#enemy takes 3-4 damage every turn
                            print("You learned a new spell! You can now cast rain of fire!")
                        elif magic == "water":
                            spells.append("hailstorm")#enemy takes 3-4 damage every turn
                            print("You learned a new spell! You can now cast hailstorm!")
                        elif magic == "earth":
                            spells.append("sandstorm")#enemy takes 3-4 damage every turn
                            print("You learned a new spell! You can now cast sandstorm!")
                        elif magic == "air":
                            spells.append("thunderstorm")#enemy takes 3-4 damage every turn
                            print("You learned a new spell! You can now cast thunderstorm!")
                    elif player1.level == 40:
                        spells.append("shield")#endurance + 10
                        print("You learned a new spell! You can now cast sheild!")
                    elif player1.level == 50:
                        if magic == "fire":
                            spells.append("summon fire elemental")# attack + 5
                            print("You learned a new spell! You can now summon a fire elemental!")
                        elif magic == "water":
                            spells.append("summon water elemental")# attack + 5
                            print("You learned a new spell! You can now summon a water elemental!")
                        elif magic == "earth":
                            spells.append("summon earth elemental")# attack + 5
                            print("You learned a new spell! You can now summon an earth elemental!")
                        elif magic == "air":
                            spells.append("summon air elemental")# attack + 5
                            print("You learned a new spell! You can now summon an air elemental!")
                    elif player1.level == 60:
                        spells.append("destroy")#attack + 10
                        print("You learned a new spell! You can now cast destroy!")
                    elif player1.level == 70:
                        if magic == "fire":
                            spells.append("summon fire dragon")# attack + 10
                            print("You learned a new spell! You can now summon a fire dragon!")
                        elif magic == "water":
                            spells.append("summon water dragon")# attack + 10
                            print("You learned a new spell! You can now summon a water dragon!")
                        elif magic == "earth":
                            spells.append("summon earth dragon")# attack + 10
                            print("You learned a new spell! You can now summon an earth dragon!")
                        elif magic == "air":
                            spells.append("summon air dragon")# attack + 10
                            print("You learned a new spell! You can now summon an air dragon!")
                    elif player1.level == 85:
                        spells.append("ancient power")# strength + 5, endurance + 5, dexterity + 5, magic + 10
                        print("You learned a new spell! You can now cast ancient power!")
                    elif player1.level == 100:
                        spells.append("death blast")# attack + 20
                        print("You learned a new spell! You can now cast death blast!")
        input("press ENTER to continue.")
        enemy = "none"
        battle_end = True
        print_area()
        return
    elif player1.health != "infinite":
        if player1.health < 1:
            game_over()

def flee():
    global battle_end
    global play
    global enemy
    if play == "no":
        return
    if enemy == "orc warrior" or enemy == "skeleton king" or enemy == "lich":
        print("You can't escape!")
        if player1.Class == "mage":
            answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item.")
            while answer != "attack" and answer != "items" and answer != "magic":
                answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'magic' to cast a spell.")
        else:
            answer = input("Type 'attack' to attack. Type 'items' to use an item.")
            while answer != "attack" and answer != "items":
                answer = input("Type 'attack' to attack. Type 'items' to use an item.")
        if answer == "attack":
            attack()
            return
        elif answer == "magic":
            magic_spell()
            return
        elif answer == "items":
            items()
            return
    else:
        if player1.dexterity != "infinite":
            number = random.randint(1, enemy_accuracy)
            if number <= player1.dexterity:
                enemy = "none"
                reset_spells()
                if player1.health > 1:
                    print("You escaped mostly unharmed.")
                else:
                    print("You escaped mostly in one piece.")
                input("Press ENTER to continue.")
            else:
                print("You can't escape!")
                if player1.Class == "mage":
                    answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item.")
                    while answer != "attack" and answer != "items" and answer != "magic":
                        answer = input("Type 'attack' to attack. Type 'items' to use an item. Type 'magic' to cast a spell.")
                else:
                    answer = input("Type 'attack' to attack. Type 'items' to use an item.")
                    while answer != "attack" and answer != "items":
                        answer = input("Type 'attack' to attack. Type 'items' to use an item.")
                if answer == "attack":
                    attack()
                    return
                elif answer == "magic":
                    magic_spell()
                    return
                elif answer == "items":
                    items()
                    return
        else:
            print("You escaped unharmed.")
            input("Press ENTER to continue.")
        enemy = "none"
        reset_spells()
        battle_end = True
        clear_screen()
        print_area()

def rest():
    global battle_end
    global play
    if play == "no":
        return
    if player1.condition != "invincible":
        player1.health = player1.max_health
        player1.hunger -= 5
        clear_screen()
        if player1.hunger < 1:
            for lines in range (23):
                print("")
            print("                                                                                 You starved to death")
            print("                                                                                     GAME OVER")
            for lines in range(23):
                print("")
            time.sleep(2)
            print("")
            play = input(str("Would you like to keep playing? Type 'yes' to keep playing. Type 'no' to quit."))
            while play != "yes" and play != "no":
                play = input(str("type 'yes' to keep playing. Type 'no' to quit"))
            if play == ("no"):
                quit()
        else:
            for lines in range(7):
                print("\n")
            print("You are well rested.")
            input("Press ENTER to continue.")
            battle_end = True
            print_area()
    else:
        print("You are well rested.")
        input("Press ENTER to continue.")
        battle_end = True
        print_area()

def search():
    global direction
    global x
    global y
    global floor
    global play
    if play == "no":
        return
    if just_entered == False:
        if player1.dexterity != "infinite":
            number = random.randint(1, 10000 - player1.dexterity)
        else:
            number = random.randint(1, 1000)
        if number < 0 and number > 100:
            number = random.randint(1, 10)
            player1.gold += number
            print(f"You find {number} gold.")
        elif number < 100 and number > 141:
            if number < 111:
                pickup = "dexterity ring" #dexterity + 5
            elif number > 110 and number < 121:
                pickup = "magic amulet" #magic + 5
            elif number > 120 and number < 131:
                pickup = "endurance ring" #endurance + 5
            elif number > 130 and number < 141:
                pickup = "bracer of strength" #strength + 5
            elif number == 141:
                pickup = "magic sock of power" #dexterity + 5, strength + 5, endurance +5, magic + 10
            if "" in inventory:
                inventory.insert(pickup, 0)
                print(f"You find a {pickup}.")
            else:
                answer = input(f"You find a {pickup}, but you have too many items in your inventory. Would you like to discard something and pick up the {pickup}? y/n")
                while answer != "yes" and answer != "y" and answer != "no" and answer != "n":
                    answer = input(f"Would you like to discard something and pick up the {pickup}? y/n.")
                if answer == "yes" or answer == "y":
                    answer = input("What would you like to discard? Type 'back' if you don't want to discard anything.")
                    while answer not in inventory and answer != "back":
                        answer = input("What would you like to discard? Type 'back' if you don't want to discard anything.")
                    if answer == "back":
                        battle_end = True
                        print_area()
                    else:
                        inventory.remove[answer]
                        inventory.insert[pickkup]
                        print(f"You discarded your {answer} and picked up the {pickup}.")
                        input("Press ENTER to continue.")
        elif number > 141 and number < 150 and player1.condition != "invincible":
            if "" in inventory:
                inventory.insert["cursed life-sucking amulet", 0]
            player1.accessory = "cursed life-sucking amulet" #-1 health every 2 minutes
            print("You find a strange amulet. As soon as you put it on, you feel it sucking the life out of you. You try to take it off but you can't.")
            input("Press ENTER to continue.")
            player1.health -= 1
            if player1.health == 0:
                game_over()
        else:
            print("There's nothing here.")
            input("Press ENTER to continue.")
            print_area()
    else:
        print("There's nothing here.")
        input("Press ENTER to continue.")
        print_area()

def magic_spell():
    global enemy
    global enemy_attack
    global enemy_health
    global enemy_avoidance
    global enemy_defence
    global enemy_accuracy
    global enemy_XP
    global enemy_gold
    global enemy_condition
    global battle_end
    global play
    global weather
    global answer
    global magic
    answer = input(f"What spell will you cast? {', '.join(str(x) for x in spells)}?")
    while answer not in spells:
        answer = input(f"What spell will you cast? {', '.join(str(x) for x in spells)}?")
    if answer == "fireball" or answer == "wind" or answer == "wave" or answer == "dirt bomb":
        if player1.strength == "infinite":
            enemy_health = 0
        else:
            number = random.randint(1, enemy_avoidance)
            bonus = random.randint(-2, 2)
            if number > 1 and number < player1.dexterity:
                if enemy_health - player1.magic - enemy_defence + bonus > 0:
                    print(f"You dealt 0 damage to the {enemy}!")
                else:
                    enemy_health -= player1.magic - enemy_defence + bonus
                    print(f"You dealt {player1.magic - enemy_defence + bonus} damage to the {enemy}!")
            else:
                print("You missed.")
    elif answer == "inferno" or answer == "ice" or answer == "rockslide" or answer == "twister":
        if player1.strength == "infinite":
            enemy_health = 0
        else:
            number = random.randint(1, enemy_avoidance)
            bonus = random.randint(-2, 2)
            if number > 1 and number < player1.dexterity:
                if enemy_health - player1.magic - enemy_defence + bonus + 3 > 0:
                    print(f"You dealt 0 damage to the {enemy}!")
                else:
                    enemy_health -= player1.magic - enemy_defence + bonus + 3
                    print(f"You dealt {player1.magic - enemy_defence + bonus + 3} damage to the {enemy}!")
            else:
                print("You missed.")
    elif answer == "courage":
        if player1.strength == "infinite":
            print("You cast courage on yourself.")
        else:
            player1.strength += 5
            courage = True
            print("You cast courage on yourself. strength + 5.")
    elif answer == "healing water":
        if player.health == "infinite":
            print(f"You healed yourself. Not that it matters, you are invicible.")
        else:
            player1.health += 5
            healing_water = True
            print(f"You healed yourself. health + 5. You are now at {player1.health} health.")
    elif answer == "stone skin":
        if player1.endurance == "infinite":
            print("You cast stone skin on yourself.")
        else:
            player1.endurance += 5
            stone_skin = True
            print("You cast stone skin on yourself. endurance + 5")
    elif answer == "escape":
        print("You cast escape!")
        time.sleep(2)
        reset_spells()
        enemy = "none"
        print_area()
        return
    elif answer == "blaze of death" or answer == "acid" or answer == "lightning":
        if player1.strength == "infinite":
            enemy_health = 0
        else:
            number = random.randint(1, enemy_avoidance)
            bonus = random.randint(-2, 2)
            if number > 1 and number < player1.dexterity:
                enemy_health -= player1.magic - enemy_defence + bonus
                if enemy_health - player1.magic - enemy_defence + bonus + 5 > 0:
                    print(f"You dealt 0 damage to the {enemy}!")
                print(f"You dealt {player1.magic - enemy_defence + bonus + 5} damage to the {enemy}!")
            else:
                print("You missed.")
    elif answer == "nature's power":
        if player1.magic == "infinite":
            print("You cast nature's power on yourself.")
        else:
            natures_power = True
            player1.magic += 5
            print("You cast nature's power on yourself. magic + 5.")
    elif answer == "teleport":
        x = 0
        y = 0
        direction = north
        floor = -1
        reset_spells()
        battle_end = True
        enemy = "none"
        print_area()
    elif answer == "burn":
        enemy_condition = "burn"
        print("You burned the {enemy}!")
    elif answer == "poison":
        enemy_condition = "poison"
        print("You poisoned the {enemy}!")
    elif answer == "stone":
        enemy_condition = "stoned"
        print("You stoned the {enemy}!")
    elif answer == "paralysis":
        enemy_condition = "paralysed"
        print("You paralysed the {enemy}!")
    elif answer == "heal":
        player1.health += 10
        print(f"You healed yourself. Health + 10. You are now at {player1.health} health.")
    elif answer == "rain of fire" or answer == "sandstorm" or answer == "hailstorm" or answer == "thunderstorm":
        weather = answer
        print("You summoned a {answer}.")
    elif answer == "sheild":
        if player1.endurance == "infinite":
            print("You summoned a magic shield.")
        else:
            shield = True
            player1.endurance += 10
            print("You summoned a magic shield. Endurance + 10.")
    elif answer == "fire elemental" or answer == "water elemental" or answer == "earth elemental" or answer == "air elemental":
        if player1.magic == "infinite":
            enemy_health = 0
        else:
            if enemy_health - player1.magic - enemy_defence + bonus + 5 > 0:
                print(f"Your {answer} dealt 0 damage to the {enemy}!")
            else:
                if enemy_health - player1.magic - enemy_defence + bonus + 5 > 0:
                    print(f"Your {answer} dealt 0 damage to the {enemy}!")
                else:
                    enemy_health -= player1.magic - enemy_defence + bonus + 5
                    print(f"Your {answer} dealt {player1.magic - enemy_defence + bonus + 5} damage to the {enemy}!")
    elif answer == "destroy":
        if player1.magic == "infinite":
            enemy_health = 0
        else:
            number = random.randint(1, enemy_avoidance)
            bonus = random.randint(-2, 2)
            if number > 1 and number < player1.dexterity:
                if enemy_health - player1.magic - enemy_defence + bonus + 10 > 0:
                    print(f"You dealt 0 damage to the {enemy}!")
                else:
                    enemy_health -= player1.magic - enemy_defence + bonus + 10
                    print(f"You dealt {player1.magic - enemy_defence + bonus + 10} damage to the {enemy}!")
            else:
                print("You missed.")
    elif answer == "fire dragon" or answer == "water dragon" or answer == "earth dragon" or answer == "air dragon":
        if player1.magic == "infinite":
            enemy_health = 0
        else:
            bonus = random.randint(-2, 2)
            if enemy_health - player1.magic - enemy_defence + bonus + 10 > 0:
                print(f"Your {answer} dealt 0 damage to the {enemy}!")
            else:
                enemy_health - player1.magic - enemy_defence + bonus + 10 > 0
                print(f"Your {answer} dealt {enemy_health - player1.magic - enemy_defence + bonus + 10 < 0} damage to the {enemy}!")
    elif answer == "ancient power":
        if player1.condition == "invincible":
            print("You cast ancient power on yourself.")
        else:
            ancient_power = True
            player1.strength += 5
            player1.endurance += 5
            player1.dexterity += 5
            player1.magic += 10
            print("You cast ancient power on yourself. Strength + 5. Endurance + 5. Dexterity + 5. Magic + 10.")
    elif answer == "death blast":
        if player1.magic == "infinite":
            enemy_health = 0
        else:
            number = random.randint(1, enemy_avoidance)
            bonus = random.randint(-2, 2)
            if number > 1 and number < player1.dexterity:
                if enemy_health - player1.magic - enemy_defence + bonus + 20 > 0:
                    print(f"You dealt 0 damage to the {enemy}")
                else:
                    enemy_health -= player1.magic - enemy_defence + bonus + 20
                    print(f"You dealt {player1.magic - enemy_defence + bonus + 20} damage to the {enemy}!")
            else:
                print("You missed.")
    if enemy_health > 0:
        if enemy_condition == "burned" or enemy_condition == "poisoned":
            number = random.randint(1, 2)
            print(f"The {enemy} takes {number} damage from its {enemy_condition}.")
            enemy_health -= number
            number = random.randint(1, 2)
            if number == 1:
                enemy_condition = "none"
        if weather != "none":
            number = random.randint(2, 4)
            print(f"The {enemy} takes {number} damage from the {weather}.")
            enemy_health -= number
        if enemy_condition == "paralysed" or enemy_condition == "stoned":
            print("The {enemy} can't attack because it's {enemy_condition}.")
            enemy_condition = "none"
        else:
            number = random.randint(1, player1.dexterity)
            bonus = random.randint(-2, 2)
            if player1.armor == "leather armor":
                armor_bonus = 3
            elif player1.armor == "none":
                armor_bonus = 3
            if number > 1 and number < enemy_accuracy:
                if enemy_attack + bonus - player1.endurance - armor_bonus > 0:
                    player1.health -= enemy_attack + bonus - player1.endurance - armor_bonus
                    if player1.health < 0:
                        player1.health = 0
                if enemy_attack - player1.endurance < 0:
                    print(f"The {enemy} attacks and deals 0 damage! You have {player1.health} health left.")
                else:
                    print(f"The {enemy} attacks and deals {enemy_attack + bonus - player1.endurance - armor_bonus} damage! You have {player1.health} health left.")
                if player1.health < 1:
                    play = "no"
                    time.sleep(3)
                    game_over()
                    return
            else:
                print(f"The {enemy} attacks and misses.")
    if enemy_health > 0:
        answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
        while answer != "attack" and answer != "items" and answer != "flee" and answer != "magic":
            answer = input("Type 'attack' to attack. Type 'magic' to cast a spell. Type 'items' to use an item. Type 'flee' to run away.")
        if answer == "attack":
            attack()
        elif answer == "magic":
            magic_spell()
        elif answer == "items":
            items()
        elif answer == "flee":
            flee()
    if enemy_health < 1:
        print(f"You defeated the {enemy}! You gained {enemy_XP} XP and {enemy_gold} gold!")
        player1.gold += enemy_gold
        player1.XP += enemy_XP
        enemy_XP = 0
        enemy_gold = 0
        if player1.level < 100:
            if player1.XP > player1.level * 10:
                player1.XP = 0
                player1.level += 1
                player1.max_health += 1
                if player1.condition != "invicible":
                    if player1.Class == "mage":
                        answer = input(f"Level up! You are now level {player1.level}! Which stat would you like to improve? Type 'strength', 'endurance', 'magic', or 'dexterity'.")
                        while answer != "strength" and answer != "endurance" and answer != "magic" and answer != "dexterity":
                            answer = input("Which stat would you like to improve? Type 'strength', 'endurance', 'magic', or 'dexterity'.")
                    else:
                        answer = input(f"Level up! You are now level {player1.level}! Which stat would you like to improve? Type 'strength', 'endurance', or 'dexterity'.")
                        while answer != "strength" and answer != "endurance" and answer != "dexterity":
                            answer = input("Which stat would you like to improve? Type 'strength', 'endurance', or 'dexterity'.")
                if answer == "strength":
                    player1.strength += 1
                    print("You are now stronger!")
                elif answer == "endurance":
                    player1.endurance += 1
                    print("You now have more endurance!")
                elif answer == "magic":
                    player1.magic += 1
                    print("You now have more powerful magic!")
                elif answer == "dexterity":
                    player1.dexterity += 1
                    print("You are now more dexterous!")
        if player1.magic != "infinite":
            if player1.level == 2:
                if magic == "fire":
                    spells.append("inferno")# attack + 3
                    print("You learned a new spell! You can now cast inferno!")
                elif magic == "water":
                    spells.append("ice")# attack + 3
                    print("You learned a new spell! You can now cast ice!")
                elif magic == "earth":
                    spells.append("rockslide")# attack + 3
                    print("You learned a new spell! You can now cast rockslide!")
                elif magic == "air":
                    spells.append("twister")# attack + 3
                    print("You learned a new spell! You can now cast twister!")
            elif player1.level == 5:
                if magic == "fire":
                    spells.append("courage")# strength + 5
                    print("You learned a new spell! You can now cast courage!")
                elif magic == "water":
                    spells.append("healing water")# health + 5
                    print("You learned a new spell! You can now cast healing water!") 
                elif magic == "earth":
                    spells.append("stone skin")# endurance + 5
                    print("You learned a new spell! You can now cast stone skin!") 
                elif magic == "air":
                    spells.append("escape")#end battle
                    print("You learned a new spell! You can now cast escape!")
            elif player1.level == 10:
                if magic == "fire":
                    spells.append("blaze of death")# attack + 5
                    print("You learned a new spell! You can now cast blaze of death!")
                elif magic == "water":
                    spells.append("acid")# attack + 5
                    print("You learned a new spell! You can now cast acid!")
                elif magic == "earth":
                    spells.append("nature's power")# magic + 5
                    print("You learned a new spell! You can now cast nature's power!")
                elif magic == "air":
                    spells.append("lightning")# attack + 5
                    print("You learned a new spell! You can now cast lightning!")
            elif player1.level == 15:
                spells.append("teleport")#teleport to entrance
                print("You learned a new spell! You can now cast teleport!")
            elif player1.level == 20:
                if magic == "fire":
                    spells.append("burn")#enemy takes 1-2 damage every turn
                    print("You learned a new spell! You can now cast burn!")
                elif magic == "water":
                    spells.append("poison")#enemy takes 1-2 damage every turn
                    print("You learned a new spell! You can now cast poison!")
                elif magic == "earth":
                    spells.append("stone")#enemy can't move
                    print("You learned a new spell! You can now cast stone!")
                elif magic == "air":
                    spells.append("paralysis")#enemy can't move
                    print("You learned a new spell! You can now cast paralysis!")
            elif player1.level == 25:
                spells.append("heal")#health + 10
                print("You learned a new spell! You can now cast heal!")
            elif player1.level == 30:
                if magic == "fire":
                    spells.append("rain of fire")#enemy takes 3-4 damage every turn
                    print("You learned a new spell! You can now cast rain of fire!")
                elif magic == "water":
                    spells.append("hailstorm")#enemy takes 3-4 damage every turn
                    print("You learned a new spell! You can now cast hailstorm!")
                elif magic == "earth":
                    spells.append("sandstorm")#enemy takes 3-4 damage every turn
                    print("You learned a new spell! You can now cast sandstorm!")
                elif magic == "air":
                    spells.append("thunderstorm")#enemy takes 3-4 damage every turn
                    print("You learned a new spell! You can now cast thunderstorm!")
            elif player1.level == 40:
                spells.append("shield")#endurance + 10
                print("You learned a new spell! You can now cast sheild!")
            elif player1.level == 50:
                if magic == "fire":
                    spells.append("summon fire elemental")# attack + 5
                    print("You learned a new spell! You can now summon a fire elemental!")
                elif magic == "water":
                    spells.append("summon water elemental")# attack + 5
                    print("You learned a new spell! You can now summon a water elemental!")
                elif magic == "earth":
                    spells.append("summon earth elemental")# attack + 5
                    print("You learned a new spell! You can now summon an earth elemental!")
                elif magic == "air":
                    spells.append("summon air elemental")# attack + 5
                    print("You learned a new spell! You can now summon an air elemental!")
            elif player1.level == 60:
                spells.append("destroy")#attack + 10
                print("You learned a new spell! You can now cast destroy!")
            elif player1.level == 70:
                if magic == "fire":
                    spells.append("summon fire dragon")# attack + 10
                    print("You learned a new spell! You can now summon a fire dragon!")
                elif magic == "water":
                    spells.append("summon water dragon")# attack + 10
                    print("You learned a new spell! You can now summon a water dragon!")
                elif magic == "earth":
                    spells.append("summon earth dragon")# attack + 10
                    print("You learned a new spell! You can now summon an earth dragon!")
                elif magic == "air":
                    spells.append("summon air dragon")# attack + 10
                    print("You learned a new spell! You can now summon an air dragon!")
            elif player1.level == 85:
                spells.append("ancient power")# strength + 5, endurance + 5, dexterity + 5, magic + 10
                print("You learned a new spell! You can now cast ancient power!")
            elif player1.level == 100:
                spells.append("death blast")# attack + 20
                print("You learned a new spell! You can now cast death blast!")
    input("press ENTER to continue.")
    enemy = "none"
    battle_end = True
    print_area()
    if player1.health != "infinite":
        if player1.health < 1:
            game_over()

def reset_spells():
    global weather
    global courage
    global stone_skin
    global natures_power
    global shield
    global ancient_power
    global ancient_power
    global play
    if play == "no":
        return
    weather = "none"
    if courage == True:
        player1.strength -= 5
        courage = False
    if stone_skin == True:
        player1.endurance -= 5
        stone_skin = False
    if natures_power == True:
        player1.magic -= 5
        natures_power = False
    if shield == True:
        player1.endurance -= 10
        shield = False
    if ancient_power == True:
        player1.strength -= 5
        player1.endurance -= 5
        player1.dexterity -= 5
        player1.magic -= 10
        ancient_power = False

def end_cutscene():
    play = "no"
    clear_screen()
    for lines in range(23):
        print("")
    print("YOU WIN, LICH SLAYER!!!")
    for lines in range(23):
        print("")
    time.sleep(2)
    play = input(str("Do you want to play again? Type 'yes' to play again. Type 'no' to quit."))
    while play != "yes" and play != "no":
        play = input(str("type 'yes' to play again. Type 'no' to quit"))
    if play == "no":
        exit()
    if play == "yes":
        return
        
class player:
    def __init__(self, name, Class, level, XP, health, max_health, strength, endurance, dexterity, magic, hunger, weapon, armor, accessory, condition, gold):
        self.name = name
        self.Class = Class
        self.level = level
        self.XP = XP
        self.health = health
        self.max_health = max_health
        self.strength = strength
        self.endurance = endurance
        self.dexterity = dexterity
        self.magic = magic
        self.hunger = hunger
        self.weapon = weapon
        self.armor = armor
        self.accessory = accessory
        self.condition = condition
        self.gold = gold

while play == "yes":
    global x
    global y
    global direction
    global floor
    in_dungeon = False
    just_entered = True
    new_room = True
    searched_fountain = False
    enemy = "none"
    battle_end = True
    player1 = player("name", "Class", 1, 0, 10, 10, 10, 10, 10, 0, 10, "none", "none", "none", "none", 0)
    invincible = False
    inventory = ["","","","","","","","","","",""]
    courage = False
    stone_skin = False
    natures_power = False
    shield = False
    ancient_power = False
    weather = "none"

    for lines in range(23):
        print("")
    print("                                                                                        Lich's Fortress")
    print("                                                                                      press ENTER to play")
    for lines in range(22):
        print("")
    input("")
    clear_screen()
    player1.name = (input("What's your name?"))
    player1.Class = (input(f"Are you a fighter, a mage, or a thief?"))
    while player1.Class != "fighter" and player1.Class != "mage" and player1.Class != "thief":
        player1.Class = (input("Are you a fighter, a mage, or a thief?"))
    if player1.Class == "fighter":
        player1.strength += 5
        player1.endurance += 5
        player1.dexterity -= 5
    elif player1.Class == "mage":
        player1.strength -= 5
        player1.magic += 10
        answer = input("What kind of magic are you trained in? fire, water, earth, or air?")
        while answer != "fire" and answer != "earth" and answer != "water" and answer != "air":
            answer = input("What kind of magic are you trained in? fire, water, earth, or air?")
        if answer == "fire":
            magic = "fire"
            spells = ["fireball"]
        elif answer == "water":
            magic = "water"
            spells = ["wave"]
        elif answer == "earth":
            magic = "earth"
            spells = ["dirt bomb"]
        elif answer == "air":
            magic = "air"
            spells = ["wind"]
    elif player1.Class == "thief":
        player1.dexterity += 5
    print("Your town has been cursed with a famine by a lich who lives in a dungeon near your town. The only way to break the curse is to slay the lich, so you head to the dungeon to defeat the lich and save your town.")
    answer = input("Input cheat code or press ENTER to continue.")
    if answer == "986753421":
        print("cheat code activated. You are now invincible!")
        player1.level = 100
        player1.strength = "infinite"
        player1.health = "infinite"
        player1.hunger = "full"
        player1.condition = "invincible"
        player1.endurance = "infinite"
        player1.dexterity = "infinite"
        player1.magic = "infinite"
        input("Press ENTER to continue.")
    player1.weapon = "shortsword"# attack + 3
    inventory.insert(0, "ration")# +5 hunger
    inventory.insert(0, "ration")
    inventory.insert(0, "shortsword")
    inventory.remove("")
    inventory.remove("")
    inventory.remove("")
    clear_screen()

    for lines in range (5):
        print("")
    print("          _____________________________________________________________________________________ ")
    print("         |                                                                                     |             stats                            inventory")
    print("         |        *                             *                                              |             -----                            ---------")
    print("         |                   *                                               *                 |")
    print(f"         |                                                 *                          *        |          name: {player1.name}")
    print(f"         |            *                      *                       *                         |                                              {player1.gold} gold")
    print(f"         |                         *                                                           |          class: {player1.Class}")
    print(f"         | *                                           *                                       |                                              {inventory[0]}")
    print(f"         |                    ______________________________________________   *               |          level: {player1.level}")
    print(f"         |                *  |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE|                  |                                              {inventory[1]}")
    print(f"         |                   |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE|            *     |          health: {player1.health}")
    print(f"         |     *             |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE|                  |                                              {inventory[2]}")
    print(f"         |                   |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE|                  |          strength: {player1.strength}")
    print(f"         |                   |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE|                  |                                              {inventory[3]}")
    print(f"         |          *        |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE|       *          |          endurance: {player1.endurance}")
    print(f"         |                   |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE|                  |                                              {inventory[4]}")
    print(f"         |                   |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE|            *     |          dexterity: {player1.dexterity}")
    print(f"         |           *       |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE|                  |                                              {inventory[5]}")
    print(f"         |*                  |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE|                  |          magic: {player1.magic}")
    print(f"         |                   |EEEEEEEEEEEEE||||||||||||||||||||||EEEEEEEEEEE|    *             |                                              {inventory[6]}")
    print(f"         |                   |EEEEEEEEEEEEE||||||||||||||||||||||EEEEEEEEEEE|             *    |          hunger: {round_to(player1.hunger)}")
    print(f"         |    *           *  |EEEEEEEEEEEEE||||||||||||||||||||||EEEEEEEEEEE|                  |                                              {inventory[7]}")
    print(f"         |       *           |EEEEEEEEEEEEE||||||||||||||||||||||EEEEEEEEEEE|      *           |          condition: {player1.condition}")
    print(f"         |                   |EEEEEEEEEEEEE||||||||||||||||||||||EEEEEEEEEEE|                  |                                              {inventory[8]}")
    print(f"         |              *    |EEEEEEEEEEEEE|||||||||||||||=[]||||EEEEEEEEEEE|                  |          weapon equiped: {player1.weapon}")
    print(f"         |                   |EEEEEEEEEEEEE||||||||||||||||||||||EEEEEEEEEEE|          *       |                                              {inventory[9]}")
    print(f"         |  *                |EEEEEEEEEEEEE||||||||||||||||||||||EEEEEEEEEEE|                  |          armor equiped: {player1.armor}")
    print("         |           *       |EEEEEEEEEEEEE||||||||||||||||||||||EEEEEEEEEEE| *                |")
    print(f"         |___________________|EEEEEEEEEEEEE||||||||||||||||||||||EEEEEEEEEEE|__________________|          accessory equiped: {player1.accessory}")
    print("         |_____________________________________________________________________________________|")
    print("")
    print("")
    print("")
    print("You arrive at the dungeon entrance and descend the treacherous staircase into the cold, dark chamber that will probably be your doom.")
    input("Press ENTER to continue.")
    x = 0
    y = 0
    floor = -1
    in_dungeon = True
    just_entered = True
    new_room = False
    chest1 = True
    chest2 = True
    chest3 = True
    chest4 = True
    chest5 = True
    chest6 = True
    chest7 = True
    chest8 = True
    chest9 = True
    chest10 = True
    chest11 = True
    level1boss_alive = True
    level2boss_alive = True
    level3boss_alive = True
    west_fountain_room_door = "locked"
    east_fountain_room_door = "locked"
    searched_fountain = False
    direction = "north"
    clear_screen()
    print_area()
