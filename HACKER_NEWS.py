#!/usr/bin/env python
# coding: utf-8

# In[7]:


pip install beautifulsoup4


# In[8]:


pip install requests


# In[9]:


import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')
links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')
m_links = links + links2
m_subtext = subtext + subtext2


# In[10]:


def sorted_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'])


# In[11]:


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title' : title, 'link' : href, 'votes' : points})
    return sorted_stories_by_votes(hn)


# In[12]:


pprint.pprint(create_custom_hn(m_links,m_subtext))


# In[ ]:




