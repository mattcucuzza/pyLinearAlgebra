# Matthew Cucuzza
# 2/18/17
# Python program doing various operations with vectors from linear algebra

import math

# Find the sum of two vectors combined
def addVectors(x1, y1, x2, y2):
    x = x1+x2
    y = y1+y2

    return x,y

# Find the length of two vectors combined
def lengthOfVector(x,y):
    x = x**2
    y = y**2
    xY = x+y

    return "sqrt("+str(xY)+")"

# Find the length of the sum of two vectors combined
def lengthOfAddVectors(x1, y1, x2, y2):
    x = (x1+x2)**2
    y = (y1+y2)**2
    xY = x+y

    return "sqrt("+str(xY)+")"

# Find the dot product (multiply x's, multiply y's, add them together)
def dotProduct(x1, y1, x2, y2):
    x = x1*x2
    y = y1*y2

    return x+y

# Check if the dot product is orthogonal (equal to 0)
def isOrthogonal(x1, y1, x2, y2):
    if dotProduct(x1,y1,x2,y2) == 0:
        return True
    else:
        return False

# Find the angle between two vectors
def findAngle(x1, y1, x2, y2):
    dot = dotProduct(x1, y1, x2, y2)
    lengthU = lengthOfVector(x1,y1)
    lengthV = lengthOfVector(x2,y2)

    return str(dot) +"/"+ "(" + str(lengthU) + " * " + str(lengthV) + ")"

# Find the unit vector of two vectors
def unitVector(x1, y1, x2, y2):
    add = addVectors(x1, y1, x2, y2)
    length = lengthOfAddVectors(x1, y1, x2, y2)

    return str(add) +"/"+ "(" + str(length) +")"


print "-----First Set of Coordinates-----"
x1 = input("Enter X1: ")
y1 = input("Enter Y2: ")
print
print "-----Second Set of Coordinates-----"
x2 = input("Enter X2: ")
y2 = input("Enter Y2: ")
print
print "-----Inputted Coordinates-----"
print "u : ("+str(x1)+ ","+ str(y1)+")"
print "v : ("+str(x2)+ ","+ str(y2)+")"
print
print "-----Calculations-----"
print "||u|| : ", lengthOfVector(x1,y1)
print "||v|| : ", lengthOfVector(x2,y2)
print "u+v : ", addVectors(x1, y1, x2, y2)
print "||u+v|| : ", lengthOfAddVectors(x1, y1, x2, y2)
print "u*v : ", dotProduct(x1, y1, x2, y2)
print "Orthogonal: ", isOrthogonal(x1, y1, x2, y2)
print "Angle of Two Vectors: ", findAngle(x1, y1, x2, y2)
print "Unit Vector: ", unitVector(x1, y1, x2, y2)
