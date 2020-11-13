# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    get_user_input = input("Shape?: ")                                                                      #Get the user input
    while get_user_input.lower() not in ['square', 'pyramid', 'triangle', 'rectangle', 'diamond', 'angle']: #A list of valid commands
        get_user_input = input("Shape?: ")                                                                  #returns user input if command is not valid
    return get_user_input.lower()                                                                           #returns the user input in a lowercase

# TODO: Step 1 - get height (it must be int!)
def get_height():
    num = input("Height?: ")                                                                                #gets the height of the shape
    while num.isdigit() == False or int(num) > 80:                                                          #limits the height of the sahape to stay below 80 lines
        num = input("Height?: ")
    return int(num)                                                                                         #returns the input as a integer


                                                                                                            #the shape functions are all the same, the only difference in them are the ranges for i(row) and j(column)
                                                                                                            #which output the differnt shapes
# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == True:                                                                                     #if outline is True it will print the outlined shape
        for i in range(1,height+1):
            for j in range(1,2*height):
                if i==height or (i+j==height+1 and i>1) :
                    print("*",end="")
                elif j-i==height-1:
                    print("*",end="")
                    break
                else:
                    print(end=" ")
            print()
    else:                                                                                                   #if outline is False it will print a solid shape
        for i in range(0,height):
            for j in range(0,height-i-1):
                print(end=" ")  
            for j in range(0,i*2+1):
                print("*",end="")
            print()

# TODO: Step 3
def draw_angle(height, outline):
    if outline == True:
        
        for i in range(height):
            for j in range(height):
                if i==height-1 or j==height-1 or j==height-i-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print("")    

    else:
        for i in range(0,height):
            for j in range(0,height-i-1):
                print(end=" ")
            for j in range(0,i+1):
                print("*",end="")
            print()  

# TODO: Step 3
def draw_diamond(height, outline):
    if outline == True:
        for i in range(1, height+1):
            for j in range(1,height-i+1):
                print(" ", end="")
            for j in range(1, 2*i):
                if j==1 or j==2*i-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        for i in range(height-1,0, -1):
            for j in range(1,height-i+1):
                print(" ", end="")
            for j in range(1, 2*i):
                if j==1 or j==2*i-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:

        for i in range(1,height-2, +1):
            print(" "*(height-i)+"* "*i)
        for i in range(height-2, 0, -1):
            print(" "*(height-i)+"* "*i)

# TODO: Step 3
def draw_rectangle(height, outline):
    if outline == True:

        for i in range(height):
            for j in range(height +7):
                if i==0 or i==height-1 or j==0 or j==height+6:
                    print("*",end="")
                else:
                    print(" ",end="")
            print("")
    
    else:

        for i in range(0,height):
            for j in range(0,height-i+7):
                print(end="*")  
            for j in range(0,i+5):
                print("*",end="")
            print()

# TODO: Step 3
def draw_square(height, outline):
    if outline == True:
       for i in range(0, height):
            for j in range(0, height):
                if i==0 or i==height-1 or j==height-1 or j==0:
                    print("*",end="")
                else:
                    print(" ",end="")
            print("")
    else:
        for i in range(0,height):
            for j in range(0,height-i):
                print(end="*")  
            for j in range(0,i*1):
                print("*",end="")
            print()

# TODO: Step 4
def draw_triangle(height, outline):
    if outline == True:
        for i in range(height):
            for j in range(i+1):
                if i==height-1 or j==0 or j==i :
                    print("*",end="")
                else:
                    print(" ",end="")
            print("")
    else:
        for i in range(0,height):
            for j in range(0,height-i-1):
                print(end="")
            for j in range(0,i+1):
                print("*",end="")
            print()

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):                                                           #handle commands for the functions
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "rectangle":
        draw_rectangle(height, outline)
    elif shape == "diamond":
        draw_diamond(height, outline)
    elif shape == "angle":
        draw_angle(height, outline)
    
# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():                                                                          #returns True or False for an outlined shape depending on the users input
    get_user = input("Do you want an outline? y/N ") 
    if get_user == "y" or get_user == "Y":
        return True
    else:
        return False

if __name__ == "__main__":
    shape = get_shape()
    height = get_height()
    outline = get_outline()
    draw(shape, height, outline)                                                            #values that were captured by previous functions are stored in the parameters, which are passed to the handle commands

