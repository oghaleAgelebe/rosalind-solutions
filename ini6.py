s = open("C:/Users/Dell/Downloads/rosalind_ini6.txt").read()
words = s.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
out = open("C:/Users/Dell/Downloads/answer.txt", "w")
for word in counts:
    out.write(word + " " + str(counts[word]) + "\n")
out.close()