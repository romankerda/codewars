def fly_by(lamps, drone):
    print(len(lamps))
    print(len(drone))
    output = ''
    for i in range(0, len(drone)):
        output += 'o'
    print(len(output))
    return output + lamps[len(drone):]



print(fly_by('xxxxxxxxxxxxxxxxxxxxxxxxx', '========----------======T'))
        