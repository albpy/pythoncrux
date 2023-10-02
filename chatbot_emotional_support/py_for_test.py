import json
import pickle
import nltk
# nltk.download('punkt')
import time
from nltk.stem import WordNetLemmatizer

intents = json.loads(open('dataset\\Mental_health_chat\\intents.json').read())

lemmatizer = WordNetLemmatizer()
# nltk.download('wordnet')
words = []
question_tags = []
context_classifier = []
ignore_letters= ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        context_classifier.append((word_list, intent['tag']))
        if intent['tag'] not in question_tags:
            question_tags.append(intent['tag'])

# for word in words:    
#     print(word)
#     print(lemmatizer.lemmatize(word))
#     # print(word)

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters] # Into lemma form
#Remove Duplicates and sort it
words = sorted(set(words))
question_tags = sorted(set(question_tags))
# print(question_tags)
# print(context_classifier)

# pickle.dump(words, open('words.pkl', 'wb'))
# pickle.dump(question_tags, open('question_tags.pkl', 'wb'))


#bag of words
training = []
output_empty = [0] *len(question_tags)
# print(words)
for context_words in context_classifier:
    
    bag = []
    word_patterns = context_words[0]
    print(word_patterns)
    # word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    lemma_word_patterns = []
    for word in word_patterns:
        lemma_word_patterns.append(lemmatizer.lemmatize(word.lower()))
        # print(word_patterns)
    # print(")***()")
    # time.sleep(5)
    # print(word_patterns)
    for word in words:
        # print(word)
        # bag.append(1) if word in word_patterns else bag.append(0)
        if word.lower() in lemma_word_patterns:
            bag.append(1)
        else:
            bag.append(0)
    



    output_row = list(output_empty)

    output_row[question_tags.index(context_words[1])] = 1
     
    training.append([bag, output_row]) 
    

import random
random.shuffle(training)

import numpy as np

training = np.array(training)
# print(len(training[:,0][1]))
train_x = list(training[:, 0])
train_y = list(training[:, 1])

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import legacy, Adam

from sklearn.preprocessing import StandardScaler
sca = StandardScaler()
# train_x = sca.fit_transform(train_x)
# train_y = sca.fit_transform(train_y)
model = Sequential()
model.add(Dense(120, input_shape=(len(train_x[0]),),activation = 'relu'))
# model.add(Dropout(0.2))
model.add(Dense(200, activation = 'relu'))
# model.add(Dropout(0.2))
model.add(Dense(200, activation = 'relu'))
model.add(Dense(120, activation = 'relu'))

model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = Adam(lr = .01, beta_1=0.9, beta_2 = 0.999)
model.compile(loss='categorical_crossentropy', optimizer = sgd, metrics = ['accuracy'])
hist = model.fit(np.array(train_x), np.array(train_y), epochs = 200, batch_size = 10, verbose = 1)
model.save('emotional_bot.h5', hist)
print('Done')