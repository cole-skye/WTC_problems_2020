def find_min(element): 
      
    if (len(element) == 1): 
        return element[0]
    if element[0] < element[1]:
        element[1] = element[0]
    return find_min(element[1:])

if __name__ == '__main__': 
    element = [3,6,8,9,3,11] 
    print(find_min(element)) 
