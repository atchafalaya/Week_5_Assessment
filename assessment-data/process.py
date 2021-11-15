log_file = open("um-server-01.txt") #opening the database

def sales_reports(log_file): #define the function 'sales_reports' and pass in object log_file from um-server-01.txt
    for line in log_file: #for each line in log_file
        line = line.rstrip() #remove trailing characters
        day = line[0:3] #set value day to the three characters following index 0 on line
        if day == "Mon": #if that value is Monday
            print(line) #print that line

#sales_reports(log_file) #call the function sales_reports with object log_file

log_file.close() #close database
log_file = open("um-server-01.txt") #open database again

def melon_sales(log_file): #define function 'melon_sales' and pass in log_file
    for line in log_file: #for each line in log_file
        melonSplit = line.split(" ") #split line at space
        melons = int(melonSplit[2]) #turn the string value of index 2 into an integer and assign it to 'melons'
        if melons > 10: #if that integer is more than 10
            print(line) #print that line

melon_sales(log_file) #call the melon function

log_file.close() #close the database again
