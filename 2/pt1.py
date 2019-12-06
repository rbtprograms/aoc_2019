import sys
sys.path.insert(0, '../modules')
from int_code_computer import int_code_computer 

data = []
with open('input.txt') as inputfile:
  for line in inputfile:
    data = [int(x) for x in line.split(',')]

result = int_code_computer(data, noun=12, verb=2)

for item in result:
  print(item[0])