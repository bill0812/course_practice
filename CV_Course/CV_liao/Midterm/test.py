import  numpy as np
def pad_with(vector, pad_width, iaxis, kwargs):
#     pad_value = kwargs.get('padder', 10)
#     vector[:pad_width[0]] = pad_value
#     vector[-pad_width[1]:] = pad_value
    return vector

a = np.arange(6)
a = a.reshape((2, 3))
print(np.pad(a, 2, pad_with))

