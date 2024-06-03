s1=[1,2,3,4,5,6,8,9]
s2=[4,5,6,7]
res=[]
a=len(s1)
b=len(s2)
for x in s1:
    res.append(x)
for x in s2:
    res.append(x)
print('начальные списки')
print(s1)
print(s2)  
for i in range(a+b-1):
    for j in range(a+b-1-i):
        if res[j]>res[j+1]:
            res[j], res[j+1] = res[j+1], res[j]
print(res)
