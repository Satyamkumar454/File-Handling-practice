""" Write a program to find out the line number where python is present from ques 6."""
with open("log.txt") as f:
    lines = f.readlines()
lineno = 0
for line in lines:
    lineno += 1
    if("python" in line):
        print(f"Yes python is present in line {lineno}")
        break    
else:
    print("No python is not present")    