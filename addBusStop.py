import csv
csv.register_dialect('myDialect',delimiter=',')  
fin = open("data/busStops.csv","r")

addBusStop_list = []
reader = csv.reader(fin,dialect='myDialect')
for row in reader:
    addBusStop_list.append(row[0])
#addBusStop_list.sort()
#print(addBusStop_list)
try:
    for i in range(0,len(addBusStop_list)):
        for j in range(i+1,len(addBusStop_list)):
            if addBusStop_list[i] == addBusStop_list[j]:
                print("!!! Bus Stops with same name --> ",addBusStop_list[i])
except:
    pass
