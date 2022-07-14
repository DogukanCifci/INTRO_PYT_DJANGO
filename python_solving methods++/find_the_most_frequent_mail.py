fhand = open("/Users/dogukan/Desktop/INTRO_PYT_DJANGO/python_solving methods++/mbox-short1.txt", "r")
my_dict = dict()
for line in fhand :
    if not line.startswith('From ') :
        continue
    line = line.split()
    words = line[1]
    my_dict[words] = my_dict.get(words, 0) + 1
print(my_dict)
    
largest = -1            #Bu metod cok faydali UNUTMAAAAA!!!!!!
the_word = None
for k, v in my_dict.items() :
    if  v > largest :
        largest = v
        the_word = k

print(the_word, largest)