import json

data = json.load(open("data.json"))


def find_meaning(word):
    if word in data:
        return data[word]
    else:
        return ["Word not found"]



