def countevenodd(lst):

    even = 0
    odd = 0 

    for i in lst:
        if i%2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even,odd

lst = [2,5,6,8,9]
result = countevenodd(lst)
print(result)
