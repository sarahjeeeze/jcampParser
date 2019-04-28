#first create a parser for one file - extracting the elements you want 

import re


def jcampParserPython(file):
    with open(file,'r',errors ='ignore') as f:
            jcamp = f.read().replace("\n", "").split('##')


   

#make tuples and put in to a dictionary - ignore the first one as its empty and last
    jcampDictionary = {}

    for tuple in jcamp[1:(len(jcamp)-1)]:
        splitTuple = tuple.split('=')
    
        name = splitTuple[0]
        data = splitTuple[1]
        jcampDictionary[name] = [data]
    
    

    return(jcampDictionary, splitTuple)

   

#put this in to a database

#create a function so this is possible on many files or 1 file 
