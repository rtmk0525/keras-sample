import numpy as np
from keras.callbacks import TensorBoard
from keras.layers import Dense
from keras.models import Sequential

# データの生成
np.random.seed(0)
X = np.random.rand(1000, 5)
y = np.random.randint(2, size=(1000, 1))

# モデルの構築
model = Sequential()
model.add(Dense(10, input_dim=5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# TensorBoardの設定
tensorboard = TensorBoard(log_dir='./logs', histogram_freq=1, write_graph=True, write_images=False)

# モデルのトレーニング
model.fit(X, y, epochs=10, batch_size=32, callbacks=[tensorboard])
