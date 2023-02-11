def matrixflip(m, d):
    if d == 'h':
        return [row[::-1] for row in m]
    elif d == 'v':
        return m[::-1]
    else:
        return m
