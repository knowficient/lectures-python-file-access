with open("test.txt",mode="r") as file:
    file.seek(5)
    print(file.tell())
    print(file.read())
