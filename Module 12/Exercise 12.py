import requests
import json
#12.1
print(f"Exercise 12.1")
try:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        joke = response.json()
        print(f"Random Chuck Norris joke:\n"
              f"{joke["value"]}")

except requests.exceptions.RequestException as example:
    print("Request could not be completed", example)

#12.2
print("-"*88)
print(f"Exercise 12.2")
try:
    city_input = input("Give the name of the city: ")
    response_city = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_input}&limit=1&appid={ipa key}")
    if response_city.status_code == 200:
        city_result = response_city.json()
        city = city_result[0]
        lat = city["lat"]
        lon = city["lon"]
        response_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={ipa key}")
        if response_weather.status_code == 200:
            weather_result = response_weather.json()

            #print(weather_result)
            #weather_result is a dictionary + value is another dictionary
            weather = weather_result["weather"][0]
            #print(type(weather))
            #weather is a list with one 1 item so we have to put index 0
            weather_description = weather["description"]

            #print(weather_result["main"])
            #weather_result["main"] is a dictionary, so just need to take the value from key "temp"
            weather_temp_kelvin = weather_result["main"]["temp"]
            print(f'- Weather description: {weather_description}')
            print(f'- Temperature: {weather_temp_kelvin} Kelvin')

            def convert_to_celsius(kelvin: float):
                celsius = kelvin - 273.15
                print(f"- In degree Celsius: {round(celsius, 2)}")
                return celsius

            convert_to_celsius(weather_temp_kelvin)

except requests.exceptions.RequestException as e:
    print("Request could not be completed", e)
