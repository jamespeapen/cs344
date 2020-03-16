"""
Lab 06
Exercise 6.3
"""

import numpy
from keras.datasets import boston_housing

(training_data, training_labels), (testing_data, testing_labels) = boston_housing.load_data()

def print_structures():
        print(
                'training images \
                \n\tcount: {} \
                \n\tdimensions: {} \
                \n\tshape: {} \
                \n\tdata type: {}\n\n'.format(
                len(training_data), 
                training_data.ndim, 
                training_data.shape, 
                training_data.dtype
                
               ),
               'testing images \
               \n\tcount: {} \
               \n\tdimensions: {} \
               \n\tshape: {} \
               \n\tdata type: {} \
               \n\tvalues: {}\n'.format(
               len(testing_labels), 
               training_labels.ndim, 
               testing_labels.shape, 
               testing_labels.dtype, 
               testing_labels
               
              )
           
          )

print_structures()

# a i. 
print("Training data size: ", len(training_data))
print("Testing data size: ", len(testing_labels))
print("Training data dimensions: ", training_data.ndim)
print("Training data shape: ", training_data.shape)
print("Training data type: ", training_data.dtype)

print("Testing data dimensions: ", testing_data.ndim)
print("Testing data shape: ", testing_data.shape)
print("Testing data type: ", testing_data.dtype)
