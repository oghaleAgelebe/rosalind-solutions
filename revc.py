comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
s = open("C:/Users/Dell/Downloads/rosalind_revc.txt").read().strip()
r = s[::-1]
result = ""
for letter in r:
    result = result + comp[letter]
out = open("C:/Users/Dell/Downloads/answer.txt", "w")
out.write(result)
out.close()