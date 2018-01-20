import pymysql.cursors


# Функция возвращает connection.
def getConnection(globalS):
    # Вы можете изменить параметры соединения.

    connection = pymysql.connect(host=globalS[0],
                                 user=globalS[1],
                                 password=globalS[2],
                                 db=globalS[3],
                                 charset=globalS[4],
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def creatDB(globalS,arg):
    connection = getConnection(globalS)
    sql='CREATE TABLE `'+arg+'` ( `id` INT(11) NOT NULL AUTO_INCREMENT ,`idUser` INT(11) NOT NULL , `userName` VARCHAR(255) NOT NULL , `countWord` INT(11) NOT NULL , `colMate` INT(11) NOT NULL , `colGood` INT(11) NOT NULL , `stat` INT(11) NOT NULL , PRIMARY KEY (`id`) USING BTREE) ENGINE = InnoDB;'
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

def selectDB(globalS,columnPrephix,column = 'idUser',table = 'users'):
    connection = getConnection(globalS)
    sql='SELECT * FROM `'+table+'` WHERE '+column+' =\''+columnPrephix+'\''

    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result[0]
    finally:
        connection.close()

def deleteDB(globalS, columnPrephix, column='idUser', table='users'):
    connection = getConnection(globalS)
    sql = 'DELETE FROM `'+table+'` WHERE '+column+' =\''+columnPrephix+'\''

    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return
    finally:
        connection.close()

def insertDB(globalS,arg, table='users'):
    connection = getConnection(globalS)
    sql = 'INSERT INTO `'+table+'`(`idUser`,`userName`, `countWord`, `col_mate`, `colGood`, `stat`) VALUES (%s,%s,%s,%s,%s,%s)'

    try:
        cursor = connection.cursor()
        cursor.executemany(sql,arg)
        connection.commit()

    finally:
        connection.close()

def updateDB(globalS, arg,column = 'idUser',table='users'):
    connection = getConnection(globalS)
    sql = 'UPDATE `'+table+'` SET  idUser = %s,userName=%s, countWord = %s, col_mate=%s,colGood=%s,stat=%s WHERE '+column+'='+arg[0][0]+''

    try:
        cursor = connection.cursor()
        cursor.executemany(sql,arg)
        connection.commit()


    finally:
        connection.close()


def selectColumnDB(globalS,researchColumn,columnPrephix=1,column = 'idUser',table = 'users'):
    connection = getConnection(globalS)
    if columnPrephix == 1:
        sql = 'SELECT ' + researchColumn + ' FROM `' + table + '` WHERE 1'
        print(sql)
    else:
        sql='SELECT ' +researchColumn+' FROM `'+table+'` WHERE '+column+ ' =\'' +columnPrephix+ '\''
        print(sql)
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    finally:
        connection.close()