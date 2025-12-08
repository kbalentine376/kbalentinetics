#imports
import seaborn as sns
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import keras

# Enable TensorFlow to use the Metal backend for Apple Silicon (M1/M2/M4)
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_METAL_DEVICE'] = 'gpu'
#print out versions of libaries
print("Tensorflow: ", tf.__version__ , " Seaborn:" , sns.__version__)

ex = random.randint(0,50000)

#load the data set
from keras.datasets import cifar10
#create the training and testing data frames
#(training images, training labels), (testing images, testing labels)
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
#show the number of examples in each labeled set

#sns.countplot(x=y_train)
#show the plot!
#plt.show()

#check to make sure there are NO values that are not a number (NaN)
#print("Any NaN Training:", np.isnan(x_train).any())
#print("Any NaN Testing: ", np.isnan(x_test).any())

#tell the model what shape to expect
input_shape = (32,32,3) #28x28 p0x, 1 color channel (grayscale) - 3 for RGB

#reshape the training and testing data
x_train = x_train.astype('float32') #convert to float32 for processing
x_train = x_train/255.0 #normalize the data to be between 0 and 1
#same for testing
x_test = x_test.astype('float32')
x_test = x_test/255.0 #normalize the data to be between 0 and 1

# Convert the labels to one-hot encoded vectors.
# This changes the labels from single integers (e.g., 3) to vectors (e.g., [0,0,0,1,0,0,0,0,0,0])
# which is required for many neural network classification models.
from keras.utils import to_categorical
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

#show an example image and its label
# Display the example image.
# x_train[ex] selects the ex-th image, which has shape (28, 28, 1).
# [:,:,0] selects all rows and columns, and the first (and only) channel (since it's grayscale).
plt.imshow(x_train[ex][:,:,0])
plt.show()
print()
print("-_"*40)
print(y_train[ex])
print("\n\n\\n")

batch_size = 128    #cannot store all data in memory at once, so we batch it. More complicated data will require smaller batches
num_classes = 10  #number of output classes, 10 for MNIST (digits 0-9)
epochs = 10 # how many times to go through the data

#build the model

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (5,5), padding='same', activation='relu', input_shape=input_shape),  #first layer needs to know input shape
    #32 kernals, 5x5 size, same padding means input and output are the same size, relu activation, f(x)= max(0,x)
    #tf.keras.layers.Conv2D(32, (5,5), padding='same', activation='relu'),  #second layer
    tf.keras.layers.MaxPool2D(), #pooling layer to reduce size
    tf.keras.layers.Dropout(0.25), #dropout layer to reduce overfitting, randomly turns off 25% of neurons during training
    tf.keras.layers.Conv2D(64, (3,3), padding='same', activation='relu'), #third layer
    tf.keras.layers.Conv2D(64, (3,3), padding='same', activation='relu'), #fourth layer
    #tf.keras.layers.MaxPool2D(strides=(2,2)), #second pooling layer
    #tf.keras.layers.Dropout(0.25),  #second dropout layer
    tf.keras.layers.Flatten(),  #flatten the 2D matrices into 1D vectors for the dense layers
    tf.keras.layers.Dense(128, activation='relu'), #fully connected layer with 128 neurons
    tf.keras.layers.Dropout(0.5), #third dropout layer
    tf.keras.layers.Dense(num_classes, activation='softmax')    #output layer, one neuron per class, softmax activation for probabilities
    
    
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc']) #lower the loss with cross entropy
#especially useful when using one-hot encoded labels vs. sparse/softmax labels
#we would NOT want to use categorical crossentropy with sparse labels! (those that are softmax and not one-hot encoded)

#OPTIONAL: Stop training once we reach 99.5% accuracy to prevent overfitting
class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('acc')>0.995):
      print("\nReached 99.5% accuracy so cancelling training!")
      self.model.stop_training = True

callbacks = myCallback()

#Test the model:
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=1,
                    validation_split=0.1,)
                    #callbacks=[callbacks])

#Plot the training and validation accuracy/loss
# Create a figure with two subplots (one for loss and one for accuracy)
fig, ax = plt.subplots(2, 1)

# Plot the training and validation loss on the first subplot
ax[0].plot(history.history['loss'], color='b', label="Training Loss")  # Training loss in blue
ax[0].plot(history.history['val_loss'], color='r', label="Validation Loss")  # Validation loss in red
# Add a legend to the first subplot for clarity
legend = ax[0].legend(loc='best', shadow=True)
# Add labels and title to the first subplot
ax[0].set_title('Loss')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('Loss')

# Plot the training and validation accuracy on the second subplot
ax[1].plot(history.history['acc'], color='b', label="Training Accuracy")  # Training accuracy in blue
ax[1].plot(history.history['val_acc'], color='r', label="Validation Accuracy")  # Validation accuracy in red
# Add a legend to the second subplot for clarity
legend = ax[1].legend(loc='best', shadow=True)
# Add labels and title to the second subplot
ax[1].set_title('Accuracy')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('Accuracy')

# Display the plots
plt.tight_layout()  # Adjust layout to prevent overlap between subplots
plt.show()  # Show the figure

#predict the test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

#generate the confusion matrix
# Predict the values from the testing dataset
Y_pred = model.predict(x_test)
# Convert predictions classes to one hot vectors 
Y_pred_classes = np.argmax(Y_pred, axis=1) 
# Convert testing observations to one hot vectors
Y_true = np.argmax(y_test, axis=1)
# compute the confusion matrix
confusion_mtx = tf.math.confusion_matrix(Y_true, Y_pred_classes) 

# Define class labels
class_labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

plt.figure(figsize=(10, 8))
sns.heatmap(confusion_mtx, annot=True, fmt='g', xticklabels=class_labels, yticklabels=class_labels)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()