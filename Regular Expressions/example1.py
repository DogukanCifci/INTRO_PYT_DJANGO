import re 
fhand = open("/Users/dogukan/Desktop/INTRO_PYT_DJANGO/Regular Expressions/mbox-short.txt", "r")
numlist = list()
for line in fhand :
    line = line.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)          #[0-9.] . konulmasi önemli yoksa 0 verir. en büyük sayi 0 dan kücük oldugu icin

    if len(stuff) != 0 : 
        num = float(stuff[0])
        numlist.append(num)
    else : 
        continue
print("The Summary = ", sum(numlist))
print("Th max number = ", max(numlist))