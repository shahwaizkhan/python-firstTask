
"""
The Purpose of this project is basically to generate report on the weather data of Lahore from 1996 to 2011.
The data is present in bunch of text files.
it will read those text files and perform operations.
After performing operations (Finding min,max temperatures) it will print report

"""


import csv     # CSV(comma seperated values) used to read data from txt files.
import glob    # Finds all the pathnames matching a specified pattern


Max_Humidity_dict = {} # Year is key and Minimum Humidity is value e.g 1998 : 20
Min_Humidity_dict = {} # Year is key and Maximm Humidity is value e.g 1998 : 50
Max_Temp_dict = {} # Year is key and Maximum Temp is value e.g 1998 : 47
Min_Temp_dict = {} # Year is key and Minimum Temp is value e.g 1998 : 2
Full_Date_dict = {} # Year is key and Full Date is value e.g 1998 : 1998-12-10







def Main():

    """
    Entry point of the program (Main Function) which will call other functions
    we will pass path of directory where all weather files are located.
    """

    Read_contents_of_File = []            #List to store data of txt file
    List = []                            #List to store each row
    dir_path = "E:\Shahwaiz Data\Semester 6\Python\Task-1\weatherdata.txt"
    files = glob.glob(dir_path)
    for afile in files:
        with open(afile) as File:
            File.__next__()
            File.__next__()
            Read_contents_of_File = csv.reader(File)
            for row in Read_contents_of_File:
                if row != 0:
                    List.append(row)
            List = List[:-1]



    Maximum_Temperature = Max_Temp_Calculation(List)
    Minimum_Temperature = Min_Temp_Calculation(List)
    Maximum_Humidity = Max_Humidity_Calculation(List)
    Minimum_Humidity = Min_Humidity_Calculation(List)

    Date_of_Max_Temperature = getDateMaxTemp(Maximum_Temperature)
    Date_of_Min_Temperature = getDateMinTemp(Minimum_Temperature)
    Date_of_Max_Humidity = getDateMaxHumidity(Maximum_Humidity)
    Date_of_Min_Humidity = getDateMinHumidity(Minimum_Humidity)




#Functions which will be called form Main Function


def getDateMaxTemp(Max_Temp):
    if Max_Temp != 0:
        Date = Max_Temp[0]
        Year = str(Date)[:4]
        Max_Temp_of_Month = Max_Temp[1]
        if Year in Max_Temp_dict.keys():
            temp = int(Max_Temp_of_Month)
            Temp_in_Dic = int(Max_Temp_dict[Year])
            if temp > Temp_in_Dic:
                Max_Temp_dict[Year] = Max_Temp_of_Month
                Full_Date_dict[Year] = Date
            else:
                pass
        else:
            Max_Temp_dict[Year] = Max_Temp_of_Month
            Full_Date_dict[Year] = Date
    else:
        pass





def getDateMinTemp(Min_Temp):
    if Min_Temp != 0:
        Date = Min_Temp[0]
        Year = str(Date)[:4]
        Min_Temp_of_Month = Min_Temp[1]
        if Year in Min_Temp_dict.keys():
            temp = int(Min_Temp_of_Month)
            Temp_in_Dic = int(Min_Temp_dict[Year])
            if temp < Temp_in_Dic:
                Min_Temp_dict[Year] = Min_Temp_of_Month
            else:
                pass
        else:
            Min_Temp_dict[Year] = Min_Temp_of_Month

    else:
        pass


def getDateMaxHumidity(Max_humi):
    if Max_humi != 0:
        Date = Max_humi[0]
        Year = str(Date)[:4]
        Maximum_Humidity_of_Month = Max_humi[1]
        if Year in Max_Humidity_dict.keys():
            humidity = int(Maximum_Humidity_of_Month)
            existing_humidity = int(Max_Humidity_dict[Year])
            if humidity > existing_humidity:
                Max_Humidity_dict[Year] =  Maximum_Humidity_of_Month
            else:
                pass
        else:
            Max_Humidity_dict[Year] = Maximum_Humidity_of_Month
    else:
        pass


def getDateMinHumidity(Min_humi):
    if Min_humi != 0:
        Date = Min_humi[0]
        Year = str(Date)[:4]
        Minimum_Humidity_of_Month = Min_humi[1]
        if Year in Min_Humidity_dict.keys():
            humidity = int(Minimum_Humidity_of_Month)
            existing_humidity = int(Min_Humidity_dict[Year])
            if humidity < existing_humidity:
                Min_Humidity_dict[Year] =  Minimum_Humidity_of_Month
            else:
                pass
        else:
            Min_Humidity_dict[Year] = Minimum_Humidity_of_Month
    else:
        pass






def Max_Temp_Calculation(List_of_Temp):
    Max_temperatures_list = []
    i = List_of_Temp[1]
    for i in range(len(List_of_Temp)):
        Max_temperatures_list = Max_temperatures_list.append(List_of_Temp[i])
        i = i+23
    if not Max_temperatures_list:
        return 0
    else:
        Max_temp = max(Max_temperatures_list)
        Max_temp_String = str(Max_temp)
    for item in range(len(List_of_Temp)):
        if List_of_Temp[item][1] == Max_temp_String:
            Max_temperatures_list.append(List_of_Temp[item][0])
            Max_temperatures_list.append(Max_temp_String)
            break


    return Max_temperatures_list



def Min_Temp_Calculation(List_of_Temp):
    Min_temperatures_list = []
    i = List_of_Temp[3]
    for i in range(len(List_of_Temp)):
        Min_temperatures_list = Min_temperatures_list.append(List_of_Temp[i])
        i = i+23
    if not Min_temperatures_list:
        return 0
    else:
        Min_temp = max(Min_temperatures_list)
        Min_temp_String = str(Min_temp)
    for item in range(len(List_of_Temp)):
        if List_of_Temp[item][3] == Min_temp_String:
            Min_temperatures_list.append(List_of_Temp[item][0])
            Min_temperatures_list.append(Min_temp_String)
            break


    return Min_temperatures_list




def Max_Humidity_Calculation(List_of_Humidity):
    i = 7
    month_max_humidity = []
    max_list_of_humidity = []
    for i in range(len(List_of_Humidity)):
        max_list_of_humidity.append(List_of_Humidity[i][7])
        i = i+23
    if not max_list_of_humidity:
        return 0

    else:
        maximum_humidity = max(List_of_Humidity)
        Max_humidity_String = str(maximum_humidity)
        for item in range(len(List_of_Humidity)):
            if List_of_Humidity[item][7] == Max_humidity_String:
                month_max_humidity.append(List_of_Humidity[item][0])
                month_max_humidity.append(Max_humidity_String)
                break
        return month_max_humidity


def Min_Humidity_Calculation(List_of_Humidity):
    i = 9
    month_min_humidity = []
    min_list_of_humidity = []
    for i in range(len(List_of_Humidity)):
        min_list_of_humidity.append(List_of_Humidity[i][9])
        i = i+23
    if not min_list_of_humidity:
        return 0

    else:
        minimum_humidity = max(List_of_Humidity)
        Min_humidity_String = str(minimum_humidity)
        for item in range(len(List_of_Humidity)):
            if List_of_Humidity[item][9] == Min_humidity_String:
                month_min_humidity.append(List_of_Humidity[item][0])
                month_min_humidity.append(Min_humidity_String)
                break
        return month_min_humidity



def year_hottest_days():
    print()
    print(" ********************************************************************************************************** ")
    print("          Year                              Date                          Temp                              ")
    print(" ********************************************************************************************************** ")
    print()
    for i in Max_Temp_dict.keys():
        print("{0}    {1}    {2}".format(i, Full_Date_dict[i], Max_Temp_dict[i]))


def Annual_Report():
    print()
    print(" ********************************************************************************************************** ")
    print("          Year    Max Temp    Min Temp    Max Humidity    Min Humidity                                "      )
    print(" ********************************************************************************************************** ")
    for i in Max_Temp_dict.keys():
        print("{0}        {1}       {2}            {3}           {4}".format(i, Max_Temp_dict[i], Min_Temp_dict[i],
                                                                             Max_Humidity_dict[i],
                                                                             Min_Humidity_dict[i]))



print()
print(" ********************************************************************************************************** ")
print("                                                   MENU                                                     ")
print(" ********************************************************************************************************** ")
print()



userChoice = str(input("1. For Annual Report\n"
                       "2. For Hottest Day\n"
                       "Please Enter Your Choice: "))

if int(userChoice) == 1:
    Main()
    Annual_Report()

elif int(userChoice) == 2:
    Main()
    year_hottest_days()

else:
    print("weatherman[report# ][data_dir]")

