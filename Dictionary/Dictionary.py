import json
from difflib import get_close_matches

data = json.load(open("/Users/Lucky/PycharmProjects/Udemy/webmap_with_folium/Dictionary/data.json"))


def dictionary(word):
    word = word.lower()
    alternative = get_close_matches(word, data.keys())[0]
    if word in data:
        return data[word]
    elif word.upper():
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % alternative)
        if yn == "Y":
            return alternative[0]
        elif yn == "N":
            return "The word doesn't Exit"
        else:
            return "We dont understand your word"

    else:
        return "The word doesn't exit. Please double check it"


word = input("Enter a word: ")

output = dictionary(word)

for arrange in output:
    print(arrange)
