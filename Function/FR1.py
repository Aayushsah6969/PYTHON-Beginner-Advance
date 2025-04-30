def show(value):
    # Base case to stop recursion
    if value <= 0:
        return
    
    # Print current value
    print("Value is", value)
    
    # Recursive call with decremented value
    show(value - 1)

show(5)