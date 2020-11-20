#this code can be used to correct the spellings in the  text  given as input by user.

#import required module
from textblob import TextBlob

#taking text input from user to be corrected
x = input("enter the text to check the spellings :")
print("*"*50)
y = TextBlob(x)
print("correct text :   " + str(y.correct()))

