import subprocess

def readData(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()
    return lines

def createEmptyList(lines):
    dataList = []
    currentTerm = ""
    currentDefinition = ""
    term = True
    temp = []

    for line in lines:
        line = line.strip()
        temp.append(line)
        if len(temp) == 2:
            if temp[1] == "":
                dataList.append(temp[0])
            temp = []
    return dataList

def checkEmpty(path):
    outputLines = readData(path)
    outputList = createEmptyList(outputLines)
    if outputList:
        print(f"\033[1mTerms in {path} which don't have a definition:\033[0m")
        string = ""
        for i in outputList:
            string = string + "\n" + i
        print(string)
        print("\nWould you like to make a file so you can add the definitions? (Y/N)")
        answer = input("")
        if answer == 'Y':
            with open(path.replace(".txt", "emptyterms.txt"), 'w') as outputFile:
                for term in outputList:
                    outputFile.write(term + '\n\n')
                print("File has been made.")

def main():
    pathInput = input("Which text files do you want to check?\nPlease separate by a ', '.\n\nFor example, \n\n'list.txt, syllabusglossaryterms.txt, ankioutput.txt'\n\nis a valid input.\n\n")
    for path in pathInput.split(", "):
        checkEmpty("../data/" + path)

if __name__ == "__main__":
    main()

