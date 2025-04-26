"""
Repeat program 4 for a list of such words to be censored.

"""

words = ["Donkey" , "good" , "more"]
with open("word.txt","r")as f:
    content = f.read()
for word in words:   
    contentNew = content.replace(word,"#" * len(word))
with open("word.txt","w")as f:
    f.write(contentNew)    