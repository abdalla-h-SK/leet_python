def kidsWithCandies(extraCandies, candies):
    
    cons_lst = []
    for candi in candies:

        con = (candi + extraCandies) >= max(candies)
        cons_lst.append(con)

    return cons_lst


candies = [2, 3, 5, 1, 3]
extraCandies = 3
               
cons = kidsWithCandies(candies = candies, extraCandies = extraCandies)

print(cons)
print(type(cons[0]))