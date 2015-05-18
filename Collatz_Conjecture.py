# Because Python is interpreted, there is no exe file.
# therefore, you need to have matplotlib installed for this program to work
# numpy (a library necessary for matplotlib) is included in the directory

def collatz(n):
    if (n < 1):
        print "n needs to be a positive integer"
        return
    plotList.append(n)
    if n is 1:
        plt.plot(plotList)
        plt.xlabel('iteration')
        plt.show()
        return
    if n % 2 is 0:
        n = n/2
    else:
        n = n * 3
        n = n + 1
    return collatz(n)

import matplotlib.pyplot as plt
plotList = []
n = input('Enter a value for n: ')
collatz(n)
