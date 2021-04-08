# list of all obstacles_list
obstacles_list = []

def get_obstacles():
    """
    Creates a list of tuples representing the coords of all the obstacles
    Returns the obstacles
    """
    draw_y()
    draw_x()
    return obstacles_list


def draw_y():
    """
    Adds all lines of the maze that run on the y-axis.
    Appends coords of those lines to obstacles_list
    """

    global obstacles_list

    for i in range(300):
        obstacles_list.append((-90, -150 + i))
    for i in range(300):
        obstacles_list.append((86, -170 + i))
    for i in range(50):
        obstacles_list.append((-45, -25 + i))
    for i in range(50):
        obstacles_list.append((45, -25 + i))


def draw_x():
    """
    Adds all lines of the maze that run on the x-axis.
    Appends coords of those lines to obstacles_list
    """
    global obstacles_list

    for i in range(55):
        obstacles_list.append((-100 + i, -170))
    for i in range(55):
        obstacles_list.append((35 + i, -180))
    for i in range(55):
        obstacles_list.append((-100 + i, 170))
    for i in range(55):
        obstacles_list.append((35 + i, 140))
    for i in range(100):
        obstacles_list.append((-50 + i, -75))
    for i in range(50):
        obstacles_list.append((-25 + i, -25))
    for i in range(100):
        obstacles_list.append((-50 + i, 75))
    for i in range(50):
        obstacles_list.append((-25 + i, 25))


def is_position_blocked(x,y):
    """
    Returns True is supplied coords are within an obstacle 
    """
    for i in range(len(obstacles_list)):
        if (obstacles_list[i][0] <= x <= (obstacles_list[i][0] + 4)) and (obstacles_list[i][1] <= y <= (obstacles_list[i][1] + 4)):
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    Returns True is there is an obstacle between to points of x or y coords
    """
    if x1 == x2:
        for y in range(sorted([y1, y2])[0], sorted([y1, y2])[1] + 1):
            if is_position_blocked(x1, y):
                return True
    else:
        for x in range(sorted([x1, x2])[0], sorted([x1, x2])[1] + 1):
            if is_position_blocked(x, y1):
                return True
    return False
