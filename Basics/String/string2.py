#we will see string functions
str="Aayush"
print(len(str))
print(str.endswith("sh"))
print(str.endswith("sha"))
print(str.startswith("A"))
print(str.startswith("a"))
print(str.find("y")) #it will return the index of first occurrence of y
str2="banana"
print(str2.count("a")) #it will return the number of occurrences of a in banana
print(str2.count("n"))

print(str2.capitalize()) #it will capitalize the first letter of the string

print(str2.upper()) #it will convert the string to upper case
print(str2.lower()) #it will convert the string to lower case

print(str2.replace("a","k"))

print("Aayush 'learns' programming")
print("Aayush \"learns\" programming")