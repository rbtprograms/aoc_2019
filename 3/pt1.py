def get_manhattan_distance(coords):
  return abs(0 - coords[0]) + abs(0 - coords[1])

def get_coords(instructions):
  x, y = 0, 0
  coords = set()

  for instruction in instructions:
    direction = instruction[0]
    movement = instruction[1:]

    for _ in range(0, int(movement)):
      if direction == 'R':
        x += 1
      if direction == 'L':
        x -= 1
      if direction == 'U':
        y += 1
      if direction == 'D':
        y -= 1
      coords.add((x,y))
  return coords

with open('input.txt') as inputfile:
  lines = [get_coords(line.split(',')) for line in inputfile]
  crossings = lines[0]&lines[1]
  result = min([get_manhattan_distance(crossing) for crossing in crossings])
  print("RESULT ", result)