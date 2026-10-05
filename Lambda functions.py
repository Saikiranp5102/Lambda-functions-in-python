
#1.Add two numbers
add = lambda a, b: a + b
print(add(10, 20)) 


#2.Subtract two numbers
sub = lambda a, b: a - b
print(sub(10, 4))

#3.Find square of a number
square = lambda x: x * x
print(square(5)) 

#4.Check even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(8))
print(check(7))     

#5. Find small number
small = lambda a, b: a if a < b else b
print(small(10, 20))

#6.Add 10 to a number
add10 = lambda x: x + 10
print(add10(5))

#7. Cube of a number
cube = lambda x: x * x * x
print(cube(3))

#8.CHECK POSITIVE OR NEGATIVE
check = lambda x: "Positive" if x > 0 else "Negative"
print(check(10))
print(check(-5))

#9.Convert Celsius to Fahrenheit
temp = lambda c: (c * 9/5) + 32
print(temp(20))      

#10.Get last digit of a number
last = lambda x: x % 10
print(last(12345))     

#11. Divide two numbers
divide = lambda a, b: a / b
print(divide(10, 2)) 

#1.lambda fonction without input and without return
#declaration
sayhello=lambda:print("hello")
#invoking
sayhello()

#2.lambda fonction with input and without return
#syntax
   #lambda parameter:expression
#declaration
displayname=lambda fname:print("My name is ",fname)
# #call or invoke
displayname("Hero") #argument

#3.lambda fonction without input and with return
#lambda:"value to be returned"
#decleration
displaymsg = lambda: "hello hero"
# #Invoking
print(displaymsg())


#4.lambda fonction with input and with return
#declaration
displayname = lambda fname: "my name is " + fname
# #Invoking 
print(displayname("Innomatics"))



#lambda function using conditional statements
#lambda function without input and with return
#check given number is even or odd.
checkeven = lambda:"even" if 10%2==0 else "odd"
print(checkeven())
  #(or)
checkeven = lambda n:"even" if n%2==0 else "odd"
print(checkeven(10))