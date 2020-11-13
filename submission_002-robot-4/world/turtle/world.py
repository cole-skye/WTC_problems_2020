import robot
import turtle
from typing import Counter
from turtle import Turtle
import world.obstacles as obs

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# Turtle 
t = turtle.Turtle()
obstacles_flag = False

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(robot_name, steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    also calls is_path_blocked with an obstacles flag to check the obstacles
    """

    global position_x, position_y, obstacles_flag
    obstacles_flag = False
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
    

    if obs.is_path_blocked(position_x, position_y, new_x, new_y):
        obstacles_flag = True
        return False
    elif is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    else:
        return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    turtle steps is implemented with a parameter (steps) to tell turtle how far to move forward
    """

    if update_position(robot_name, steps):
        t.forward(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        if obstacles_flag == True:
            return True, robot_name+': Sorry, there is an obstacle in the way.'
        else:
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    turtle steps is implemented with a parameter (steps) to tell turtle how far to move backward
    also update position is checked to indentify which print statement is supposed to be called 
    """

    if update_position(robot_name, steps):
        t.backward(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        if obstacles_flag == True:
            return True, robot_name+': Sorry, there is an obstacle in the way.'
        else:
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    turtle right turn 90 degrees is calles when the "right" command is executed
    also update position is checked to indentify which print statement is supposed to be called 
    """

    global current_direction_index
    t.rt(90)
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)

    """

    global current_direction_index
    t.lt(90)
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def turtle_screen():
    """
    Draws the turtle screen outline
    """

    t.color("red")
    t.pu()
    t.goto(-100,200)
    t.pd()
    t.fd(200)
    t.rt(90)
    t.fd(400)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(400)
    t.pu()


def screen_size():
    """
    defines the turtle screens size
    """

    screen = turtle.Screen()
    screen.setup(width=1000, height=1000)


def show_obstacles():
    """
    prints out the obstacles on the turtle screen
    """

    obs.get_obstacles()
    for ob in obs.obstacles:
        t.goto(ob)
        t.pd()
        t.goto(ob[0],ob[1])
        t.goto(ob[0]+4,ob[1])
        t.goto(ob[0]+4,ob[1]+4)
        t.goto(ob[0],ob[1]+4)
        t.goto(ob[0],ob[1])
        t.pu()

    t.home()
    t.lt(90)


def reset():
    """
    resets all variables when robot is switched off
    """

    global obstacles_flag, position_x, position_y, current_direction_index

    obs.obstacles = []
    obstacles_flag = False
    position_x = 0
    position_y = 0
    current_direction_index = 0


"""
the order of commands when world.turtle.world is called

"""

turtle.tracer(False)
screen_size()
turtle_screen()
show_obstacles()
turtle.tracer(True)

