string = input("Please enter a string")
a=""
a= {i: string.count(i) for i in set(string)}
print(a)
s