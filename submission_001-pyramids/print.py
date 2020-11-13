height = int(input("Enter the number of rows:"))
for i in range(0,height):
    for j in range(0,height-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end="")
    print()