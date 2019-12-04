# address 1 - noun
# address 2 - verb
# each will be between 0 and 99 inclusive
#output available at address 0

result = []
for noun in range(0, 100):
  for verb in range(0, 100):
    with open('input.txt') as inputfile:
      for line in inputfile:
        result = [int(x) for x in line.split(',')]
        result[1]=noun
        result[2]=verb
    i = 0
    while True:
      if result[i] == 99:
        break
      if result[i] == 1:
        result[result[i + 3]] = result[result[i + 1]] + result[result[i + 2]]
      if result[i] == 2:
        result[result[i + 3]] = result[result[i + 1]] * result[result[i + 2]]
      i += 4
    if result[0] == 19690720:
      print(result[0], result[1], result[2])