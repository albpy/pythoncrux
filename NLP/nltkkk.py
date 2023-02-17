import nltk

#nltk.download('stopwords')
from nltk.corpus import stopwords
data=stopwords.words('english')
print(len(data))

#nltk.download('punkt')
sentence="""I AM the hero Of the Universe, But What is called a hero"""
tokens=nltk.word_tokenize(sentence)
#print(tokens)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent="""This is the Start of the legeNd, Stop Filteration is started"""
"""STOP WORDS"""
#Convert to a set
stop_words=set(stopwords.words('english'))
"""TOKENIzATION"""
filter_data=word_tokenize(example_sent)
#print(filter_data)
filter_data1=[w for w in filter_data if not w.lower() in stop_words]
print(filter_data1)

#nltk.download('averaged_perceptron_tagger')

"""pos_tag"""# ==>#Abbreviation
tagged = nltk.pos_tag(tokens)
#print(tagged)


"""n gram"""    #--> How many words to be get tokenised
############********************************************
from nltk.util import ngrams
text1='Earth is the third planet from the sun'
data=ngrams(sequence=nltk.word_tokenize(text1),n=2) #2 Gram tokenisation
#for i in data:
#    print(i)
"""Stemming"""  #using PorterStemmer function
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps=PorterStemmer()
words=['manhatten','Milano','Capi', 'calculator', 'Casio','Married', 'Dies', 'Summoning']
"""for i in  words:
    print(i, ":",ps.stem(i))"""

"""Stemming Using Snowball stemmer"""
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
sb=SnowballStemmer('english')
"""for j in words:
    print(j, ":" , sb.stem(i))"""

"""Lementization"""
#nltk.download('wordnet')
#nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
lem=WordNetLemmatizer()
print("rocks",":", lem.lemmatize('rocks'))
print("removed", ":", lem.lemmatize('removed'))
print("corpora", ":", lem.lemmatize('corpora'))
print("better", ":", lem.lemmatize('better', pos='a')) #pos=a is convert it to adjecentive 


