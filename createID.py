# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:11:36 2018

@author: joe
"""
import numpy as np
import random
class CreateID():    
    def __init__(self,location,gender,L):
        self.location=location
        self.gender=gender
        self.L=L
    def process(self):
        all=1
        try:
            if self.location=='台北市':
                self.L[0]=1
                self.L[1]=0
            elif self.location=='新北市':
                self.L[0]=1
                self.L[1]=5
            self.L[1]*=5
            
            if self.gender=='男':
                self.L[2]=8
            else:
                self.L[2]=2*8

        except TypeError as err:
            print(err)
            
        while(all%10!=0):
            all=0
            for c in range(3,11):
                if c==10:
                    x=1
                else:
                    x=10-c
                self.L[c]=random.randint(1,9)*x

            for sum in range(0,11):
                all+=self.L[sum]
        
        for i in range(2,9):
            self.L[i]/=(10-i)
            
        if self.location=='新北市':
            first='F'
        print(first)
        
        for c in range(2,11):
            print(self.L[c])
        

while True:
    location=input('請輸入地址')
    gender=input('請輸入性別')
    CreateID(location,gender,np.zeros(11,dtype=np.int)).process()
      
