import json, codecs

with codecs.open('russian_nouns_with_definition.json', encoding='utf-8') as f:
    data = json.load(f)
key = data.keys()
with open('dictionary.txt', 'a') as f:
    for i in key:
        print([i, "", data[i]['definition']])
        f.write(f'{[i, "", data[i]["definition"]]}, ')
