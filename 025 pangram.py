import string

def is_pangram(s):
    for i in range(ord('a'), ord('z')+1):
        if chr(i) not in s.lower():
            return False
    return True
    
pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))


