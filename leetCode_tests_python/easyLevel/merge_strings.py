def mergeAlternately(word1, word2):
    
    output = ""
    idx = 0

    min_len_word = min(word1, word2, key = len)
    len_min = len(min_len_word)

    for i in range(len_min):
        new_word = f"{word1[idx]}{word2[idx]}"
        output += new_word
        idx += 1

    if len(word1) > len(word2):
        output += word1[len(word2):]
    else:
        output += word2[len(word1):]

    return output

st_word = input("input a word : ")
nd_word = input("input another word : ")

output = mergeAlternately(st_word, nd_word)

print(output)

# It's identified easy but it got me