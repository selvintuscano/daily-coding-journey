def vowelandconsonant(strn):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    if strn in vowels:
        return f"{strn} is a vowel"   
    else:
        return f"{strn} is a consonant"
        

result = vowelandconsonant("b")
print(result)