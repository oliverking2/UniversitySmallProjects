options = []
value = []
for x1 in range(0, 9):
    for x2 in range(0, 9):
        for y1 in range(0, 9):
            for y2 in range(0, 9):
                for y3 in range(0, 9):
                    for y4 in range(0, 9):
                        for y5 in range(0, 9):
                            if x1 + y1 >= 6 and x1 + x2 + y1 + y2 >= 5 and x1 + x2 + y1 + y2 + y3 >= 7 and x2 + y1 + y2 + y3 + y4 >= 8 and x1 + y2 + y3 + y4 + y5 >= 8 and x1 + x2 + y3 + y4 + y5 >= 7 and x1 + x2 + y4 + y5 >= 5 and x2 + y5 >= 6:
                                if x1+x2 >= 4:
                                    options.append([x1, x2, y1, y2, y3, y4, y5])
                                    cost = 12*7*(x1+x2) + 7.5*4*(y1+y2+y3+y4+y5)
                                    value.append(cost)
                                    if cost < 650:
                                        print(cost, [x1, x2, y1, y2, y3, y4, y5])


print(min(value), options[value.index(min(value))])