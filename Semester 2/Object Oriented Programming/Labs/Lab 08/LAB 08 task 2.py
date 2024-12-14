e = open("errors.txt")
g = open("grades.txt", "r+")   # read and also write mode

e.readline()   # read and skip first header line
e.readline()   # read and skip second header line

s = e.readline()
while s != "":
    lineno = int(s)
    s = e.readline()   # read next record line
    g.seek((lineno-1)*59)
    g.writelines(s)
    s = e.readline()
    
g.close()
e.close()

print("Update done")
