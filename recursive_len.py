def recursive_len(list):
    if(list == []):
        return 0
    else:
        list.pop(0)
        return 1 + recursive_len(list)

print(recursive_len([1,2,3,4,3,2,1]))