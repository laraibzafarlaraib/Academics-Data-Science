r=int(input('Rows='))
i=1
while i<=r:
    j=1
    while j<=i:
        print('+',end='')
        j+=1
        k=r
    while k>=i:
        print('+',end='')
        k-=1
    i+=1
    print()
