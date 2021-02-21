import sys
import os
from menus import main_menu
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="password",
database="SB_MP"
)

mycursor = mydb.cursor(dictionary = True)

mycursor.execute('''CREATE TABLE IF NOT EXISTS products (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    price FLOAT NOT NULL,
    PRIMARY KEY(id)
    );''')

mycursor.execute('''CREATE TABLE IF NOT EXISTS couriers (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    phone_number VARCHAR(30) NOT NULL,
    PRIMARY KEY(id)
    );''')

mycursor.execute('''CREATE TABLE IF NOT EXISTS orders (
    id INT NOT NULL AUTO_INCREMENT,
    customer_name VARCHAR(30) NOT NULL,
    customer_address VARCHAR(100) NOT NULL,
    customer_phone_number VARCHAR(30) NOT NULL,
    courier INT NOT NULL,
    status VARCHAR(30) NOT NULL,
    items VARCHAR(30) NOT NULL,
    PRIMARY KEY(id)
    );''')

main_menu(mycursor, mydb)