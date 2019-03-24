import csv
import re

with open('/home/akash/Documents/CDAP/Cropus/Original CSV Files/Lankadeepa( CSV )/lankadeep17.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    heading = []
    x = 10589
    for row in readCSV:

        f = open(str(x)+".txt", "w+")
        x += 1
        print(x)
        # print(row[0])
        # print(row[0],row[1],row[2],)
        heading.append(row[1])
        content = row[0]

        # remove white spaces
        textsplitSpace = re.sub("\s\s+", " ", content)

        # Remove tab spaces
        f.write(re.sub("\t+", " ", textsplitSpace))
        f.close()

    print(x)

