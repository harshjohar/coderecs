import numpy as np
import pandas as pd
# from collections import OrderedDict
from gen_pred import recommendations

df = pd.read_csv('test_data/nanak.csv')
# df.head()

# df.shape

df.drop(['COMPILATION_ERROR', 'SKIPPED', 'TESTING','PRESENTATION_ERROR','FAILED','CRASHED','CHALLENGED','REJECTED','PARTIAL','SECURITY_VIOLATED','INPUT_PREPARATION_CRASHED','SUBMITTED'], axis = 1, inplace=True)
# df.head()

users = df['username'].unique()

# users

# len(users)

# db = pd.DataFrame()

# db.append(df[df['username'] == 'user1'])

def mean(WA, RE, TLE, cnt):
    return (WA + 0.6 * TLE + 0.8 * RE) / max(1, cnt)
    
def rating(OK, WA, RE, TLE, avg):
    ans = 0
    ans = abs(OK * avg - WA - 0.6 * TLE - 0.8 * RE)
    return ans

"""### Finding average number of Wrong attempts, TLE submissions, etc"""

# user = users[0]
# WA = [0]
# TLE = [0]
# RE = [0]
# cnt = 0
# j = 0
# means = []
# for i in range(df.shape[0]):
#     if (df.at[i, 'username'] != user):
        
#         means.append(mean(WA, RE, TLE, cnt))
#         # print(f'User {user} has been processed')
#         j += 1
#         user = df.at[i, 'username']
#         WA = RE = TLE = cnt = 0
#         continue
#     WA += (df.at[i, 'WRONG_ANSWER'] + df.at[i, 'MEMORY_LIMIT_EXCEEDED'])
#     TLE += (df.at[i, 'TIME_LIMIT_EXCEEDED'] + df.at[i, 'IDLENESS_LIMIT_EXCEEDED'])
#     RE += df.at[i, 'RUNTIME_ERROR']
#     cnt += 1

cnt = 0 
idx = 0
for i in users:
    db = df[df['username'] == i]
    m1 = np.mean(db['WRONG_ANSWER'] + db['MEMORY_LIMIT_EXCEEDED'])
    m2 = np.mean(db['TIME_LIMIT_EXCEEDED'] + db['IDLENESS_LIMIT_EXCEEDED'])
    m3 = np.mean(db['RUNTIME_ERROR'])
    idx += 1
    m = m1 + 0.6 * m2 + 0.8 * m3
    for j, row in db.iterrows():
        db.at[j, 'rating'] = rating(db.at[j, 'OK'], db.at[j, 'WRONG_ANSWER'] + db.at[j, 'MEMORY_LIMIT_EXCEEDED'], db.at[j, 'RUNTIME_ERROR'], db.at[j, 'TIME_LIMIT_EXCEEDED'] + db.at[j, 'IDLENESS_LIMIT_EXCEEDED'], m)
    mean_, sd = np.mean(db['rating']), np.std(db['rating'])
    db.loc[:, 'rating'] = (db['rating'] - mean_) / sd
    # df[df['username'] == i]['rating'] = db['rating']
    for j, row in db.iterrows():
      df.at[j, 'rating'] = db.at[j, 'rating']
    print(idx, f'{i} has been processed')
    # cnt += db.shape[0]
df.loc[:, 'rating'] = df['rating'].apply(lambda x: abs(x) if (x < 1 and x > -1) else 1)
# print(m1, m2, m3)
# dx = (df[df['username'] == 'microtony'].index)

# df

df.loc[:, 'rating'] *= 10

df.loc[:, 'rating'] = df['rating'].apply(lambda x: round(x))

# df.loc[:, 'rating']

def val(ele):
    if (ord(ele) < 47):
        return ord(ele) - 45
    if (ord(ele) < 58):
        return ord(ele) - 46
    if (ord(ele) < 91):
        return ord(ele) - 53
    if (ord(ele) == 95):
        return 38
    return ord(ele) - 58


def hash_user(username):
    username = username[::-1]
    # print ('username: ', username)
    ans1 = ans2 = 0; k = 1
    for i in username:
        x = val(i) * k
        ans1 += x
        ans2 += x
        # print('ans: ', ans)
        k *= 65
        ans1 %= (1e9 + 7) 
        ans2 %= (2760727302517)
    ans = ans2 + ans1
    return ans

def de_hash(hash_val):
    contest = hash_val // 80
    offset = hash_val % 80
    index = chr(offset // 3 + 65)
    if offset % 3 == 1:
        index += '1'
    elif offset % 3 == 2:
        index += '2'
    return contest, index

# df.loc[:, 'user_id'] = df.loc[:, 'username'].apply(lambda x : hash_user(x))

# df['user_id'] = df['user_id'].astype(np.int64)

# df

# df.columns

df = df.drop(['OK', 'WRONG_ANSWER', 'TIME_LIMIT_EXCEEDED', 'RUNTIME_ERROR', 'IDLENESS_LIMIT_EXCEEDED', 'MEMORY_LIMIT_EXCEEDED'], axis= 1)

df.to_csv('validation_data/rating_nnk.csv')

solved = dict(zip(df['ID'], df['rating']))

li = recommendations(10, solved)

for i in li:
    print(de_hash(i))
