import numpy as np

from time import process_time


np_array = np.array([i for i in range (10000)])

start_time = process_time()

np_array += 5

end_time = process_time()

print(end_time - start_time)



# NUMPY ARRAYS

np_array =np.array ([1,2,3,4,5])

print(np_array)
type(np_array)

# Creating a numpy array of ones

a = np.ones([1,2,3,4,5])

print(a)

a.shape

# Creating a np array for a particular value

b = np.full([5,4],2)


print(b)

# Creating a np array of identity matrix

z = np.eye(4)

print(z)

# Creat a numpy array of random values

import numpy as np

X = np.random.random([3,4])

print(X)


#Random integer value array within a specific range



C = np.random.randint(10,100,(3,5))

print(C)

# Array of evenly spaced values specifying the number of values required 

G = np.linspace(10,30,5)

print(G)

# Array of evenly spaced values

import numpy as np
y = np.arange(10,30,5)

print(y)


# convert a list to a np array

list_2 = [10,20,20,30,50]

np_array = np.asarray(list_2)

print(np_array)
type(np_array)



# ANALYSING A NUMPY ARRAY

C= np.random.randint(10,90,(5,5))

print(C)


# array dim

print(C.shape)

# Number of dimensions

print(C.ndim)

# Number of elements

print(C.size)

# Cheking the data type of values in the array

print(C.dtype)

# MATHEMATICAL OPERATION ON A NP ARRAY
        #example 1
list1 = [1,2,3,4,5]

list2 = [6,7,8,9,10]

print(list1 + list2 )   # Concatenates or joins two list

       # example 2


a = np.random.randint(0,10,(3,3))

b = np.random.randint(10,20,(3,3))

print(a-b)


# Array manipulation 

array = np.random.randint(0,10,(2,3))

print(array)
print(array.shape)

#Transpose (converts rows into columns)

Trans1 = np.transpose(array)

print(Trans1)
print(Trans1.shape)

# Reshaping array

a = np.random.randint(0,10,(2,3))

print(a)
print(a.shape)

            #reshaping...

b = a.reshape(3,2)

print(b)
print(b.shape)


