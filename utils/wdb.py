#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module      : utils.wdb
Function    : DB接続クラス（MySQL）
Author      : K.Shibuya
Version     : 2020/09/21 v1.0.0
History     : 2020/09/21 v1.0.0 K.Shibuya init
              ****/**/** v*.*.* *.******* ****
"""
from utils.config import Config
import MySQLdb


class WDB:
    def __init__(self, db_sec="DB"):
        self._connection = MySQLdb.connect(
            host=Config[db_sec]["host"],
            db=Config[db_sec]["db"],
            user=Config[db_sec]["user"],
            passwd=Config[db_sec]["passwd"],
        )
        self._cursor = self._connection.cursor()
        self._sql = ""
        self._param = {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._cursor.close()
        self._connection.close()

    def beginTran(self):
        self._connection.beginTran()

    def addQuery(self, sql):
        self._sql += sql

    def addParam(self, key, value):
        self._param[key] = value

    def execute(self):
        self._cursor.execute(self._sql, self._param)
        return self._cursor.fetchall()
