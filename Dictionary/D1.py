a={
    "name":"Aayush",
    "marks":{
        "maths":90,
        "english":80,
        "science":85
    },
    "Dress":["red","blue","green"],
    1:"Aayush"
}

print(a)
print(a["Dress"])

print(a.items())
print(a.keys())
print(a.values())

a.update({"name":"Kumar", "Field":"CS"})
print(a)
print(a.get("name"))

#print(a.get("Dress2")) #Prints none
#print(a["Dress2"]) #KeyError: 'Dress2'

value = a.pop("Dress")
print(value) #['red', 'blue', 'green']
print(a)