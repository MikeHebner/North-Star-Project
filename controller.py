import sqlite3 as sql
from typing import Tuple
import pandas as pd
# import guiwindow
import sys

# Test: Connect to Database and execute query
conn = sql.connect('identifier.sqlite')
cursor = conn.execute("SELECT * FROM Student")
for row in cursor:
    print("ID: ", row[0])
    print("NAME: ", row[1])
