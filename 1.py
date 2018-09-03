import numpy
vectorA = numpy.array([1,2,3,4,5,6,7])
print(vectorA)
vectorB = vectorA[::-1].copy()
print(vectorB)

#addition
vectorC = vectorA + vectorB
print(vectorC)

#dot/scalar product
dotProduct1 = numpy.dot(vectorA, vectorB)
print(dotProduct1)
#alternatively we do it
dotProduct2 = (vectorA*vectorB).sum()
print(dotProduct2)

#cross product
vectorA = numpy.array([5, 6, 7])
vectorB = numpy.array([7, 6, 5])

crossProduct = numpy.cross(vectorA, vectorB)
print(crossProduct)

crossProduct = numpy.cross(vectorB, vectorA)
print(crossProduct)

#matrix creation
A=numpy.matrix("1,2,3;4,5,6")
print(A)

A=numpy.matrix([[1,2,3],[4,5,6]])
print(A)