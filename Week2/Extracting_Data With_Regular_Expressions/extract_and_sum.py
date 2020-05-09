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
