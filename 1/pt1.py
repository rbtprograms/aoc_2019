import math

result = 0
with open('input.txt') as inputfile:
    for line in inputfile:
        result += math.floor(int(line)/3) - 2
print(result)