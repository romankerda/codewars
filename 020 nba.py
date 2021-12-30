import re

def nba_cup(result_sheet, to_find):
    w,d,l,sc,con,pts = 0
    list_matches = result_sheet.split(',')
    for match in list_matches:
        s1 = re.search(r' \d+ ', match)
        s2 = re.search(r'\d+$', match)
        home = {'team': match[:s1.start()].strip(), 'pts': match[s1.start():s1.end()].strip()}
        vis = {'team': match[s1.end():s2.start()].strip(), 'pts': match[s2.start():].strip()}
        if to_find == home['team'] and home[]
        pass
    
    
    

home1 = {'team': 'ahoj', 'pts': 20} 
print(home1['team'])
    
txt = "tym jedna 78th 320 tym dva 88"
res1 = re.search(r' \d+ ', txt)
print(txt[:res1.start()])
print(txt[res1.start():res1.end()].strip())
res2 = re.search(r' \d+$', txt)
print(txt[res1.end():res2.start()].strip()) 
print(txt[res2.start():].strip())
        

    

# target_string = "Abraham Lincoln was born on February 12, 1809,"
# # \d to match digits
# res = re.search(r'\{4}', target_string)
# # match value
# print(res.group()) 
# # Output 1809

# # start and end position
# print(res.span())
# # Output (41, 45)

# # start position
# print(res.start())
# # Output 41

# # end position
# print(res.end())
# # Output 45








