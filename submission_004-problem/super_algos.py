
def find_min(element):
    """TODO: complete for Step 1"""
    if (len(element) == 1): 
        return element[0]
    if len(element) <= 0 :
        return -1
    for i in element:
        if type(i)!= int or i == "":
            return -1
    if element[0] < element[1]:
        element[1] = element[0]
    return find_min(element[1:])
      

def sum_all(element):
    """TODO: complete for Step 2"""
    if (len(element) == 1): 
        return element[0]
    if len(element) <= 0 :
        return -1
    for i in element:
        if type(i)!= int or i == "":
            return -1
    if (len(element) !=1):
        element[1] = element[0] + element[1]
    return sum_all(element[1:])


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    for i in character_set:
        if type(i) == int or i == "":
            return []
    if len(character_set) < 1 :
        return []
    if n == 1:
        return character_set
    elif len(character_set) > 1:
        new_list = []
        for i in character_set:
            for j in find_possible_strings(character_set, n-1):
                new_list.append(i + j)
    return new_list


# if __name__ == '__main__': 
#     element =  [9,8,3,5,12,27] 
#     print(find_min(element))
#     element =  [1,2,3,4,5,-10] 
#     print(sum_all(element))
#     character_set = ['a','b','c']
#     print(find_possible_strings(character_set, 3))