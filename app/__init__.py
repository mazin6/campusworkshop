"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr1iheuhlq287cmjh0-a.oregon-postgres.render.com",
        database="task_t5b7",
        user="task_t5b7_user",
        password="hujjQU3pwn3SyHBTO95Prreh5qOt6JKD")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
