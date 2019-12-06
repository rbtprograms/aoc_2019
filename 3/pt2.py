def get_coords_length(instructions):
  x, y, length = 0, 0, 0
  coords = {}

  for instruction in instructions:
    direction = instruction[0]
    movement = instruction[1:]

    for _ in range(0, int(movement)):
      length += 1
      if direction == 'R':
        x += 1
      if direction == 'L':
        x -= 1
      if direction == 'U':
        y += 1
      if direction == 'D':
        y -= 1
      coords[(x, y)] = length
  return coords

with open('input.txt') as inputfile:
  [first, second] = [get_coords_length(line.split(',')) for line in inputfile]
  combined = set(first.keys()) & set(second.keys())
  result = min([first[coord]+second[coord] for coord in combined])
  print(result)