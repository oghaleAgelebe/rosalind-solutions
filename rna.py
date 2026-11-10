s = open("C:/Users/Dell/Downloads/rosalind_rna.txt").read().strip()
rna = s.replace("T", "U")
out = open("C:/Users/Dell/Downloads/answer.txt", "w")
out.write(rna)
out.close()

