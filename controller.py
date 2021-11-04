import sqlite3 as sql
from typing import Tuple
import pandas as pd
import guiwindow
import sys

def open_db(filename: str) -> Tuple[sql.Connection, sql.Cursor]:
    db_connection = sql.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor