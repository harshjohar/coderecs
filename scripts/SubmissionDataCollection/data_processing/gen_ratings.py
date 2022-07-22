import numpy as np
import pandas as pd

df = pd.read_csv('/Users/harshjohar/Documents/WebProjects/coding-platform-deep-learning/scripts/SubmissionDataCollection/submissions.csv')


# df.drop(['COMPILATION_ERROR', 'SKIPPED', 'TESTING','PRESENTATION_ERROR','FAILED','CRASHED','CHALLENGED','REJECTED','PARTIAL','SECURITY_VIOLATED','INPUT_PREPARATION_CRASHED','SUBMITTED'], axis = 1, inplace=True)
# df.drop(df.index[df['ID'] >= 144000], inplace= True)
# df.to_csv('/Users/harshjohar/Documents/WebProjects/coding-platform-deep-learning/scripts/SubmissionDataCollection/submissions.csv', index= False)
# df = pd.read_csv('/Users/harshjohar/Documents/WebProjects/coding-platform-deep-learning/scripts/SubmissionDataCollection/submissions.csv')
users = df['username'].unique()
    
def rating(OK, WA, RE, TLE, avg):
    ans = 0
    ans = abs(OK * avg - WA - 0.6 * TLE - 0.8 * RE)
    return ans

"""### Finding average number of Wrong attempts, TLE submissions, etc"""

# cnt = 0 
# idx = 0
# for i in users:
#     db = df[df['username'] == i]
#     m1 = np.mean(db['WRONG_ANSWER'] + db['MEMORY_LIMIT_EXCEEDED'])
#     m2 = np.mean(db['TIME_LIMIT_EXCEEDED'] + db['IDLENESS_LIMIT_EXCEEDED'])
#     m3 = np.mean(db['RUNTIME_ERROR'])
#     idx += 1
#     m = m1 + 0.6 * m2 + 0.8 * m3
#     for j, row in db.iterrows():
#         db.at[j, 'rating'] = rating(db.at[j, 'OK'], db.at[j, 'WRONG_ANSWER'] + db.at[j, 'MEMORY_LIMIT_EXCEEDED'], db.at[j, 'RUNTIME_ERROR'], db.at[j, 'TIME_LIMIT_EXCEEDED'] + db.at[j, 'IDLENESS_LIMIT_EXCEEDED'], m)
#     mean_, sd = np.mean(db['rating']), np.std(db['rating'])
#     db.loc[:, 'rating'] = (db['rating'] - mean_) / sd
#     # df[df['username'] == i]['rating'] = db['rating']
#     for j, row in db.iterrows():
#       df.at[j, 'rating'] = db.at[j, 'rating']
#     print(idx, f'{i} has been processed')
#     # cnt += db.shape[0]
# print(m1, m2, m3)
# dx = (df[df['username'] == 'microtony'].index)
m = np.mean(df['WRONG_ANSWER'] + df['MEMORY_LIMIT_EXCEEDED'] + 0.6 * df['TIME_LIMIT_EXCEEDED'] + 0.6 * df['IDLENESS_LIMIT_EXCEEDED'] + 0.8 * df['RUNTIME_ERROR'])
for i in range(df.shape[0]):
    if (i % 100000 == 0):
        print(i)
    df.at[i, 'rating'] = rating(df.at[i, 'OK'], df.at[i, 'WRONG_ANSWER'] + df.at[i, 'MEMORY_LIMIT_EXCEEDED'], df.at[i, 'RUNTIME_ERROR'], df.at[i, 'TIME_LIMIT_EXCEEDED'] + df.at[i, 'IDLENESS_LIMIT_EXCEEDED'], m)
mean_, sd = np.mean(df.loc[:, 'rating']), np.std(df.loc[:, 'rating'])
df.loc[:, 'rating'] = abs(df['rating'] - mean_) / sd
df.loc[:, 'rating'] = df['rating'].apply(lambda x: abs(x) if (x < 1 and x > -1) else 1)

# df

df.loc[:, 'rating'] *= 5

# df.loc[:, 'rating'] = df['rating'].apply(lambda x: round(x))

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

df.to_csv('/Users/harshjohar/Documents/WebProjects/coding-platform-deep-learning/ContentBased/ratings.csv', index= False)
