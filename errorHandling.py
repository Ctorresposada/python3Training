acronyms = {'LOL':'laugh out loud',
            'IDK':"I dont't know",
            'TBH':'to be honest'}

try:
    with open('acronimos.txt') as file:
        #do file operations here
        result = file.read()
        print(result)
        
    for key, value in acronyms.items():
      print(key, value)

    definition = acronyms[input("Write your acronym you want to query:")]
    print(definition)
except:
       print("Key doesn't exist")
finally:
    print('Complete list of acronyms: \n')

    for acronym in acronyms:
        print(acronym)

