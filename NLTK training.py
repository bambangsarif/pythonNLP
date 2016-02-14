
# coding: utf-8

# In[2]:

# first import the nltk module
import nltk


# In[3]:

# First we need to download some text to play with. We need to download Corpora and resources 
# to explore natural language. For that, run a one-off command nltk.download() --> it will open
# a new IPy window. Note, we might fail to download a few module. Thus, we may need to select
# or deselect a few corpus/book individually. Once it is done, we will have plenty of book or
# corpus to play with

# now import the book
from nltk.book import *


# In[4]:


# now we have the books are loaded. We can refer to them by their names as an object with the
# type of text.

# concordance will display all occurence of a word in a text along with is context. Let's us start 
# with Moby Dick (text1) and Sense and sensibility (text2) book for word 'monstrous'. These two 
# books have different context use of that word

text1.concordance('monstrous')


# In[5]:

text2.concordance("monstrous")


# In[6]:

# text1 uses monstrous to depic huge scary things. text2 use monstrous as 
# a synonym of very (positive connotation)
# let's see what other words was used in a similar context as monstrous

text2.similar("monstrous")


# In[9]:

# text2 use monstrous for positive emotion. Let's see where the word monstrous 
# and very are used in the same context

text2.common_contexts(["monstrous", "very"])


# In[12]:

# Now let's see the change of usage of certain words by the Presidents over the years.
# we will use matplotlib
text4.dispersion_plot(["citizen","democracy","duties","freedom","America"])


# In[13]:

# it is interesting to see that:
# all presidents like to mention citizen
# earlier presidents like to mention the word duties
# later presidents like to use the word America, freedom and democracy


# In[ ]:



