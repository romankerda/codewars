def odd_row(n):
    def nums_used(n):
        a, b = 1, 2
        for num in range(1, n):
            a, b = b, a + b
        return b
    