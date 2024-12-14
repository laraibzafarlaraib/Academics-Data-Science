from random import*
i=1
while i<=10:
    x=randint(1,10)
    y=randint(1,10)
    if x>y:
        print('First random number', x, 'is larger than Second.', y)
    elif y>x:
        print('Second number',y, 'is larger than First', x)
    i=i+1
    
