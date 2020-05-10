'''
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/json2.py. The program will prompt for a URL,
read the JSON data from that URL using urllib
and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment.
One is a sample file where we give you the sum for your testing
and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_535469.json (Sum ends 55)
'''

import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def extract_json():
    while True:
        url = input('Enter the url: ')
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

        count = 0
        sum = 0

        for item in js['comments']:
            count += 1
            sum += int(item['count'])

        print('Count is %d and sum is %d.' % (count, sum))

if __name__ == '__main__':
    extract_json()
