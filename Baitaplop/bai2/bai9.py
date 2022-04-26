str=input("Enter a string:")
dict = { }
for i in str:
    dict[i] = str.count(i)
    print (dict)