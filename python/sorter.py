from collections import OrderedDict
import os
import json

def readData(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()
    return lines

def createDictionary(lines):
    dataDict = {}
    currentTerm = ""
    currentDefinition = ""
    term = True
    temp = []

    for line in lines:
        line = line.strip()
        temp.append(line)
        if len(temp) == 2:
            dataDict[temp[0]] = temp[1]
            temp = []
    return dataDict

def processAllFilesInFolder(folderPath):
    allData = []

    files = os.listdir(folderPath)
    for fileName in files:
        filePath = os.path.join(folderPath, fileName)
        print(f'Reading {filePath}')
        if os.path.isfile(filePath):
            lines = readData(filePath)
            linesDict = createDictionary(lines)
            allData.append(linesDict)
    return allData

def main():

    allData = processAllFilesInFolder('../data/')
    combinedDict = {}
    for d in allData:
        for key, value in d.items():
            if key in combinedDict:
                if value != '':
                    if combinedDict[key] != '':
                        print(f"Oh no! We have a repeated term, {key}! It is either\n{combinedDict[key]}\nor\n{value}")
                    combinedDict[key] = value
            else:
                combinedDict[key] = value

    sortedDict = OrderedDict(sorted(combinedDict.items()))


    with open('../data/output.txt', 'w') as outputFile:
        for term, definition in sortedDict.items():
            outputFile.write(term + '\n')
            outputFile.write(definition + '\n')

if __name__ == "__main__":
    main()
