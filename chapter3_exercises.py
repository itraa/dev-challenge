# Exercises for chapter 3:
# Problem 3.1: Since the function was not defined before the call the following error occured while execution
# Traceback (most recent call last):
#  File "problem31.py", line 1, in <module>
#    repeat_lyrics()
#  NameError: name 'repeat_lyrics' is not defined
#-------------------------------------------------------------
#  Problem 3.2: Sucessfully executes with following display
# I'm a lumberjack and I'm okay.
# I sleep all night and I work all day.
# I'm a lumberjack and I'm okay.
# I sleep all night and I work all day.
#--------------------------------------------------------------
#  Problem 3.3: 
def right_justify(s):
    y = 70 - len('s')
    print ' ' * y + s

right_justify('allen')
#---------------------------------------------------------------
#  Problem 3.4:
# 1. Displays the following:
#spam
#spam
# 2. 3.  4. 5. Code below:
def do_twice(f,g):
    f(g)
    f(g)

def print_twice(g):
    print g
    print g

def do_four(f,g):
    do_twice(f,g)
    do_twice(f,g)

do_twice(print_twice,'spam')

do_four(print_twice,'spam')
#-----------------------------------------------------------------------
# Name:Aarthi Narayan