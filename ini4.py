numbers = open("C:/Users/Dell/Downloads/rosalind_ini4.txt").read().split()
a = int(numbers[0])
b = int(numbers[1])
total = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        total = total + i
print(total)