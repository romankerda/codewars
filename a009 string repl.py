def alphabet_position(text):
    output = ''
    for ch in text.lower():
        if ch.isalpha():
            output += str(ord(ch.lower())-96) + ' '
    return output[:len(output)-1]

def alphabet_position2(text):
    return ' '.join(str(ord(ch) - 96) for ch in text.lower() if ch.isalpha())

            



print (alphabet_position2('Tab=cde'))