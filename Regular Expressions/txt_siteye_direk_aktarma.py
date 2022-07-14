import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand :
    words = line.decode().split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

count_sirali = sorted(counts)
print(count_sirali)
print()


listem = list()
for k, v in counts.items() :
    listem.append((v,k))

word_list = sorted(listem)
print(word_list)
