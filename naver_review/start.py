import pandas as pd
import urllib.request
import matplotlib.pyplot as plt

import re
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt", filename="ratings_train.txt")
urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt", filename="ratings_test.txt")

train_data = pd.read_table('ratings_train.txt')
test_data = pd.read_table('ratings_test.txt')

print('훈련용 리뷰 개수 : ', len(train_data)) # 15000

print(train_data[:5])

print(train_data['document'].nunique()) # 146182 // 중복문장이 146182 만큼 존재한다

print(train_data['label'].nunique()) # 2 // 중복 이 2개 있다 이유는 0과 1로

train_data.drop_duplicates(subset=['document'], inplace=True)

print('총 샘플의 수 : ', len(train_data)) # 총 샘플의 수 :  146183

# train_data['label'].value_counts().plot(kind='bar') # 긍정과 부정의 샘플의 갯수가 비슷함
# plt.show()

#### 결측치 확인
print(train_data.isnull().values.any()) # True 결측치 존재

print(train_data.isnull().sum()) # 어떤 열에 결측치가 존재하는지 확인 document열에서 확인됨

print(train_data.loc[train_data.document.isnull()]) # 몇 행에 결측치가 존재하는지 확인 25857번째 행에 존재

train_data = train_data.dropna(how='any')
print(train_data.isnull().values.any()) # False

print(len(train_data)) # 146182

# 정규표현식을 이용하여 정상적인 한글과 공백을 제외한 모든 글자들을 삭제
train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎ ㅏ-ㅣ 가-힣 ]","")

print(train_data[:5])

## 한글이 없는 리뷰 였다면 null이 되기때문에 확인해야함
train_data['document'].replace('', np.nan, inplace=True)
print(train_data.isnull().sum()) # 391개 발견

print(train_data.loc[train_data.document.isnull()][:5]) # null값이 있는 5행 출력
train_data = train_data.dropna(how='any')
print(len(train_data))
print("최종 null 확인 ",train_data.isnull().sum()) # 


# train_data['label'].value_counts().plot(kind='bar') # 긍정과 부정의 샘플의 갯수가 비슷함
# plt.show()
# 여기서 데이터의 개수의 차이가 생김 200~300개 정도 차이남

test_data.drop_duplicates(subset=['document'], inplace=True)
test_data['document'] = test_data['document'].str.replace("[^ㄱ-ㅎ ㅏ-ㅣ 가-힣 ]","")
test_data['document'].replace('', np.nan, inplace=True)
test_data = test_data.dropna(how='any')
print("최종 null 확인 ",test_data.isnull().sum()) # 


#### Tokenize use konlpy
stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']

okt = Okt()
okt.morphs('와 이런 것도 영화라고 차라리 뮤직비디오를 만드는 게 나을 뻔', stem=True)

x_train = []
for sentence in train_data['document']:
    temp_x = []
    temp_x = okt.morphs(sentence, stem=True) # Tokenize
    temp_x = [word for word in temp_x if not word in stopwords] # 불용어 제거
    x_train.append(temp_x)

print(x_train[:3])