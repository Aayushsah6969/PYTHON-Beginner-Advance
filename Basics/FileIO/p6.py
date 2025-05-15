with open("log.txt") as f:
    text = f.read()

if("Python" in text):
    print("Python is present")
else:
    print("Not present")