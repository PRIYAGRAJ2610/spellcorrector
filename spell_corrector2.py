# this code can check the spellings of a given text file and correct them by itself.

# importing required modules.
from textblob import TextBlob
#file handling
file1 = open("original.txt" ,"r+")
a = file1.read()

# it will return the original text of the  given text file
print("original text :   " + str(a))
print("*"*50)
b = TextBlob(a)
# it will return  the corrected text .
print("correct text :   " +str(b.correct()))
file1.close
p = open("correct", "w")
p.write(str(b.correct()))
p.close