from surprise.model_selection import train_test_split
from problem_lens import ProblemLens
from surprise import KNNBasic
import pandas as pd

ml = ProblemLens()
data, size = ml.loadProblemLens()

problems = ml.gettags()


size = 1e-10
trainSet, testSet = train_test_split(data, test_size=size, shuffle=False)
raw_to_innerid = {} # A dict to store mapping from raw id to inner_iid

for i in problems.keys():
    try :
        raw_to_innerid[i] = trainSet.to_inner_iid(i)
    except ValueError:
        pass

df = pd.DataFrame(list(raw_to_innerid.items()))
df.to_csv('raw_to_inner.csv', index = False) # Storing it in csv format

sim_options = {
                'name': 'pearson',
                'user_based': False
               }
# setting the parameters for model training and training it accordingly
model = KNNBasic(sim_options=sim_options)
model.fit(trainSet)
simsMatrix = model.compute_similarities()
# Storing the trained data to csv file
df = pd.DataFrame(simsMatrix)
df.to_csv('trained_data.csv', index=False)
