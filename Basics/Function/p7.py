# Write a python function to remove a given word from a list ad strip it at the same time.

l=["This", "Help", "Go", "Laptop", "House", "Plane","Sheep", "Net"]

def lists(list,word):
    i=list.index(word)
    if(i):
        print(f"Word found at index {i}")
        list.insert(i,"*")
        print("Replacing done")
        print(list)
    else:
        print("Eord not found in the list")

lists(l,"House")