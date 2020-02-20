#Sum of an array elements
def sum_array(n):
    j = 0
    for i in n:
        j = j+i

    return j
l = [1, 2, 3, 4, 5]
print(sum_array(l))