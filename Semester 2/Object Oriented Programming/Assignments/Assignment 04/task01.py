g = open("grades.txt")
e = open("errors.txt", "w")

s = g.readline()   # read and skip first header line
e.writelines(s)
s = g.readline()   # read and skip second header line
e.writelines(s)

errs = 0
lineno = 3
s = g.readline()   # read first record line
while s != "":
    rollno = s[0:10]
    name = s[10:41]
    sess = s[52:54]
    if len(s) != 58:
        errs += 1
        e.writelines(str(lineno)+"\n")
        e.writelines(s)   
    elif len(rollno.strip()) != 10:
            errs += 1
            e.writelines(str(lineno)+"\n")
            e.writelines(s)
    elif not (sess[0] >= '0' and sess[0] <= '9' and sess[1] >= '0' and sess[1] <= '9'):
            errs += 1
            e.writelines(str(lineno)+"\n")
            e.writelines(s)
    lineno += 1
    s = g.readline()   # read next record line
    
g.close()
e.close()

if errs == 0:
    print("grades file is error FREE")
else:
    print(errs, "errors are present in grades file")
