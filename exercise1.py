# This is a Python comment. Lines that begin with a '#' are ignored by the
# Python interpreter. Comments are useful for documenting code or explaining
# quiz questions!
# 
# Write a Python program that prints out the number of minutes in seven weeks.
# Remember: 7 weeks 7 days in a week, 24 hours in a day, and 60 mins in an hour.
# Multiplying these numbers together will give you the result
#
# Click the "Test Run" button below to try running your code and see the output,
# and click "Submit" to submit your answer.

print 49*24*60

answer is 70560


----------------------------

# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the values
# defined below.    
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second

print 299792458 * 100 * 1.0/1000000000

answer is 29.9792458


----------------------------------

# Write python code that defines the variable 
# age to be your age in years, and then prints 
# out the number of days you have been alive.

age = 28
number_of_days_per_year = 365
alive_Days = age * number_of_days_per_year
print alive_Days  

answer is 10220


-----------------------

# Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.

s = 'audacity'
print s [1:].capitalize()

or

# Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.

s = 'audacity'
print 'U' + s[2:]


---------------------------------

# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''

start_link = page.find('<a.href=')



----------------------------------------------

# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')

#page= '<a href="http://udacity.com">Hello world</a>'
start_link=page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote+1)
url = page[start_quote+1:end_quote]



-----------------------------------

# Write Python code that stores the distance 
# in meters that light travels in one 
# nanosecond in the variable, nanodistance. 

# These variables are defined for you:

speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000. # 1 billion

# After your code, running the following:

# print nanodistance

# should output: 0.2998

# Note that nanodistance must be a decimal number.

# ASSIGN nanodistance BELOW this line

nanodistance = speed_of_light/nano_per_sec

print nanodistance


---------------------------------------

# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

>>>print s[:3]+t[4:]
udacious

>>>print (s[:-2]+t[-3:])
udacious


---------------------------------------------

	# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.

text = "first hoo" 

# ENTER CODE BELOW HERE


>>>print text.find('hoo')

6

----------------------------------

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

# ENTER CODE BELOW HERE

# IMPORTANT BEFORE SUBMITTING: 
# You should only have one print command in your function

>>>first_zip = text.find('zip')
>>>print text.find('zip',first_zip+1)

answer is 18 

OR

>>>print text.find('zip',text.find('zip')+1)

answer is 18 

------------------------------------------

###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace 
# the tricky parts with a marker. 
# Write a program that takes a line of text and 
# finds the first occurrence of a certain marker 
# and replaces it with a replacement text. 
# The resulting line of text should be stored in a variable. 
# All input data will be given as variables.
#
# Replace the first occurrence of marker in the line below.
# There will be at least one occurrence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# Hint: You can find out the length of a string by command
# len(string). We might test your code with different markers!

# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

# Example 2 # uncomment this to test with different input
#marker = "EY"
#replacement = "Eyjafjallajokull"
#line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###

replaced = line[:line.find(marker)] + replacement + line[line.find(marker)+len(marker):]
print replaced



# Example 1 output should be:
#>>> I will now go to sleep and be away from keyboard until lunch time tomorrow.
# Example 2 output should be:
#>>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.

--------------------------------------------------------

###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads 
# the same backwards as forwards. Make a program 
# that checks if a word is a palindrome. 
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise. 
# The word contains lowercase letters a-z and 
# will be at least one character long.
#
### HINT! ###
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# This exercise can be solved with only unit 1 knowledge
# (no loops or conditions)

#word = "madam"
# test case 2
word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###


is_palindrome = word.find(word[::-1])

# TESTING

print is_palindrome
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"