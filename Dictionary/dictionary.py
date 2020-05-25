import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead?" %get_close_matches(word, data.keys())[0])
        decision = input("Press y for yes and n for no...\n")
        if decision == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decision == "n":
            print("You have entered a wrong word. Please check it again.....\n")
            return
        else:
            printf("You have entered an invalid input. Please try again...\n")
            return
    else:
        print("You have entered a wrong word. Please check it again.....\n")



word = input("Enter the word you need to search\n")
result = meaning(word)

for i in result:
    print(i)
