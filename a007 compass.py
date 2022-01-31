directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

def direction(facing, turn):
    return directions[(directions.index(facing) + turn // 45) % 8]



print(direction('S', 180))
