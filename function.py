


def creatDataBase(name,connection):
    sql='CREATE TABLE `%s` ( `id` INT(11) NOT NULL AUTO_INCREMENT , `userName` VARCHAR(255) NOT NULL , `value` INT(11) NOT NULL , `colMate` INT(11) NOT NULL , `colGood` INT(11) NOT NULL , `stat` INT(11) NOT NULL , PRIMARY KEY (`id`) USING BTREE) ENGINE = InnoDB;'
    try:
        cursor = connection.cursor()
        print(name)
        # Выполнить sql и передать 1 параметр.
        cursor.execute(sql,name)

        connection.commit()
    finally:
        # Закрыть соединение
        connection.close()