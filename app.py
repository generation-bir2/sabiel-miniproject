import sys
import os

def clear():
    os.system( 'cls' )

#global variables are bad practise

def myfunc():
    global products
    products = ["coke", "fanta", "7up"]
myfunc()

def menu():
    print("""
welcome to the app

close app           [0]
show products       [1]
add product         [2]
change product      [3]
remove product      [4]
""")

    choice = int(input())

    if choice == 0:
        clear()
        sys.exit(0)

    elif choice == 1:
        clear()
        print(products)
        print("press any key for main menu")
        type = input()
        if type == "0":
            clear()
            menu()
        else:
            clear()
            menu()

    elif choice == 2:
        clear()
        print(products)
        add = input("enter new product: ")
        products.append(add)
        print("product has been added")
        print("press any key for main menu")
        result = (input())
        if result == "0":
            clear()
            menu()
        else:
            clear()
            menu()

    elif choice == 3:
        clear()
        print(products)
        print("what product would you like to change? (first product = 0)")
        change = int(input())
        changeto = input("new name for product: ")
        products[change] = changeto
        print("product has been changed")
        print("press any key for main menu")
        result = (input())
        if result == "0":
            clear()
            menu()
        else:
            clear()
            menu()

    elif choice == 4:
        clear()
        print(products)
        print("what product would you like to remove? (first product = 0)")
        removing = int(input())
        products.pop(removing)
        print("product has been removed")
        print("press any key for main menu")
        result = input()
        if result == "0":
            clear()
            menu()
        else:
            clear()
            menu()


menu()