from flask import Flask, render_template, request, redirect, url_for
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('.sqlite')
    conn.row_factory = sqlite3.Row
    return conn
class Book():
    def borrow():

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO loans (title, user) VALUES (?, ?)', ())
        conn.commit()
        conn.close()

