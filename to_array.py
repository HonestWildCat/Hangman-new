arr = []

# with open('categories/animals.txt', 'r', encoding='utf-8') as f:
#     line = f.readline()
#     while line != "@":
#         arr.append(line[:-1])
#         print(f'{line.lower()}', end="")
#         line = f.readline()

with open('categories/berries.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != "@":
        arr.append(line[:-1])
        # print(f'{line.lower()}', end="")
        line = f.readline()
# with open('categories/clothing.txt', 'r', encoding='utf-8') as f:
#     line = f.readline()
#     while line != "@":
#         arr.append(line[:-1])
#         print(f'{line.lower()}', end="")
#         line = f.readline()
with open('categories/countries.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != "@":
        arr.append(line[:-1])
        # print(f'{line.lower()}', end="")
        line = f.readline()
# with open('categories/dishes.txt', 'r', encoding='utf-8') as f:
#     line = f.readline()
#     while line != "@":
#         arr.append(line[:-1])
#         print(f'{line.lower()}', end="")
#         line = f.readline()
with open('categories/flowers.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != "@":
        arr.append(line[:-1])
        # print(f'{line.lower()}', end="")
        line = f.readline()
with open('categories/fruits.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != "@":
        arr.append(line[:-1])
        # print(f'{line.lower()}', end="")
        line = f.readline()
with open('categories/furniture.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != "@":
        arr.append(line[:-1])
        # print(f'{line.lower()}', end="")
        line = f.readline()
with open('categories/herbs and spices.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != "@":
        arr.append(line[:-1])
        # print(f'{line.lower()}', end="")
        line = f.readline()
# with open('categories/professions.txt', 'r', encoding='utf-8') as f:
#     line = f.readline()
#     while line != "@":
#         arr.append(line[:-1])
#         print(f'{line.lower()}', end="")
#         line = f.readline()
with open('categories/trees.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != "@":
        arr.append(line[:-1])
        # print(f'{line.lower()}', end="")
        line = f.readline()
with open('categories/vegetables.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != "@":
        arr.append(line[:-1])
        # print(f'{line.lower()}', end="")
        line = f.readline()

print(arr)
with open('dictionary_edited.txt', 'w') as f:
    f.write(", ".join(arr))
