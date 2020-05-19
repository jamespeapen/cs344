# -*- coding: utf-8 -*-
"""Predicting antibiotic resistance

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zv54LHzXLmSIpDzzaB9aE5NEMwHvXUtA

# Predicting Antibiotic Resistance Using Genetic Sequences
James Eapen

## Vision
I will be training a model to predict whether a genetic sequence contains a gene that confers antibiotic resistance. The dataset is a collection of artifical genetic sequences labelled with whether or not it has a resistance gene. The features are genomic sequences, made of four letter nucleotides A, C, G, and T. Groups of three nucleotides are called codons and code for a unit of a protein. The order in which they come is important as it determines the structure and function of the protein it encodes.  

The model is based on an example by Scarlat that is a binary classifier trained with convolutional and recurrent networks. Based on a review of machine learning methods on antibiotic resistance prediction, I will be adding a random forest model, a model with just a convolutional neural network and a linear regression.

## Background
Antibiotic resistance is a naturally occuring phenomenon that has
been made worse by the human abuse of antibiotics. Antibiotics are compounds that interfere with bacterial metabolism and prevent normal functioning. They cure infections by killing the bacteria or by preventing its reproduction in the host. Every antibiotic has a mode of action that depends on a it getting into and staying inside the bacterium and on structures within it that can be used to disrupt normal function. 

However, if a bacterium aquires a gene that causes a change a structure that the antibiotic distrups, the antibiotic is no longer able to work. A bacterium becomes resistant when it aquires an antibiotic resistance gene that codes for a protein that can either protect the baterium by either changing a characteristic that the antibiotic depends on to work or by pumping the antibiotic out before it can take effect.

Studies of genomes have revealed the sequences that confer resistance and there are databases of known antibiotic resistance genes. Predicting whether a bacterium is resistant to an antibiotic from these sequences can help direct patients to the right antibiotic.

The review by Su et al. examined the perfomance of a number of machine learning models on different antibiotics and bacteria. Random forests and linear regressions were common models among the studies they reviewed.

I will be using Keras for the neural networks, numpy and pandas for data manipulation and matplotlib for plotting accuracy scores. The random forest and linear regression models will be implemented with the Scikit-learn package.

## Implementation
This draft implementation is the implemtation by Scarlat on Kaggle that uses convolutional and bi-directional Gated Recurrent Unit networks. The first part uses the raw nucleotides, A, C, G, and T. The second approach takes them in groups of three calle codons that represent a unit of the protein the sequence codes. 

Since the codon approach is more successful, I will build the random forest and linear regression using the codon data to build on the Kaggle notebook.
"""

# Commented out IPython magic to ensure Python compatibility.
# IMPORT MODULES

import os
import keras
import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt
import time
# %matplotlib inline

from keras.models import Sequential
from keras.layers import Flatten, Dense, Dropout, Embedding, LSTM
from keras import regularizers, layers, preprocessing
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score, f1_score
from sklearn.metrics import roc_auc_score, roc_curve, precision_recall_curve, average_precision_score
from sklearn.ensemble import RandomForestClassifier

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

import tensorflow as tf

# IMPORT MODULES
# Load the dataset.npy

DataRaw = np.load('drive/My Drive/Colab Notebooks/dataset.npy', allow_pickle=True)
print(type(DataRaw))
print(DataRaw.ndim)
DataRaw

# As a dictionary
Datadict = DataRaw[()]
print(Datadict)

# As a dataframe
DataDf = pd.DataFrame.from_dict(Datadict)
print(DataDf.shape)
DataDf

# Mean  / Max / Min column width

DataDf.fillna('').astype(str).apply(lambda x:x.str.len()).max()

# Tokenize from characters to integers (sequences and then pad / truncate data)

Datatok = DataDf.copy()
maxlen = 160 # cut off after this number of characters in a string

max_words = 4 # considers only the top number of characters in the dictionary A C T G
max_features = max_words

tokenizer = Tokenizer(num_words=max_words, char_level=True)
tokenizer.fit_on_texts(list(Datatok['genes']))
sequences = tokenizer.texts_to_sequences(list(Datatok['genes']))
word_index = tokenizer.word_index
Xpad = pad_sequences(sequences, maxlen=maxlen, padding='post', truncating='post', value=0)

print('Found %s unique tokens.' % len(word_index))
print('word_index', word_index)

# Separate the label

labels = np.asarray(Datatok['resistant'])
print(Xpad.shape)
print(labels.shape)

# Check a sample
rowNum = 37149
print(Datatok['genes'][rowNum])
print(sequences[rowNum])
print(Xpad[rowNum])
print(labels[rowNum])

# Create train & val and test datasets with inital shuffle (as the original dataset may be arranged)

training_samples = int(Xpad.shape[0] * 0.9)
# The validation is being taken by keras - below
# test = remaining

indices = np.arange(Xpad.shape[0])
np.random.shuffle(indices) # FOR TESTING PURPOSES comment it out - to keep indices as above

Xpad = Xpad[indices]
labels = labels[indices]

x_train = Xpad[:training_samples]
y_train = labels[:training_samples]
x_test = Xpad[training_samples: ]
y_test = labels[training_samples: ]

print('ix_train', x_train.shape)
print('y_train', y_train.shape)
print('x_test', x_test.shape)
print('y_test', y_test.shape)

# Model ... 128 CNN window 27 & Bidirectional GRU accuracy = 

model = Sequential()
model.add(Embedding(4, 1, input_length=maxlen))
model.add(layers.Conv1D(128, 27, activation='relu'))
model.add(layers.MaxPooling1D(9))
model.add(layers.Dropout(0.5))
model.add(layers.Conv1D(128, 9, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Bidirectional(layers.GRU(32, dropout=0.2, recurrent_dropout=0.2)))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.summary()

# Train / Validate model
start_time = time.time()
history = model.fit(x_train, y_train,
epochs = 10,
batch_size=32,
validation_split=0.2)
nn1_runtime = time.time() - start_time
print("Runtime: %s seconds" % nn1_runtime)

# Learning curves

# VALIDATION LOSS curves

plt.clf()
history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
epochs = range(1, (len(history_dict['loss']) + 1))
plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.plot(epochs, val_loss_values, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# VALIDATION ACCURACY curves

plt.clf()
acc_values = history_dict['acc']
val_acc_values = history_dict['val_acc']
epochs = range(1, (len(history_dict['acc']) + 1))
plt.plot(epochs, acc_values, 'bo', label='Training acc')
plt.plot(epochs, val_acc_values, 'r', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Final Predict on test

final_predictions = model.predict(x_test)
print(final_predictions)

# Modify the raw final_predictions - prediction probs  - into 0 and 1
# Cutoff point = 0.5

Preds = final_predictions.copy()
print(len(Preds))

Preds[ np.where( Preds >= 0.5 ) ] = 1
Preds[ np.where( Preds < 0.5 ) ] = 0
print(Preds)

"""A confusion matrix can be used to visualize the results and see how well the model is making its predictions. It shows the true and false positives and negatives. This is useful because a false negative prediction can be clinically more damaging than a false postive prediction since it is worse to take ineffective action against an antibiotic resistant bacterium than to take an intensive treatment against a susceptible baterium."""

# Confusion matrix

conf_mx = confusion_matrix(y_test, Preds)

TN = conf_mx[0,0]
FP = conf_mx[0,1]
FN = conf_mx[1,0]
TP = conf_mx[1,1]

print ('TN: ', TN)
print ('FP: ', FP)
print ('FN: ', FN)
print ('TP: ', TP)

recall = TP/(TP+FN)
precision = TP/(TP+FP)

print (recall, precision)

# Function to visualize the confusion matrix

def plot_confusion_matrix(cm,target_names,title='Confusion matrix',cmap=None,
                          normalize=False):
    import itertools
    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")


    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.show()

plot_confusion_matrix(conf_mx, 
                      normalize    = False,
                      target_names = ['resistant', 'sensistive'],
                      title        = "Confusion Matrix ")

print ('precision ',precision_score(y_test, Preds))
print ('recall ',recall_score(y_test, Preds) )
print ('accuracy ',accuracy_score(y_test, Preds))
print ('F1 score ',f1_score(y_test, Preds))

# AUC/ROC curves should be used when there are roughly equal numbers of observations for each class
# Precision-Recall curves should be used when there is a moderate to large class imbalance

# calculate AUC
auc = roc_auc_score(y_test, Preds)
print('AUC: %.3f' % auc)
# calculate roc curve
fpr, tpr, thresholds = roc_curve(y_test, Preds)
plt.plot([0, 1], [0, 1], linestyle='--')
# plot the roc curve for the model
plt.plot(fpr, tpr, marker='.')
plt.title('ROC ')
plt.show()

# calculate precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_test, Preds)
# calculate F1 score
f1 = f1_score(y_test, Preds)
# calculate average precision score
ap = average_precision_score(y_test, Preds)
print('f1=%.3f ap=%.3f' % (f1, ap))
plt.plot([0, 1], [0.5, 0.5], linestyle='--')
# plot the roc curve for the model
plt.plot(recall, precision, marker='.')
plt.show()

"""### Codon Tokenization"""

# From nucleotides to codons ... w/o considering the start / stop codons as the data is synthetic and may not have these

DataCod = DataDf.copy()

Codons = list(DataCod['genes'])
print(len(Codons))

for n in range(len(Codons)):
    Codons[n] = list([Codons[n][i:i+3] for i in range(0, len(Codons[n]), 3)])
    
DataCod['codons'] = Codons
DataCod

# Tokenize from codons to integers (sequences and then pad / truncate data)

maxlen = 53 # cut off after this number of codons in a list

max_words = 64 # considers only the top number of codons  in the dictionary (It finds 66 below because of 'a' and 'ga')
max_features = max_words

#tokenizer = Tokenizer(num_words=max_words, char_level=True)
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(list(DataCod['codons']))
sequences = tokenizer.texts_to_sequences(list(DataCod['codons']))
word_index = tokenizer.word_index
Xpad = pad_sequences(sequences, maxlen=maxlen, padding='post', truncating='post', value=0)

print('Found %s unique tokens.' % len(word_index))
print('word_index', word_index)

# Separate the label

labels = np.asarray(DataCod['resistant'])
print(Xpad.shape)
print(labels.shape)

# Check a sample

rowNum = 37149
print(DataCod['genes'][rowNum])
print(DataCod['codons'][rowNum])
print(sequences[rowNum])
print(Xpad[rowNum])
print(labels[rowNum])

# Create train & val and test datasets with inital shuffle (as the original dataset may be arranged)

training_samples = int(Xpad.shape[0] * 0.9)
# The validation is being taken by keras - below
# test = remaining

indices = np.arange(Xpad.shape[0])
np.random.shuffle(indices) # FOR TESTING PURPOSES comment it out - to keep indices as above

Xpad = Xpad[indices]
labels = labels[indices]

x_train = Xpad[:training_samples]
y_train = labels[:training_samples]
x_test = Xpad[training_samples: ]
y_test = labels[training_samples: ]

print('x_train', x_train.shape)
print('y_train', y_train.shape)
print('x_test', x_test.shape)
print('y_test', y_test.shape)

# Model ... 64 CNN window 27 & Bidirectional GRU accuracy = 0.99

model = Sequential()
model.add(Embedding(64, 1, input_length=maxlen))
model.add(layers.Conv1D(128, 27, activation='relu'))
model.add(layers.MaxPooling1D(3))
model.add(layers.Dropout(0.5))
model.add(layers.Conv1D(128, 9, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Bidirectional(layers.GRU(32, dropout=0.2, recurrent_dropout=0.2)))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.summary()

# Train / Validate model
start_time = time.time()
history = model.fit(x_train, y_train,
epochs = 10,
batch_size=32,
validation_split=0.2)
nn2_runtime = time.time() - start_time
print("Runtime: %s seconds" % nn2_runtime)

# Learning curves

# VALIDATION LOSS curves

plt.clf()
history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
epochs = range(1, (len(history_dict['loss']) + 1))
plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.plot(epochs, val_loss_values, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# VALIDATION ACCURACY curves

plt.clf()
acc_values = history_dict['acc']
val_acc_values = history_dict['val_acc']
epochs = range(1, (len(history_dict['acc']) + 1))
plt.plot(epochs, acc_values, 'bo', label='Training acc')
plt.plot(epochs, val_acc_values, 'r', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Final Predict on test

final_predictions = model.predict(x_test)
print(final_predictions)

# Modify the raw final_predictions - prediction probs  - into 0 and 1
# Cutoff point = 0.5

Preds = final_predictions.copy()
print(len(Preds))

Preds[ np.where( Preds >= 0.5 ) ] = 1
Preds[ np.where( Preds < 0.5 ) ] = 0
print(Preds)

# Confusion matrix

conf_mx = confusion_matrix(y_test, Preds)

TN = conf_mx[0,0]
FP = conf_mx[0,1]
FN = conf_mx[1,0]
TP = conf_mx[1,1]

print ('TN: ', TN)
print ('FP: ', FP)
print ('FN: ', FN)
print ('TP: ', TP)

recall = TP/(TP+FN)
precision = TP/(TP+FP)

print (recall, precision)

plot_confusion_matrix(conf_mx, 
                      normalize    = False,
                      target_names = ['resistant', 'sensistive'],
                      title        = "Confusion Matrix ")

# AUC/ROC curves should be used when there are roughly equal numbers of observations for each class
# Precision-Recall curves should be used when there is a moderate to large class imbalance

# calculate AUC
auc = roc_auc_score(y_test, Preds)
print('AUC: %.3f' % auc)
# calculate roc curve
fpr, tpr, thresholds = roc_curve(y_test, Preds)
plt.plot([0, 1], [0, 1], linestyle='--')
# plot the roc curve for the model
plt.plot(fpr, tpr, marker='.')
plt.title('ROC ')
plt.show()

# calculate precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_test, Preds)
# calculate F1 score
f1 = f1_score(y_test, Preds)
# calculate average precision score
ap = average_precision_score(y_test, Preds)
print('f1=%.3f ap=%.3f' % (f1, ap))
plt.plot([0, 1], [0.5, 0.5], linestyle='--')
# plot the roc curve for the model
plt.plot(recall, precision, marker='.')
plt.show()

"""## Random Forest Classifier

This random forest classifier creates 100 decision trees during the training phase. The final model is the most commmon of the classes
"""

rf = RandomForestClassifier(n_estimators=100, criterion='entropy', verbose=1)
rf.get_params()

start_time = time.time()
rf = rf.fit(x_train, y_train)
rf_runtime = time.time() - start_time
print("Runtime: %s seconds" % rf_runtime)

rf_Preds = rf.predict(x_test)
print("Test accuracy score: ", accuracy_score(y_test, rf_Preds))

# Confusion matrix

rf_conf_mx = confusion_matrix(y_test, rf_Preds)

TN = conf_mx[0,0]
FP = conf_mx[0,1]
FN = conf_mx[1,0]
TP = conf_mx[1,1]

print ('TN: ', TN)
print ('FP: ', FP)
print ('FN: ', FN)
print ('TP: ', TP)

recall = TP/(TP+FN)
precision = TP/(TP+FP)

print (recall, precision)

plot_confusion_matrix(rf_conf_mx, 
                      normalize    = False,
                      target_names = ['resistant', 'sensistive'],
                      title        = "Confusion Matrix ")

# AUC/ROC curves should be used when there are roughly equal numbers of observations for each class
# Precision-Recall curves should be used when there is a moderate to large class imbalance

# calculate AUC
auc = roc_auc_score(y_test, rf_Preds)
print('AUC: %.3f' % auc)
# calculate roc curve
fpr, tpr, thresholds = roc_curve(y_test, rf_Preds)
plt.plot([0, 1], [0, 1], linestyle='--')
# plot the roc curve for the model
plt.plot(fpr, tpr, marker='.')
plt.title('ROC ')
plt.show()

# calculate precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_test, rf_Preds)
# calculate F1 score
f1 = f1_score(y_test, rf_Preds)
# calculate average precision score
ap = average_precision_score(y_test, rf_Preds)
print('f1=%.3f ap=%.3f' % (f1, ap))
plt.plot([0, 1], [0.5, 0.5], linestyle='--')
# plot the roc curve for the model
plt.plot(recall, precision, marker='.')
plt.show()

from sklearn.linear_model import LogisticRegression 
reg = LogisticRegression(max_iter=1000).fit(x_train, y_train)
reg.score(x_train, y_train)
accuracy_score(y_test, reg.predict(x_test))



"""## Results

The codon based model had much better success than the raw nucleotide based model and had no false positives. 

The neural network and the random forest performed quite similarly on the codon dataset, with the random forest getting more false posititves than the neural network, which is clinically not so bad a problem.

The runtimes of the models were not correlated with their quality.
"""

print("Nucleotide neural network: ", nn1_runtime)
print("Codon neural network: ", nn2_runtime)
print("Codon random forest: ", rf_runtime)

"""## Implications

The ability to predict antibiotic resistance from genomic data will be an asset to fighting infections and antibiotic resistant bacteria. 

This dataset was a synthetic one and may have been easy to work with compared to a full bacterial genome. A full genome will be harder to analyze and predict resistance with and the chances of false negatives will be higher as new mutations arise that confer bacteria with novel resistance mechanisms. 

Using a random forest could allow for quick preliminary analyses that are quite robust and can be used to guide the making of better neural network models that take a lot longer to train.

## Citations
Scarlat, Alexander, Predict antibiotic resistance w gene sequence, Kaggle. https://www.kaggle.com/drscarlat/predict-antibiotic-resistance-w-gene-sequence/data

Su, M., Satola, S. W., & Read, T. D. (2019). Genome-Based Prediction of Bacterial Antibiotic Resistance. Journal of clinical microbiology, 57(3), e01405-18. https://doi.org/10.1128/JCM.01405-18
"""