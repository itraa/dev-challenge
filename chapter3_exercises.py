# Exercises for chapter 3:
print "Problem 3.1: "
print "Since the function was not defined before the NameError occured while execution."

# Traceback (most recent call last):
#  File "problem31.py", line 1, in <module>
#    repeat_lyrics()
#  NameError: name 'repeat_lyrics' is not defined
print "------------------------------------------------------------"
print "Problem 3.2: "
def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
    print "I'm a lumberjack and I'm okay."
    print "I sleep all night and I work all day."

print "Sucessfully executes and the lyrics are displayed"

repeat_lyrics()

print "------------------------------------------------------------"
print "Problem 3.3: "
def right_justify(s):
    y = 70 - len('s')
    print ' ' * y + s

right_justify('allen')
print "-------------------------------------------------------------"
print "Problem 3.4: 1 "
def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'

print "Displays 'spam' twice"

do_twice(print_spam)

print "Problem 3.4 : 2. 3.  4. 5"
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
print "-------------------------------------------------------------"
# Name:Aarthi Narayan