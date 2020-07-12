from keras.layers import Embedding, Dense, LSTM
from keras.models import Sequential
from keras.models import load_model
from keras.callbacks import EarlyStopping, ModelCheckpoint

import numpy as np

vocab_size = 19417

x_train = np.load('./data/naver_review_x_train.npy')
y_train = np.load('./data/naver_review_y_train.npy')
x_test = np.load('./data/naver_review_x_test.npy')
y_test = np.load('./data/naver_review_y_test.npy')

# model 
model = Sequential()
model.add(Embedding(vocab_size,100))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))

# compile, fit
els = EarlyStopping(monitor='val_loss', mode='min', verbose=1,patience=4)
mc = ModelCheckpoint('./savemodel/best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only='True')

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(x_train, y_train, epochs=15, callbacks=[els, mc], batch_size=60, validation_split=0.2)

# load, evaluate
loaded_model = load_model('./savemodel/best_model.h5')

res = loaded_model.evaluate(x_test, y_test)[1]
print('acc : ',res)