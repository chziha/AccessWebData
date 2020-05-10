'''
Extracting Data from XML

In this assignment you will write a Python program
somewhat similar to http://www.py4e.com/code3/geoxml.py.
The program will prompt for a URL, read the XML data from that URL 
using urllib and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.

We provide two files for this assignment.
One is a sample file where we give you the sum for your testing
and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_535468.xml (Sum ends 90)
'''

import urllib.request, ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def extract_XML():
    url = input('Enter the url: ')
    data = urllib.request.urlopen(url, context = ctx).read()

    count = 0
    sum = 0

    tree = ET.fromstring(data)
    counts = tree.findall('.//count')

    for c in counts:
        count += 1
        sum += int(c.text)

    print('Count = %d and sum = %d.' % (count, sum))

if __name__ == "__main__":
    extract_XML()
