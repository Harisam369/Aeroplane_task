def fillA(line_no):
    row = [0,0,0]
    if (1+((line_no*10)) < n+1):
        row[1]=((line_no*10)+1)
    else:
        row[1] = 0
    if row[1]!=0 and (row[1]+4) < n+1:
        row[0]=row[1]+4
    else:
        row[0]=0
    if row[0] !=0 and (row[0]+2) < n+1:
        row[2]=row[0]+2
    else:
        row[2]=0
    return row
def fillC(line_no):
    row = [0,0,0]
    if (4+((line_no*10)) < n+1):
        row[1]=((line_no*10)+4)
    else:
        row[1]=0
    if row[1]!=0 and ((row[1]+6) < n+1):
        row[0]=row[1]+6
    else:
        row[0]=0
    if row[0] !=0 and ((row[1]+2) < n+1):
        row[2]=row[1]+2
    else:
        row[2]=0
    return row
def fillB(line_no):
    row = [0,0,0,0]
    if 2+(line_no*10) < n+1:
        row[1]=2+(line_no*10)
    else:
        row[1]=0
    if row[1]!=0 and (row[1]+1)< n+1:
        row[2]=row[1]+1
    else:
        row[2]=0
    if row[2] !=0 and (row[1]+6)< n+1:
        row[0]=row[1]+6
    else:
        row[0]=0
    if row[0] !=0 and (row[2]+6) < n+1:
        row[3]=row[2]+6
    else:
        row[3]=0
    return row

n=int(input("Enter Number Of Passanger:"))
no_of_row = (n//10) + 1
print(no_of_row)


tableA=[]
tableB=[]
tableC=[]
for i in range(no_of_row):
    tableA.append(fillA(i))
    tableB.append(fillB(i))
    tableC.append(fillC(i))

print("tableA")
print(*tableA,sep="\n")
print("tableB")
print(*tableB,sep="\n")
print("tableC")
print(*tableC,sep="\n")