#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:51:44 2021
@author: masum
@mail: billahcse@gmail.com
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-c","--classes", metavar='', required=True, help="classes name")
parser.add_argument("-d","--description", metavar='', required=True, help="path to descriptions file")
parser.add_argument("-p","--annotation", metavar='', required=True, help="path to annotations file")
args = vars(parser.parse_args())


classes = args['classes']
classes = classes.split(',')

file_type = ''

if 'train' in args['annotation']:
    file_type = "train"
elif 'test' in args['annotation']:
    file_type = "test"
elif 'annotation' in args['annotation']:
    file_type = 'annotation'
else:
    print("Error: annotation file name should contain train/test/annotation keyword")
    exit()
    

def getCode(filename):
    myList = []
    with open(filename) as lines:
        for line in lines:
            line = line.strip().split(',')
            myCode = line[0]
            myClass = line[1]
            if myClass in classes:
                myList.append(myCode)
    return myList
                
def getID(filename, file_type, classID ):
    f = open('IMAGE_LIST_FILE.txt', "w")
    with open(filename) as lines:
        for line in lines:
            line = line.strip().split(',')
            if line[2] in classID:
                f.write("{}/{}\n".format(file_type,line[0]))
                
myList = getCode(args['description'])

if len(myList) != len(classes):
    print("Error: please check class name")
else:
    getID(args['annotation'], file_type, myList)
