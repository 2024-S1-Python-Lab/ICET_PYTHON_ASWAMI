s=input("enter a sentance:");
print(s)
wordsList =s.split()
print(wordsList)
for i in wordsList:
    print (f"{i} occurs {wordsList.count(i)} times")
