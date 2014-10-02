def fibonacci(x):
 a = 0   #first number
 b = 1   #second number
 for x in range(x - 1):
  a, b = b, a + b        #a becomes b and b becomes a and b added together
 return a                #returns the next number in the sequence

print "Fibonacci Answer"
for x in range(1, 35):       #number of times I need the sequence to run to reach 4million
    print fibonacci(x)
