# 💳 Card Generator

A Python-based console application to simulate a credit card management system with support for creating new cards, checking balances, and adding funds. The project uses MySQL for backend storage.

---

## 📌 Features

- ✅ Create new card with random unique barcode
- ✅ Store cardholder name, Aadhaar number, and initial balance
- ✅ Check card balance
- ✅ Add funds to existing card
- ✅ Option to create or reset MySQL database

---

## 🛠️ Requirements

- Python 3.x
- MySQL Server
- MySQL Connector for Python

Install MySQL connector via pip:

pip install mysql-connector-python

## ⚙️ Setup Instructions

1. Configure MySQL
Ensure MySQL server is running. Update the following credentials in the code if different:

mydb = mysql.connector.connect(
    user='root',
    password='password',
    host='localhost',
    auth_plugin='mysql_native_password'
)

2. Run the Application

python card_generator.py

3. Choose from the Menu
Press Enter to continue or Q to quit
Choose one of the following:
1: Create Card
2: Add Balance
3: Check Balance
🧠 Database Structure

Database: credit_card_data
Table: card_db

Column Name	Data Type	Description
Bar_Num	INT(10)	Unique barcode number
Name	VARCHAR(50)	Cardholder name
Adhar_Number	BIGINT(12)	Aadhaar number
Balance	INT(20)	Account balance
🔐 Security Notes

Aadhaar number is stored as plain integer — consider encrypting in production.
SQL queries use string formatting — replace with parameterized queries to prevent SQL injection.


👨‍💻 Author

Khushan Poptani
Email: poptanikhushan@gmail.com
GitHub: github.com/khushanpoptani

