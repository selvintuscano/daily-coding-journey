def reverse_string(n):

    reversed = ''

    for char in n:
        reversed = char + reversed 

    return reversed

n = 'world'
print(reverse_string(n))