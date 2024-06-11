import urllib
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand :
    word = line.decode().split()
    for words in word:
        counts[words] = counts.get(words,0)+1
print(counts)
