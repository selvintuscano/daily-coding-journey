def longest_word(sentence):

    word = sentence.split()

    longest = max(word, key=len)

    return longest, len(longest)

print(longest_word("Find the longest word here")) 
