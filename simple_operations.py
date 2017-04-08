
import tensorflow as tf 
import numpy as np 

sess = tf.InteractiveSession()


#Create a variable 
ran_val=tf.Variable(12,name='random_value')

Y, X = np.mgrid[-1.3:1.3:0.005, -2:1:0.005]

print(ran_val)
print(Y.shape)

Z = X+1j*Y


