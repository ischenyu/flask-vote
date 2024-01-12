import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('flask-layui.sqlite')
        self.cursor = self.conn.cursor()

    def create_table(self):
        sql = """create table user
            (
                id       integer primary key,
                nickname varchar(255),
                mobile   varchar(50),
                password varchar(50)
            );
            """
        self.cursor.execute(sql)
        self.conn.commit()

    def insert(self, nickname, mobile, password):
        sql = 'insert into user(nickname, mobile, password) values (?, ?, ?);'
        self.cursor.execute(sql, (nickname, mobile, password))
        self.conn.commit()

    def search(self, mobile):
        sql = 'select password from user where mobile=?;'
        self.cursor.execute(sql, (mobile,))
        return self.cursor.fetchone()


db = Database()

if __name__ == '__main__':
    db.create_table()
    # db.insert('正心全栈编程', '18675867241', '123456')
    # ret = db.search('18675867241')
    # print(ret)