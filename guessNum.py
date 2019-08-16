# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:57:58 2019

@author: 22606
"""

import random
def guessNum():
    begin=True
    while begin:
        x=random.sample(list(range(1,10)), 4)
        while True:    
            A=0
            B=0
            print('Guess now!')
            while True:
                y=input()
                
                if len(y)!=4 or len(set([i for i in y]))!=4:
                    print('Please insert 4 different number in 0-9')
                else:break
            for i in range(4):
                for j in range(4):    
                    if x[i]==int(y[j]):
                        if i==j:
                            A+=1
                        else:
                            B+=1
                        break
            print('\n'+str(A)+'A'+str(B)+'B')
            if A==4:
                print('Congratulation!')
                print('Wanna try again?(Y/N)')
                while True:
                    y=input()
                    if y=='N':
                        begin=False
                        break
                    elif y!='Y':
                        break
                    print('Please insert T or N')
                break
                
guessNum()
