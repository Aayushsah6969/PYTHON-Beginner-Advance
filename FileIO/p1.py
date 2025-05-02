#Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("poems.txt", "r") as f:
    text = f.read()
print(type(text))
print(text)
p=text.count("twinkle")
print(f" 'Twinkle' appears for {p} times")