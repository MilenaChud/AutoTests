import json
import csv

users = []
library = []

with open("books.csv", encoding='utf-8') as c:
    reader = csv.DictReader(c, delimiter=",")
    for row in reader:
        copy = {
            "title": row['Title'], "author": row['Author'],
            "pages": row['Pages'], "genre": row['Genre'],
        }
        library.append(copy)


with open("users.json", "r") as j:
    templates = json.load(j)
    for txt in templates:
        person = {
            "name": txt['name'], "gender": txt['gender'],
            "address": txt['address'], "age": txt['age'],
            "books": []
        }
        users.append(person)

y = 0
len_users = len(users)
for lib in library:
    users[y]["books"].append(lib)
    y += 1
    if y == len_users:
        y = 0

with open("result.json", "w") as result:
    json.dump(users, result, indent=4)
