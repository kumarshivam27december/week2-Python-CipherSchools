a=[]
for i in range(5):
    a.append(i)
print(a)


print([ i for i in range(5)])



b=[]
for m in range(5):
    b.append(m**2)
    
print(b)

k=list(map(lambda n:n**3, range(5)))
print(k)





h=[]
for d in range(5):
    temp=[]
    for j in range(5):
        temp.append(j)
    h.append(temp)
    
print(h)



s=5
print([[max(i+1,j+1,s-i,s-j) for i in range(s)]])
# print(w)


o={
    2:4,
    3:9,
    4:16,
}

print(o)

print({ i: i**2 for i in range(5)})


g=(i for i in range(5))
print(type(g))

it=iter(a)
print(next(it))