def is_multiple_of_3_or_5(x):
  if (  x%3 == 0 ) or ( x%5 == 0 ) :
    return True
  else:
    return False

def sum(top):
  total = 0
  for i in range(3,top):
    if is_multiple_of_3_or_5(i):
      total += i
  return total

print sum(10)
print sum(1000) #233168