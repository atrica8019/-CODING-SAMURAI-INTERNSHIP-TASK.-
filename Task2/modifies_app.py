import requests

def fetch_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        # Make a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)

        # Parse JSON response
        data = response.json()

        # Display weather details
        print(f"Weather in {city_name.capitalize()}:")
        print(f"  Description       : {data['weather'][0]['description'].capitalize()}")
        print(f"  Temperature       : {data['main']['temp']}°C")
        print(f"  Feels Like        : {data['main']['feels_like']}°C")
        print(f"  Humidity          : {data['main']['humidity']}%")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")
    except KeyError:
        print("Error: Unable to fetch weather data. Please check the city name or API key.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    API_KEY = "e18fdd38601271b9c46a694e1e70bf29"
    city_name = input("Enter the city name: ").strip()

    if city_name:
        fetch_weather(city_name, API_KEY)
    else:
        print("City name cannot be empty!")