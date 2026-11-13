data = open("C:/Users/Dell/Downloads/rosalind_gc.txt").read()
records = data.split(">")
best_label = ""
best_gc = 0
for record in records[1:]:
    parts = record.split()
    label = parts[0]
    dna = "".join(parts[1:])
    gc = (dna.count("G") + dna.count("C")) / len(dna) * 100
    if gc > best_gc:
        best_gc = gc
        best_label = label
out = open("C:/Users/Dell/Downloads/answer.txt", "w")
out.write(best_label + "\n" + str(best_gc))
out.close()