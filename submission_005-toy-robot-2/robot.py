def get_input():
    """
    Gets the name of the robot
    """
    name = input('What do you want to name your robot? ').upper()
    print(name + ": Hello kiddo!")

    return name


def get_command(name):
    """
    identifies which command has been invoked and calls the respected functions
    """
    x = 0                                                       # x value is defined
    y = 0                                                       # y value is defined
    direction = 'up'                                            # direction is defined by 'up', this becomes the starting point of the robot
    Power = True                                                # this decleration allows us to keep the while loop open, cause power will remain True until a command break is implemented

    while Power == True:                                        # keeps the decleration in play

        command = input(name + ': What must I do next? ')

        if command.lower() == 'off':                            # shuts the robot down by adding a print function and introducing a break
            print(name + ': Shutting down..')
            break

        elif 'help' in command.lower():                         # calls the defined list of commands in the help function
            get_help()
            
        elif 'forward' in command.lower(): 
            x , y = forward_command(name,command, x , y, direction) # x and y values are stored before next function gets implemented
            
        elif 'back' in command.lower():
            x , y = back_command(name, command, x , y, direction)
            
        elif 'right' == command.lower():
            direction = get_direction(command, direction)
            x , y = right_command(name, command, x , y)

        elif 'left' in command.lower():
            direction = get_direction(command, direction)
            x , y = left_command(name, command, x , y)
        
        elif 'sprint' in command.lower():
            step = command.split()                                 # command for sprint gets split here making it easy to implement a recursive function, and preventing nesting if statements
            if len(step) != 2:
                print(name + ": Sorry, I did not understand" , "'" + command.capitalize() + "'.")
            else:
                no_step = int(step[1])
                x , y = sprint_command(name, no_step, x , y, direction)
            
        else:
            print(name + ": Sorry, I did not understand" , "'"+command.capitalize()+"'.")          


def get_help():
    """
    prints out the commands
    """

    print("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands 
FORWARD - moves the robot foward
BACK - moves the robot backward
RIGHT - turns the robot to the right
LEFT - turns the robot to the left
SPRINT - robot sprints foward\n""")


def print_co(name, x ,y):
    """
    Prints the co-ordinates, co-ordinates are updated through the parameters
    """
    x = str(x)
    y = str(y)
    print(" > "+ name +" now at position ("+ x +","+ y +").")


def forward_command(name, command, x , y, direction):
    """
    Controls the forward function, with the robot name, command, direction and position as parameters.
    """

    step = command.split() # command gets split into two, a list is formed, and this makes it possible to refference the index's 
    if len(step) != 2: # conditioning the user to add a number of steps to the command
        print(name + ": Sorry, I did not understand" , "'" + command.capitalize() + "'.")
    else:
        no_step = int(step[1]) # the second index of the command line gets converted to an int
        if direction == 'up':
            if y + no_step > 200: # condition defines the safe zone for positive y-axis
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                print_co(name, x ,y)
            else:
                step[1] = int(step[1])
                print(f" > {name} moved {step[0].lower()} by {step[1]} steps.")
                y += no_step # y value gets incremented by the value of the number of steps_y
                print_co(name, x ,y)
        elif direction == 'down':
            if y - no_step < -200: # condition defines the safe zone for negative y-axis
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                print_co(name, x ,y)
            else:
                step[1] = int(step[1])
                print(f" > {name} moved {step[0].lower()} by {step[1]} steps.")
                y -= no_step # y value gets decremented by the value of the number of steps_y
                print(f" > {name} now at position ({x},{y}).")    
        elif direction == 'right':
            if x + no_step > 100: # condition defines the safe zone for positive x-axis
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                print_co(name, x ,y)
            else:
                step[1] = int(step[1])
                print(f" > {name} moved {step[0].lower()} by {step[1]} steps.")
                x += no_step # x value gets incremented by the value of the number of steps_y
                print_co(name, x ,y)
        elif direction == 'left':
            if x - no_step < -100: # condition defines the safe zone for negative x-axis
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                print(f" > {name} now at position ({x},{y}).")
            else:
                step[1] = int(step[1])
                print(f" > {name} moved {step[0].lower()} by {step[1]} steps.")
                x -= no_step # x value gets decremented by the value of the number of steps_y
                print_co(name, x ,y)

    return x , y # x , y values are returned allowing us to store the values


def back_command(name, command, x , y, direction):
    """
    Controls the back function, with the robot name, command, direction and position as parameters.
    """

    step = command.split()
    if len(step) != 2:
        print(name + ": Sorry, I did not understand" , "'" + command.capitalize() + "'.")
    else:
        no_step = int(step[1])
        if direction == 'up':
            if y - no_step < -200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                print_co(name, x ,y)
            else:
                step[1] = int(step[1])
                print(f" > {name} moved {step[0].lower()} by {step[1]} steps.")
                y -= no_step
                print_co(name, x ,y)
        elif direction == 'down':
            if y + no_step > 200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                print_co(name, x ,y)
            else:
                step[1] = int(step[1])
                print(f" > {name} moved {step[0].lower()} by {step[1]} steps.")
                y += no_step
                print_co(name, x ,y)     
        elif direction == 'right':
            if x - no_step < -100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                print_co(name, x ,y)
            else:
                step[1] = int(step[1])
                print(f" > {name} moved {step[0].lower()} by {step[1]} steps.")
                x -= no_step
                print_co(name, x ,y)
        elif direction == 'left':
            if x + no_step > 100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                print_co(name, x ,y)
            else: 
                step[1] = int(step[1])
                print(f" > {name} moved {step[0].lower()} by {step[1]} steps.")
                x += no_step
                print_co(name, x ,y)    

    return x , y


def right_command(name, command, x , y):
    """
    Handles the right command.
    """

    step = command.split()
    if len(step) == 1:
        print(f" > {name} turned right.")
        print_co(name, x ,y)
    return x , y


def left_command(name, command, x , y):
    """
    Handles the right command.
    """

    step = command.split()
    if len(step) == 1:
        print(f" > {name} turned left.")
        print_co(name, x ,y)
    return x , y


def sprint_command(name, no_step, x , y, direction):
    """
    Controls the sprint function using recursion with the robots name, numbers steps, the direction and the position as parameters.
    """

    if direction == 'up':
        if y + no_step > 200:
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
            return x , y # return the position to enforce the condition of not exiting the safe zone
        if no_step == 1:
            print(f" > {name} moved forward by {y-y+1} steps.") # prints out the final value
            y += no_step
            print_co(name, x ,y)
            return x , y
        else:
            print(f" > {name} moved forward by {no_step} steps.")
            y += no_step
            return sprint_command(name, no_step-1, x , y, direction) # [function gets called into itself] [step_y-1: is 1 being subtracted from the command value]
    if direction == 'down':
        if y + no_step < -200:
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
            return x , y
        if no_step == 1:
            print(f" > {name} moved forward by {y-y+1} steps.")
            y -= no_step
            print_co(name, x ,y)
            return x , y
        else:
            print(f" > {name} moved forward by {no_step} steps.")
            y -= no_step
            return sprint_command(name, no_step-1, x , y, direction)
    if direction == 'right':
        if x + no_step > 100:
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
            return x , y
        if no_step == 1:
            print(f" > {name} moved forward by {x-x+1} steps.")
            x += no_step
            print_co(name, x ,y)
            return x , y
        else:
            print(f" > {name} moved forward by {no_step} steps.")
            x += no_step
            return sprint_command(name, no_step-1, x , y, direction)
    if direction == 'left':
        if x + no_step < -100:
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
            return x , y
        if no_step == 1:
            print(f" > {name} moved forward by {x-x+1} steps.")
            x -= no_step
            print_co(name, x ,y)
            return x , y
        else:
            print(f" > {name} moved forward by {no_step} steps.")
            x -= no_step
            return sprint_command(name, no_step-1, x , y, direction)


def get_direction(command, direction):
    """
    Gets direction by comparing direction to an initial starting point,
    this gives the robot bearing an positioning
    """

    if command == 'right' and direction == 'up': # initial starting point
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
    return direction


def robot_start():
    """This is the entry function, do not change"""
    name = get_input()

    get_command(name)


if __name__ == "__main__":
    robot_start()
