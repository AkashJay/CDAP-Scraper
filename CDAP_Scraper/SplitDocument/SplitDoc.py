import csv

with open('/home/akash/Documents/CDAP/Scraper/CDAP_Scraper/Lankadeepa/lankadeep14.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    heading = []
    x = 1
    for row in readCSV:

        f = open(str(x)+".txt", "w+")
        x += 1
        print(x)
        # print(row[0])
        # print(row[0],row[1],row[2],)
        heading.append(row[1])
        content = row[0].replace("\n", "")

        f.write(content)
        f.close()

    print(heading)

