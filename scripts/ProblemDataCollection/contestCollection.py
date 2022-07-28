import json
import requests
import csv

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

url = 'https://codeforces.com/api/contest.standings'
with open('contest.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=',')
    
    csv_writer.writerow(['contestID', 'index', 'problemID', 'problemName', 'problemRating', 'problemTags'])
    for i in range(1, 1712):
        print(i)
        params = {'contestId': i, 'from': 1, 'count': 1}
        try:
            r = requests.get(url, params=params).content
            r = json.loads(r.decode())
            
            problems = r['result']['problems']
            print(problems)
            for problem in problems:
                contest, index = problem['contestId'], problem['index']
                problem_id = hash(contest, index)
                rating = problem['rating']
                tags = editTags(problem['tags'])
                csv_writer.writerow([contest, index, problem_id, problem['name'], rating, tags])
        except:
            print("error")
        