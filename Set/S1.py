s = set()
print(type(s))

s1={1,2,5,8,2,4,9,9}
print(s1)

l1=[1,2,4,5,7]
print("List l1: ",type(l1))

s2=set(l1)
print(s2)
print(type(s2))

s1.add("Aayush") #add single element
print(s1)
s1.update(["Aayush", "Kumar"]) #add multiple elements
print(s1)
s1.remove("Aayush") #remove single element ERROR IF NOT FOUND
print(s1)
s1.discard("Aayush") #remove single element NO ERROR IF NOT FOUND
print(s1)

b = s1.pop() #remove and return random element
print(b)
print(s1)
s1.clear() #remove all elements
print(s1)