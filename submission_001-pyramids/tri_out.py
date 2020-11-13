height = int(input("number of rows?"))    
for i in range(1,height+1):
            for j in range(1,2*height):
                if i==height or i+j==height+1 :
                    print("*",end="")
                elif j-i==height-1:
                    print("*",end="")
                else:
                    print(end=" ")
            print()