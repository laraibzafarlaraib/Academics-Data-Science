from random import*
length=randint(5,9)
d=[[randint(1,9)for i in range(length)]for j in range (length)]
for i in range (length):
    d[i][i]=0
for i in range(length):
    for j in range(length):
        y=randint(0,1)
        if y==0:
            d[i][j]=-1
for i in range(length):
    for j in range(length):
        print(d[i][j],end=' ')
    print()
for i in range(length):
    print(f'city{i} has direct link with: ',end=' ')
    for j in range (length):
        if d[i][j]!=-1:
            a=d[i][j]
            print(j,end=' ')
    print()
