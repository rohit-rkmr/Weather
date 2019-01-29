import json,requests
cityname=input("enter city name")

response=requests.get("http://api.openweathermap.org/data/2.5/weather?appid=0adc6b2eaf035393c5008f478f36447f&q="+ cityname)
climate=response.json( )
print(cityname,climate['sys']['country'])
print(climate['main']['temp']-273.15,"degree celcius")


