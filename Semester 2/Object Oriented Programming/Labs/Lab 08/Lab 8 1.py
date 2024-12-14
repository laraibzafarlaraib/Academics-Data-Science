f = open('grades.txt','r')
f1 = open('errors.txt','w')
a = f.readline()
f1.write(a)
a = f.readline()
f1.write(a)
a = f.readlines()
#a = f.readline()
#print(a)
errors = 0

for i in range(len(a)):
    d = 0
    b = a[i]
    l = b[10:41]
    m = b[52:54]
    n = b[42:45]
    
    if len(b) != 58:
        errors += 1
        d = 1
        f1.write(str(i+1)+'\n')
        f1.write(b)
    
    elif ' ' in b[0:10]:
        errors+= 1
        d = 1
        f1.write(str(i+1)+'\n')
        f1.write(b)
    elif d == 0:
        if '  ' in n:
            errors += 1
            d = 1
            f1.write(str(i+1)+'\n')
            f1.write(b)
    if d == 0:
        if not(b[52]>= '0' and b[52]<= '9' and b[53]>= '0' and b[53]<= '9'):
            errors += 1
            f1.write(str(i+1)+'\n')
            f1.write(b)
print(errors)
f.close()
f1.close()

        
    

        

    

    
