# coding: utf-8


import MySQLdb


class MySQL(object):
    def __init__(self, dba, ismaster):
            "docstring"
            self.conn = None
            self.cur = None
            self.db = dba.get('db')

    def __del__(self):
        self.close()

    def connect(self, dba):
        self.conn = MySQLdb.connect()
        self.cur = self.conn.cursor()
        self.cur.execute('set names utf8')
        self.cur.execute('set autocommit = 1')

    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


class MySQLPool(object):
    def __init__(self, dbconf):
        "docstring"
        self.mdbpool, self.sdbpool = {}, {}

    def getdb(self):
        pass

    def disconnect(self):
        for db in self.mdbpool:
            db.close()
        for db in self.sdbpool:
            db.close()
