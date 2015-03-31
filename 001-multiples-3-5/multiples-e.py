# Function SumDivisibleBy(n)
#   SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15)
# EndFunction

target = 999

def SumDivisibleBy(n):
  p = target // n
  print p
  return n*(p*(p+1)) // 2

def sum():
  return SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15)

print sum() #233168

#print 3 * 333 * 334 * .5
#print 5 * 199 * 200 * .5