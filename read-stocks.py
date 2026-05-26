fhand = open("stocks.txt")
for line in fhand:
    line = line.rstrip()
    words = line.split()
    print(words[0], words[1])