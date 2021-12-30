def to_weird_case(string):
    output = ''
    for w in string.split():
        for i in range(len(w)):
            if i % 2 == 0:
                output += w[i].upper()
            else:
                output += w[i].lower()
        output += ' '
    return output.strip()         
            




print(to_weird_case('This is a test'))