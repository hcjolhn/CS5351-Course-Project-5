import csv;
import re

def changeToObject(csvFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['Features']
            data[key] = rows
    return data

def changeFeatures(object):
    lineNumber = -1
    for key, value in object.items():
        count = 0
        filepath = "./" + key
        feature = open(filepath+".feature", "r")
        list_of_lines = feature.readlines()
        scenarioAnchor = False
        targetList = []
        for line in list_of_lines:
            if value["Scenario"] in line:
                print(line)
                scenarioAnchor = True
            if "Examples" in line and scenarioAnchor:
                print(line)
                scenarioAnchor = False
                lineNumber = count
            count += 1
        if lineNumber >= 0:
            fieldLists = list_of_lines[lineNumber + 1].split("|")[1:-1] 
            for item in fieldLists:
                for it in value["Examples"].split("AND"):
                    if item in it:
                        targetList.append(it.split('is')[-1].strip().replace("\"",""))
            print(targetList)
            targetLine = list_of_lines[lineNumber + 2].split("|")
            for i in range(len(targetList)):
                targetLine[i+1] = targetList[i]
            print("|".join(targetLine))
            list_of_lines[lineNumber + 2] = "|".join(targetLine)
            writeFile = open(filepath+".feature", "w")
            writeFile.writelines(list_of_lines)
            writeFile.close()
            feature.close()
            


    
                

            
    return

csvFilePath = r'test.csv'

object = changeToObject(csvFilePath)
changeFeatures(object)