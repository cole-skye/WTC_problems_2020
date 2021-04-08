obstacles_list = []
n = 1


def generate():
    """
    Gets a random list of obstacles_list ranging from 0-10(using random.randint). the obstacles_list range from the range limit(-5)
    so that it doesnt fall over the boundary.
    """

    global obstacles_list
    obstacles_list = [(80,180), (80,-180), (-80,180), (-80,-180), 
    (60,160), (60,-160), (-60,160), (-60,-160), 
    (40, 140), (40,-140), (-40,140), (-40,-140),
    (20, 120), (20, -120), (-20,120), (-20,-120)]

    connect_wall_outer_wall(obstacles_list, n)
    connect_wall_second_outer(obstacles_list, n)
    connect_wall_second_inner(obstacles_list, n)
    connect_wall_inner_wall(obstacles_list, n)
    
    opening(obstacles_list)
    dead_ends(obstacles_list)


def connect_wall_outer_wall(obstacles_list, n):
    """
    Connects the outer wall of the maze by connecting the outer corners with for loops.
    """

    for y in range(obstacles_list[0][1], obstacles_list[1][1], -n):

        x = obstacles_list[0][0]
        new_y = (x,y)
        obstacles_list.append(new_y)
    
    for y in range(obstacles_list[2][1], obstacles_list[3][1], -n):

        x = obstacles_list[2][0]
        new_y = (x,y)
        obstacles_list.append(new_y)

    for x in range(obstacles_list[0][0], obstacles_list[2][0], -n):

        y = obstacles_list[0][1]
        new_x = (x,y)
        obstacles_list.append(new_x)
    
    for x in range(obstacles_list[1][0], obstacles_list[3][0], -n):

        y = obstacles_list[1][1]
        new_x = (x,y)
        obstacles_list.append(new_x)
        

    return obstacles_list


def connect_wall_second_outer(obstacles_list, n):
    """
    Connects the second outer wall of the maze by connecting the outer corners with for loops.
    """
    
    for y in range(obstacles_list[4][1], obstacles_list[5][1], -n):

        x = obstacles_list[4][0]
        new_y = (x,y)
        obstacles_list.append(new_y)
    
    for y in range(obstacles_list[6][1], obstacles_list[7][1], -n):

        x = obstacles_list[6][0]
        new_y = (x,y)
        obstacles_list.append(new_y)

    for x in range(obstacles_list[4][0], obstacles_list[6][0], -n):
        
        y = obstacles_list[6][1]
        new_x = (x,y)
        obstacles_list.append(new_x)

    for x in range(obstacles_list[5][0], obstacles_list[7][0], -n):

        y = obstacles_list[7][1]
        new_x = (x,y)
        obstacles_list.append(new_x)   



    return obstacles_list


def connect_wall_second_inner(obstacles_list, n):
    """
    Connects the second inner wall of the maze by connecting the outer corners with for loops.
    """
    
    for y in range(obstacles_list[8][1], obstacles_list[9][1], -n):

        x = obstacles_list[8][0]
        new_y = (x,y)
        obstacles_list.append(new_y)

    for y in range(obstacles_list[10][1], obstacles_list[11][1], -n):

        x = obstacles_list[10][0]
        new_y = (x,y)
        obstacles_list.append(new_y)

    for x in range(obstacles_list[8][0], obstacles_list[10][0], -n):
        
        y = obstacles_list[8][1]
        new_x = (x,y)
        obstacles_list.append(new_x)

    for x in range(obstacles_list[9][0], obstacles_list[11][0], -n):

        y = obstacles_list[11][1]
        new_x = (x,y)
        obstacles_list.append(new_x) 


def connect_wall_inner_wall(obstacles_list, n):
    """
    Connects the inner most wall of the maze by connecting the outer corners with for loops.
    """
    
    for y in range(obstacles_list[12][1], obstacles_list[13][1], -n):

        x = obstacles_list[12][0]
        new_y = (x,y)
        obstacles_list.append(new_y)

    for y in range(obstacles_list[14][1], obstacles_list[15][1], -n):

        x = obstacles_list[14][0]
        new_y = (x,y)
        obstacles_list.append(new_y)

    for x in range(obstacles_list[13][0], obstacles_list[15][0], -n):

        y = obstacles_list[13][1]
        new_x = (x,y)
        obstacles_list.append(new_x)

    for x in range(obstacles_list[12][0], obstacles_list[14][0], -n):

        y = 120
        new_x = (x,y)
        obstacles_list.append(new_x) 


def opening(obstacles_list):
    """
    Pops indexes that create openings in the maze.
    """

    obstacles_list.pop(obstacles_list.index((80 , 175)))
    obstacles_list.pop(obstacles_list.index((80 , 174)))
    obstacles_list.pop(obstacles_list.index((80 , 173)))
    obstacles_list.pop(obstacles_list.index((80 , 172)))
    obstacles_list.pop(obstacles_list.index((80 , 171)))
    obstacles_list.pop(obstacles_list.index((80 , 170)))
    obstacles_list.pop(obstacles_list.index((80 , 169)))
    obstacles_list.pop(obstacles_list.index((80 , 168)))
    obstacles_list.pop(obstacles_list.index((80 , 167)))
    obstacles_list.pop(obstacles_list.index((80 , 166)))
    obstacles_list.pop(obstacles_list.index((80 , 165)))
    obstacles_list.pop(obstacles_list.index((-60 , -155)))
    obstacles_list.pop(obstacles_list.index((-60 , -154)))
    obstacles_list.pop(obstacles_list.index((-60 , -153)))
    obstacles_list.pop(obstacles_list.index((-60 , -152)))
    obstacles_list.pop(obstacles_list.index((-60 , -151)))
    obstacles_list.pop(obstacles_list.index((-60 , -150)))
    obstacles_list.pop(obstacles_list.index((-60 , -149)))
    obstacles_list.pop(obstacles_list.index((-60 , -148)))
    obstacles_list.pop(obstacles_list.index((-60 , -147)))
    obstacles_list.pop(obstacles_list.index((-60 , -146)))
    obstacles_list.pop(obstacles_list.index((-60 , -145)))
    obstacles_list.pop(obstacles_list.index((40 , -5)))
    obstacles_list.pop(obstacles_list.index((40 , -4)))
    obstacles_list.pop(obstacles_list.index((40 , -3)))
    obstacles_list.pop(obstacles_list.index((40 , -2)))
    obstacles_list.pop(obstacles_list.index((40 , -1)))
    obstacles_list.pop(obstacles_list.index((40 , 0)))
    obstacles_list.pop(obstacles_list.index((40 , 1)))
    obstacles_list.pop(obstacles_list.index((40 , 2)))
    obstacles_list.pop(obstacles_list.index((40 , 3)))
    obstacles_list.pop(obstacles_list.index((40 , 4)))
    obstacles_list.pop(obstacles_list.index((40 , 5)))
    obstacles_list.pop(obstacles_list.index((40 , 6)))
    obstacles_list.pop(obstacles_list.index((40 , 7)))
    obstacles_list.pop(obstacles_list.index((40 , 8)))
    obstacles_list.pop(obstacles_list.index((40 , 9)))
    obstacles_list.pop(obstacles_list.index((40 , 10)))
    obstacles_list.pop(obstacles_list.index((15 , 120)))
    obstacles_list.pop(obstacles_list.index((14 , 120)))
    obstacles_list.pop(obstacles_list.index((13 , 120)))
    obstacles_list.pop(obstacles_list.index((12 , 120)))
    obstacles_list.pop(obstacles_list.index((11 , 120)))
    obstacles_list.pop(obstacles_list.index((10 , 120)))
    obstacles_list.pop(obstacles_list.index((9 , 120)))
    obstacles_list.pop(obstacles_list.index((8 , 120)))
    obstacles_list.pop(obstacles_list.index((7 , 120)))
    obstacles_list.pop(obstacles_list.index((6 , 120)))
    obstacles_list.pop(obstacles_list.index((5 , 120)))
    obstacles_list.pop(obstacles_list.index((4 , 120)))
    obstacles_list.pop(obstacles_list.index((3 , 120)))
    obstacles_list.pop(obstacles_list.index((2 , 120)))
    obstacles_list.pop(obstacles_list.index((1 , 120)))
    obstacles_list.pop(obstacles_list.index((0 , 120)))


def dead_ends(obstacles_list_list):
    """
    connects to allowcated co-ordinates that create dead ends.
    the co-ordinates are defined through the obstacles_list index.
    """

    for y in range(obstacles_list_list[13][1], obstacles_list_list[8][1], n):

        x = obstacles_list_list[13][0]
        new_y = (x,y)
        obstacles_list_list.append(new_y)

    for x in range(obstacles_list_list[12][0], obstacles_list_list[8][0], -n):

        y = 30
        new_x = (x,y)
        obstacles_list_list.append(new_x)

    for x in range(obstacles_list_list[8][0], obstacles_list_list[4][0], n):

        y = -60
        new_x = (x,y)
        obstacles_list_list.append(new_x)

    for y in range(obstacles_list_list[11][1], obstacles_list_list[7][1], -n):

        x = 5
        new_y = (x,y)
        obstacles_list_list.append(new_y)

    for x in range(obstacles_list_list[3][0], obstacles_list_list[7][0], n):

        y = -30
        new_x = (x,y)
        obstacles_list_list.append(new_x)


def get_obstacles():
    """
    Returns the obstacles_list_list list to world.turtle.world
    """

    return generate()


def is_position_blocked(x, y):
    """
    Does a check to see if the new x or y position falls within a obstacles_list
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

