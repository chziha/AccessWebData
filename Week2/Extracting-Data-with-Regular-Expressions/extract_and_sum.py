'''
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment.
One is a sample file where we give you the sum for your testing
and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_535464.txt (sum ends 653)
These links open in a new window.
Make sure to save the file into the same folder
as you will be writing your Python program.
Note: Each student will have a distinct data file for the assignment -
so only use your own data file for analysis.
'''

import re

def extract_and_sum_interger():
    filename = input('The file name is: ')

    f = open(filename)
    sum = 0

    for line in f:
        num_list = re.findall('[0-9]+', line)
        for num in num_list:
            sum += int(num)

    print('Sum of the integers in the text is %d' % sum)

if __name__ == '__main__':
    extract_and_sum_interger()
