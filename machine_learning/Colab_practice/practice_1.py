import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Use numpy to generate a bunch of random data in a bell curve around 5.
n = 5 + np.random.randn(1000)
print(n)

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

print(ys)
print(x)

# plt.hist(ys, bins=20)
# plt.title("Histogram")
# plt.show()

xs = []
ys = []
  
for i in range(20):
    x = i
    y = np.random.randint(10)
    
    xs.append(x)
    ys.append(y)
print(xs)
print(ys)
print(np.zeros(10))

y = 10 + np.arange(20) + 5 * np.random.randn(20)

print(y)
print(np.random.randn(20))
print(np.arange(20))

# Make a 10 x 10 heatmap of some random data
side_length = 10
# Start with a 10 x 10 matrix with values randomized around 5
data = 5 + np.random.randn(side_length, side_length)
print(data)
print("==============")
# The next two lines make the values larger as we get closer to (9, 9)
data += np.arange(side_length)
print(data)
print("==============")
data += np.reshape(np.arange(side_length), (side_length, 1))
print(data)
print("=================")
print(np.arange(side_length))
# Generate the heatmap
sns.heatmap(data)
plt.show()
