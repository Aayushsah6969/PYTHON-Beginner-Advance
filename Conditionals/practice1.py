#spam detectot

s=input("Enter a string: ")
res = s.find("click this")
print(res)
if (res != -1):
    print("Spam Message Detected")
    print("ALLERT")