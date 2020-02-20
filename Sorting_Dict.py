def sort_dict(n):
    print(n)
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i]["name"] > n[j]["name"]:
                n[i],n[j] = n[j],n[i]

    return n


li = [{"name":"Kota","salary":20000},{"name":"Raja","salary":30000},{"name":"Mohan","salary":40000},{"name":"Reddy","salary":50000}]
print(sort_dict(li))