li = []
l = int(input("enter the range"))
for i in range(l):
    v = input("entr the item")
    li.append(v)
print(li)
n= []
for i in range(len(li)):
    if li[i].isnumeric()== True:
        n.append(li[i])
print(n)


