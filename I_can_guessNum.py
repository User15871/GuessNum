# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:14:10 2019

@author: 22606
"""


import numpy as np

def choose(scores):    
    max_scores_pos = [np.random.choice(np.where(x == np.max(x))[0]) for x in scores]
    accept_x = {0:[True]*10, 1:[True]*10, 2:[True]*10, 3:[True]*10, 4:[True]*10}
    while len(set(max_scores_pos)) != 4:
        for x in set(max_scores_pos):
            if sum(max_scores_pos == x) != 1:
                x_pos = (max_scores_pos==x)
                x_win_pos = np.where(x_pos)[0][np.argmax(scores[x_pos, x])]
                x_pos[x_win_pos] = False
                for i in np.where(x_pos)[0]:
                    accept_x[i][x] = False
                    choice = np.random.choice(np.where(scores[i, accept_x[i]] == np.max(scores[i, accept_x[i]]))[0])
                    max_scores_pos[i] = np.where(accept_x[i])[0][choice]
    return max_scores_pos
                    
def give_hint(ques, ans):
    A=0
    B=0
    for i, x in enumerate(ques):
        for j, y in enumerate(ans):    
            if x==y:
                if i==j:
                    A+=1
                else:
                    B+=1    
    return {'A':A, 'B': B}


record = []
for run in range(10000):
    ques = [1, 2, 3, 4]
    Round = 0
    scores = np.zeros((4,10))
    ans = choose(scores)
    ans_storage=[]
    miss_ans_storage=[]
    hint_storage={}
    while ques != ans:
        i = 0
        ans = choose(scores)
        while i < len(ans_storage):
            while ans in miss_ans_storage:
                for j, x in enumerate(ans):
                    scores[j, x] -= 1
                ans = choose(scores)
                
            for miss_ans in ans_storage:
                if give_hint(ans, miss_ans) != hint_storage[i]:
                    for j, x in enumerate(ans):
                        scores[j, x] -= 1 
                    miss_ans_storage.append(ans)
                    ans = choose(scores)
                    i = 0
                    break
                else:
                    i += 1
        hint = give_hint(ques, ans)
        miss = 4 - hint['A'] - hint['B']
        scores += miss
        for i, x in enumerate(ans):
            scores[i, x] -= (Round + 1) ** hint['B']
            scores[:, x] += (Round + 1) ** hint['A'] + (Round + 1) ** hint['B'] -  (Round + 1) ** miss
        ans_storage.append(ans)
        miss_ans_storage.append(ans)
        hint_storage[Round] = hint
        Round += 1
    print(Round)
    record.append(Round)
    
record = np.array(record)
print(record.mean())
print(record.std())