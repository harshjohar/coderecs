import csv
import re

from surprise import Dataset
from surprise import Reader

from collections import defaultdict
import pandas as pd


class ProblemLens:

    ratingsPath = '/Users/harshjohar/Documents/WebProjects/coding-platform-deep-learning/ContentBased/ratings.csv'
    problemsPath = '/Users/harshjohar/Documents/WebProjects/coding-platform-deep-learning/scripts/ProblemDataCollection/problems.csv'

    def loadProblemLens(self):

        score_dataset = 0
        
        df = pd.read_csv(self.ratingsPath).loc[:, ['username', 'ID', 'rating']]
        
        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
        score_dataset = Dataset.load_from_df(df= df, reader=reader)
        
        index = df.index
        number_of_rows = len(index)
        return score_dataset, number_of_rows

    def gettags(self):
        tags = {}
        tagIDs = {}
        maxtagID = 0
        with open(self.problemsPath, newline='', encoding='ISO-8859-1') as csvfile:
            problemReader = csv.reader(csvfile)
            next(problemReader)  #Skip header line
            for row in problemReader:
                problemID = int(row[0])
                tagList = row[2].split('|')
                tagIDList = []
                for tag in tagList:
                    if tag in tagIDs:
                        tagID = tagIDs[tag]
                    else:
                        tagID = maxtagID
                        tagIDs[tag] = tagID
                        maxtagID += 1
                    tagIDList.append(tagID)
                tags[problemID] = tagIDList
        # print(tagIDs)
        for (problemID, tagIDList) in tags.items():
            bitfield = [0] * maxtagID
            for tagID in tagIDList:
                bitfield[tagID] = 1
            tags[problemID] = bitfield            
        
        return tags

    def get_problem_ratings(self):
        p = re.compile(r"(?:\((\d{4})\))?\s*$")
        ratings = defaultdict(int)
        with open(self.problemsPath, newline='', encoding='ISO-8859-1') as csvfile:
            problemReader = csv.reader(csvfile)
            next(problemReader)
            for row in problemReader:
                problemID = int(row[0])
                rating = row[1]
                if rating:
                    ratings[problemID] = int(rating)
        return ratings

    def getUserRatings(self, user):
        userRatings = []
        hitUser = False
        with open(self.ratingsPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                userID = int(row[0])
                if (user == userID):
                    movieID = int(row[1])
                    rating = float(row[2])
                    userRatings.append((movieID, rating))
                    hitUser = True
                if (hitUser and (user != userID)):
                    break

        return userRatings

    def getPopularityRanks(self):
        ratings = defaultdict(int)
        rankings = defaultdict(int)
        with open(self.ratingsPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                movieID = int(row[1])
                ratings[movieID] += 1
        rank = 1
        for movieID, ratingCount in sorted(ratings.items(), key=lambda x: x[1], reverse=True):
            rankings[movieID] = rank
            rank += 1
        return rankings
    
    