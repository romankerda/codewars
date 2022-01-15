# def travel_chessboard(s):
#     rows, cols= int(s[8]) -int(s[3]), int(s[6]) - int(s[1])
#     sq = min(rows, cols)
def rec(sq):
    for i in range(sq):
        return 2 if sq == 1 else 4 + rec(sq-1)
    
    



# print(travel_chessboard("(1 1)(3 3)"))
print(rec(4))