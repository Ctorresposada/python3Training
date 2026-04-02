acronyms = {'LOL':'laugh out lod','IDK':"I dont't know", 'TBH':'to be honest'}

print("Printing original dictionary \n")

for i in acronyms:
    print(i)
print("\n")


print("Adding acronym FM \n")

acronyms['FM']= "f me"
print("\n")

for i in acronyms:
    print(i)
print("\n")

print("Deleting acronym lol \n")

del acronyms['LOL']
for i in acronyms:
    print(i)

print("Printing dictionary values: \n")
for i in acronyms:
    definition = acronyms.get(i)
    print(i+": "+definition)