import requests
from requests import Response

response = requests.get('https://api.github.com')

# if response.status_code == 200:
#     print('Success!')
# elif response.status_code == 404:
#     print('Not Found.')

if response:
    print('Success!')
else:
    print('An error has occurred.')
