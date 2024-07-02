import pymysql

# 1. Connect Database
conn = pymysql.connect(host='localhost', port=3306, user='root', password='cc20010712', charset='utf8', db="shoes")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) # 收发指令的工具

# 2. Execute SQL
while True:
    username = input("Enter your username: ")
    if username.upper() == "Q":
        break
    password = input("Enter your password: ")
    email = input("Enter your email: ")
    
    sql = "INSERT INTO Users(userName, password, email) VALUES (%(n1)s, %(n2)s, %(n3)s)"
    cursor.execute(sql, {"n1": username, "n2": password, "n3": email})
    conn.commit()

# 3. Close
cursor.close()
conn.close()
