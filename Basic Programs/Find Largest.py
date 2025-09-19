def largest(lst):
    large = 0
    
    for i in lst:
        if i > large:
            large = i
    return large 

liist= [3,4,2,7]
result = largest(liist)
print(result)