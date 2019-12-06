import sys
sys.path.insert(0, '../modules')
from int_code_computer import int_code_computer 

data = []
for noun in range(0, 100):
  for verb in range(0, 100):
    with open('input.txt') as inputfile:
      for line in inputfile:
        data = [int(x) for x in line.split(',')]
    
    result = int_code_computer(data, noun=noun, verb=verb)
    for item in result:
      if item[0] == 19690720:
        print(item[0], item[1], item[2])
      
