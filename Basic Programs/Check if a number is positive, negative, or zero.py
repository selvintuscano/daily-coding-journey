def checknumber(lst):

    positive = []
    negative = []
    zero = []

    for i in lst:
        if i == 0:
            zero.append(i)
        elif i >= 1:
            positive.append(i)
        else:
            negative.append(i)
    return positive,negative,zero

se = [3,5,0,-3,-4,7]
result = checknumber(se)
print(result)