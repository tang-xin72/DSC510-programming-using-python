#DSC 510-301
#Week 9: Programming Assignment Week 9
#Author Xin Tang
#5/10/2023

#Change control log:
'''Change #1: remove printprint function and create the process_file function
   date of change: 5/8/2023
   Change #2: add \n inside write method call
   date of change: 5/9/2023
   change #3: try different f method inside write
   date of change: 5/9/23
   change #4 add check to validate the directory exist.
   date of change 5/9/23
   change#5: move the length and header write session out of process line function to main()
   date of change 5/10/23
'''

#Author: Xin Tang
#Change approved by: Xin Tang
#Date move to production: NA

import re, requests
import os


# add_word will count upper and lower case word the same, also it will count in number as word as well
def add_word(word_list, dict):
    for word in word_list:
        count = dict.get(word.lower(), 0)
        dict[word.lower()] = count + 1
    #dict_list = dict.keys()


def process_line(line, dict):
    string2 = re.sub('[,.-]', "", line)
    word_list = string2.split()
    add_word(word_list, dict)


def process_file(dict, fileName):
    # with open(completePath, 'w') as fileHandle:
    #     fileHandle.write(f'{"Length of the dictionary:  "}{len(dict)}''\n')
    #     fileHandle.write(f'{"word":18s}{"count":8s}''\n')
    #     fileHandle.write('-' * 24)
    #     fileHandle.write('\n')

    new_dict = {key: value for key, value in sorted(dict.items(), key=lambda x: x[1], reverse=True)}

    with open(fileName, 'a') as fileHandle:
        for (key, value) in new_dict.items():
            fileHandle.write(f'{key:20}{value}''\n')


def main():
    url = 'https://content.bellevue.edu/cst/dsc/510/resources/new/gettysburg.txt'

    r = requests.get(url, allow_redirects=True)
    open('gettysburg.txt', 'wb').write(r.content)

    try:
        with open('gettysburg.txt', 'r') as handler:
            gba_file = handler.readlines()
    except FileNotFoundError:
        print('no file found')

    frequency = {}  # frequency is the dictionary store word and its counts
    for line in gba_file:
        content_list = line.rstrip()
        process_line(content_list, frequency)

    #filePath = 'C:\\Users\\Daisy\\Documents\\Xin\\Data science\\DSC510\\week9\\'
    #if os.path.isdir(filePath):
    #    print('Directory Exists')
    fileName = input("input file name in xx.txt format, must end with txt: ")
    #completePath = filePath + fileName
    with open(fileName, 'w') as fileHandle:
        fileHandle.write(f'{"Length of the dictionary:  "}{len(frequency)}''\n')
        fileHandle.write(f'{"word":18s}{"count":8s}''\n')
        fileHandle.write('-' * 24)
        fileHandle.write('\n')

    process_file(frequency, fileName)


if __name__ == "__main__":
    main()

