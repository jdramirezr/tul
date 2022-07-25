def cost(start_x:int, start_y:int, end_x:int, end_y:int) -> int:
    '''return  '''
    x = abs(end_x - start_x)
    y = abs(end_y - start_y)
    cost = x + y

    if cost > 0:
        cost -= 1
    
    coordinates = []

    for num in range(1, x):
        if start_x < end_x:
            coordinates.append((start_y, start_x+num))
        else:
            coordinates.append((start_y, start_x-num))
    print(coordinates)
    c = 0
    if not coordinates:
        c = 1
        
    for num in range(c, y):
        if start_y < end_y:
            coordinates.append((start_y+num, end_x))
        else:
            coordinates.append((start_y-num, end_x))

    return {
        'cost':cost,
        'coordinates':coordinates
    }
    