# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?
class Test:
    a = 10  # class attribute

# Create object
obj = Test()
print(f"Initial class attribute Test.a: {Test.a}")
print(f"Initial object attribute obj.a: {obj.a}")

# Change attribute using object
obj.a = 0
print("\nAfter changing obj.a = 0:")
print(f"Class attribute Test.a: {Test.a}")
print(f"Object attribute obj.a: {obj.a}")

# Create another object to verify class attribute
obj2 = Test()
print("\nNew object obj2's attribute value:")
print(f"obj2.a: {obj2.a}")