def reverseWords(s):
    
    words_lst = s.split()
    words_lst.reverse()
    
    return " ".join(words_lst)


s = "the sky is blue"
output = reverseWords(s)
print(output)
