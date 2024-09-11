def getMaxPoints(points):
    x1 , y1 = 0 , 0
    x2 , y2 = 0 , 0
    slopes_lsts = []

    for i, dem in enumerate(points):
        slope_lst = []
        x1, y1 = dem[0], dem[1]
        points2 = points[:]
        points2.pop(i)

        for dem2 in points2:
            x2 , y2 = dem2[0], dem2[1]

            try:
                slope = (y2 - y1)/(x2 - x1)
            except ZeroDivisionError:
                slope = float('inf')

            slope_lst.append(slope)

        slopes_lsts.append(slope_lst)

    count_slopes = set()
    for lst in slopes_lsts:
        for i in lst:
            cwnt = 1
            for x in lst:
                if i == x:
                    cwnt += 1
            count_slopes.add(cwnt)

    msg = f"The max points on a single line is : {max(count_slopes)}"


    return msg



points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
output = getMaxPoints(points)
print(output)

