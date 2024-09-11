def reverseVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_lst = list(s)

    reversed_vowels = []

    for ltr in word_lst :
        if ltr in vowels:
            reversed_vowels.append(ltr)
    reversed_vowels.reverse()

    idx = 0
    for i , char in enumerate(word_lst):
        if char in vowels:
            del char
            word_lst[i] = reversed_vowels[idx] 
            idx += 1

    word = "".join(word_lst)
    return word

s = "leetcode"
output = reverseVowels(s)
print(output)


# that was damn shit hard

