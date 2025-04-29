# Break Example 1 - Basic for loop
# The break statement terminates the entire loop prematurely.
print("Break Example 1:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Break Example 2 - With while loop
print("\nBreak Example 2:")
count = 1
while True:
    print(count)
    if count >= 3:
        break
    count += 1

### Continue Statement
# The `continue` statement skips the rest of the current iteration and moves to the next iteration.

# Continue Example 1 - Skip even numbers
print("\nContinue Example 1:")
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

# Continue Example 2 - Skip specific value
print("\nContinue Example 2:")
for letter in "Python":
    if letter == "h":
        continue
    print(letter, end="")

# Practical Example - User Input
print("\n\nPractical Example:")
while True:
    user_input = input("\nEnter a number (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        print("Exiting the program...")
        break
    
    if not user_input.isdigit():
        print("Please enter a valid number!")
        continue
        
    number = int(user_input)
    print(f"You entered: {number}")