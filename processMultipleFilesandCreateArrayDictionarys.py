#file to run function on multiple files and extract dictionary of just file name and array of data - nothing else

import os
import Boomer
import infrared_spectra
directory = os.fsencode('infrared_spectra')


listOfFileNames = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    #filename = ('\''+ filename + '\'')
    listOfFileNames.append(filename)

    

print(listOfFileNames)

dicOfData = {}
dicOfData['title'] = 1

for i in listOfFileNames:
    jcampDictionary = Boomer.jcampParserPython(i)
    title = jcampDictionary['TITLE']
    data = jcampDictionary['XYDATA']
    #dicOfData('\''+ title + '\'') = data

    
    title = ''.join(title)
    data = ''.join(data)
    print(type(title),type(data))
    dicOfData[title] = data

print(dicOfData)
