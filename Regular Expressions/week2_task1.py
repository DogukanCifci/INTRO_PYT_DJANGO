import re 
hand = open("/Users/dogukan/Desktop/INTRO_PYT_DJANGO/Regular Expressions/regex_sum_1462203.txt", "r")
sumlist =list()
for lines in hand :
    lines = lines.rstrip()
    y = re.findall("[0-9]+", lines)
    number = 0
    for i in y : 
        if len(y) != 0 :
            num = float(y[number])
            sumlist.append(num)
            number += 1
print("The sum of the numbers are = ", sum(sumlist))
        