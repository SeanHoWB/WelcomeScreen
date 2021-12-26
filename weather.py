# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json
import calendar
import datetime
import time
#switcher
def degtodir(current_dir):
    if (current_dir> 337.5 or current_dir <= 22.5): 
        return "N"
    elif ( 22.5 < current_dir <= 67.5):
        return "NW"
    elif ( 67.5 < current_dir <= 112.5) : 
        return  "W"
    elif ( 112.5 < current_dir <= 157.5) :
        return "SW"
    elif ( 157.5 < current_dir <= 202.5) :
        return "S"
    elif ( 202.5 < current_dir <= 247.5) : 
        return "SE"
    elif ( 247.5 < current_dir <= 297.5) :
        return "E"
    elif ( 297.5 < current_dir <= 337.5) :
        return "NE"
    else:
        return "NIL"


# Enter your API key here


# Enter your API key here
api_key = 'YOUR_API_KEY'

# base_url variable to store url
base_url = "https://api.openweathermap.org/data/2.5/forecast?"

# Give city name
#city_name = input("Enter city name : ")

# complete_url variable to store
#https://www.latlong.net/
#complete_url = base_url + "appid=" + api_key + "&q=" + "Singapore, SG"
complete_url = base_url + "lat=<YOUR_LOCATION>" + "&lon=" + "<YOUR_LOCATION>" + "&appid=" + api_key #home
loc = "<NAME_OF_YOUR_HOME"

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] == "200":
    count = 0
    for item in x["list"]:
        #time...
        time_now = item["dt_txt"]
        day, time1 = time_now.split()
        if str(day)== str(datetime.date.today()): #remeber to type cast ther str
            if time1 < time.strftime("%H:%M:%S"):
                continue
        elif str(day)< str(datetime.date.today()):
            continue
        #counter...
        if count > 2:
            break
        count += 1
        #details
        y = item["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        current_max = y["temp_max"]
        current_fl= y["feels_like"]
        current_min= y["temp_min"]
        z = item["weather"]
        weather_description = z[0]["description"]

        w = item["wind"]
        current_ws = w["speed"]
        current_dir = w["deg"]
                # print following values
        print(f'{loc}' + "\n" + str(day) + " " + str(time1) + "\n Temperature (\u00B0C) = " +str("%.2f" %(current_temperature-273.15)) + 
                "\n     Max (\u00B0C) = " + str("%.2f" %(current_max-273.15)) + "\n     Min (\u00B0C) = " + str("%.2f"
                        %(current_min-273.15)) + "\n     Feels Like (\u00B0C) = " + str("%.2f" %(current_fl-273.15)) +
                "\n Wind (m/s) = " + str("%.2f" %(current_ws)) + "\n Direction = " + str(degtodir(current_dir)) + " " + str("%.2f" %(current_dir)) + "\u00B0"+
                "\n Atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
                "\n Humidity (in percentage) = " +
                    str(current_humidity) +
                "\n Description = " +
                    "\033[1;33;40m" + str(weather_description) +"\033[0;37;40m" + "\n")
elif x["cod"] == "402":
    print("Call limit reached")
else:
    print(" City Not Found ")
