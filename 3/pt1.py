def get_manhattan_distance(coords):
  if coords == 0:
    coords = [0,0]
  return abs(0 - coords[0]) + abs(0 - coords[1])

def get_coords(instructions):
  coord = (0, 0)
  coords = set(coord)

  for instruction in instructions:
    direction = instruction[0]
    movement = instruction[1:]

    for x in range(0, int(movement)):
      if direction == 'R':
        coord = (coord[0] + 1, coord[1])
      if direction == 'L':
        coord = (coord[0] - 1, coord[1])
      if direction == 'U':
        coord = (coord[0], coord[1] + 1)
      if direction == 'D':
        coord = (coord[0], coord[1] - 1)
      coords.add(coord)
  return coords

# get_coords('1,2')

with open('input.txt') as inputfile:
  lines = [get_coords(line.split(',')) for line in inputfile]
  crossings = lines[0].intersection(lines[1])
  result = [get_manhattan_distance(crossing) for crossing in crossings]
  result.sort()
  print("RESULT ", result)