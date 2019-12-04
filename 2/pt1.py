result = []
with open('input.txt') as inputfile:
  for line in inputfile:
    result = [int(x) for x in line.split(',')]
i = 0
while i < len(result):
  if result[i] == 99:
    break
  if result[i] == 1:
    result[result[i + 3]] = result[result[i + 1]] + result[result[i + 2]]
  if result[i] == 2:
    result[result[i + 3]] = result[result[i + 1]] * result[result[i + 2]]
  i += 4

print(result)