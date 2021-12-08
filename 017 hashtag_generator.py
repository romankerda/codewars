def generate_hashtag(s):
    output = '#'
    big = True
    if len(s)==0:
        return False
    else:
        for i in range(0, len(s)):
            if s[i].isalpha() and big:
                output += s[i].upper()
                big = False
            elif s[i].isalpha():
                output += s[i].lower()
            else:
                bit = True
        if len(output) > 140:
            return False
        return str(output)
                
def generate_hashtag2(s):
    output = '#'
    for word in s.split():
        output += word.capitalize()
    if len(output) > 140 or len(s) == 0:
        return False
    return str(output)
                
                
print(generate_hashtag2('Do      We have A Hashtag'))