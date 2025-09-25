def dupi(s):


    seen = set()
    result = ""

    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result
    
print(dupi("programming"))   # progamin
print(dupi("banana"))        # ban
print(dupi("hello world")) 