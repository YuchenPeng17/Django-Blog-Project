import pymysql

# 1. Connect Database
conn = pymysql.connect(host='localhost', port=3306, user='root', password='cc20010712', charset='utf8', db="shoes")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) # 收发指令的工具

# 2. Execute SQL
cursor.execute("SELECT * FROM Users")
data = cursor.fetchall()  # 获取返回回来的值
print(data)

# 3. Close
cursor.close()
conn.close()
