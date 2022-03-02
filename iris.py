import csv
with open('D:\akash.python\iris.data','rb') as csvfile:
    lines=csv.reader(csvfile)
    for row in lines:
        print ','.join(row)