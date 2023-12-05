import csv;
import re

def changeToObject(csvFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['Features']
            if not key in data:
                data[key] = [rows]
            else :
                data[key].append(rows)
    return data

# Update
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

def createFeatures(object):
    for key, value in object.items():
        count = 0
        filepath = "./" + key
        writeFile = open(filepath+".feature", "w")
        has_title = False
        for line in value:
            if not has_title:
                writeFile.writelines("Feature: "+ line["Name"])
                has_title = True
            writeFile.writelines("\n")
            writeFile.writelines("\n")
            writeFile.writelines('\t@test_' + line['browser'] + "\n")
            writeFile.writelines('\tScenario Outline: ' + line['Scenario'] + "\n")
            writeFile.writelines('\t\tGiven : ' + line['Pre-step'] + "\n")
            if(len(line["Another Step"].split(" And ")) > 1):
                for li in line["Another Step"].split(" And "):
                    writeFile.writelines('\t\tAnd : ' + li +"\n")
            writeFile.writelines("\tExamples:\n")
            targetExampleKeys = "\t\t|"
            targetValueKeys = "\t\t|"
            for l in line["Examples"].split(" AND "):
                targetExampleKeys += l.split(" is ")[0] + "|"
                targetValueKeys += l.split(" is ")[1] + "|"
            writeFile.writelines(targetExampleKeys + "\n")
            writeFile.writelines(targetValueKeys + "\n")
        writeFile.close()
    return

csvFilePath = r'test2.csv'
print("Starting ...")
object = changeToObject(csvFilePath)
# print(object)
createFeatures(object)
print("CSV to Features files success!")
#changeFeatures(object)