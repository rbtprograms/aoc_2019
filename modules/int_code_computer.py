def int_code_computer(input, noun, verb):
  comp_input = input.copy()
  comp_input[1]=noun
  comp_input[2]=verb
  i = 0
  while True:
    if comp_input[i] == 99:
      break
    if comp_input[i] == 1:
      comp_input[comp_input[i + 3]] = comp_input[comp_input[i + 1]] + comp_input[comp_input[i + 2]]
    if comp_input[i] == 2:
      comp_input[comp_input[i + 3]] = comp_input[comp_input[i + 1]] * comp_input[comp_input[i + 2]]
    i += 4
  yield comp_input