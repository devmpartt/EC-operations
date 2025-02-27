# adding points on elliptic curve
def addEC(x, y, c):
    p, a, b = c
    x1, y1 = x
    x2, y2 = y
    
    # check for infinity points
    if x == [0, 0]:
        return y
    if y == [0, 0]:
        return x
    
    if x1 == x2 and y1 == y2:
        return doublEC(x, c)
    
    # check for inverse points
    if x1 == x2 and (y1 + y2) % p == 0:
        return [0, 0]
    
    # slope of the line between points
    lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return [x3, y3]

# point doubling on elliptic curve
def doublEC(x, c):
    p, a, b = c
    x1, y1 = x
    
    # infinity check
    if x == [0, 0]:
        return [0, 0]
    
    # slope for the tangent at point
    lam = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    x3 = (lam * lam - 2 * x1) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return [x3, y3]

# test data
additions = [
    [[997, 187, 658], [0, 0], [0, 0], [0, 0]], 
    [[997, 187, 658], [0, 0], [259, 116], [259, 116]], 
    [[997, 187, 658], [918, 431], [0, 0], [918, 431]], 
    [[997, 187, 658], [918, 431], [918, 566], [0, 0]], 
    [[997, 187, 658], [918, 431], [259, 116], [954, 104]]
]

doublings = [
    [[997, 187, 658], [0, 0], [0, 0]], 
    [[997, 187, 658], [918, 431], [580, 560]]
]

print("Testing addEC function:")
for params, x, y, expected in additions:
    result = addEC(x, y, params)
    print(f"addEC({x}, {y}, {params}) = {result}, expected: {expected}")

print("\nTesting doublEC function:")
for params, x, expected in doublings:
    result = doublEC(x, params)
    print(f"doublEC({x}, {params}) = {result}, expected: {expected}")
