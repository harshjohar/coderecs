from unittest import result
import requests
import csv
import json
from hashing import hash

with open('problems.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['ID', 'contestId', 'index', 'name', 'rating'])

    url = "https://codeforces.com/api/problemset.problems"
    data = requests.get(url).content
    result = json.loads(data.decode())
    problems = result['result']['problems']

    for problem in problems:
        if 'contestId' not in problem.keys() or 'rating' not in problem.keys():
            continue

        qId = hash(problem['contestId'], problem['index'])
        qData = [qId, problem['contestId'], problem['index'], problem['name'], problem['rating']]

        csv_writer.writerow(qData)