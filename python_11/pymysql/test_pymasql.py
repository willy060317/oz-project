import pymysql

connection = pymysql.connect(
    host = '127.0.0.1',
    user='root',
    password= '0000',
    db = 'classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
 
cursor =connection.cursor()

sql = "SELECT * FROM customers"
cursor.execute(sql)

customers = cursor.fetchone()
print("customers : ", customers)
print("customers : ", customers['customerNumber'])
print("customers : ", customers['customerName'])
print("customers : ", customers['country'])
name = 'inseop'
family_name = 'kim'
sql = f"INSERT INTO customers(customerNumber, customerName) VALUES({1000}{name}{family_name})"
cursor.execute(sql)
connection.commit() 