import requests
import subprocess
from bs4 import BeautifulSoup

def readData(filePath):
    data = []
    with open(filePath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            data.append(line)
    return data

def getDefinition(term):
    url = f'https://www.wordreference.com/definition/{term}'

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        definition_tag = soup.find('span', {'class': 'rh_def'})
        
        if definition_tag:
            for cat_tag in definition_tag.find_all('span', {'class': 'rh_cat'}):
                cat_tag.decompose()

            definition = definition_tag.text.strip()
            return definition
        else:
            return f"Definition not found for '{term}'."

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main():
    pathInput = input("Which text files do you want to check?\nPlease separate by a ', '.\n\nFor example, \n\n'list.txt, syllabusglossaryterms.txt, ankioutput.txt'\n\nis a valid input.\n\n").split(", ")
    pathList = []
    for path in pathInput:
        pathList.append("../data/" + path.replace(".txt", "emptyterms.txt"))
    for path in pathList:
        try:
            data = readData(path)
            print(f"Here are some proposed definitions for the empty terms in {path}")
            for term in data:
                definition = getDefinition(term)
                print(f"{term}\n{definition}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

