#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[11]:


this = pd.read_csv('./data/train.csv')


# In[12]:


f, ax = plt.subplots(1, 2, figsize=(18, 8))
series = this['Survived'].value_counts()
series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('0.Death toll vs 1.Survivors')
ax[0].set_ylabel('')
ax[1].set_title('0.Death toll vs 1.Survivors')
sns.countplot('Survived', data=this, ax=ax[1])
f.suptitle('Percentage between Death and Survivor Graph')


# In[14]:


this['Survival Results'] = this['Survived'].replace(0, 'Death toll').replace(1, 'Survivors')
this['Seat Class'] = this['Pclass'].replace(1, 'First class').replace(2, 'Second class').replace(3, 'Third class')
sns.countplot(data=this, x='Seat Class', hue='Survival Results')


# In[15]:


this['Survival Results'] = this['Survived'].replace(0, 'Death toll').replace(1, 'Survivors')
this['port of embarkation'] = this['Embarked'].replace('C', 'Shellberg').replace('S', 'South').replace('Q', 'Queenstown')
sns.countplot(data=this, x='port of embarkation', hue='Survival Results')


# In[16]:


f, ax = plt.subplots(1, 2, figsize=(18, 8))
male_series = this['Survived'][this['Sex'] == 'male'].value_counts()
female_series = this['Survived'][this['Sex'] == 'female'].value_counts()
male_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
female_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
ax[0].set_title('survival rate of men 0.Death toll vs 1.Survivors')
ax[0].set_ylabel('')
ax[1].set_title('survival rate of women 0.Death toll vs 1.Survivors')
f.suptitle('Gender-specific survival rates')


# In[17]:


this['port of embarkation'] = this['Embarked'].replace('C', 'Shellberg').replace('S', 'South').replace('Q', 'Queenstown')
this['Seat Class'] = this['Pclass'].replace(1, 'First class').replace(2, 'Second class').replace(3, 'Third class')
sns.countplot(data=this, x='Seat Class', hue='port of embarkation')

