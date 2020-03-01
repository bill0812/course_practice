# coding: utf-8

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt

# 讀入 MNIST
mnist = input_data.read_data_sets("MNIST_data/", one_hot = True) # one-hot 編碼模式讀取資料

# MNIST 中的「 訓練集資料 」（估計模型）
x_train = mnist.train.images # 有 55000 張圖片可以訓練
y_train = mnist.train.labels # 訓練後的標籤結果（訓練後的數字）

# MNIST 中的「 測試集資料 」（最後測試模型）
x_test = mnist.test.images # 有 10000 張圖片可以測試
y_test = mnist.test.labels # 測試後的標籤結果

# MNIST 中的「 測試集資料 」（驗證模型）
x_vadilation = mnist.validation.images # 有 10000 張圖片可以驗證
y_vadilation = mnist.validation.labels # 驗證後的標籤結果

#  MNIST 資料集中也有驗證資料集

# 檢視三個資料集結構
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
print(x_vadilation.shape)
print(y_vadilation.shape)
print("---")

# 檢視觀測值（以訓練資料集來做觀測）
#print(x_test[1,:])
#print(x_train[1, :])
#print(y_train[1,:])
#print(np.argmax(y_train[1, :])) # 第一張訓練圖片的真實答案，用argmax來取得「 1 」的索引值

# 印出來看看
# 印出訓練集資料的第一張圖
first_train_img = np.reshape(x_train[1, :], (28, 28))
#print(type(first_train_img))
#plt.matshow(first_train_img, cmap = plt.get_cmap('gray')) # 圖譜用 「 灰諧 」 
#plt.show()

# 印出測試集資料的第一張圖
first_test_img = np.reshape(x_test[1, :], (28, 28))
#print(type(first_test_img))
#plt.matshow(first_test_img, cmap = plt.get_cmap('gray')) # 圖譜用 「 灰諧 」 
#plt.show()

# 印出驗證集資料的第一張圖
first_vadilation_img = np.reshape(x_vadilation[1, :], (28, 28))
#print(type(first_vadilation_img))
#plt.matshow(first_vadilation_img, cmap = plt.get_cmap('gray')) # 圖譜用 「 灰諧 」 
#plt.show()

# Softmax 函數，
# 我們需要透過 Softmax 函數將分類器輸出的分數（Evidence）轉換為機率（Probability），
# 然後依據機率作為預測結果的輸出，可想而知深度學習模型的輸出層會是一個 Softmax 函數。

# Cross-entropy，
# 不同於我們先前使用 Mean Squared Error 定義 Loss，
# 在這個深度學習模型中我們改用 Cross-entropy 來定義 Loss。

# 實作 tensorflow，實作分類器

# 設定參數
learning_rate = 0.5
training_steps = 1000
batch_size = 100
logs_path = 'TensorBoard/'
n_features = x_train.shape[1] # 訓練集的第一張圖片特徵值
n_labels = y_train.shape[1] # 訓練集的第一張圖片數字

# 建立 Feeds （要餵的資料）
with tf.name_scope('Inputs'):
    x = tf.placeholder(tf.float32, [None, n_features], name = 'Input_Data')
with tf.name_scope('Labels'):
    y = tf.placeholder(tf.float32, [None, n_labels], name = 'Label_Data')
    print(x)
    print(y)

# 建立 Variables （模型參數）
with tf.name_scope('ModelParameters'):
    W = tf.Variable(tf.zeros([n_features, n_labels]), name = 'Weights') # 權重
    b = tf.Variable(tf.zeros([n_labels]), name = 'Bias') # 斜率

# 開始建構深度學習模型
with tf.name_scope('Model'):
    # Softmax 函數
    prediction = tf.nn.softmax(tf.matmul(x, W) + b)

with tf.name_scope('CrossEntropy'):
    # Cross-entropy
    loss = tf.reduce_mean(-tf.reduce_sum(y * tf.log(prediction), reduction_indices = 1))
    tf.summary.scalar("Loss", loss)

with tf.name_scope('GradientDescent'):
    # Gradient Descent
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

with tf.name_scope('Accuracy'):
    correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
    acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    tf.summary.scalar('Accuracy', acc)

# 初始化
init = tf.global_variables_initializer()

# 開始執行運算
sess = tf.Session()
sess.run(init)

# 將視覺化輸出
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter(logs_path, graph = tf.get_default_graph())

# 訓練
for step in range(training_steps):
    batch_xs, batch_ys = mnist.train.next_batch(batch_size)
    #print(type(batch_xs))
    #print(batch_ys)
    sess.run(optimizer, feed_dict = {x: batch_xs, y: batch_ys})
    if step % 50 == 0:
        #print(loss)
        print(sess.run(loss, feed_dict = {x: batch_xs, y: batch_ys}))
        summary = sess.run(merged, feed_dict = {x: batch_xs, y: batch_ys})
        writer.add_summary(summary, step)

print("---")
# 準確率
print("Accuracy: ", sess.run(acc, feed_dict={x: x_test, y: y_test}))

sess.close()
