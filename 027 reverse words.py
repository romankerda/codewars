def reverse_words2(text):
    result = ''
    word = ''
    word_is_complete = False
    for i in range (len(text)):
        if text[i] == ' ':
            word_is_complete = True
            if word_is_complete:
                result += word[::-1]
                word = ''
                word_is_complete = False
                result += ' '
        else:
           word += text[i]
           word_is_complete = False
        result += word[::-1]
    return result


def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))
    

print(reverse_words('The quick brown fox jumps over the lazy dog.'))