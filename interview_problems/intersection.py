def intersection(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result     
    
print(intersection([1,2,3,6,4], [2,5,7,6]))