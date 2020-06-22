with open("abc.txt",mode="w+") as file:
    print(file.closed)
    file.read()
print(file.closed)
