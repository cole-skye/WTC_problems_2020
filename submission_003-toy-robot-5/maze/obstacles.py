import random

obstacles_list = []

def generate():
    """
    Gets a random list of obstacles ranging from 0-10(using random.randint). the obstacles range from the range limit(-5)
    so that it doesnt fall over the boundary.
    """

    global obstacles_list
    no_of_obs = random.randint(0,10)
    for i in range(no_of_obs):
        x,y = random.randint(-95,95),random.randint(-195,195)
        # x,y = random.randint(1,1),random.randint(1,1)
        position = (x,y)
        obstacles_list.append(position)
    return obstacles_list


def get_all():
    """
    Returns the obstacles list to world.text.world.
    """

    return generate()


def get_obstacles():
    """
    Returns the obstacles list to world.turtle.world
    """

    return generate()


def is_position_blocked(x, y):
    """
    Does a check to see if the new x or y position falls within a obstacles
    returns "True" is the new postion is within a obstacle.
    """

    global obstacles_list
    for position in obstacles_list:
        if position[0] <= x <= (position[0]+4) and position[1] <= y <= (position[1]+4):
            return True
    return False


def is_path_blocked(x1,y1,x2,y2):
    """
    First does a check to see if the new x or new y position is a negative, if it is it switches x1 with x2 
    the same applies for the y values.
    The range check is to see which position is being moved and then calles is_position_blocked(x,y) 
    """
    
    if x1 > x2:
        x1, x2 = x2, x1
    
    if y1 > y2:
        y1, y2 = y2, y1
    
    if x1 == x2:
        for y in range(y1, y2 +1):
            if is_position_blocked(x1,y) == True:
                return True

    elif y1 == y2:
        for x in range(x1, x2 +1):
            if is_position_blocked(x,y1) == True:
                return True
    return False

