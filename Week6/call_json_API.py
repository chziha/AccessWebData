'''
Calling a JSON API

In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/geojson.py. The program will prompt for a location,
contact a web service and retrieve JSON for the web service and parse that data,
and retrieve the first place_id from the JSON.
A place ID is a textual identifier that uniquely identifies
a place as within Google Maps.

API End Points
To complete this assignment, you should use this API endpoint
that has a static subset of the Google Data:
http://py4e-data.dr-chuck.net/json?
This API uses the same parameter (address) as the Google API.
This API also has no rate limit so you can test as often as you like.
If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to include a key= parameter
and provide the address that you are requesting
as the address= parameter that is properly URL encoded
using the urllib.parse.urlencode() function as shown in
http://www.py4e.com/code3/geojson.py

You will get different results from the geojson and json endpoints
so make sure you are using the same end point as this autograder is using.
'''

import urllib.request, urllib.parse
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def call_API():
    while True:
        loc = input('Enter the location: ')
        if len(loc) < 1 : break

        service_url = 'http://py4e-data.dr-chuck.net/json?'
        url = service_url + urllib.parse.urlencode({'key':42, 'address':loc})
        print('Retrieving ', url)

        data = urllib.request.urlopen(url, context = ctx).read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js:
            print('Failure to Retrieve JSON')
            continue

        print('place_id is ', js['results'][0]['place_id'])

if __name__ == '__main__':
    call_API()
