import requests
import json
import csv
from collections import OrderedDict
from hashing import hash
# usernames
f = open('output.json')


data = json.load(f)

with open('submissions2.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['username', 'user_rating','ID' ,'contestId', 'index','problem_rating', 'timestamp' ,'OK', 'WRONG_ANSWER', 'TIME_LIMIT_EXCEEDED', 
        'COMPILATION_ERROR', 'RUNTIME_ERROR', 'IDLENESS_LIMIT_EXCEEDED', 'MEMORY_LIMIT_EXCEEDED',
        'SKIPPED', 'TESTING', 'PRESENTATION_ERROR', 'FAILED', 'CRASHED',
        'CHALLENGED', 'REJECTED', 'PARTIAL', 'SECURITY_VIOLATED', 'INPUT_PREPARATION_CRASHED', 'SUBMITTED'])

    url = "https://codeforces.com/api/user.status"
    urlUser="https://codeforces.com/api/user.info"
    i=0
    for user in data['names']:
        questions = OrderedDict()
        i+=1
        try:
            print(user, i)
            args = {'handle': user}
            argsUser = {'handles': user}
            data = requests.get(url, params=args).content
            userData = requests.get(urlUser, params=argsUser).content
            # print()
            userResult = json.loads(userData.decode())['result'][0]['rating']
            result = json.loads(data.decode())
            result = result['result']

            for row in result:
                qId=0
                if 'contestId' not in row.keys():
                    continue

                qId=hash(row['contestId'], row['problem']['index'])

                if qId not in questions:
                    if 'rating' not in row['problem'].keys():
                        continue
                    questions[qId] = OrderedDict({'contestId': row['contestId'],
                        'index': row['problem']['index'],
                        'problem_rating': row['problem']['rating'],
                        'tiemstamp' : row["creationTimeSeconds"] + row["relativeTimeSeconds"],
                        'OK': 0, 
                        'WRONG_ANSWER': 0, 
                        'TIME_LIMIT_EXCEEDED': 0, 
                        'COMPILATION_ERROR': 0, 
                        'RUNTIME_ERROR': 0, 
                        'IDLENESS_LIMIT_EXCEEDED': 0, 
                        'MEMORY_LIMIT_EXCEEDED': 0,
                        'SKIPPED': 0, 
                        'TESTING': 0, 
                        'PRESENTATION_ERROR': 0, 
                        'FAILED': 0, 
                        'CRASHED': 0,
                        'CHALLENGED': 0, 
                        'REJECTED': 0, 
                        'PARTIAL': 0, 
                        'SECURITY_VIOLATED': 0, 
                        'INPUT_PREPARATION_CRASHED': 0,
                        'SUBMITTED': 0})
                questions[qId][row['verdict']]+=1
            
            for question in questions.keys():
                qData = [user,userResult, question]
                qData.extend(list(questions[question].values()))
                csv_writer.writerow(qData)
        except Exception as e:
            print(e)
