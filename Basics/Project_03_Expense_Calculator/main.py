print("WElcome to the expense calculator\n")

totalFriends = int(input("Enter total no. of friends: "))
n = totalFriends

people = []
for i in range(0, n):
    name = input(f"Enter name of {i+1}th person: ")
    people.append(name)

costs = []
for i in range(0, n):
    cost = int(input(f"Enter amount expensed by {people[i]}: "))
    costs.append(cost)

# Calculate total and cost per head
totalExpenses = sum(costs)
costPerHead = totalExpenses / n

print(f"\nTotal expenses: ₹{totalExpenses}")
print(f"Cost per person: ₹{round(costPerHead, 2)}\n")

# Create a list of net balances
balances = []
for i in range(n):
    balances.append(round(costs[i] - costPerHead, 2))  # rounded for neatness

# Create mapping of person -> balance
transactions = list(zip(people, balances))

# Separate creditors and debtors
creditors = []
debtors = []

for name, balance in transactions:
    if balance > 0:
        creditors.append([name, balance])
    elif balance < 0:
        debtors.append([name, -balance])  # store as positive owed amount

# Now settle expenses
i = 0  # debtor index
j = 0  # creditor index

print("\n--- Settlement Details ---\n")

while i < len(debtors) and j < len(creditors):
    debtor, debt_amount = debtors[i]
    creditor, credit_amount = creditors[j]

    settled_amount = min(debt_amount, credit_amount)
    
    print(f"{debtor} should pay ₹{settled_amount} to {creditor}")

    debtors[i][1] -= settled_amount
    creditors[j][1] -= settled_amount

    if debtors[i][1] == 0:
        i += 1
    if creditors[j][1] == 0:
        j += 1
