arr = []
count = 0
categories = ["_berries", "_fruits", "_vegetables",
              "_trees", "_flowers" , "_herbs and spices",
              "furniture", "animals", "clothing",
              "_countries", "dishes", "proffessions",
              "_stationery", "_buildings"]

with open(f'categories/{categories[13]}.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != "@":
        arr.append(line[:-1])
        count += 1
        print(f'{line.lower()}', end="")
        line = f.readline()

with open('dictionary_edited.txt', 'w') as f:
    f.write(", ".join(arr))

print(count)
