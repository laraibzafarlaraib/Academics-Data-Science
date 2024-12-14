from random import*
x=[1]*10
for i in range(len(x)):
    x[i]=randint(10,99)
    y=[x[i]for i in range (len(x))]
    print(x[i],end=' ')
print()
for i in range (10):
    for j in range(10-i-1):
       if y[j]>y[j+1]:
            y[j],y[j+1]=y[j+1],y[j]
    for k in range(10):
         s=y[k]
         print(s,end=' ')
    print()
for i in range(len(x)):
    for j in range (10):
        if x[i]==y[j]:
            print(f'{x[i]} is at position {j}')
