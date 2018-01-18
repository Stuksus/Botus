import pymysql.cursors


# Функция возвращает connection.
def getConnection():
    # Вы можете изменить параметры соединения.
    connection = pymysql.connect(host='localhost',
                                 user='rooting',
                                 password='123123',
                                 db='bot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection