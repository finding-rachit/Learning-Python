def middle_element(lst):
    try:
        length = len(lst)
        mid = int(length/2)
        
        if ((length%2) == 0):
            return ((lst[mid] + lst[mid-1]) / 2)
        else:
            return lst[mid]
    except:
        return lst

print(middle_element([5, 2, -10, -4, 4, 5]))