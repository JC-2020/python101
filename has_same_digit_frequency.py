# frequency counter method
def has_same_digit_frequency(a, b):
    if len(a) != len(b):
      return False
    result = {}
    for number in a:
      if number in result.keys():
        result[number] += 1
      else:
        result[number] = 1
    for number in b:
      try:
        if result[number] == 0:
          return False
        else: 
          result[number] -= 1
      except KeyError:
        return False
    return True
# sort method
def has_same_digit_frequency(a, b):
  if len(a) != len(b):
    return False
  a.sort(), b.sort()
  if a != b:
    return False
  else:
    return True
print(has_same_digit_frequency([1,2,3,4], [4,3,2,1]))
print(has_same_digit_frequency([1,3,4], [3,2,1]))