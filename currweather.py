# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json


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
api_key = 'YOUR_API_KEY'

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
#city_name = input("Enter city name : ")

# complete_url variable to store
#https://www.latlong.net/
#complete_url = base_url + "appid=" + api_key + "&q=" + "Singapore, SG"
complete_url = base_url + "lat=<YOUR_LOCATION>" + "&lon=" + "<YOUR_LOCATION>" + "&appid=" + api_key #home
loc = "<NAME_OF_YOUR_HOME"

#example
#complete_url = base_url + "lat=1.294887" + "&lon="+"103.773722" + "&appid=" + api_key #nus com1
#loc = 'COM 1'

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
if x["cod"] != "404" or "402":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    current_max = y["temp_max"]
    current_fl= y["feels_like"]
    current_min= y["temp_min"]
    z = x["weather"]
    weather_description = z[0]["description"]
    w = x["wind"]
    current_ws = w["speed"]
    current_dir = w["deg"]
    print(f'{loc}' + 
            "\n Temperature (\u00B0C) = " +
            str("%.2f" %(current_temperature-273.15)) + "\n     Max (\u00B0C) = " + str("%.2f" %(current_max-273.15)) + "\n     Min (\u00B0C) = " + str("%.2f"
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
