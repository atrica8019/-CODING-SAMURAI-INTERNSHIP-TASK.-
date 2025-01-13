import requests

city_name = input("Enter the city name : ")
API_key ="e18fdd38601271b9c46a694e1e70bf29"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

response = requests.get(url)
if response.status_code == 200: #status_code is to check whether we get the url
    print("Yes ! URL is Successfull")#to check whether URL fetched Successfully
    data = response.json()#by default Json is used to fetch the data from the Api because data is in list format
    print("Weather is ",data["weather"][0]["description"])#0th index is used to access the first element in the list
    print("Current Temperature is ",data["main"]["temp"])#inside main we have temp
    print("Current Temperature feels like is ",data["main"]["feels_like"])
    print("Current Humidity is ",data["main"]["humidity"])
