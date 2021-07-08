import tensorflow as tf
import pandas as pd
import numpy as np


df = pd.read_csv("ai4i2020.csv")
X = df[df.columns[3:8]].values
Y = df["Machine failure"].values
Xin = X[:9000]
Yin = Y[:9000]
Xin_in = Xin[:8000]/1.
Yin_in = Yin[:8000]/1.
X_valid,Y_valid = Xin[8000:]/1., Yin[8000:]/1.
layers = [tf.keras.layers.Dense(5, activation="relu", input_shape=Xin.shape[1:]),
          tf.keras.layers.Dense(300, activation="relu", name="h1"),
          tf.keras.layers.Dense(100, activation="relu", name="h2"),
          tf.keras.layers.Dense(100, activation="relu", name="h3"),
          tf.keras.layers.Dense(2, activation="softmax", name="op")]
model_clf = tf.keras.models.Sequential(layers)
model_clf.compile(loss="sparse_categorical_crossentropy", optimizer="Adam", metrics = ["accuracy"])
model_clf.fit(Xin_in, Yin_in, epochs=100, validation_data=(X_valid, Y_valid))
X_t = X[9500].reshape(1,5,)
model_clf.predict(X_t).round()