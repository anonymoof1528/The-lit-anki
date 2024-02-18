import subprocess
import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class RandomTermWindow(QWidget):
    def __init__(self, term, definition):
        super().__init__()

        self.term_label = QLabel(f'Term: {term}')
        self.definition_label = QLabel(f'Definition: {definition}')

        self.definition_label.setWordWrap(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.term_label)
        layout.addWidget(self.definition_label)

        self.show()

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

def main():
    outputLines = readData("../data/output.txt")
    outputDict = createDictionary(outputLines)
    while True:
        term = random.choice(list(outputDict.keys()))
        definition = outputDict[term]

        if definition != "":
            break
        else:
            print(f"Empty definition detected for {term}")
    app = QApplication(sys.argv)
    window = RandomTermWindow(term, definition)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

