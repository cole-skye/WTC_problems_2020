import random

code_list = ["0","0","0","0"]
for i in range(0, len(code_list)):
    code = random.randint(1, 8) # 8 possible digits
    while code in code_list:
        code = random.randint(1, 8)  # 8 possible digits
    code_list[i] = code
    print(code)
print(code_list)


        # if    print("Please enter exactly 4 digits.")
        #     get_user_input = int(input("Input 4 digit code: "))
        # elif len(get_list) < 4 or "0" in get_list or len(get_list) >4 or "9" in get_list:
        #     print("Please enter exactly 4 digits.")
        #     tries -=1
        #     get_user_input = int(input("Input 4 digit code: "))
        # else:
        #     print("+")