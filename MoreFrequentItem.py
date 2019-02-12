def more_frequent_item(lst,item1,item2):
    count_1 = lst.count(item1)
    count_2 = lst.count(item2)

    if (count_1 >= count_2):
        return item1
    else:
        return item2
        
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))