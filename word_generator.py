import random
import json

# Parameters: input, tokenizing or not, number of grams
def collect_ngrams(in_list, tokens = True, n = 1):
    #turn any input into a list
    ngrams = []

    # Conditional to see if input is a single String
    if isinstance(in_list, list) and len(in_list) == 1 and isinstance(in_list[0], str):
        in_list = in_list[0]

        # Tokenize grams into words with .split() or n amount of characters
        if tokens:
            in_list = in_list.split()
        else:
            in_list = list(in_list)
    elif isinstance(in_list, str):
        in_list = in_list.split() if tokens else list(in_list)

    # Adds each gram to the n_gram list
    for i in range(len(in_list) - n + 1):
        if tokens:
            ngrams.append(' '.join(in_list[i:i + n]))
        else:
            ngrams.append(''.join(in_list[i:i + n]))

    # Return the final list
    return ngrams

file = open('puzzle_text', 'r')
file_text = file.read()
file_ngrams = collect_ngrams(file_text)
key = -1
words = {}

for value in file_ngrams:
    if value not in words:
        words[value] = []

    if (key > -1):
        words[file_ngrams[key]].append(value)
    key += 1

with open('word_data.json', 'w') as outfile:
    json.dump(words, outfile)

def generate_challenge():
    returnValues = []
    sentence = ""
    random_key = random.choice(list(words.keys()))
    while(not random_key[0].isupper() or list(words.keys()).index(random_key) > len(words.keys()) - 10):
        random_key = random.choice(list(words.keys()))

    for num in range(10):
        num += 1
        sentence += random_key + " "
        if (list(words.keys()).index(random_key) == len(words.keys()) - 2):
            break
        else:
            random_value = random.choice(words[random_key])
            random_key = random_value

    returnValues.append(sentence)
    returnValues.append(random_key)

    return returnValues
