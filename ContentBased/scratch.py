from MovieLens import ProblemLens

ml = ProblemLens()

tags = ml.gettags()
for i in tags:
    print(i, tags[i])
# x = len(tags[80])

# for i in tags.keys():
#     if (len(tags[i]) != x):
#         print(i)