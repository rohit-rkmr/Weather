import json,requests
cityname=input("enter city name")

response=requests.get("http://api.openweathermap.org/data/2.5/weather?appid=<your api id>"+ cityname)
climate=response.json( )
print(cityname,climate['sys']['country'])
print(climate['main']['temp']-273.15,"degree celcius")


