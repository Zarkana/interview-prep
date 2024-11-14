def recursive_max_number(list, max = 0):
    if(list == []):
        return max
    else:
        number = list.pop(0)
        if(number > max):
            max = number

        return recursive_max_number(list)

print(recursive_max_number([1,2,3,4,3,2,1]))