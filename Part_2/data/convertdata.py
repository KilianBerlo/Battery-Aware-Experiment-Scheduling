import csv, sys, datetime, os, math

path = "./"
dirs = os.listdir(path)
result = open("data.txt", "w")
stringlist  = []
elementlist = []
for file in dirs:
    starttime = datetime.datetime(2016, 3, 20, 5, 0, 0, 0)
    endtime = datetime.datetime(2016, 3, 22, 22, 0, 0, 0)

    string = ""
    elementstring = ""
    elementcount = 0

    if file == "Sun.csv":
        f=open(file, 'r')
        string += "transient int(0 .. 4320)[] Sun_data = ["
        elementstring += "const int Sun_data_size = "
        csvfile = csv.reader(f, delimiter=',')
        next(csvfile)
        for row in csvfile:   
            d0 = str(row[0])
            d1 = str(row[1])
            startjob = datetime.datetime.strptime(d0, "%d %b %Y %H:%M:%S.%f")
            endjob = datetime.datetime.strptime(d1, "%d %b %Y %H:%M:%S.%f")
            starttostart = str(int(round((startjob - starttime).total_seconds()/60)))
            starttoend = str(int(round((endjob - starttime).total_seconds()/60)))
            if starttime < startjob < endtime or starttime < endjob < endtime:
                #print("Start: ", starttostart, "\tEnd: ", starttoend)
                string += starttostart + ", " + starttoend + ", "
                elementcount += 2
        string = string[:-2]
        string += ", 0];\n"

        stringlist.append(string)        
        elementlist.append(elementstring + str(elementcount-1) + ";\n")

        f.close()

    elif file.endswith(".csv"):
        f=open(file, 'r')
        filename = file[:-4]
        string += "transient int(0 .. 4320)[] " + filename.replace("-", "_") + "_data = ["
        elementstring += "const int " + filename.replace("-", "_") + "_data_size = "
        csvfile = csv.reader(f, delimiter=',')
        next(csvfile)
        for row in csvfile: 
            d0 = str(row[1])
            d1 = str(row[2])
            if file.endswith("Toulouse.csv") or file.endswith("3F3.csv") or file.endswith("3F2.csv"):
                startjob = datetime.datetime.strptime(d0, "%Y/%m/%d %H:%M:%S.%f")
                endjob = datetime.datetime.strptime(d1, "%Y/%m/%d %H:%M:%S.%f")
            else:
                startjob = datetime.datetime.strptime(d0, "%d %b %Y %H:%M:%S.%f")
                endjob = datetime.datetime.strptime(d1, "%d %b %Y %H:%M:%S.%f")
            starttostart = str(int(round((startjob - starttime).total_seconds()/60)))
            starttoend = str(int(round((endjob - starttime).total_seconds()/60)))
            if starttime < startjob < endtime or starttime < endjob < endtime:
                #print("Start: ", starttostart, "\tEnd: ", starttoend)
                string += starttostart + ", " + starttoend + ", "
                elementcount += 2
        string = string[:-2]
        string += ", 0];\n"

        stringlist.append(string)        
        elementlist.append(elementstring + str(elementcount-1) + ";\n")

        f.close()
    
    

stringlist.sort()
for datastring in stringlist:
    result.write(datastring)  
result.write("\n//The following sizes are the maximum array index sizes plus the '0' to prevent array out of bounds in modest so (0 .. *_data_size)\n")
elementlist.sort()
for elementstr in elementlist:
    result.write(elementstr)
result.close()