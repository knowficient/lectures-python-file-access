try:
    file = open("abc.txt",mode="w+")
    print("Try to close file = ",file.closed)  #check if file is closed
    print(1/0)          #create an exception using 1 divides by 0
finally:
    file.close()
    print("Finally file closed = ",file.closed)  #check if file is closed again
