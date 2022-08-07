"""
ACTIVITY 19 - MADINA Monowara
"""

#example18 - PASS STATEMENT
def myfunction():
    pass

#example17 - BOOLEAN
def is_divisible(x, y):
    if x%y == 0 or y%x == 0:
        return True
    else:
        return False

#example16 - COMPOSITION
def sum(num1, num2):
    total = num1+num2
    return total
def number():
    n1 = int(input("Enter num1: "))
    n2 = int(input("Enter num2: "))
    t = sum(n1,n2)
    print("The sum of %s and %s is %s" %(n1,n2, t ))


#example15 - INCREMENTAL DEVELOPMENT
def distance(x1, y1, x2, y2): #step1
    dx = x2 - x1
    dy = y2 - y1
    print('dx is' , dx)
    print('dy is' , dy)
    return 0.0
def distance(x1, y1, x2, y2): #step2
    dx = x2 - x1
    dy = y2 - y1
    dsquared = math.pow(x,2)+ math.pow(dy,2)
    print('dsquared is: ' , dsquared)
    return 0.0
def distance(x1, y1, x2, y2): #step3
    dx = x2 - x1
    dy = y2 - y1
    dsquared = math.pow(x,2)+ math.pow(dy,2)
    result = math.sqrt(dsquared)
    return result



#example14 - ARBITRARY ARGUMENTS
def function3(*kids):
    n = len(kids)
    print("The last kid is: " + kids[n-1])
function3("Tobias","Peter","Alex")


#example13 - ARBITRARY ARGUMENTS
def children(*kids):
    n = len(kids[0])
    return kids
    # print("The second kid is %s amoung %s children" %(kids[1], n))
    print(n)
names = ['Emil','Tobias','Linus','Peter']
names1 = ['Emil','Tobias']
print(children(names, names1))


#example12 - ARBITRARY ARGUMENTS
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#example11 - KEYWORD ARGUMENTS
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#example10 - RETURN VALUES
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#example9 - PARAMETERS & ARGUMENTS
def sum(num1,num2):
    total = num1+num2
    return total

n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
x = sum(n1,n2)
print("The sum of %s and %s is %s" %(n1,n2,x))

#example8 - DEFAULT PARAMETERS
def country(c= "Norway"):
    print("I am from " + c)
country("Sweden")
country("India")
country()
country("Brazil")

#example7 - PARAMETERS
def name(fname):
    print(" Welcome to the program: " + fname)
name("Tobias")
name("Peter")
name(input("Enter a name: "))

#example6- CALLING FUNCTIONS
def hello_function():
    print("Hello from a function")
hello_function()

#example5 - FUNCTIONS
def my_function():
    print("Hello from a function")

#example4- RANDOM
import random
color =['red','blue','green']
randomIndex = random.randint(0,2)

#example3 - RANDOM NUMBER
import random
# Will return a number, float, between 0 and 10
print("uniform()", random.uniform(0,10))
# Will return an integer between 0 and 10
print("randint()", random.randint(0,10))
# Will return number multiple of 5 between 0 and 101
print("randrange()", random.randrange(0,101,5))
# Will return a number between 0 and RAND_MAX
print("random()", random.random())
for x in range(10):
    print(random.randint(1,101))

#example2- MATH FUNCTIONS
import math
radius = int(input("Enter a radius: "))
area = math.pow(radius,2)*math.pi
area = math.floor(area)
print("The area with radius %s is %s" %(radius, area))

#example1 - MATH FUNCTIONS
import math
radius = int(input("Enter a radius: "))
circumference = 2*radius*math.pi
circumference=round(circumference,2)
print("The circumference with radius %s is %s" %(radius, circumference))
