#regression algorithm - data is being MEASURED - time, height
#classification- data is being COUNTED - number of dogs, students, e-mails

import tensorflow as tf
import pandas as pd


# naming the collums as type of flowers while being 0-2 in the file
CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']

# gathering info
train_path = tf.keras.utils.get_file(
    "iris_training.csv", "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv")
test_path = tf.keras.utils.get_file(
    "iris_test.csv", "https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv")


# test and train data
train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)

#labels
train_y = train.pop('Species')
test_y = test.pop('Species')

#input function, which does not return a function
def input_fn(features, labels, training=True, batch_size=256):
    # Convert the inputs to a Dataset
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle and repeat if you are in training mode ---> used only for train data
    if training:
        dataset = dataset.shuffle(1000).repeat()

    return dataset.batch(batch_size)



# Feature columns describe how to use the input
my_feature_columns = []
for key in train.keys(): # key means ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))


# Build a Deep Neural Network with 2 hidden layers with 30 and 10 hidden nodes each
classifier = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    # Two hidden layers of 30 and 10 nodes respectively.
    hidden_units=[30, 10],
    # The model must choose between 3 classes.
    n_classes=3)

# training
classifier.train(
    input_fn=lambda: input_fn(train, train_y, training=True),
    steps=5000) # lambda because we did not return a function in our input_fn, steps = how many elements close to epoch 

#evaluation
eval_result = classifier.evaluate(
    input_fn=lambda: input_fn(test, test_y, training=False))
print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))