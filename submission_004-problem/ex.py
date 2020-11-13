    if (len(element) == 1): 
        return element[0]
    if (len(element) !=1):
        element[1] = element[0] + element[1]
    return find_min(element[1:])

