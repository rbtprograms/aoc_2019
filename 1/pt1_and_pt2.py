import math

result = 0
with open('input.txt') as inputfile:
  for line in inputfile:
    amt = int(line)
    amt = (amt//3) - 2
    while amt > 0:
      result += amt
      amt = (amt//3) - 2

print(result)
