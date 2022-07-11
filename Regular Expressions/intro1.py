fhand = open("/Users/dogukan/Desktop/Regular Expressions/mbox-short.txt", "r")

for lines in fhand :
    lines =lines.rstrip()
    if lines.startswith('From: ') :
        print(lines)