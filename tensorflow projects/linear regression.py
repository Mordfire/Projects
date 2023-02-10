import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
from tensorflow import feature_column as fc


categorical_col = ['sex','n_siblings_spouses','parch','class','deck','embark_town','alone']
numeric_col = ['age','fare']
dftrain = pd.read_csv(r"C:\Users\jojo\Downloads\train.csv")
dfeval = pd.read_csv(r"C:\Users\jojo\Downloads\eval.csv")
y_train = dftrain.pop("survived")
y_eval = dfeval.pop("survived")

def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
  def input_function():
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
    if shuffle:
      ds = ds.shuffle(1000)
    ds = ds.batch(batch_size).repeat(num_epochs)
    return ds
  return input_function

train_input_fn = make_input_fn(dftrain, y_train)
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)

feature_columns = []

for featur_name in categorical_col:
    voc = dftrain[featur_name].unique()
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(featur_name,voc))

for featur_name in numeric_col:
    feature_columns.append(tf.feature_column.numeric_column(featur_name,dtype=tf.float32))

linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)

linear_est.train(train_input_fn)
result = linear_est.predict(eval_input_fn)
print(list(result))



