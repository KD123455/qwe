s1=[1,2,3,4,5,6,8,9]
s2=[4,5,6,7]
s3=[]
a=len(s1)
b=len(s2)
for x in s1:
    s3.append(x)
for x in s2:
    s3.append(x)
print(s3)
  
for i in range(a+b-1):
    for j in range(a+b-1-i):
        if s3[j]>s3[j+1]:
            s3[j], s3[j+1] = s3[j+1], s3[j]
print(s3)
