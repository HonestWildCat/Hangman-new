import json, codecs

with codecs.open('russian_nouns_with_definition.json', encoding='utf-8') as f:
    data = json.load(f)
key = data.keys()
with open('dictionary.txt', 'w') as f:
    for i in key:
        print(f'{[i, "", data[i]["definition"]]},\n')
        f.write(f'{[i, "", data[i]["definition"]]},\n')
