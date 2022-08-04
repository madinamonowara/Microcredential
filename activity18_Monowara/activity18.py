"""
Madina Monowara
ACTIVITY 18: FOR AND WHILE LOOPS
8/3/2022
"""
print("\n\n---------------- THIS IS ACTIVITY 18 --------------- ")
print("\n\n---------------- WHILE LOOPS --------------- ")
#Example 15) ask user to enter 2 numbers between 0 and 10 with checkpoints. Use a while loop to increment each number by 2 until the sum of them reach up to 30
print("Example 15) ask user to enter 2 numbers between 0 and 10 with checkpoints. Use a while loop to increment each number by 2 until the sum of them reach up to 30")
number1 = int(input("Enter a number between 0 and 10: "))
while number1<0 or number1>10:
    number1 = int(input("Try again! Enter a number between 0 and 10: "))

number2= int(input("Enter a 2nd number between 0 and 10: "))
while number2<0 or number2>10:
    number2 = int(input("Try again! Enter a number between 0 and 10: "))

while number1<=20 and number2<=20:
    addition = number1+number2
    print("%s + %s = %s" %(number1,number2,addition))
    number1 += 2
    number2 += 2
    
                 
#Example 14) checkpoint: create a while loop that checks if an entered number is between 0 and 10
print("Example 14) checkpoint: create a while loop that checks if an entered number is between 0 and 10")
number = int(input("Enter a number between 0 and 10: "))
while number<0 or number>10:
    number = int(input("Try again! Enter a number between 0 and 10: "))
print("Entered number = ", number)
             

#Example 13) user enters 2 numbers between 0 and 10. Use while loop to increment each number by 2 until both of them reach up to 20
print("Example 13) user enters 2 numbers between 0 and 10. Use while loop to increment each number by 2 until both of them reach up to 20")
num1= int(input("Enter a number between 0 and 10: "))
num2= int(input("Enter a 2nd number between 0 and 10: "))
while num1<=20 and num2<=20:
    print("number 1 = %s and number 2 = %s" %(num1,num2))
    num1 += 2
    num2 += 2


#Example 12) while loop basics
print("Example 12) while loop basics")
i = 0
while i<6:
    print("i = ",i)
    i += 1
else:
    print("i is no longer less than 6!")

print("\n\n---------------- FOR LOOPS --------------- ")
#Example 11) for-else statement
print("Example 11) for-else statement")
for n in range(7):
    print(n)
else:
    print("DONE!")


#Example 10) use for loop to print num from 10 to -5 and skip numbers that are multiples of 4
print("Example 10) use for loop to print num from 10 to -5 and skip numbers that are multiples of 4")
for num in range(10,-5,-1):
    if num%4 == 0:
        continue
    print(num)


#Example 9) Nesting for loop and if statement
print("Example 9) Nesting for loop and if statement")
for counter in range(10):
    if counter ==5:
        continue
    print("Now counting: ", counter)
    print(" =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")


#Example 8) for loop in a string
print("Example 8) for loop in a string")
msg="Hello World!"
for m in msg:
    print("character = ", m)

#Example 7) for loop in a list
print("Example 7) for loop in a list")
colors =['yellow','red','blue','green','white','black']
for c in colors:
    print("color = ", c)

#Example 6) for loop decrement counting
print("Example 6) for loop decrement counting")
for z in range(20, -10, -5):
    print("z = ", z)
    
#Example 5) for loop with 3 arguments
print("Example 5) for loop with 3 arguments")
for y in range(2,30,3):
    print("y = ", y)

#Example 4) for loop basics
print("Example 4) for loop basics")
for x in range(1,5):
    print("Counting: ", x)



print("\n\n---------------- CONDITIONAL STATEMENT --------------- ")
#Example 3: and, or operators
print("Example 3: and, or operators")
age = int(input("Enter an age: "))
gender = input("Type M for male or F for female: ")
if age == 5 and gender == "M" or gender=="m":
    print("5 year-old boy!")
elif age==5 and gender=="F" or gender=="f":
    print("5 year-old girl!")
else:
    print("Any other ages rather than 5")
    

#Example 2: if-elif-else statement
print("Example 2: if-elif-else statement")   
age = int(input("Enter an age: "))
if age == 5:
    print("Age = 5. Height should be around 102 cm and weight 14.8 lbs.")
elif age == 6:
    print("Age = 6. Height should be around 108 cm and weight 16.3 lbs.")
elif age == 7:
    print("Age = 7. Height should be around 113 cm and weight 18.0 lbs.")
else:
    print("Unable to display height and weight")
    
    
#Example 1) if statement, check if an age in an adult using if-else
print("Example 1) if statement, check if an age in an adult using if-else") 
if age >=21:
    print("You are an adult!")
else:
    print("You are underage")
print("Welcome to the class!")
