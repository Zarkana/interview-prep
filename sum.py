def sum(integers):
    if (len(integers) > 1): 
        a = integers.pop(0)
        return a + sum(integers)
    else:
        return integers.pop(0)

print(sum([1,2,4]))