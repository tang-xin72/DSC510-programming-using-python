#DSC 510-301
#Week 8, Programming Assignment Week 8
#Author Xin Tang
#5/3/2023

#Change control log:
'''Change #1: turn word into lower case so word will not be counted differently
   date of change: 5/1/2023
   Change #2: define a way to sort the dictionary descending based on value in pretty_print function
   date of change: 5/2/2023
   change #3: update the pretty_print function to regulate the print location
   change #4: use "with" to safe open the file
   change #5: add try to safe open the file.
'''

#Author: Xin Tang
#Change approved by: Xin Tang
#Date move to production: NA





import re, urllib.request
import requests

#add_word will count upper and lower case word the same, also it will count in number as word as well
def add_word(word_list, dict):
    for word in word_list:
        count = dict.get(word.lower(), 0)
        dict[word.lower()] = count + 1
    #dict_list = dict.keys()


def Process_line(line, dict):
    string2 = re.sub('[,.-]', "", line)
    word_list = string2.split()
    add_word(word_list, dict)


def Pretty_print(dict):
    print('Length of the dictionary:', len(dict))
    print(f'{"word":18s}{"count":8s}')
    print('-'*24)
    new_dict = {key: value for key, value in sorted(dict.items(), key=lambda x: x[1], reverse=True)}

    for (key, value) in new_dict.items():
        print(f'{key:20}{value}')

def main():
    url = 'https://content.bellevue.edu/cst/dsc/510/resources/new/gettysburg.txt'

    r = requests.get(url, allow_redirects=True)
    open('gettysburg.txt', 'wb').write(r.content)

    try:
        #with open('C:\\Users\\Daisy\\Documents\\Xin\\Data science\\DSC510\\week8\\gettysburg.txt', 'r') as handler:
        with open('gettysburg.txt', 'r') as handler:
            gba_file = handler.readlines()
    except FileNotFoundError:
        print('no file found')
    frequency = {}   # frequency is the dictionary store word and its counts
    for line in gba_file:
        print(line)
        content_list = line.strip()
        Process_line(content_list, frequency)

    Pretty_print(frequency)

if __name__ == "__main__":
    main()