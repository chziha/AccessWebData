'''
Scraping Numbers from HTML using BeautifulSoup

In this assignment you will write a Python program
similar to http://www.py4e.com/code3/urllink2.py.
The program will use urllib to read the HTML from the data files below,
and parse the data, extracting numbers
and compute the sum of the numbers in the file.

We provide two files for this assignment.
One is a sample file where we give you the sum for your testing
and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_535466.html (Sum ends 59)
'''

import urllib.request, ssl
from bs4 import BeautifulSoup

def extract_sum():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter the url: ')
    html = urllib.request.urlopen(url, context = ctx)
    soup = BeautifulSoup(html, 'html.parser')

    sum = 0
    count = 0

    for span in soup.find_all('span'):
        num = int(span.get_text())
        count += 1
        sum += num

    print('There are in total %d numbers summing up to %d.' % (count, sum))

if __name__ == '__main__':
    extract_sum()
