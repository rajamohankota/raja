a = [ ]
s = "raja"
print(type(a))
for i in range(1,10):
    a.append(i)
print(a)
l = len(a)
print(l)
print(a[3:5])
print(len(a))

for j in range(9):
    a.remove(j)

    print(a)