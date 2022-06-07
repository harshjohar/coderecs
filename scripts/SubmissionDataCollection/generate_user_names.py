import json
f = open('input.json')

data = json.load(f)

users = []

for i in data:
    if len(data[i]):
        for user in data[i]:
            users.append(user)

dict = {"names": users}
json_object = json.dumps(dict)

with open("output.json", "w") as outfile:
    outfile.write(json_object)