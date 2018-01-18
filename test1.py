import function
import connection

connection = connection.getConnection()
name = 'test6'
test = function.creatDataBase(name,connection)
print('Все удалось')
print(test)