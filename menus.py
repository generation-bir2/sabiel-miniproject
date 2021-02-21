import sys
import os
import time
import mysql

def clear():
    os.system( 'cls' )
    
def products_menu(mycursor, mydb):
    clear()
    menu = True
    while menu == True:
        print("""
main menu           [0]

show products       [1]
add product         [2]
change product      [3]
remove product      [4]
""")
        choice = int(input())

        if choice == 0:
            clear()
            menu = False
        
        elif choice == 1:
            clear()
            mycursor.execute("SELECT id, name, price FROM products")
            products = mycursor.fetchall()
            for product in products:
                print(f"({product['id']}) {product['name']} £{product['price']}") 
        
        elif choice == 2:
            clear()
            new_product = input("enter new product: ")
            clear()
            price = float(input("enter price: "))
            mycursor.execute("""INSERT INTO products(name, price)
                                VALUES(%s, %s)""", (new_product, price))
            mydb.commit()
            print("product added")
            time.sleep(2)
            clear()

        elif choice == 3:
            clear()
            mycursor.execute("SELECT name, price FROM products")
            products = mycursor.fetchall()
            change = input("what would you like to change? ")
            for product in products:
                if change in product.values() and change != "0":
                    name = input("enter new name or press enter to keep the same: ")
                    clear()
                    price = input("enter new price or press enter to keep the same: ")
                    clear()
                    if name != "":
                        mycursor.execute(f"""UPDATE products
                                            SET name = '{name}' 
                                            WHERE name = '{change}'""")
                        clear()
                        print("name changed")
                        mydb.commit()
                        time.sleep(2)
                    if price != '':
                        price = float(price)
                        mycursor.execute(f"""UPDATE products
                                            SET price = '{price}'
                                            WHERE name = '{change}'""")
                        clear()
                        print("price changed")
                        mydb.commit()
                        time.sleep(2)
                        clear()

        elif choice == 4:
            clear()
            removal = input("enter what you would like remove or press enter to cancel: ")
            mycursor.execute("SELECT name FROM products")
            products = mycursor.fetchall()
            for product in products:
                if removal in product.values()and removal != "0":
                    mycursor.execute(f"""DELETE FROM products
                                        WHERE name = '{removal}'""")
                    print("product removed")
                    mydb.commit()
                    time.sleep(2)
                    clear()

def couriers_menu(mycursor, mydb):
    clear()
    menu = True
    while menu == True:
        print("""
main menu           [0]

show couriers       [1]
add courier         [2]
change courier      [3]
remove courier      [4]
""")
        choice = int(input())

        if choice == 0:
            clear()
            menu = False
        
        elif choice == 1:
            clear()
            mycursor.execute("SELECT id, name, phone_number FROM couriers")
            couriers = mycursor.fetchall()
            for courier in couriers:
                print(f"({courier['id']}) {courier['name']} {courier['phone_number']}") 
        
        elif choice == 2:
            clear()
            new_courier = input("enter new courier: ")
            clear()
            phone_number = input("enter phone number: ")
            mycursor.execute("""INSERT INTO couriers(name, phone_number)
                                VALUES(%s, %s)""", (new_courier, phone_number))
            mydb.commit()
            print("courier added")
            time.sleep(2)
            clear()

        elif choice == 3:
            clear()
            mycursor.execute("SELECT name, phone_number FROM couriers")
            couriers = mycursor.fetchall()
            change = input("what would you like to change? ")
            for courier in couriers:
                if change in courier.values() and change != "0":
                    name = input("enter new name or press enter to keep the same: ")
                    clear()
                    phone_number = input("enter new phone number or press enter to keep the same: ")
                    clear()
                    if name != "":
                        mycursor.execute(f"""UPDATE couriers
                                            SET name = '{name}' 
                                            WHERE name = '{change}'""")
                        clear()
                        print("name changed")
                        mydb.commit()
                        time.sleep(2)
                    if phone_number != '':
                        mycursor.execute(f"""UPDATE couriers
                                            SET phone_number = '{phone_number}'
                                            WHERE name = '{change}'""")
                        clear()
                        print("phone number changed")
                        mydb.commit()
                        time.sleep(2)
                        clear()

        elif choice == 4:
            clear()
            removal = input("enter what you would like remove or press enter to cancel: ")
            mycursor.execute("SELECT name FROM couriers")
            couriers = mycursor.fetchall()
            for courier in couriers:
                if removal in courier.values()and removal != "0":
                    mycursor.execute(f"""DELETE FROM couriers
                                        WHERE name = '{removal}'""")
                    print("courier removed")
                    mydb.commit()
                    time.sleep(2)
                    clear()

def orders_menu(mycursor, mydb):
    clear()
    menu = True
    while menu == True:
        print("""
main menu           [0]

show orders         [1]
create order        [2]
update order status [3]
""")
# update order        [4]
# delete order        [5]

        choice = int(input())

        if choice == 0:
            clear()
            menu = False
        
        elif choice == 1:
            clear()
            mycursor.execute("SELECT * FROM orders")
            orders = mycursor.fetchall()
            for order in orders:
                print(f"{order}") 

        if choice == 2:
            clear()
            name = input("enter the name of the customer: ")
            clear()
            address = input("enter the address of the customer: ")
            clear()
            phone = input("enter the phone number of the customer: ")
            clear()
            product_idx = []
            item = 1
            mycursor.execute("SELECT id, name FROM products")
            products = mycursor.fetchall()
            while item != 0:
                for product in products:
                    print(f"{product['id']} {product['name']}")
                    print()
                item = int(input("select products then press 0 to continue: "))
                clear()
                if item != 0:
                    product_idx.append(item)
            mycursor.execute("SELECT id, name from couriers")
            couriers = mycursor.fetchall()
            for courier in couriers:
                print(f"{courier['id']} {courier['name']}")
                print()
            item = int(input("select courier id: "))
            courier_idx = item
            status = "preparing"
            product_idx = (f"{product_idx}")
            mycursor.execute("""INSERT into orders(customer_name, customer_address, customer_phone_number, courier, status, items)
                                VALUES(%s, %s, %s, %s, %s, %s)""",(name, address, phone, courier_idx, status, product_idx))
            mydb.commit()
            print("order added")
            time.sleep(2)
            clear()

        if choice == 3:
            mycursor.execute("SELECT customer_name, status FROM orders")
            orders = mycursor.fetchall()
            clear()
            for order in orders:
                print(order)
            print()
            order_name = input("enter who's order you would like to change or press 0 to go to the order menu: ")
            for order in orders:
                if order_name in order.values():
                    menu = True
                    while menu == True:
                        clear()
                        print("""
on the way          [1]
completed           [2]
""")
                        user = int(input())
                        if user == 1:
                            mycursor.execute(f"""UPDATE orders
                                                SET status = "on the way"
                                                WHERE customer_name = '{order_name}'""")
                            clear()
                            mydb.commit()
                            print("status changed")
                            time.sleep(2)
                            menu = False
                            clear()
                        elif user == 2:
                            mycursor.execute(f"""UPDATE orders
                                                SET status = "completed"
                                                WHERE customer_name = '{order_name}'""")
                            clear()
                            mydb.commit()
                            print("status changed")
                            time.sleep(2)
                            menu = False
                            clear()
            clear() 

def main_menu(mycursor, mydb):
    clear()
    menu = True
    while menu == True:
        print("""
close app          [0]

product menu       [1]
courier menu       [2]
order menu         [3]
""")
        choice = int(input())

        if choice == 0:
            clear()
            menu = False
        elif choice == 1:
            products_menu(mycursor, mydb)
        elif choice == 2:
            couriers_menu(mycursor, mydb)
        elif choice == 3:
            orders_menu(mycursor, mydb)
        else:
            clear()
    return mycursor, mydb