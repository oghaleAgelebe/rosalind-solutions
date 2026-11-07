items = open("C:/Users/Dell/Downloads/rosalind_ini3.txt").read().split()
s = items[0]
a = int(items[1])
b = int(items[2])
c = int(items[3])
d = int(items[4])
print(s[a:b+1] + " " + s[c:d+1])