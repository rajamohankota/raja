#Factorial of a number
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

n = int(input("Enter a number to get a factorial: "))
print("Factorial of {} is {} ".format(n,fact(n)))