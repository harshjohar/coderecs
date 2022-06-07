import requests
import json
import csv

f = open('output.json')

data = json.load(f)

# extract user names from data['name']

questions = dict()

for user in data['names']:
    print(user)
    url = "https://codeforces.com/api/user.status"
    args = {'handle': user}
    data = requests.get(url, params=args).content
    result = json.loads(data.decode())
    result = result['result']

    for row in result: 
        qId=69
        if 'contestId' in row.keys():
            qId = row['contestId'] * 60
        else:
            row['contestId'] = 0
        if len(row['problem']['index']) == 2:
            offset = 2 * ord(row['problem']['index'][0]) + (bool)(row['problem']['index'][1] == '2') - 130
        elif len(row['problem']['index']) == 1:
            offset = 2*(ord(row['problem']['index']) - 65)
        qId += offset

        if qId not in questions:
            questions[qId] = {'contestId': row['contestId'], 'index':row['problem']['index'],'OK': 0, 'WRONG_ANSWER': 0, 'TIME_LIMIT_EXCEEDED': 0, 
            'COMPILATION_ERROR': 0, 'RUNTIME_ERROR': 0, 'IDLENESS_LIMIT_EXCEEDED': 0, 'MEMORY_LIMIT_EXCEEDED': 0,
            'SKIPPED': 0, 'TESTING': 0, 'PRESENTATION_ERROR': 0, 'FAILED': 0, 'CRASHED': 0,
            'CHALLENGED': 0, 'REJECTED': 0, 'PARTIAL': 0, 'SECURITY_VIOLATED': 0, 'INPUT_PREPARATION_CRASHED': 0}
        
        questions[qId][row['verdict']] += 1

with open('./output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['ID','contestId','index', 'OK', 'WRONG_ANSWER', 'TIME_LIMIT_EXCEEDED', 
        'COMPILATION_ERROR', 'RUNTIME_ERROR', 'IDLENESS_LIMIT_EXCEEDED', 'MEMORY_LIMIT_EXCEEDED',
        'SKIPPED', 'TESTING', 'PRESENTATION_ERROR', 'FAILED', 'CRASHED',
        'CHALLENGED', 'REJECTED', 'PARTIAL', 'SECURITY_VIOLATED', 'INPUT_PREPARATION_CRASHED'])

    for questionId in questions:
        qDat = [questionId, ]
        qDat.extend(list(questions[questionId].values()))
        # print(qDat)
        csv_writer.writerow(qDat)