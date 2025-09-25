def sed(n):

    vowels = 'aeiouAEIOU'

    st = ""

    for char in n:
        if char not in vowels:
            st = st + char

    return st

n = 'my khan is selvin'
print(sed(n))
