import random


def run_game():
    """
    TODO: implement Mastermind code here
    """
#Step1: Guess a code

    # for numbers in range (1111 , 8889):          
    #     num = random.randint(numbers)
    #     print (num)

    # code_list = ["0","0","0","0"]
    # for i in range(0, len(code_list)):
    #     code_list[i] = random.randint(1, 8)
    # print(code_list)

    code_list = ["0","0","0","0"]
    for i in range(0, len(code_list)):
        code = random.randint(1, 8)
        while code in code_list:
            code = random.randint(1, 8)
        code_list[i] = code
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")


#Step2: Get a guess

    tries = 12
    

    while tries != 0:

        get_user_input = input("Input 4 digit code: ")

        while (get_user_input.isdigit() == False 
        or len(get_user_input) < 4
        or len(get_user_input) > 4
        or "0" in get_user_input
        or "9" in get_user_input):

            print("Please enter exactly 4 digits.")
            get_user_input = input("Input 4 digit code: ")
        get_list = list(get_user_input)
        
#Step3: Evaluate input
        right_number = 0
        wrong_number = 0
        for number in range(0, len(code_list)):
            # print("1" , get_list[number])
            # print("2" , code_list[number])
            if  code_list[number] == int(get_list[number]) :
                right_number +=1
            elif int(get_list[number]) in code_list:
                wrong_number +=1
            else:
                number+=1

        print("Number of correct digits in correct place:    ", right_number)
        print("Number of correct digits not in correct place:", wrong_number)
        
        if right_number == 4:
            print("Congratulations! You are a codebreaker!")
            print("The code was: ", end="")
            for i in range(0, len(code_list)):
                print(code_list[i], end="")
            break

#Step4: Count guesses

        elif right_number != 4:
            tries -=1
            print("Turns left:", tries )
        if tries == 0:
            print("The code was: ", end="")
            for i in range(0, len(code_list)):
                print(code_list[i], end="")
            break




    pass
if __name__ == "__main__":
    run_game()
