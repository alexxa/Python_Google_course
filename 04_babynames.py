#!/usr/bin/python
#PERFORMED BY: alexxa
#DATE: 20.12.2013
#SOURCE: Google Python course https://developers.google.com/edu/python/
# https://developers.google.com/edu/python/exercises/baby-names

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


import sys, re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename, flag = True):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    
    if flag = True, then write the output to the file, 
    else to the stdout
    """
    
    # read file into string
    fin = open(filename)
    data = fin.read().replace('\n', '')
    
    # find the year of statistic
    year = re.search(r'(Popularity\sin\s\d{4})', data)
    year = ''.join(year.group())
    year = re.search(r'\d{4}', year)
    year = year.group()
  
    # find rank, boy_name, girl_name 
    # return it as a list of tuples
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', data)

    # create dictionary of names
    name_list = {}
    
    for item in tuples:
        (rank, boy_name, girl_name) = item
        if boy_name not in name_list:
            name_list[boy_name] = int(rank)
        if girl_name not in name_list:
            name_list[girl_name] = int(rank)
    
    sorted_d = sorted(name_list, key = name_list.get)

    # print the output to the stdout or to a file
    if flag:
            file_name = 'stat' + year + '.txt'
            f = open(file_name, 'a')
            
            # Update needed: to check whether file exists, 
            # to prompt user whether crate a new one, or 
            # rewrite the old one, or quite maybe
            # or maybe ask the name of file where to write
            
            # if os.path.exists(file_name):
            #    f = file(file_name, '?')
            # else:
            #    f = file(file_name, '?')
            
            for name in sorted_d:
                line = name + ' ' + str(name_list[name]) + '\n'
                f.write(line)
            f.close()
    else:
        for name in sorted_d:
            print(name, name_list[name])
    
    return name_list
    
def name_stat(name, filename):
    '''
        Checks whether given name is in filename
    '''
    name_list = extract_names(filename)
    if name in name_list:
        print('\n', name, name_list[name])
    else:
        print('\nIn {} there is no name {}'.format(filename, name))
    
extract_names('baby1990.html')
#name_stat('Alex', 'baby1990.html')
#name_stat('Irina', 'baby1990.html')