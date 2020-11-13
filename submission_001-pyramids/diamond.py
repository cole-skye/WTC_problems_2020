height = int(input("Enter the number of rows:"))
for i in range(0,height+1):
    print(" "*(height-i)+"*"*i)


#for i in range(0,height):
#    for j in range(0,height-i-1):
#        print(end=" ")  
#    for j in range(0,i*2+1):
#        print("*",end="")
#for i in range(0,height):
#   for j in range(0, height*-1):
#       print(end=" ")  
#   for j in range(height-2, i*2-1):
#        print("*",end="")
#    print()
