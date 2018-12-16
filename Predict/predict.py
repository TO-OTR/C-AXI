# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

data=pd.read_csv('weibo_status.csv',sep=',')
word=pd.read_csv('word2.txt',sep=' ')

users = {}
for index, row in data.iterrows():
    if index > 100000:
        break
    print(index)
    for idx_w, w in word.iterrows():
        #print(w[0])
        #print(row.status)
        if w[0] in row.status:
            if not (row.weibo_user_id in users.keys()):
                users[row.weibo_user_id] = [0]*(len(word)+1)
            users[row.weibo_user_id][idx_w] += 1
            users[row.weibo_user_id][-1] += 1
            
df_users = pd.DataFrame.from_dict(users, orient='index')
df_users.to_csv('df_users.csv')

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=10, random_state=0).fit(df_users)
kmeans.predict([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,
 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
 0., 0., 0., 1., 0., 0., 0., 0., 0., 2.]])
    
kmeans.predict([[0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,
 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
 0., 0., 0., 1., 0., 0., 0., 0., 0., 2.]])