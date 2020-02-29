import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
def add(a,b):
    print("The sum of",a,"and",b,"is",a+b)
def sub(a,b):
    print("The difference {} and {} is {}".format(a,b,a-b))
def mul(a,b):
    print("The product {} and {} is {}".format(a,b,a*b))
def div(a,b):
    if b==0:
        print("Division by zero not possible")
    else:
        print("The division of {} by {} is {}".format(a,b,a/b))
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
