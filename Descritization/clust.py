#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math



def normalize(c):
    maxi = c.max()
    mini = c.min()
    for i in range(len(c)):
        c[i] = (c[i]-mini)/float(maxi-mini)


def eucl_dist(a,b):
    dista = 0
    for i in range(4):
        dista += (a[i]-b[i])**2
    return math.sqrt(dista)



# REMOVING SUBSETS
def sixthstep(aa):
    l = len(aa)
    for i in range(l):
        for j in range(l):
            if(i!=j and set(aa[j]).issubset(set(aa[i]))):
                aa[j]=[]
    # REMOVING EMPTY SUBSETS
    new_cls = []
    for i in range(l):
        if(len(aa[i])!=0):
            new_cls.append(aa[i])
    return new_cls



def seventh(a):
    length = len(a) #Dekhna hai idhar
    sim = np.zeros((length,length))
    for i in range(length):
        for j in range(length):
            sim[i][j] = len(set(a[i]).intersection(set(a[j]))) / float(len(set(a[i]).union(set(a[j]))))
    return sim


def eighth(sim):
    l = len(sim)
    k = 0
    m = 0
    maxi=-1
    for i in range(l):
        for j in range(l):
            if(i!=j and maxi==-1):
                maxi = sim[i][j] 
            elif(sim[i][j]>=maxi and i!=j):
                k = i
                m = j
    return k,m

def EEDD(a):
    return a[0]+a[1]+a[2]+a[3]

def nikl(i,a,data_again,centroid,pp):
    total_dist=0
    dist = 0
    for m in a:
        total_dist += math.sqrt((data_again[i][0]-centroid[m][0])**2 + (data_again[i][1]-centroid[m][1])**2 + (data_again[i][2]-centroid[m][2])**2 + (data_again[i][3]-centroid[m][3])**2)  
    for m in a:
        dist = math.sqrt((data_again[i][0]-centroid[m][0])**2 + (data_again[i][1]-centroid[m][1])**2 + (data_again[i][2]-centroid[m][2])**2 + (data_again[i][3]-centroid[m][3])**2)  
        pp[i][m] = (dist/total_dist)
