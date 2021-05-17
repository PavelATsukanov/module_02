#!/usr/bin/env python
# coding: utf-8

# In[73]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import itertools


# In[28]:


data = pd.read_csv('C:\Python\Millinaire\movie_bd_v5.csv')
data.sample(10)
len(data)


# In[23]:


data.describe()


# # Предобработка

# In[39]:


# answers = {} # создадим словарь для ответов

# тут другие ваши предобработки колонок например:

#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...
answers = {}


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[ ]:


# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = '...'
# если ответили верно, можете добавить комментарий со значком "+"


# In[6]:


s=data.loc[data['budget'].idxmax()]
display(s)


# In[41]:


answers['1'] = 'irates of the Caribbean: On Stranger Tides'


# ВАРИАНТ 2

# In[ ]:


# можно добавлять разные варианты решения


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[8]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = '...'


# In[9]:


d=data.loc[data['runtime'].idxmax()]
display(d)


# In[42]:


answers['2'] = 'Gods and Generals'


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[ ]:





# In[128]:


d=data.loc[data['runtime'].idxmin()]
display(d)


# In[43]:


answers['3'] = 'Winnie the Pooh'


# # 4. Какова средняя длительность фильмов?
# 

# In[10]:


d=data['runtime'].mean()
display(d)


# In[44]:


answers['4'] = '109.6'


# # 5. Каково медианное значение длительности фильмов? 

# In[12]:


d=data['runtime'].median()
display(d)


# In[45]:


answers['5'] = '107.0'


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[13]:


data['profit'] = data['revenue'] - data['budget']
data1=data.loc[data['profit'].idxmax()]
display(data1)


# In[46]:


answers['6'] = 'Avatar'


# # 7. Какой фильм самый убыточный? 

# In[14]:


data['profit'] = data['revenue'] - data['budget']
data1=data.loc[data['profit'].idxmin()]
display(data1)


# In[47]:


answers['7'] = 'The Lone Ranger'


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[15]:


data_more_nill = data[data['profit'] > 0]
display(data_more_nill)
len(data_more_nill)


# In[48]:


answers['8'] = '1478'


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[11]:


data_2008 =data[data['release_year'] == 2008]
data_2008max=data_2008.loc[data_2008['profit'].idxmax()]
display(data_2008max)


# In[49]:


answers['9'] = 'The Dark Knight'


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[12]:


data_2012_14 =data[data['release_year'].isin(['2012','2013','2014'])]
data_2012_14min=data_2012_14 .loc[data_2012_14 ['profit'].idxmin()]
display(data_2012_14min)


# In[50]:


answers['10'] = 'The Lone Ranger'


# # 11. Какого жанра фильмов больше всего?

# In[ ]:


# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале


# In[13]:


data.genres.str.split('|').explode('genres').value_counts().idxmax()


# ВАРИАНТ 2

# In[51]:


answers['11'] = 'Drama'


# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[13]:


data_more_nill['genres'].str.split('|').explode().value_counts().idxmax()


# In[52]:


answers['12'] = 'Drama'


# # 13. У какого режиссера самые большие суммарные кассовые сборы?

# In[14]:


df = data.groupby(['director'])['revenue'].sum().sort_values(ascending=False)
print(df)


# In[53]:


answers['13'] = 'Peter Jackson'


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[15]:


data[data.genres.str.contains('Action')].director.str.split('|').explode('director').mode()[0]


# In[54]:


answers['14'] = 'Robert Rodriguez'


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[16]:


data_2012 =data[data['release_year'] == 2012]
data_2012max=data_2012.loc[data_2012['revenue'].idxmax()]
display(data_2012max['cast'])


# In[55]:


answers['15'] = 'Chris Evans'


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[17]:


data[data.budget>data.budget.mean()].cast.str.split('|').explode('cast').value_counts().idxmax()


# In[56]:


answers['16'] = 'Matt Damon'


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[18]:


data[data.cast.str.contains('Nicolas Cage')]['genres'].str.split('|').explode().value_counts().idxmax()


# In[57]:


answers['17'] = 'Action'


# # 18. Самый убыточный фильм от Paramount Pictures

# In[62]:


data_less_nill = data[data['profit'] < 0]

display(data_less_nill)


# In[6]:


data_less_nill[data_less_nill.production_companies.str.contains('Paramount Pictures')].sort_values(by=['profit'], ascending=True)   


# In[58]:


answers['18'] = 'K-19: The Widowmaker'


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[17]:


data = pd.read_csv('C:\Python\Millinaire\movie_bd_v5.csv')
data.sample(10)


# In[38]:


data_max_cash=data.groupby('release_year')['revenue'].sum().sort_values(ascending=False).idxmax()
display(data_max_cash)


# In[59]:


answers['19'] = '2015'


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[19]:


data_WB=data_more_nill[data_more_nill.production_companies.str.contains('Warner')].sort_values(by=['release_year'],ascending=True) 
display(data_WB)


# In[61]:


max_cash_WB = data_WB.groupby('release_year')['profit'].sum().sort_values(ascending=False).idxmax()
display(max_cash_WB)


# In[62]:


answers['20'] = '2014'


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[21]:


data = pd.read_csv('C:\Python\Millinaire\movie_bd_v5.csv')
data.sample(10)


# In[16]:


pd.DatetimeIndex(data['release_date']).month.value_counts().idxmax()


# In[63]:


answers['21'] = '9'


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[17]:


pd.DatetimeIndex(data['release_date']).month.value_counts()


# In[64]:


answers['22'] = '450'


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[20]:


mov_wint = data.copy()
mov_wint['release_date'] = pd.to_datetime(mov_wint['release_date'])
mov_wint[mov_wint.release_date.dt.month.isin([1, 2, 12,])].director.str.split('|').explode('director').value_counts()


# In[65]:


answers['23'] = 'Peter Jackson'


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[39]:


data['title_length'] = data['original_title'].map(lambda x: len(x))
companies = data['production_companies'].str.split('|').explode().unique()
for comp in companies:
    sum_gen[comp] = data['title_length'][data['production_companies'].map(lambda x: True if comp in x else False)].mean()
sum_gen.sort_values(ascending=False).head()


# In[66]:


answers['24'] = 'Four By Two Productions'


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[9]:


data_max_words = data.copy()
data_max_words['overview_length'] = data_max_words['overview'].str.split(' ').str.len()
data_max_words.production_companies = data_max_words.production_companies.str.split('|')
data_max_words = data_max_words.explode('production_companies')
data_max_words.groupby('production_companies')['overview_length'].mean().sort_values(ascending=False)


# In[67]:


answers['25'] = 'Midnight Picture Show'


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[34]:


data = pd.read_csv('C:\Python\Millinaire\movie_bd_v5.csv')
df = data['vote_average'].value_counts(bins=100, ascending = False)
border = np.quantile(data.vote_average, 0.99)
data[data.vote_average >= border].sort_values(by='vote_average', ascending=False)['original_title']


# In[68]:


answers['26'] = 'Midnight Picture Show'


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# In[76]:


from collections import Counter


# In[77]:


from itertools import combinations


# In[78]:


data = pd.read_csv('C:\Python\Millinaire\movie_bd_v5.csv')
pairs = Counter()
for i in range(0,len(data)):
    artists = data.cast[i].split('|')
    for j in list(combinations(artists, 2)):
        if j not in pairs:
            pairs[j] = 1
        else:
            pairs[j] += 1
pairs.most_common(5)


# In[79]:


answers['27'] = 'Daniel Radcliffe', 'Rupert Grint'


# ВАРИАНТ 2

# # Submission

# In[ ]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[ ]:


# и убедиться что ни чего не пропустил)
len(answers)


# In[80]:


answers


# In[ ]:




