import random
import mysql.connector
import re


mydb = mysql.connector.connect(user='root', password='password', host='localhost', auth_plugin='mysql_native_password')

def create_db():
    #card_db -> bar_num (10), name (50), adhar_number (12), balance(20)
    try:
        print("Creating Data base \n")
        cursor = mydb.cursor()
        cursor.execute("create database credit_card_data")
        cursor.execute("use credit_card_data")
        cursor.execute("create table card_db(Bar_Num int(10), Name varchar(50), Adhar_Number int, Balance int(20))")
        mydb.commit()
        print("Data base created \n")

    except mysql.connector.errors.ProgrammingError and mysql.connector.errors.DatabaseError as e:
        cursor = mydb.cursor()

        while True:
            print("Data base already exist do you want to delete Y/N")
            y_n = input("Enter -: ")
            print("")
            if y_n == "n" or y_n == "N":
                print("continuing forward")
                print("Using old databse only \n")
                break

            elif y_n == "y" or y_n == "Y":
                print("Deleting data and creating new data base")

                cursor.execute("use credit_card_data")
                cursor.execute("drop table card_db")
                cursor.execute("drop database credit_card_data")

                cursor.execute("create database credit_card_data")
                cursor.execute("use credit_card_data")
                cursor.execute("create table card_db(Bar_Num int(10), Name varchar(50), Adhar_Number bigint(12), Balance int(20))")

                print("Data base created \n")
                break

            else:
                print("Wrong input try again... \n")


def create_card():
    adhar_number = int(input("Enter the adhar-card number :- "))

    if len(str(adhar_number)) == 12:
        name = input("Enter the name of the owner :- ")
        balance = int(input("Enter the amount of money you want to add -: "))
        range_1 = 111111111
        range_2 = 999999999

        cursor = mydb.cursor()
        cursor.execute("use credit_card_data")
        cursor.execute("SELECT bar_num FROM card_db")
        last_bar_num = str(cursor.fetchall())
        a = re.findall(r'\d+', last_bar_num)

        last_bar_num = [int(i) for i in a]

        while True:
            bar_num = random.randrange(range_1, range_2)
            if bar_num in last_bar_num:
                print()

            else:
                print()
                break



        s = "INSERT INTO card_db (bar_num, name, adhar_number, balance) VALUES (%s, %s, %s, %s)"

        add_data = (bar_num, name, adhar_number, balance)
        cursor.execute(s, add_data)
        mydb.commit()
        print(f"Your bar code number is {bar_num}")

    else:
        print("Wrong Adhar-card number")


def add_balance():
    bar_num = int(input("Enter the barcode number :- "))
    new_balance = int(input("Enter the amount of money you want to add -: "))
    print("")

    cursor = mydb.cursor()
    cursor.execute("use credit_card_data")
    cursor.execute(f"select * from card_db where bar_num = '{bar_num}'")
    result = cursor.fetchone()

    user_row2 = []
    for i in result:
        user_row2.append(i)

    past_balance = int(user_row2[3])
    total_balance = past_balance+new_balance

    cursor = mydb.cursor()
    sql = f"Update card_db SET balance = {total_balance} WHERE bar_num = {bar_num}"
    cursor.execute(sql)
    mydb.commit()

    print(f"{new_balance} added in the {bar_num}")
    print("Total balance", total_balance)


def check_balance():
    bar_num = int(input("Enter the barcode number :- "))

    cursor = mydb.cursor()
    cursor.execute(f"select * from card_db where bar_num = '{bar_num}'")
    result = cursor.fetchone()

    user_row = []
    for i in result:
        user_row.append(i)

    balance_left = int(user_row[3])
    name = user_row[1]
    print(balance_left, "In your Card", name)


create_db()
while True:
    print("")
    ask = input("Press enter to continue or Q to quit -: ")
    print("")

    if ask == "q" or ask == "Q":
        exit()

    elif ask == "":
        print("What you want to do")
        print("1. Create card")
        print("2. Add Balance")
        print("3. Check Balance")
        inp = int(input("Enter the number -: "))
        print("")

        if inp == 1:
            create_card()

        elif inp == 2:
            add_balance()

        elif inp == 3:
            check_balance()

    else:
        print("Wrong input try again")


