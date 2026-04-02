menus = {"Breakfasts ":["Cereal","Eggs","Pancakes"],
         "Lunches ":["Fish","Chcken","Salad"],
         "Dinners ":["Pita","Sandwich"]}
for a,b in menus.items():
    print(a,b)
print(menus.get("Breakfasts "))
print(menus.get("Lunches "))
print(menus.get("Dinners "))