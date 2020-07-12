import pandas as pd
import urllib.request
import matplotlib.pyplot as plt

import re
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt", filename="ratings_train.txt")
# urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt", filename="ratings_test.txt")

train_data = pd.read_table('ratings_train.txt')
test_data = pd.read_table('ratings_test.txt')

train_data.drop_duplicates(subset=['document'], inplace=True)

train_data = train_data.dropna(how='any')

# 정규표현식을 이용하여 정상적인 한글과 공백을 제외한 모든 글자들을 삭제
train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎ ㅏ-ㅣ 가-힣 ]","")

## 한글이 없는 리뷰 였다면 null이 되기때문에 확인해야함
train_data['document'].replace('', np.nan, inplace=True)

train_data = train_data.dropna(how='any')

# train_data = train_data[:140000]

test_data.drop_duplicates(subset=['document'], inplace=True)
test_data['document'] = test_data['document'].str.replace("[^ㄱ-ㅎ ㅏ-ㅣ 가-힣 ]","")
test_data['document'].replace('', np.nan, inplace=True)
test_data = test_data.dropna(how='any')

#### Tokenize use konlpy
stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']


### ________________________-------------------------------______________________-----------------------_________________________
okt = Okt()
x_train = []

for idx, sentence in enumerate(train_data['document']):
    temp_x = []
    temp_x = okt.morphs(sentence, stem=True) # Tokenize
    temp_x = [word for word in temp_x if not word in stopwords] # 불용어 제거
    x_train.append(temp_x)
    print(idx,'train 진행중')

# print(x_train[-1])
# print(len(x_train))

x_pred = []
for idx, sentence in enumerate(test_data['document']):
    temp_x = []
    temp_x = okt.morphs(sentence, stem=True)
    temp_x = [word for word in temp_x if not word in stopwords]
    x_pred.append(temp_x)
    print(idx,'test 진행중')


tokenize = Tokenizer()
tokenize.fit_on_texts(x_train)

# print(tokenize.word_index)

# 단어의 등장 빈도수를 확인하고 등장 수가 적은 단어들은 자연어 처리에 영향이 없을듯 하여 제거해야한다.
threshold = 3 
total_cnt = len(tokenize.word_index) # 총 단어의 수
rare_cnt = 0 # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
total_freq = 0 # 훈련 데이터의 전체 단어 빈도수 총 합
rare_freq = 0 # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총합

# 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
for key,value in tokenize.word_counts.items():
    total_freq += value # ??

    # 단어의 등장 빈도수가 threshold보다 작으면
    if(value < threshold):
        rare_cnt += 1
        rare_freq += value

vocab_size = total_cnt - rare_cnt + 2 # 단어 집합의 크기
print(vocab_size) # 19417

tokenizer = Tokenizer(vocab_size, oov_token='OOV')
tokenizer.fit_on_texts(x_train)
x_train = tokenizer.texts_to_sequences(x_train)
x_pred = tokenizer.texts_to_sequences(x_pred)

print(x_train[:3])

y_train = np.array(train_data['label'])
y_test = np.array(test_data['label'])

# 빈 샘플 제거
drop_idx = [idx for idx, sentence in enumerate(x_train) if len(sentence) < 1]

x_train = np.delete(x_train, drop_idx, axis=0)
y_train = np.delete(y_train, drop_idx, axis=0)

print(len(x_train))
print(len(y_train))

x_train = pad_sequences(x_train, maxlen=30)
x_pred = pad_sequences(x_pred, maxlen=30)

np.save('./data/naver_review_x_train.npy',arr=x_train)
np.save('./data/naver_review_y_train.npy',arr=y_train)
np.save('./data/naver_review_x_pred.npy',arr=x_pred)