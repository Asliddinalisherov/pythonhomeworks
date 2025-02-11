import math
num = int(input())
factors = []
ran = round(num ** (1/2))
for i in range(1, ran+2, 1):
    if num % i == 0:
        factors.append(i)
        factors.append(round(num/i))

factors = sorted(list(set(factors)))

for i in range(len(factors)):
    print(f"{factors[i]} is a factor of {num}")