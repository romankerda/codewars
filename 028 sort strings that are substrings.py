def in_array(array1, array2):
    result = set()
    for string1 in array1:
        for string2 in array2:
            if string1 in string2:
                result.add(string1)
    return sorted(result) 
            
            
            
            
a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
    