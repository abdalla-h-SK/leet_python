def gcdOfStrings(word1, word2):

    if len(word1) < len(word2):
        word1, word2 = word2, word1

    for i, char in enumerate(word1):
        if word1[0] == char:
            if i == 0:
                continue
            fac = word1[:i]
            break
    con1 = (len(word1) % len(fac) == 0)
    con2 = (len(word2) % len(fac) == 0)
    con3 = (word1 == fac * (len(word1)//len(fac)))
    con4 = (word2 == fac * (len(word2)//len(fac)))

    idx_lst = []
    divisions = []

    if con1 and con2 and con3 and con4 :
        for i, char in enumerate(word2):
            if fac[-1] == char:
                idx = i + 1
                idx //= len(fac)
                idx_lst.append(idx)

        for num in idx_lst:
            if (len(word1)//len(fac)) % num == 0 and (len(word2)//len(fac)) % num == 0 :
                divisions.append(num)

        g_c_d = max(divisions)

        return fac * g_c_d
        
      
    else:
        return "non matched"





# That was damn hard


output, lst = gcdOfStrings("abcabc", "abcabcabc")
print(output)
