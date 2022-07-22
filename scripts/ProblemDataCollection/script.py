import requests
import json
import csv
from collections import OrderedDict

def hash(contest, index):
    contest *= 80 # multiply by 80 (> 78 = 26 * 3)
    offset = 3 * (ord(index[0]) - 65) # A0 = A, A1, A2
    if len(index) == 2:
        offset += ord(index[1]) - ord('0')
    return contest + offset

def editTags(tags):
    ans = ""
    for i in tags:
        ans+=i
        ans+='|'
    ans = ans[:-1]
    return ans

with open('problems.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['id', 'rating', 'tags'])

    url = 'https://codeforces.com/api/problemset.problems'
    data = requests.get(url).content
    result = json.loads(data.decode())
    result = result['result']['problems']

    for problem in result:
        # {'contestId': 1, 'index': 'A', 'name': 'Theatre Square', 'type': 'PROGRAMMING', 'rating': 1000, 'tags': ['math']}
        try:
            problemId = hash(problem['contestId'], problem['index'])
            rating = problem['rating']
            tags = editTags(problem['tags'])

            problemData = [problemId, rating, tags]
            csv_writer.writerow(problemData)
            print(problem['contestId'], problem['index'])
        except:
            print("error", problem['contestId'], problem['index'])