import sqlite3 as sql
import pandas as pd


def insert_data():
    input_data = pd.read_excel("inventory_data.xlsx")
    conn = sql.connect('my_database.db')
    print ("Opened database successfully")
    cur = conn.cursor()
    try:
        inv_table = "DROP TABLE inventory"
        cus_table = "DROP TABLE customer_balance"

        cur.execute(inv_table)
        cur.execute(cus_table)
        

        conn.execute('CREATE TABLE inventory (itemID INTEGER PRIMARY KEY, itemName TEXT ,cost DECIMAL,QTY INTEGER, cart INTEGER, total_cost DECIMAL, baseQTY INTEGER)')
        print ("Created Table Inventory successfully ...")

        conn.execute('CREATE TABLE customer_balance (customerID INTEGER PRIMARY KEY, c_balance TEXT, remaining_balance TEXT,purchase_amount TEXT, total_cart TEXT)')
        print ("Created Table Customer Balance successfully ...")
        c_b = ("£1087.65",)
        conn.execute("INSERT INTO customer_balance (c_balance) VALUES (?)",(c_b) )
        conn.commit()

        for c, i in enumerate(input_data.iterrows()):
            item_name = i[1]['Item']
            item_cost = i[1]['Cost']
            item_qty  = i[1]['Quantity']
            conn.execute("INSERT INTO inventory (itemName, cost, QTY, cart, baseQTY) VALUES (?,?,?,?,?)",(item_name,item_cost,item_qty,0, item_qty) )
            conn.commit()
        cur.execute("select * from inventory")
   
        rows = cur.fetchall();
        for row in rows:
            print(row)
        print("Try mode")

    except:
        conn.execute('CREATE TABLE inventory (itemID INTEGER PRIMARY KEY, itemName TEXT ,cost DECIMAL,QTY INTEGER, cart INTEGER)')
        print ("Created Table Inventory successfully ...")

        conn.execute('CREATE TABLE customer_balance (customerID INTEGER PRIMARY KEY, c_balance TEXT)')
        print ("Created Table Customer Balance successfully ...")
        c_b = ("£1087.65",)
        conn.execute("INSERT INTO customer_balance (c_balance) VALUES (?)",(c_b) )
        conn.commit()

        for c, i in enumerate(input_data.iterrows()):
            item_name = i[1]['Item']
            item_cost = i[1]['Cost']
            item_qty  = i[1]['Quantity']
            conn.execute("INSERT INTO inventory (itemName, cost, QTY, cart) VALUES (?,?,?,?)",(item_name,item_cost,item_qty,0) )
            conn.commit()
        print("Except mode")

if __name__ == '__main__':
    insert_data()