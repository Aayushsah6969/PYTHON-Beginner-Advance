a=(1)
print(type(a))
b=(2,)
print(type(b))

c=(1,False,3.14,"hello")
print(type(c))
c[0]=2 # TypeError: 'tuple' object does not support item assignment