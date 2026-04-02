total = 0
num_expenses=int(input("Enter number of expenses: "))
expenses= []
for i in range(0,num_expenses,1):
    print(i)
    expenses.append(float(input("Enter an expense:")))

for x in expenses:
    print(x)

total = sum(expenses)
print("Your total expense is: "+str(total))