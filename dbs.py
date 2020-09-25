import sqlite3
conn=sqlite3.connect("details.db")
print("Database connected")
conn.execute("Create table Product(Prod_id varchar PRIMARY KEY)")
conn.execute("Create table Location(Location_id INTEGER NOT NULL)")
conn.execute("Create table ProdMove(move_id INTEGER NOT NULL,Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,from_location TEXT,to_location TEXT,Prod_id varchar NOT NULL,Qty Integer)")
print("Tables created successfully")
conn.close()