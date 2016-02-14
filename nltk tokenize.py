
# coding: utf-8

# In[12]:

import nltk


# In[4]:

# Now let us create a feature vectors from a text. We need to tokenize a text using 
# word_tokenize and sent_tokenize
from nltk.tokenize import word_tokenize, sent_tokenize


# In[20]:

text="Marry has a little lamb. Her fleece was white as snow"
sents=sent_tokenize(text)
print(sents)


# In[15]:

# sent_tokenize will divide the text into different token of sentences 
# on the other hand, word_tokenize divide the text into tokens of words
words=word_tokenize(text)


# In[10]:

print(words)


# In[13]:

# if we want to create array of tokens for each sentences, we can put 
# the word_tokenize for each sentence in one line
words=[word_tokenize(sent) for sent in sents]
print(words)


# In[21]:

# now let's filter out stopwords like 'a' 'was' 'as', etc
# we need to first import stopwords and punctuation
from nltk.corpus import stopwords
from string import punctuation

# now create a set of customStopWords
customStopWords=set(stopwords.words("english")+list(punctuation))


# In[22]:

wordsWOStopWords=[word for word in words if word not in customStopWords]
print(wordsWOStopWords)


# In[24]:


# Now example with stemming
text2="Mary closed on closing night when she's in the mood to close"
# 'close' appears in many forms. we can stem it to its root
# NLTK has many stemmer with different algorithm/rules. Note: stemming is also called lemmatization

from nltk.stem.lancaster import LancasterStemmer


# In[27]:

st=LancasterStemmer()
stemmedWords=[st.stem(word) for word in word_tokenize(text2)]
print(stemmedWords)


# In[28]:

# to get part of speech, we can use pos_tag
nltk.pos_tag(word_tokenize(text2))


# In[ ]:



