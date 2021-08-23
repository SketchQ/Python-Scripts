#! python3
#getOpenWeather.py -- Prints the weather for a location from the command line

APPID = '568e213d7755eb31f25278300108aa8f'

import json,requests,sys

# Compute location from comman line arguments.

'''if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
'''
prompt = input()

location = ''.join(list(prompt[1:]))

# TODO : Download the JSON data from OpenWeatherMap.org's API

url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s'% (location,APPID)
response = requests.get(url)
response.raise_for_status()
# Uncomment to see the raw JSON text:
print(response.text)

# TODO : Load JSON data into a Python Variable
'''
{'city': {'coord': {'lat': 37.7771, 'lon': -122.42},
          'country': 'United States of America',
          'id': '5391959',
          'name': 'San Francisco',
          'population': 0},
 'cnt': 3,
 'cod': '200',
 'list': [{'clouds': 0,
           'deg': 233,
           'dt': 1402344000,
           'humidity': 58,
           'pressure': 1012.23,
           'speed': 1.96,
           'temp': {'day': 302.29,
                    'eve': 296.46,
                    'max': 302.29,
                    'min': 289.77,
                    'morn': 294.59,
                    'night': 289.77},
           'weather': [{'description': 'sky is clear',
                        'icon': '01d',
'''

weatherData = json.loads(response.text)

# Print Weather Descriptions.

w = weatherData['list']
print('Current weather in %s:'% (location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])
print()
print('Day after Tomorrow:')
print(w[2]['weather'][0]['main'],'-',w[2]['weather'][0]['description'])