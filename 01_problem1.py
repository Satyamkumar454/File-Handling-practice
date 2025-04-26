""" Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’."""
f = open("poem.txt", "r")
poem = f.read()
if("twinkle" in poem):
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()
