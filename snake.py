def snake(m, b):
    c = m - b
    matchings = [m,c]
    while b > 2:
        b = m - c
        if b >= c/2:
            matchings.append(b)
            m = c
            c = b
        elif b < c/2:
            matchings.append(c - b)
            matchings.append(b)
            m = c - b
            c = b
    if b != 2:
        print("WRONG" + str(b))
    matchings.reverse()
    return matchings


