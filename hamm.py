lines = open("C:/Users/Dell/Downloads/rosalind_hamm.txt").read().split()
s = lines[0]
t = lines[1]
count = 0
for i in range(len(s)):
    if s[i] != t[i]:
        count = count + 1
out = open("C:/Users/Dell/Downloads/answer.txt", "w")
out.write(str(count))
out.close()