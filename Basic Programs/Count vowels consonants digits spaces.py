def selvin(n):
    vowels = 'aeiouAEIOU'

    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    space_count = 0

    for char in n :
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1

    return vowel_count, consonant_count, digit_count, space_count


n = "Hello World 123"
print(selvin(n))
