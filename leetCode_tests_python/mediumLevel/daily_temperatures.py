def dailyTemperatures(temperatures):
    lst = []

    for i , char in enumerate(temperatures):
        if temperatures[i+1 : ]:
            for x in temperatures[i+1 : ]:
                if char < x :
                    difference = temperatures.index(x) - temperatures.index(char)
                    lst.append(difference)
                    break  
            if char == max(temperatures[i:]):
                lst.append(0)
        else:
            lst.append(0)


    return lst



temperatures = [73,74,75,71,69,72,76,73]
output = dailyTemperatures(temperatures)
print(output)



# it's marked as medium but its way easier than easy ones('_')