import re

#replay things
record = []
silent = False

# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.

def record_history(command):
    """
    Stores the previous commands in a empty list. 
    Except for the 'help' command or any 'replay' commands
    """
    global record
    command = str(command)
    if command != 'help' and 'replay' not in command:
        record.append(command)
        return record


def get_robot_name():
    """
    Gets the robots name.
    """
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """

    (command_name, arg1) = split_command_input(command)

    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1)) or replay_check(command) == True


def replay_check(command):
    """
    Checks to see if either silent/reversed/a digit or a digit with a dash is next to 'replay'
    if not it will return False and not pass valid commands
    """

    flags = command.split(' ', 1)[1]
    range_count = 0
    for flag in flags.split():
        if not re.match("^(silent|reversed|\d+|\d+-\d+)$", flag.lower()):
            return False
        if re.match("^(\d+|\d+-\d+)$", flag):
            range_count += 1
        if re.match("^(\d+-\d+)$", flag):
            if int(flag.split("-")[0]) < int(flag.split("-")[1]):
                return False
    if range_count > 1:
        return False
    if len(flags.split()) != len(set(flags.split())):
        return False
    return True


def split(delimiters, text):
    """
    Splits the string into a list and removes which ever variables are specified.
    """
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def replay_flag(command, robot_name):
    """
    Checks to see if 'reversed' or 'silent' is in command
    and calls funtions according to which word is present or not.
    """
    global silent
    command = command.lower()

    if 'reversed' in command and 'silent' in command:
        silent = True
        replay_reversed_silent(handle_command, command, robot_name)

    elif 'reversed' not in command and 'silent' in command:
        silent = True
        replay_silent(handle_command, command, robot_name)

    elif 'reversed' in command and 'silent' not in command:
        replay_reversed(handle_command,command, robot_name)

    elif 'reversed' not in command and 'silent' not in command:
        do_replay(handle_command, command, robot_name)


def do_replay(handle_command, command, robot_name):
    """
    Does norrmal replay function by calling handle command,
    if an int is passed through as an argument, the int will be passed through as either starting or ending index of recorded list.
    """
    global record
    counter = 0
    command = list(filter(lambda word: word, split(' -',command)))
    if len(command) == 2:
        n = int(command[1])
        for i in record[-n:] :
            handle_command(robot_name, i)
            counter += 1
        print(f" > {robot_name} replayed {(counter)} commands.")
    elif len(command) > 2:
        n = int(command[1])
        n1 = int(command[2])
        for i in record[-n:] :
            handle_command(robot_name, i)
            if counter == n1:
                break
            else:
                counter += 1
        print(f" > {robot_name} replayed {(n-n1)} commands.")
    else:
        for i in record:
            handle_command(robot_name, i)
        print(f" > {robot_name} replayed {len(record)} commands.")


def replay_silent(handle_command, command, robot_name):
    """
    Does norrmal replay silent function by calling handle command,
    if an int is passed through as an argument, the int will be passed through as either starting or ending index of recorded list.
    """
    global silent
    global record
    counter = 0
    command = list(filter(lambda word: word, split(' -',command)))
    
    if len(command) == 3:
        command.sort()
        n = int(command[0])
        for i in record[-n:] :
            handle_command(robot_name, i)
            counter += 1
        print(f" > {robot_name} replayed {(counter)} commands silently.")
    elif len(command) > 3:
        command.sort()
        n = int(command[1])
        n1 = int(command[0])
        for i in record[-n:] :
            handle_command(robot_name, i)
            if counter == n1:
                break
            else:
                counter += 1
        print(f" > {robot_name} replayed {(n-n1)} commands silently.")
    else:
        for i in record:
                handle_command(robot_name, i)
        print(f" > {robot_name} replayed {len(record)} commands silently.")
    silent = False


def replay_reversed(handle_command, command, robot_name):
    """
    Does norrmal replay reversed function by calling handle command,
    if an int is passed through as an argument, the int will be passed through as either starting or ending index of recorded list.
    """
    global record
    record1 = record[::-1]
    counter = 0
    command = list(filter(lambda word: word, split(' -',command)))
    
    if len(command) == 3:
        command.sort()
        n = int(command[0])
        for i in record1[-n:] :
            handle_command(robot_name, i)
            counter += 1
        print(f" > {robot_name} replayed {(counter)} commands in reverse.")
    elif len(command) > 3:
        command.sort()
        n = int(command[1])
        n1 = int(command[0])
        for i in record1[-n:] :
            handle_command(robot_name, i)
            if counter == n1:
                break
            else:
                counter += 1
        print(f" > {robot_name} replayed {(n-n1)} commands in reverse.")
    else:
        for i in record1:
                handle_command(robot_name, i)
        print(f" > {robot_name} replayed {len(record)} commands in reverse.")


def replay_reversed_silent(handle_command, command, robot_name):
    """
    Does norrmal replay reversed silent function by calling handle command,
    if an int is passed through as an argument, the int will be passed through as either starting or ending index of recorded list.
    """
    global record
    global silent
    record1 = record[::-1]
    counter = 0
    command = list(filter(lambda word: word, split(' -',command)))
    
    if len(command) == 4:
        command.sort()
        n = int(command[0])
        for i in record1[-n:] :
            handle_command(robot_name, i)
            counter += 1
        print(f" > {robot_name} replayed {(counter)} commands in reverse silently.")
    elif len(command) > 4:
        command.sort()
        n = int(command[1])
        n1 = int(command[0])
        for i in record1[n1:n] :
            handle_command(robot_name, i)
            if counter == n1:
                break
            else:
                counter += 1
        print(f" > {robot_name} replayed {(n-n1)} commands in reverse silently.")
    else:
        for i in record1:
                handle_command(robot_name, i)
        print(f" > {robot_name} replayed {len(record)} commands in reverse silently.")
    silent = False


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays previous commands
REPLAY SILENT - replays previous commands silently
REPLAY REVERSED - replays previous commands in reverse
REPLAY REVERSED SILENT - replays previous commands silently in reverse
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
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

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

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

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    global silent
    (command_name, arg) = split_command_input(command)
    do_next = True


    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command_name == 'replay':
        replay_flag(command, robot_name)

    if 'replay' in command:
        show_position(robot_name)
    elif silent == True:
        return do_next
    else:
        print(command_output)
        show_position(robot_name)
    return do_next


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index, record

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    record = []
    position_x = 0
    position_y = 0
    current_direction_index = 0

    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = record_history(command)
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
