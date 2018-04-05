import requests
response = requests.get('http://tgftp.nws.noaa.gov/data/observations/metar/stations/KEWR.TXT')
print(response.text)
