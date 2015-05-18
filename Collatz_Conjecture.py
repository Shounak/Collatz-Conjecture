def collatz(n):
    if (n < 1):
        print "n needs to be a positive integer"
        return
    print( str(n) + "  "),
    if n is 1:
        return
    if n % 2 is 0:
        n = n/2
    else:
        n = n * 3
        n = n + 1
    return collatz(n)

import sys
print (sys.version)
import numpy
#print numpy.__version__

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
#collatz(3)
