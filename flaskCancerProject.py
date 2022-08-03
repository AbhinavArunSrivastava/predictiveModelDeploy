#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 


dataset = pd.read_csv('data.csv')

dataset['diagnosis'] = dataset['diagnosis'].map({'B': 0, 'M': 1}).astype(int)
X = dataset.iloc[:,2:32].values
Y = dataset.iloc[:,1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)



from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train) 
X_test = sc.transform(X_test)


# In[2]:


from sklearn.svm import SVC

models = SVC(gamma='auto')
models.fit(X_train, y_train)
y_pred = models.predict(X_test)


# In[3]:


np.array(Y).shape


# In[4]:


import pickle
pickle.dump(models,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


# In[ ]:




