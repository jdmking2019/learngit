from keras.layers import Dense,Input
from keras.models import Model
import numpy as np

data = np.random.random((784,784))
labels = np.random.randint(2, size=(784, 10))
inputs = Input(shape=(784,))

x = Dense(64,activation="relu")(inputs)
x = Dense(64,activation="relu")(x)
predictions = Dense(10,activation="softmax")(x)

model = Model(inputs=inputs,outputs=predictions)
model.compile(optimizer="rmsprop",
              loss="categorical_crossentropy",
              metrics=["accuracy"])
model.fit(data,labels)

x = Input(shape=(784,))
y = model(x)