def larger_list(lst1,lst2):
    len1 = len(lst1)
    len2 = len(lst2)

    if (len1 >= len2):
        return lst1[-1]
    else:
        return lst2[-1]