import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/words.txt')

dict_counts = dict()

for line in fhand :
    words = line.decode().split()
    for word in words :
        dict_counts[word] = dict_counts.get(word, 0) + 1
print(dict_counts)
print()
word_list = list()
for k, v in dict_counts.items() :
    word_list.append((v,k))

print(sorted(word_list))