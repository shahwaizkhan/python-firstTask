"""

This project will display results extracted from weather data

files which are stored in project directory.

"""

import csv
import glob

max_temp_dict = {}  # Monthly maximum temp will store e.g 1998:45
min_temp_dict = {}  # Monthly minimum temp will store e.g 1998:3
min_humidity_dict = {}  # Monthly minimum humidity will store e.g 1998:31
max_humidity_dict = {}  # Monthly maximum temp will store e.g 1998:100
full_date_dict = {}  # Complete date will store e.g 1998:1998-2-3


def main():
    """
    This is Main function
    
    """
    files = glob.glob("*.txt")
    for afile in files:
        max_temp_reader_list = []
        date_of_max_temp = []
        min_temp_reader_list = []
        max_humidity_reader_list = []
        min_humidity_reader_list = []
        
        with open(afile) as file:
            # skip first and last lines
            read_contents_of_file = csv.DictReader(file.readlines()[1:-1])
            for row in read_contents_of_file:
                # iterate over a file lines
                if row:
                    # if row is not empty
                    if row['Max TemperatureC']:
                        max_temp_reader_list.append(row['Max TemperatureC'])
                        min_temp_reader_list.append(row['Min TemperatureC'])
                        max_humidity_reader_list.append(row['Max Humidity'])
                        min_humidity_reader_list.append(row['Min Humidity'])
                        # if date format is PKT or PKST 
                         if 'PKT' in row.keys(): 
                            date_of_max_temp.append(row['PKT']) 
                        else: 
                             date_of_max_temp.append(row['PKST']) 
        
        # Passing list to functions for calculations
        maximum_temperature = max_temp_calculation(max_temp_reader_list)
        minimum_temperature = min_temp_calculation(min_temp_reader_list)
        maximum_humidity = max_temp_calculation(max_humidity_reader_list)
        minimum_humidity = min_temp_calculation(min_humidity_reader_list)
        # Getting dates of temperatures(Max, Min)  
        date_of_max_temperature = get_date_of_maxTemp(maximum_temperature)
        date_of_min_temperature = get_date_of_minTemp(minimum_temperature)
        date_of_max_humidity = get_date_of_maxHumidity(maximum_humidity)
        date_of_min_humidity = get_date_of_minHumidity(minimum_humidity)


def get_date_of_maxTemp(max_temp):
    """
    This function will give date of 
    Maximum temperature
    
    """
    if max_temp != 0:
        date = max_temp[0]

        # Split the date so that we can use Year e.g 1996 as a key
        year = str(date)[:4]
        max_temp_of_month = max_temp[1]
        
        # If key:Year is already store in dictionary. So data of month is already stored
        if year in max_temp_dict.keys():
            temp = int(max_temp_of_month)
            temp_in_dic = int(max_temp_dict[year])
            
            if temp > temp_in_dic:
                # Compare the NewTemp with existed Temp
                # If Temp is greater than existed Temp
                # Replace it with Temp and Date in both dictionaries
                # Remember: Year will be the key in all dictionaries
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
    """
    This function will give date of 
    Minimum temperature
    
    """
    if min_temp != 0:
        date = min_temp[0]
        # Split the date so that we can use Year e.g 1996 as a key
        year = str(date)[:4]
        min_temp_of_month = min_temp[1]
        
        # If key:Year is already store in dictionary. So data of month is already stored
        if year in min_temp_dict.keys():
            temp = int(min_temp_of_month)
            temp_in_dic = int(min_temp_dict[year])
            
            if temp < temp_in_dic:
                # Compare the NewTemp with existed Temp
                # If Temp is Less than existed Temp
                # Replace it with Temp and Date in both dictionaries
                # Remember: Year will be the key in all dictionaries
                min_temp_dict[year] = min_temp_of_month
                full_fate_dict[year] = date
            else:
                pass
        else:
            min_temp_dict[year] = min_temp_of_month
            full_date_dict[year] = date
    else:
        pass


def get_date_of_maxHumidity(max_humidity):
    """
    This function will give date of 
    Maximum humidity
    
    """
    if max_humidity != 0:
        date = max_humidity[0]
        # Split the date so that we can use Year e.g 1996 as a key
        year = str(date)[:4]
        maximum_humidity_of_month = max_humidity[1]
        # If key:Year is already store in dictionary. So data of month is already stored
        if year in max_humidity_dict.keys():
            humidity = int(maximum_humidity_of_month)
            existing_humidity = int(max_humidity_dict[year])
            
            if humidity > existing_humidity:
                # Compare the NewHumidity with existed Humidity 
                # If NewHumidity is greater than existed Humidity. 
                # Replace it with NewHumidity 
                max_humidity_dict[year] =  maximum_humidity_of_month
            else:
                pass
        else:
            max_humidity_dict[year] = maximum_humidity_of_month
    else:
        pass


def get_date_of_minHumidity(min_humidity):
    """
    This function will give date of 
    Minimum humidity
    
    """
    if min_humidity != 0:
        date = min_humidity[0]
        # Split the date so that we can use Year e.g 1996 as a key
        year = str(date)[:4]
        minimum_humidity_of_month = min_humidity[1]
        # If key:Year is already store in dictionary. So data of month is already stored
        if year in min_humidity_dict.keys():
            humidity = int(minimum_humidity_of_month)
            existing_humidity = int(min_humidity_dict[year])
            
            if humidity < existing_humidity:
                # Compare the NewHumidity with existed Humidity 
                # If NewHumidity is less than existed Humidity. 
                # Replace it with NewHumidity 
                min_humidity_dict[year] =  minimum_humidity_of_month
            else:
                pass
        else:
            min_humidity_dict[year] = minimum_humidity_of_month
    else:
        pass


def max_temp_calculation(list_of_temp):
    """ 
    This function will calculate maximum value
    :param list_of_temp: List from where to find Max number 
    :return: maximum number in string
    """  
    if len(list_of_temp) == 0: 
        return 0 
    if len(temp_list) == 1: 
         return list_of_temp 
    maximum = max(map(int,list_of_temp)) 
     return str(maximum) 
         

def min_temp_calculation(list_of_temp):
    """ 
    :param list_of_temp: list to apply minimum function 
    :return: string minimum number 
    """ 
    if len(list_of_temp) == 1: 
        return list_of_temp 
    minimum = min(map(int,list_of_temp)) 
     return str(minimum) 


def year_hottest_days(): 
     """ 
     it will show the the Hottest days with year and complete date 
 
    """ 
    print(str("Year").rjust(4), 
           str("Date").rjust(10), 
           str("Temp").rjust(11), 
           "[Report#2][Hottest Days Report]".rjust(8) 
           )
    print("-" * 90) # 90 dashes
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
     print("-" * 90) # 90 dashes
     # iterate over dictionary key @Year e.g 1996 and display it's value.Uses same key for all dictionaries 
    for i in full_date_dict.keys(): 
        print(str(i).rjust(6), 
              str(max_temp_dict[i]).rjust(6), 
              str(min_temp_dict[i]).rjust(6), 
              str(max_humidity_dict[i]).rjust(8), 
              str(min_humidity_dict[i]).rjust(9) 
               ) 

# Take input from user. What type of report to display
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

