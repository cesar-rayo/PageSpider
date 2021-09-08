import sqlite3 as lite
import logging

LOGGER = logging.getLogger(__name__)


def create_database(database_path):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists words")
        ddl = "CREATE TABLE main.words(word TEXT PRIMARY KEY NOT NULL, usage_count INT DEFAULT 1 NOT NULL );"
        cur.execute(ddl)
        ddl = "CREATE UNIQUE INDEX words_word_unidex ON words(word);"
        cur.execute(ddl)
    LOGGER.info("Connected to Database!")


def save_words_to_database(database_path, words_list):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in words_list:
            sql = "select count(word) from words where word='{}'".format(word)
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word='{}'".format(word)
            else:
                sql = "insert into words(word) values ('{}')".format(word)
            cur.execute(sql)
    LOGGER.info("Database save complete!")
