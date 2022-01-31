import a005_single_digit as a

def test_single_digit():
    assert a.single_digit(15) == 4, "Should be 4"
    assert a.single_digit(157) == 5, "Should be 5"

# if __name__ == '__main__':
#     test_single_digit()