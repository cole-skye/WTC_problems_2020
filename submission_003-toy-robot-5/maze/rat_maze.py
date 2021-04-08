import random
import turtle
from world.text import world

# Create an empty list to store created 
obstacles_list = []


def get_obstacles():
    '''
    Generates a maze for the robot the solve.
    '''

    global obstacles_list

    obstacles_list = [
    (80,-180), (-80,-180), (-80,180), (80,180),
    (65,-160), (-65,-160), (-65,160), (65,160),
    (50,-140), (-50,-140), (-50,140), (50,140),
    (35,-120), (-35,-120), (-35,120), (35,120),
    (20,-100), (-20,-100), (-20,100), (20,100),
    ]

    obstacle_wall_generator_first_layer(obstacles_list)
    obstacle_wall_generator_second_layer(obstacles_list)
    obstacle_wall_generator_third_layer(obstacles_list)
    obstacle_wall_generator_fourth_layer(obstacles_list)
    obstacle_wall_generator_fifth_layer(obstacles_list)

    dead_end(obstacles_list)
    open_doorway_exit(obstacles_list)
    open_trap_door(obstacles_list)

    return obstacles_list


def obstacle_wall_generator_first_layer(obstacles_list):
    '''
    Generates a first-layer-wall for the maze.
    '''

    for x in range(obstacles_list[0][0], obstacles_list[1][0], -1):

        y = obstacles_list[0][1]
        bottom_x = (x,y)

        obstacles_list.append(bottom_x)

    for y in range(obstacles_list[1][1], obstacles_list[2][1]):

        x = obstacles_list[1][0]
        left_wall_y = (x,y)

        obstacles_list.append(left_wall_y)

    for x in range(obstacles_list[2][0], obstacles_list[3][0]):

        y = obstacles_list[2][1]
        top_wall_x = (x,y)

        obstacles_list.append(top_wall_x)

    for y in range(obstacles_list[3][1], obstacles_list[0][1],  -1):

        x = obstacles_list[3][0]
        right_wall = (x,y)

        obstacles_list.append(right_wall)

    return obstacles_list


def obstacle_wall_generator_second_layer(obstacles_list):
    '''
    Generates a second-layer-wall for the maze.
    '''

    for x in range(obstacles_list[4][0], obstacles_list[5][0], -1):

        y = obstacles_list[4][1]
        top_wall = (x,y)

        obstacles_list.append(top_wall)

    for y in range(obstacles_list[5][1], obstacles_list[6][1]):

        x = obstacles_list[5][0]
        left_wall = (x,y)

        obstacles_list.append(left_wall)

    for x in range(obstacles_list[6][0], obstacles_list[7][0]):

        y = obstacles_list[6][1]
        bottom_wall = (x,y)

        obstacles_list.append(bottom_wall)

    for y in range(obstacles_list[7][1], obstacles_list[4][1], -1):

        x = obstacles_list[7][0]
        right_wall = (x,y)

        obstacles_list.append(right_wall)

    return obstacles_list


def  obstacle_wall_generator_third_layer(obstacles_list):
    '''
    Generates a third-layer-wall for the maze.
    '''

    for x in range(obstacles_list[8][0], obstacles_list[9][0], -1):
    
        y = obstacles_list[8][1]
        bottom_x = (x,y)

        obstacles_list.append(bottom_x)

    for y in range(obstacles_list[9][1], obstacles_list[10][1]):

        x = obstacles_list[9][0]
        left_wall_y = (x,y)

        obstacles_list.append(left_wall_y)

    for x in range(obstacles_list[10][0], obstacles_list[11][0]):

        y = obstacles_list[10][1]
        top_wall_x = (x,y)

        obstacles_list.append(top_wall_x)

    for y in range(obstacles_list[11][1], obstacles_list[8][1], -1):

        x = obstacles_list[11][0]
        right_wall = (x,y)

        obstacles_list.append(right_wall)

    return obstacles_list


def obstacle_wall_generator_fourth_layer(obstacles_list):
    '''
    Generates a fourth-layer-wall for the maze.
    '''

    for x in range(obstacles_list[12][0], obstacles_list[13][0], -1):
    
        y = obstacles_list[12][1]
        bottom_x = (x,y)

        obstacles_list.append(bottom_x)

    for y in range(obstacles_list[13][1], obstacles_list[14][1]):

        x = obstacles_list[13][0]
        left_wall_y = (x,y)

        obstacles_list.append(left_wall_y)

    for x in range(obstacles_list[14][0], obstacles_list[15][0]):

        y = obstacles_list[14][1]
        top_wall_x = (x,y)

        obstacles_list.append(top_wall_x)

    for y in range(obstacles_list[15][1], obstacles_list[12][1], -1):

        x = obstacles_list[15][0]
        right_wall = (x,y)

        obstacles_list.append(right_wall)

    return obstacles_list


def obstacle_wall_generator_fifth_layer(obstacles_list):
    '''
    Generates a fifth-layer-wall for the maze.
    '''

    for x in range(obstacles_list[16][0], obstacles_list[17][0], -1):
    
        y = obstacles_list[16][1]
        bottom_x = (x,y)

        obstacles_list.append(bottom_x)

    for y in range(obstacles_list[17][1], obstacles_list[18][1]):

        x = obstacles_list[17][0]
        left_wall_y = (x,y)

        obstacles_list.append(left_wall_y)

    for x in range(obstacles_list[18][0], obstacles_list[19][0]):

        y = obstacles_list[18][1]
        top_wall_x = (x,y)

        obstacles_list.append(top_wall_x)

    for y in range(obstacles_list[19][1], obstacles_list[16][1], -1):

        x = obstacles_list[19][0]
        right_wall = (x,y)

        obstacles_list.append(right_wall)

    return obstacles_list


def open_doorway_exit(obstacles_list):
    '''
    Creates an opening for the robot to pass through.
    **This is the correct path opening the robot should go through***
    '''

    for i in range(165, 180):

        opening = (80,i)
        obstacles_list.remove(opening)

    for b in range(50, 65):

        opening = (b,-160)
        obstacles_list.remove(opening)

    for i in range(0,20):
        
        opening = (i,140)
        obstacles_list.remove(opening)

    for d in range(105,120):

        opening = (-35,d)
        obstacles_list.remove(opening)

    for i in range(60,80):
    
        opening = (20,i)
        obstacles_list.remove(opening)

    return obstacles_list


def open_trap_door(obstacles_list):
    '''
    Creates an opening for the robot to trick it in to going towards a dead-end.
    **This is not the correct path opening the robot should go through***
    '''

    for i in range(80,100):

        opening = (-65,i)
        obstacles_list.remove(opening)
    
    for c in range(-35,-50, -1):
    
        opening = (c,-140)
        obstacles_list.remove(opening)

    for i in range(35,15):

        opening = (i,-120, -1)
        obstacles_list.remove(opening)

    for e in range(-85,-100, -1):
    
        opening = (20,e)
        obstacles_list.remove(opening)

    return obstacles_list


def dead_end(obstacles_list):
    '''
    Creates a dead-end to trap the robot.
    '''

    #First Layer Walls
    for i in range(160,180):

        wall = (65, i)
        obstacles_list.append(wall)
    
    for i in range(-80,-65):

        wall = (i,-140)
        obstacles_list.append(wall)

    #Second Layer Walls
    for i in range(-65,-50):

        wall = (i,-100)
        obstacles_list.append(wall)

    for i in range(-160,-140):
    
        wall = (50,i)
        obstacles_list.append(wall)

    #Third Layer Walls
    for i in range(-35,-20):
    
        wall = (i,-85)
        obstacles_list.append(wall)

    for i in range(20,35):
    
        wall = (i,60)
        obstacles_list.append(wall)

    return obstacles_list


def is_position_blocked(x, y):
    '''
    Checks if any obstacles_list are on the coordinates of the robot's coordinates.
    '''

    global obstacles_list

    for i in obstacles_list:
        if i[0] <= x <= i[0] + 4 and i[1] <= y <= i[1] + 4:
            return True  
    return False


def is_path_blocked(x1, y1, x2, y2):
    '''
    Checks if any obstacles_list are in the way of the robots path.
    * Using 'is_position_blocked', it prechecks if any obstacles_list in the direction the robot is moving towards.
    '''

    global obstacles_list

    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    if x1 == x2:
        for y in range(y1, y2 +1):
            if is_position_blocked(x1, y):
                return True

    if y1 == y2:            
        for x in range(x1, x2 +1):
            if is_position_blocked(x, y1):
                return True

    return False