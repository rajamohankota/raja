#Factorial of a number
import sys
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

n = int(sys.argv[1])
print("Factorial of {} is {} ".format(n,fact(n)))
