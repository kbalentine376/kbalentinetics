import seaborn as sns
import tensorflow as tf
import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#print out versions of libraries
print("Tensorflow:", tf.__version__, "Seaborn:", sns.__version__)

#load the dataset
mnist = tf.keras.datasets.mnist
#creating the training and testing data frames
#training images, training labels ; testing images, testing labels
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#show the number of examples in each labeled set
sns.countplot(x=y_train)
#show the plot
plt.show()

#check to make sure there are NO values that are not a number (NaN)
print("Any NaN training:", np.isnan(x_train).any())
print("Any NaN training:", np.isnan(x_test).any())

#tell the model what shape to expect
input_shape = (28, 28, 1) #28x28 p0x, 1 color channel (grayscale) - 3 for RGB

#reshape the training and testing data
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
x_train = x_train/255.0 #normalize the data to be between 0 and 1
#same for testing
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)
x_test = x_test/255.0 #normalize the data to be between 0 and 1

#conevrt our labels to be one-hot, not sparse
y_train = tf.one_hot(y_train.astype(np.int32), depth = 10)
y_test = tf.one_hot(y_test.astype(np.int32), depth = 10)

#show an example image from MNIST
plt.imshow(x_train[rd.randint(0, 99999)][:, :, 0], cmap =  'gray')
plt.show()


batch_size = 128
num_classes = 10
epochs = 5

#build the model
model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Conv2D(32, (5, 5), padding = 'same', activation = 'relu', input_shape = input_shape),
        tf.keras.layers.Conv2D(32, (3, 3), padding = 'same', activation = 'relu', input_shape = input_shape),
        tf.keras.layers.MaxPool2D(),
        tf.keras.layers.Dropout(.25),
        tf.keras.layers.Conv2D(64, (3, 3), padding = 'same', activation = 'relu', input_shape = input_shape),
        tf.keras.layers.Conv2D(64, (3, 3), padding = 'same', activation = 'relu', input_shape = input_shape),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(num_classes, activation = 'softmax')
    ]
)

model.compile(optimizer = tf.keras.optimizers.RMSprop(epsilon=1e-08), loss = 'categorical_crossentropy', metrics = ['acc'])

history = model.fit(x_train, y_train, batch_size = batch_size, epochs = epochs, validation_data = (x_test, y_test))


#plot out training and validation accuracy and loss
fig, ax = plt.subplots(2,1)

ax[0].plot(history.history['loss'], color = 'b', label = "Training Loss")
ax[0].plot(history.history['val_loss'], color = 'r', label = "Validation Loss")
legend = ax[0].legend(loc = 'best', shadow = True)
ax[0].set_title("Loss")
ax[0].set_xlabel("Epochs")
ax[0].set_ylabel("Loss")

ax[1].plot(history.history['acc'], color = 'b', label = "Training Accuracy")
ax[1].plot(history.history['val_acc'], color = 'r', label = "Validation Accuracy")
legnd = ax[1].legend(loc = 'best', shadow = True)
ax[1].set_title("Accuracy")
ax[1].set_xlabel("Epochs")
ax[1].set_ylabel("Accuracy")

plt.tight_layout()
plt.show()

#predict the test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

#generate the confusion matrix

# Predict the values from the testing dataset
Y_pred = model.predict(x_test)
# Convert predictions classes to one hot vectors 
Y_pred_classes = np.argmax(Y_pred,axis = 1) 
# Convert testing observations to one hot vectors
Y_true = np.argmax(y_test,axis = 1)
# compute the confusion matrix
confusion_mtx = tf.math.confusion_matrix(Y_true, Y_pred_classes) 

plt.figure(figsize=(10, 8))
sns.heatmap(confusion_mtx, annot=True, fmt='g')
plt.show()