output= ''
emp = ['first', 'second', 'third','fourth']
print(emp[2],emp[3])
# emp2 = emp[::1]
# print(emp2)
# print(output)
# for i in emp:
#     print(i)

for i in emp:
    print(i-2)

# if 'first' not in emp or 'second' not in emp:
#     emp.append('fifth')
#     print(emp)


# i = 0
# while i < len(emp):
#     print(emp[i])
#     i+=1

# # print(emp)

# record = []

# def history(command):

#     command = str(command)
#     # print(type(command), "command")
#     com = command.split()
#     # print(type(com), "com")
#     print(com, "com2")
#     for i in com:
#         print(type(i))
#     if 'help' not in com and 'replay' not in com:
#         record.append(command)
#         print(record)   
#         return command

# while True:
#     command = input("what?!!!")
#     history(command)
#     if command == 'off':
#         False
