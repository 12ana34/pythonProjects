score=input('Enter a score: ')
fscore=float(score)
if fscore <0.0 or fscore >1.0:
    print('Score is out of range')
elif fscore >=0.9:
    print('A')
elif fscore >=0.8:
    print('B')
elif fscore>=0.7:
    print('C')
elif fscore >=0.6:
    print('D')
elif fscore <0.6:
    print('F')
