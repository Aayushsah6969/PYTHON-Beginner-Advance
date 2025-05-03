words = ["Donkey", "bad", "fool"]

with open("donkey.txt", "r") as file:
    text = file.read()

for word in words:
    text=text.replace(word, "#"*len(word))

with open("donkey.txt", "w") as f:
    f.write(text)
