#!/usr/bin/python
#PERFORMED BY: alexxa
#DATE: 20.12.2013
#SOURCE: Google Python course https://developers.google.com/edu/python/
#https://developers.google.com/edu/python/exercises/copy-special


# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys, re, os, shutil, zipfile

"""Copy Special exercise
"""
def get_special_paths(dir):
    
    '''
        Returns a list of all special files in a given directory
    '''
    
    res = []
    paths = os.listdir(dir)  
    for file in paths:
        match = re.search(r'__(\w+)__', file)
        if match:
            res.append(os.path.abspath(os.path.join(dir, file)))
    #for item in res:
    #    print(item)
    return res

def copy_to(to_dir):
    
    '''
        Copy all files to the given destination
    '''
    files = get_special_paths('.')
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    for file in files:
        file = os.path.basename(file)
        try: 
            shutil.copy(file, os.path.join(to_dir, file))
            print('{} was copied to {}'.format(file, to_dir))
        except:
            pass

def zip_to(zipfile_name):
    
    '''
        Zip all given files into a new zip file 
        with the defined name.
    '''
    
    files = get_special_paths('.')
    zipf = zipfile.ZipFile(zipfile_name, 'w')
    for file in files:
        zipf.write(os.path.join(file))
    zipf.close()


# part A
#get_special_paths('.')

# part B
# copy_to('new_dir')

# part C
zip_to('file.zip')
