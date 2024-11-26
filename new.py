def sayhello(a):
    if a == 1:
        print("Hello world")
    else:
        print("Error")


a = 1
while a != 0:
    a = int(input("Enter a number : "))
    sayhello(a)


# print("Hello")
