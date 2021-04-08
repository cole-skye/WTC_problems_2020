from world.turtle import world as obs

#maze solve things
grid_coordinates = []
grid_maze = [[' ' for rows in range(201)] for columns in range(401)]
path = list()
check_list = list()
solution = list()
commands_list = list()
visited = set()
direction = 'up'
y = 201
x = 101
start = (y,x)


def y_x_maze(grid_coordinates):
    """
    converts turtles (x,y) co-ordinates to positive co-ordinates that can be
    displayed on arrays
    """
    for i in obs.maze_obstacles:
        x , y = i[0], i[1]
        if y <= 0:
            y = 201 + y * -1
        else:
            y = 201 - y
        if x <= 0:
            x = 101 - x * -1
        else:
            x = 101 + x
        grid_co = (y,x)
        grid_coordinates.append(grid_co)

    return grid_coordinates


def grid_co_ordinates(grid_coordinates, grid_maze):
    """
    Takes the converted co-ordinates and draws them on the defined array
    "grid_maze".
    """

    for i in grid_coordinates:
        y , x = i[0] , i[1]
        for new_y in range(y, y - 5, -1):
            for new_x in range(x, x + 5, 1):
                grid_maze[new_y][new_x] = 'x'

    return grid_maze


def grid_boarders(grid_maze):
    """
    Plots out the boaders with designated characters allong the edges of the array.
    These characters help the solver identify which edge it is at.
    """

    for x in range(len(grid_maze[0])):
        grid_maze[0][x] = 'T'

    for x in range(len(grid_maze[0])):
        grid_maze[400][x] = 'B'
    
    for y in range(len(grid_maze)):
        for x in range(len(grid_maze[y][0])):
            grid_maze[y][x] = 'L'

    for y in range(len(grid_maze)):
        for x in range(len(grid_maze[y][200])):
            grid_maze[y][200] = 'R'

    return grid_maze


def maze_solve(grid_maze, edge):
    """
    - Solves the maze by first appending a starting to point to the queue.
    - Path is then given the first index of the queue
    - this new point now becomes the new current position.
    - cuurent position gets cross checked with edge to see if it is at that point
    - if it is the function will return a list of co-ordinates out of the maze.
    - if not the function will continue to run finding all available spaces until it finds the end.
    - a visited set keeps track of all past postions to make sure a co-ordinate is not visited twice.
    """
    global solution, start, path, visited

    end = edge

    queue = [start]
    
    while len(queue) > 0:
        if queue[0] == start:
            path = [queue.pop(0)]
        else:
            path = queue.pop(0)
        current = path[-1]
        if grid_maze[ current[0] ][ current[1] ] == end:
            solution = path
            if edge == "T":
                start = (1,186)
            return path
        elif current not in visited:
            for space in open_spaces(grid_maze, visited, current, end):
                new_path = list(path)
                new_path.append(space)
                queue.append(new_path)
            visited.add(current)


def open_spaces(grid_maze, visited, current, end):
    """
    appends all index around the current position.
    then does a check to see if the index is in the visited list or if the index
    is a open space which can be added to path
    """
    
    spaces = list()
    spaces.append((current[0] -1,current[1]))  #y axis up
    spaces.append((current[0] +1,current[1]))  #y axis down
    spaces.append((current[0], current[1]-1))  #x axis left
    spaces.append((current[0], current[1]+1))  #x axis right

    final = list()
    for i in spaces:
        if grid_maze[ i[0] ][ i[1] ] in [' ', end]  and i not in visited:
            final.append(i)
    return final


def commands():
    """
    Takes in a list of co-ordinates and taked out the first 2 indexes to be passed to
    'command()' which identifies the difference between the two co-ordinates.
    """
    global solution, check_list , commands_list, path, visited

    while len(solution) > 1:
        for i in solution[:2]:
            check_list.append(i)
        command()
        solution.pop(0)
        check_list.clear()

    visited.clear()
    solution.clear()
    path.clear()

    return commands_list


def command():
    """
    appends either 'forward 1', 'left' or 'right'
    depending on the difference between the two co-ordinates.
    """
    global check_list, commands_list, direction

    y1 = check_list[0][0]
    y2 = check_list[1][0]
    x1 = check_list[0][1]
    x2 = check_list[1][1]

    if x1 == x2 and y1 > y2 and direction == 'up':
        commands_list.append("forward 1")

    elif x1 == x2 and y1 < y2 and direction == 'down':
        commands_list.append("forward 1")

    elif y1 == y2 and x1 > x2 and direction == 'left':
        commands_list.append('forward 1')
        
    elif y1 == y2 and x1 < x2 and direction == 'right':
        commands_list.append('forward 1')

    elif x1 == x2 and y1 > y2 and direction == 'left':   
        get_direction('right') 

        commands_list.append('right')
        commands_list.append('forward 1')

    elif x1 == x2 and y1 < y2 and direction == 'left':   
        get_direction('left')  

        commands_list.append('left')
        commands_list.append('forward 1')

    elif x1 == x2 and y1 > y2 and direction == 'right':  
        get_direction('left')  

        commands_list.append('left')
        commands_list.append('forward 1')

    elif x1 == x2 and y1 < y2 and direction == 'right':  
        get_direction('right') 

        commands_list.append('right')
        commands_list.append('forward 1')

    elif y1 == y2 and x1 > x2 and direction == 'up':      
        get_direction('left')  

        commands_list.append('left')
        commands_list.append('forward 1')

    elif y1 == y2 and x1 < x2 and direction == 'up':      
        get_direction('right') 

        commands_list.append('right')
        commands_list.append('forward 1')

    elif y1 == y2 and x1 > x2 and direction == 'down':   
        get_direction('right') 

        commands_list.append('right')
        commands_list.append('forward 1')

    elif y1 == y2 and x1 < x2 and direction == 'down':   
        get_direction('left')    

        commands_list.append('left')
        commands_list.append('forward 1')


def get_direction(command):
    """
    Keeps track of direction.
    """
    global direction

    if command == 'right' and direction == 'up': 
        direction = 'right'

    elif command == 'right' and direction == 'right':
        direction = 'down'

    elif command == 'right' and direction == 'down':
        direction = 'left'

    elif command == 'right' and direction == 'left':
        direction = 'up'

    elif command == 'left' and direction == 'up':
        direction = 'left'

    elif command == 'left' and direction == 'left':
        direction = 'down'

    elif command == 'left' and direction == 'down':
        direction = 'right'

    elif command == 'left' and direction == 'right':
        direction = 'up'


def maze_run(edge):
    """
    sequence of how functions are called in the mazerunner functions.
    """
    y_x_maze(grid_coordinates)
    grid_co_ordinates(grid_coordinates, grid_maze)
    grid_boarders(grid_maze)
    maze_solve(grid_maze, edge)

    return commands()

