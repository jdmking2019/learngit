from keras.models import Sequential
from keras.layers import Dense
import keras
import numpy as np
model = Sequential()
model.add(Dense(units=64, activation="relu",input_dim=100))
model.add(Dense(units=1, activation="softmax",))
model.compile(loss="categorical_crossentropy",
              optimizer="sgd",
              metrics=["accuracy"])
model.compile(loss=keras.losses.binary_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01,momentum=0.9,nesterov=True))
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))
model.fit(data,labels, epochs=10, batch_size=32)


