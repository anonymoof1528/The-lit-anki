
import requests

def getCardsInDeck(deckName):
    url = "http://127.0.0.1:8765"
    payload = {
        "action": "findCards",
        "version": 6,
        "params": {
            "query": f'deck:"{deckName}"'
        }
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    return response.json()

def getCardDetails(cardIds):
    url = "http://127.0.0.1:8765"
    payload = {
        "action": "cardsInfo",
        "version": 6,
        "params": {
            "cards": cardIds
        }
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    return response.json()

if __name__ == "__main__":
    try:
        deckName = "Literature Terms"

        cardIdsInDeck = getCardsInDeck(deckName)

        cardDetails = getCardDetails(cardIdsInDeck['result'])['result']

        print("Simple Card Details:")
        for i in cardDetails:
            print(i['fields']['Front']['value'])
            print(i['fields']['Back']['value'])
            print("")
        outputDict = {}
        for i in cardDetails:
            outputDict[i['fields']['Front']['value']] = i['fields']['Back']['value']
        with open('../data/ankioutput.txt', 'w') as outputFile:
            for term, definition in outputDict.items():
                outputFile.write(term + '\n')
                outputFile.write(definition.replace("\n", " ") + '\n')

    except requests.exceptions.RequestException as e:
        print("Error:", e)
