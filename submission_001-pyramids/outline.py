height = int(input("number of rows?"))
for i in range(1,height+1):
    for j in range(1,2*height):
        if i+j==height-3 or j-i==height+3 or i-j==height+3 or i+j==height+1:
            print("*",end="")
        else:
            print(end=" ")
    print()
# for i in range (1,height +1):
#     if i == 1 or i == height:
#         print(" " * (height - i) + "*" * (2 * i - 1))
#     else: 
#         print(" " * (height - i) + "*" + " " * (2 * i - 3) + "*")