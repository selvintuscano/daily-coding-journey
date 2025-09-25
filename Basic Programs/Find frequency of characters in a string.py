def freq(n):
    freqq = {}

    for char in n:
        if char in freqq:
            freqq[char] += 1 
        else:
            freqq[char] = 1

    return freqq

n = "hello world"
result = freq(n)
print(result)