count = 0

for x in range(273025,767253):
  digits = str(x)
  pairs = any([digits.count(digits[i]) == 2 for i in range(len(digits)-1)])
  next_is_smaller = any([digits[i] > digits[i+1] for i in range(len(digits)-1)])
  if pairs and not next_is_smaller:
    count += 1

print(count)
