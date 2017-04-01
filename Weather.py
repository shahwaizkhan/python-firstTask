
"""
The Purpose of this project is basically to generate report on the weather data of Lahore from 1996 to 2011.
The data is present in bunch of text files.
it will read those text files and perform operations
After performing operations (Finding min,max temperatures) it will print report

"""


import csv     #CSV(comma seperated values) used to read data from txt files.
import glob    # Finds all the pathnames matching a specified pattern


max_humidity_dict = {} # Year is key and Minimum Humidity is value e.g 1998 : 20
min_humidity_dict = {} # Year is key and Maximm Humidity is value e.g 1998 : 50
max_temp_dict = {} # Year is key and Maximum Temp is value e.g 1998 : 47
min_temp_dict = {} # Year is key and Minimum Temp is value e.g 1998 : 2
full_date_dict = {} # Year is key and Full Date is value e.g 1998 : 1998-12-10







def main():

    """
    Entry point of the program (Main Function) which will call other functions
    we will pass path of directory where all weather files are located.
    """

    read_contents_of_file = []            #List to store data of txt file
    List = []                            #List to store each row
    dir_path = "E:\Shahwaiz Data\Semester 6\Python\Task-1\weatherdata.txt"
    files = glob.glob(dir_path)
    for afile in files:
        with open(afile) as File:
            File.__next__()
            File.__next__()
            Read_contents_of_File = csv.reader(File)
            for row in read_contents_of_file:
                if row != 0:
                    List.append(row)
            List = List[:-1]



    maximum_temperature = max_temp_calculation(List)
    minimum_temperature = min_temp_calculation(List)
    maximum_humidity = max_humidity_calculation(List)
    minimum_humidity = min_humidity_calculation(List)

    date_of_max_temperature = get_date_of_maxTemp(maximum_temperature)
    date_of_min_temperature = get_date_of_minTemp(minimum_temperature)
    date_of_max_humidity = get_date_of_maxHumidity(maximum_humidity)
    date_of_min_humidity = get_date_of_minHumidity(minimum_humidity)




#Functions which will be called form Main Function


def get_date_of_maxTemp(max_temp):
    if max_temp != 0:
        date = max_temp[0]
        year = str(date)[:4]
        max_temp_of_month = max_temp[1]
        if year in max_temp_dict.keys():
            temp = int(max_temp_of_month)
            temp_in_dic = int(max_temp_dict[year])
            if temp > temp_in_dic:
                max_temp_dict[year] = max_temp_of_month
                full_fate_dict[year] = date
            else:
                pass
        else:
            max_temp_dict[year] = max_temp_of_month
            full_date_dict[year] = date
    else:
        pass





def get_date_of_minTemp(min_temp):
    if min_temp != 0:
        date = min_temp[0]
        year = str(date)[:4]
        min_temp_of_month = min_temp[1]
        if year in min_temp_dict.keys():
            temp = int(min_temp_of_month)
            temp_in_dic = int(min_temp_dict[year])
            if temp < temp_in_dic:
                min_temp_dict[year] = min_temp_of_month
            else:
                pass
        else:
            min_temp_dict[year] = min_temp_of_month

    else:
        pass


def get_date_of_maxHumidity(max_humidity):
    if max_humidity != 0:
        date = max_humidity[0]
        year = str(date)[:4]
        maximum_humidity_of_month = max_humidity[1]
        if year in max_humidity_dict.keys():
            humidity = int(maximum_humidity_of_month)
            existing_humidity = int(max_humidity_dict[year])
            if humidity > existing_humidity:
                max_humidity_dict[year] =  maximum_humidity_of_month
            else:
                pass
        else:
            max_humidity_dict[year] = maximum_humidity_of_month
    else:
        pass


def get_date_of_minHumidity(min_humidity):
    if min_humidity != 0:
        date = min_humidity[0]
        year = str(date)[:4]
        minimum_humidity_of_month = min_humidity[1]
        if year in min_humidity_dict.keys():
            humidity = int(minimum_humidity_of_month)
            existing_humidity = int(min_humidity_dict[year])
            if humidity < existing_humidity:
                min_humidity_dict[year] =  minimum_humidity_of_month
            else:
                pass
        else:
            min_humidity_dict[year] = minimum_humidity_of_month
    else:
        pass






def max_temp_calculation(list_of_temp):
    max_temperatures_list = []
    i = list_of_temp[1]
    for i in range(len(list_of_temp)):
        max_temperatures_list = max_temperatures_list.append(list_of_temp[i])
        i = i+23
    if not max_temperatures_list:
        return 0
    else:
        max_temp = max(max_temperatures_list)
        max_temp_string = str(max_temp)
    for item in range(len(list_of_temp)):
        if list_of_temp[item][1] == max_temp_string:
            max_temperatures_list.append(list_of_temp[item][0])
            max_temperatures_list.append(max_temp_string)
            break


    return max_temperatures_list



def mix_temp_calculation(list_of_temp):
    min_temperatures_list = []
    i = list_of_temp[3]
    for i in range(len(list_of_temp)):
        min_temperatures_list = min_temperatures_list.append(list_of_temp[i])
        i = i+23
    if not min_temperatures_list:
        return 0
    else:
        min_temp = min(min_temperatures_list)
        min_temp_string = str(min_temp)
    for item in range(len(list_of_temp)):
        if list_of_temp[item][3] == min_temp_string:
            min_temperatures_list.append(list_of_temp[item][0])
            min_temperatures_list.append(min_temp_string)
            break


    return min_temperatures_list


def max_humidity_calculation(list_of_humidity):
    i = 7
    month_max_humidity = []
    max_list_of_humidity = []
    for i in range(len(list_of_humidity)):
        max_list_of_humidity.append(list_of_humidity[i][7])
        i = i+23
    if not max_list_of_humidity:
        return 0

    else:
        maximum_humidity = max(list_of_humidity)
        max_humidity_string = str(maximum_humidity)
        for item in range(len(list_of_humidity)):
            if list_of_humidity[item][7] == max_humidity_string:
                month_max_humidity.append(list_of_humidity[item][0])
                month_max_humidity.append(max_humidity_string)
                break
        return month_max_humidity


def min_humidity_calculation(list_of_humidity):
    i = 9
    month_min_humidity = []
    min_list_of_humidity = []
    for i in range(len(list_of_humidity)):
        min_list_of_humidity.append(list_of_humidity[i][9])
        i = i+23
    if not min_list_of_humidity:
        return 0

    else:
        minimum_humidity = min(list_of_humidity)
        min_humidity_string = str(minimum_humidity)
        for item in range(len(list_of_humidity)):
            if list_of_humidity[item][9] == min_humidity_string:
                month_min_humidity.append(list_of_humidity[item][0])
                month_min_humidity.append(min_humidity_string)
                break
        return month_min_humidity



def year_hottest_days(): 
     """ 
     it will show the the Hottest days with year and complete date 
 
    """ 
    print(str("Year").rjust(4), 
           str("Date").rjust(10), 
           str("Temp").rjust(11), 
           "[Report#2][Hottest Days Report]".rjust(8) 
           ) 
     # iterate over dictionary key @Year e.g 1996 and display it's value.Uses same key for two dictionaries 
     # e.g 1996:1996-12-1 and 1996:49 
    for i in full_date_dict.keys(): 
         print(str(i).rjust(4), 
               str(full_date_dict[i]).rjust(12), 
               str(max_temp_dict[i]).rjust(8) 
              ) 


def annual_report(): 
    """ 
    It will show the annual report to the user   
    """ 
    print(str("Year").rjust(7), 
          str("MAXTemp").rjust(7), 
          str("MINTemp").rjust(7), 
          str("MAXHumidity").rjust(7), 
          str("MINHumidity").rjust(7), 
          "[Report#1][Annual Report]".rjust(8) 
          ) 
     
     # iterate over dictionary key @Year e.g 1996 and display it's value.Uses same key for all dictionaries 
    for i in full_date_dict.keys(): 
        print(str(i).rjust(6), 
              str(max_temp_dict[i]).rjust(6), 
              str(min_temp_dict[i]).rjust(6), 
              str(max_humidity_dict[i]).rjust(8), 
              str(min_humidity_dict[i]).rjust(9) 
               ) 



userChoice = str(input("1. For Annual Report\n"
                       "2. For Hottest Day\n"
                       "Please Enter Your Choice: "))

if int(userChoice) == 1:
    main()
    annual_report()

elif int(userChoice) == 2:
    main()
    year_hottest_days()

else:
    print("weatherman[report# ][data_dir]")

