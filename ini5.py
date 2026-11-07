n = 0
out = open("C:/users/Dell/Downloads/answers.txt", "w")
for line in open("c:/Users/Dell/Downloads/rosalind_ini5.txt"):
    n = n + 1
    if n % 2 == 0:
        out.write(line)
out.close()

