"""Program to create a list of tuples from
   given list having a number and its cube"""
def cube_num(n):
    list = []
    for i in n:
        t = (i,i*i*i)
        list.append(t)

    return list
n = [1,2,3]
print(cube_num(n))
