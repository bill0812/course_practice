import numpy as np
import pandas as pd
import tensorflow as tf


def get_seq(start_point, end_point):
    X_input = np.arange(start_point, end_point)
    y_input = np.arange(start_point+1, end_point+1)

    return X_input, y_input

# print('==== get_seq =====')
# print(get_seq(0, 5))

num_time_steps = 50

tf.reset_default_graph()
# Just one feature, the time series
num_inputs = 1
# 100 neuron layer, play with this
num_neurons = 200
# Just one output, predicted time series
num_outputs = 1
# learning rate, 0.0001 default, but you can play with this
learning_rate = 0.001
# how many iterations to go through (training steps), you can play with this
num_train_iterations = 1000
# Size of the batch of data
batch_size = 1

X = tf.placeholder(tf.float32, [None, num_inputs, num_time_steps])
y = tf.placeholder(tf.float32, [None, num_outputs, num_time_steps])

cell = tf.contrib.rnn.OutputProjectionWrapper(
    tf.contrib.rnn.BasicRNNCell(num_units=num_neurons, activation=tf.nn.relu),
    output_size=num_time_steps)

outputs, states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)

loss = tf.reduce_mean(tf.square(outputs - y))


optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)

    for iteration in range(num_train_iterations):
        X_input, y_input = get_seq(100, 150)

        X_batch = X_input.reshape(1, -1, num_time_steps)
        y_batch = y_input.reshape(1, -1, num_time_steps)
        sess.run(train, feed_dict={X: X_batch, y: y_batch})


        if iteration % 500 == 0:

            mse = loss.eval(feed_dict={X: X_batch, y: y_batch})
            print(iteration, "\tMSE:", mse)

    # Save Model for Later
    saver.save(sess, "./rnn_time_series_model")


with tf.Session() as sess:
    print('test')
    saver.restore(sess, "./rnn_time_series_model")

    X_new, Y_true = get_seq(102,152)
    X_new = X_new.reshape(1, -1, num_time_steps)
    print('==== New X input =====')
    print(X_new)
    y_pred = sess.run(outputs, feed_dict={X: X_new})

print('Our Prediction')
result = np.squeeze(y_pred.reshape(1, -1, num_time_steps), axis=0)
print(result)
# result = np.squeeze(y_pred.reshape(1, -1, num_time_steps), axis=0)[:,-1]
# print('Our Prediction')
# print(floor_to_given_decimal(result, 2))



