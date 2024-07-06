# Create a 4X2 integer array and Prints its attributes
import numpy

firstArray = numpy.empty([4,2], dtype = numpy.uint16) 
print("Printing Array")
print(firstArray)

print("Printing numpy array Attributes")
print("1> Array Shape is: ", firstArray.shape)
print("2>. Array dimensions are ", firstArray.ndim)
print("3>. Length of each element of array in bytes is ", firstArray.itemsize)

# Printing Array

# [[64392 31655]
#  [32579     0]
#  [49248   462]
#  [    0     0]]

# Printing NumPy array Attributes

# Array Shape is:  (4, 2)
# Array dimensions are  2
# Length of each element of array in bytes is  2


# Split the array into four equal-sized sub-arrays
print("Creating 8X3 array using numpy.arange")
sampleArray = numpy.arange(10, 34, 1)
sampleArray = sampleArray.reshape(8,3)
print (sampleArray)

print("\nDividing 8X3 array into 4 sub array\n")
subArrays = numpy.split(sampleArray, 4) 
print(subArrays)

# Creating 8X3 array using numpy.arange
# [[10 11 12]
#  [13 14 15]
#  [16 17 18]
#  [19 20 21]
#  [22 23 24]
#  [25 26 27]
#  [28 29 30]
#  [31 32 33]]

# Dividing 8X3 array into 4 sub array

# [array([[10, 11, 12],[13, 14, 15]]), 
# array([[16, 17, 18],[19, 20, 21]]), 
# array([[22, 23, 24],[25, 26, 27]]), 
# array([[28, 29, 30],[31, 32, 33]])]