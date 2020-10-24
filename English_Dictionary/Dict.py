import json

data = json.load(open("dictionary.json"))
decision = True

def get_meaning(word):
    if word in data:
        return "The Meaning for the word '%s' is:" %word , data[word]


while decision == True:
    word = input("Enter the word: ").lower()
    meaning = get_meaning(word)

    if not meaning == None:
        print(*meaning)

    else:
        print("Sorry!!! The word '%s' doesn't exit. Please check the word one more time." % word)

    yes_or_no = input("Do you want to continue Y/N: ").lower()

    if yes_or_no in ['yes','y']:
        decision = True

    else:
        print("☺☺ Thank You ☺☺")
        decision = False
