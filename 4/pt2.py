
# def count_digits(number):
#   digits_dict = {}
#   for digit in number:
#     if digit in digits_dict:
#       digits_dict[digit] += 1
#     else:
#       digits_dict[digit] = 1
#   if 2 in digits_dict.values():
#     return True
#   return False

# for x in range(273025,767253):
#   digits = str(x)
#   pairs = any([count_digits(digits) for i in range(len(digits)-1)])
#   next_is_smaller = any([digits[i] > digits[i+1] for i in range(len(digits)-1)])
#   if pairs and not next_is_smaller:
#     count += 1

# print(count)

# this literally felt so simple that I implemented something similar above because it felt too easy
count = 0

for x in range(273025,767253):
  digits = str(x)
  pairs = any([digits.count(digits[i]) == 2 for i in range(len(digits)-1)])
  next_is_smaller = any([digits[i] > digits[i+1] for i in range(len(digits)-1)])
  if pairs and not next_is_smaller:
    count += 1

print(count)
