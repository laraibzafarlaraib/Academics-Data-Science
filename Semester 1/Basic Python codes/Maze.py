from random import*
f=[[randint(0,1)for j in range (10)]for i in range (10)]
for i in range(10):
    for j  in range(10):
        print(f[i][j],end=' ')
    print()
i = 0
j = 0
SIZE=8
while True:
    print(f"{i}, {j}", end=' ')
    if i != SIZE - 1 or j != SIZE - 1:
        print("-", end=' ')
    if j + 1 < SIZE and f[i][j + 1] == 1:
        j += 1
    elif i + 1 < SIZE and f[i + 1][j] == 1:
        i += 1
    else:
        break
if i != SIZE - 1 or j != SIZE - 1:
    print("path blocked")
else:
    print()
