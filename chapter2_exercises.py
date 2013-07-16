# Exercises for chapter 2:
print "Problem 2.1:" 
print "The leading 0 indicates to Python that it is octal and since 02492 has a 9, which is not a valid octal representation." 
print "The others numbers in the example work because they are comverted to octal number and do not have a 8 or a 9."
print "--------------------------------------------------"
print "Problem 2.2:" 
x = 5
print x
print x + 1
print "--------------------------------------------------"
print "Problem 2.3:"
width = 17
height = 12.0
delimiter = '.'
value1 = width/2
print "1. Value 1 = " + str(value1) + " " + str(type(value1))
value2 = width/2.0 
print "1. Value 2 = " + str(value2) + " " + str(type(value2))
value3 = height/3
print "1. Value 3 = " + str(value3) + " " + str(type(value3))
value4 = 1 + 2 * 5
print "1. Value 4 = " + str(value4) + " " + str(type(value4))
value5 = delimiter * 5
print "1. Value = " + value5 + " " + str(type(value5))
# Answer 1. Value = 8, Type = int
# Answer 2. Value = 8.5, Type = float
# Answer 3. Value = 4.0, Type = float
# Answer 4. Value = 11, Type = int
# Answer 5. Value = '.....', Type = str
print "--------------------------------------------------"
print "Problem 2.4: 1"
import math
r = 5
volume = 4.0/3.0 * math.pi * r ** 3.0
print volume 
# Answer : Volume is 523 cubic unit
print "--------------------------------------------------"
print "Problem 2.4: 2"
price = 24.95
total_cost = 24.96 * 60
discounted_cost = total_cost - 0.4 * (total_cost)
shipping = 3 + 0.75 * 60
final_cost = discounted_cost + shipping
print final_cost 
# Answer : Cost is $945.45
print "--------------------------------------------------"
print "Problem 2.4: 3"
hour = 6
minutes = 52
sec = 00
minutes = minutes + 8 + ( 7 * 3 )+ 8
sec = sec + 15 + (3 * 12) + 15
if minutes > 60:
   hour = hour + 1
   minutes = minutes - 60
if sec > 60:
   minutes = minutes + 1 
   sec = sec - 60   
print str(hour) + ":" + str(minutes) + ":" + str(sec) + "am"     
# Answer : Time = 7:30:06am 
print "--------------------------------------------------"
# Name: Aarthi Narayan