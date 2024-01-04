#weather of a city

import requests #to cnct website to to our code
import datetime #to cnvrt date time
api_key="3d31026dc74aec3ed6c03e4360dfafcc"#unq c creatin acc
city=input("Enter city: ")
response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=Metric")#to get info from webs to our code
a=response.json()#cnvrts complex inf to dict
print(a)
if 'message' in a:
    print("City not Found!") #if not found
else:
    print("\nCity:",city)
    print("Temperature:",a['main']['temp'],"C")
    print("Humidity:",a['main']['humidity'])
    print("Sunrise(IST):",datetime.datetime.fromtimestamp(a['sys']['sunrise']))#complex tinfo that are unarranged
    print("Sunset(IST):",datetime.datetime.fromtimestamp(a['sys']['sunset']))