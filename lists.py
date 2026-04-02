acronyms=["LOL","IDK","SMH","TBH"]
print(acronyms)
print("Lenght of the List:")
print(str(len(acronyms)))
acronyms.append("FM")
print("Adding an item to the list:")
print(acronyms)
print("Lenght of the List:")
print(str(len(acronyms)))
print("Ordering the List:")
acronyms.sort(reverse=False)
print(acronyms)
print("Checking if something is in the List:")
if "FEM" in acronyms:
    print("true")
else:
    print("false")
print("printing the List inside a loop:")

for acronym in acronyms:
    print(acronym)



print("Going to list expenses, float list numbers")
expenses=[10.5,36,35.1,12,3.5]
for x in expenses:
    print("$", x)
sum=0
for x in expenses:
    sum=sum+x
print("You spent $",sum)
print("bye")
