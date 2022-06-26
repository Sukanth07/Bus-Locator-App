import csv
csv.register_dialect('myDialect',delimiter=',')  
fin = open("data/busStops.csv","r")
fin_data = open("data/data.csv","r")

mainList = []
secondList = []
data = csv.reader(fin_data,dialect='myDialect')
for row in data:
    #print(row)
    for i in range(3,len(row),2):
        if row[i] not in secondList:
            inner = []
            inner.append(row[i])
            mainList.append(inner)
            secondList.append(row[i])
mainList.sort()
secondList.sort()
print(mainList)

fout = open("data/busStops.csv","w",newline="")
fout_writer = csv.writer(fout)
fout_writer.writerows(mainList)

fin_data.close()
fin.close()
fout.close()