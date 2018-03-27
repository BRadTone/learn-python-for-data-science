import numpy as np

a = np.array([[1, 2.2], [3, 4], [5, 6], [7, 8]], int)

print('shape: ', a.shape)
print('data type: ', a.dtype)
print('check presence of value: ', 0 in a)

r = range(20, 0, -2)  # ([start], stop[, step])
b = np.array(r).reshape(2, 5)
print(b)
c = b.transpose()

print(c)

# todo continue on page 6