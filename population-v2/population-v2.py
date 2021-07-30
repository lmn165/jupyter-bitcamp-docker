#!/usr/bin/env python
# coding: utf-8

# In[32]:


import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[33]:


data: [] = list()
home: object = None
away: object = None
result_name: str = ''


# In[34]:


# df = pd.read_csv('./data/202106_202106_연령별인구현황_월간.csv', encoding='UTF-8', thousands = ',', index_col = 0)
# df.to_csv('./data/202106_202106_연령별인구현황_월간_without_comma.csv', sep=',', na_rep='NaN')
data = csv.reader(open('./data/202106_202106_population.csv', 'rt', encoding='UTF-8'))
next(data)
data = list(data)


# In[35]:


# print(data)


# In[36]:


arr = []
[arr.append(int(j)) for i in data if '필동' in i[0] for j in i[3:]]
print([i for i in arr])


# In[40]:


plt.style.use('ggplot')
plt.plot(arr)


# In[41]:


for i in data:
    if '필동' in i[0]:
        home = np.array(i[3:], dtype=int)/int(i[2])


# In[42]:


mn = 1
result = 0
for i in data:
    away = np.array(i[3:], dtype=int) / int(i[2])
    s = np.sum((home - away) ** 2)
    if s < mn and '필동' not in i[0]:
        mn = s
        result_name = i[0]
        result = away
away = result


# In[47]:


plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.title(f'The area with the most similar population structure to the Pil-dong area.')
plt.plot(home, label='Pil-dong')
plt.plot(away, label='similar to Pil-dong')
plt.legend()
plt.show()

