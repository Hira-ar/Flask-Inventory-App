from flask import Flask, render_template
from flask import Flask,render_template,redirect, url_for
from flask import request
import sqlite3 as sql
from connect import insert_data
from jinja2 import Template


con = sql.connect("my_database.db",check_same_thread=False)
con.row_factory = sql.Row
cur = con.cursor()
app = Flask(__name__)

@app.route("/")
def Product():


   con = sql.connect("my_database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from inventory")
   
   rows = cur.fetchall();
   for row in rows:
        print(row)
   b = con.cursor()
   b.execute("select * from customer_balance")
   balance = b.fetchall();

   return  render_template('Product.html',rows = rows, balance = balance)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    return render_template('checkout.html')


@app.route('/addcart', methods=['GET', 'POST'])
def addcart():
    if request.method == 'POST':
        total_cart = request.form['checkout']
        
        print("cart value",total_cart)
    con = sql.connect("my_database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("SELECT itemID, itemName, cost, cart FROM inventory WHERE cart!=0;")
   
    rows = cur.fetchall();

    for row in rows:
        print("Per anum",row['cost'])
        print("Qty",row['cart'])
        
        total_cost = round(float(row['cost'].strip("£")) * row['cart'],3)
        print("Total","£"+str(total_cost))
        total_cost = "£"+str(total_cost)
        cur.execute("UPDATE inventory SET total_cost = ? WHERE itemID = ?",(total_cost, row['itemID']) )
    cur.execute("SELECT itemID, itemName, cost, cart, total_cost FROM inventory WHERE cart!=0;")
   
    rows = cur.fetchall();
    grand_total = 0
    for row in rows:
        grand_total = round(float(row['total_cost'].strip("£")) + grand_total,3)
    
    grand_total = "£"+str(grand_total)
    cur.execute("UPDATE customer_balance SET purchase_amount= ? ",(grand_total, ) )
    

    print("Grand total", "£"+str(grand_total))
    b = con.cursor()
    b.execute("select * from customer_balance")
    balance = b.fetchall();
    for row in balance:
        cust_balance = row['c_balance']
    remaining_balance = round(float(cust_balance.strip("£")) - float(grand_total.strip("£")),3)
    
    remaining_balance = "£"+str(remaining_balance)
    cur.execute("UPDATE customer_balance SET remaining_balance= ? ",(remaining_balance, ) )
    
    b = con.cursor()
    b.execute("select * from customer_balance")
    balance = b.fetchall();
    grand_total = float(grand_total.strip("£"))
    cust_balance = float(cust_balance.strip("£"))
    return  render_template('addcart.html',rows = rows, balance = balance, grand_total = grand_total, cust_balance = cust_balance )



@app.route('/delete', methods=['GET', 'POST'])

def delete():
    if request.method == 'POST':
        del_id = request.form['del_id']
        cart_id = request.form['cart_id']
        print("Delete idd", del_id)
        cur.execute("UPDATE inventory SET cart = ? WHERE itemID = ?",(0, del_id) )
        cur.execute("SELECT * FROM inventory WHERE itemID= ?",(del_id))
        cart_inf = cur.fetchall()
        for rows in cart_inf:
            print(rows['baseQTY'])
        for row in cart_inf:
            cur.execute("UPDATE inventory SET QTY = ? WHERE itemID = ?",(row['baseQTY'], del_id) )

        con.commit()
        cur.execute("SELECT itemID, itemName, cost, cart, total_cost FROM inventory WHERE cart!=0;")
   
        rows = cur.fetchall();
    
       
    
    return redirect(url_for('addcart'))
    

@app.route('/cart', methods=['GET', 'POST'])

def cart():

    
    if request.method == 'POST':
        
  
        total_cart=0
        cart = request.form['ct']
        print("cart value",cart)
        pr_id = request.form['pid']
        con = sql.connect("my_database.db")
        con.row_factory = sql.Row
   
        cur = con.cursor()
        cur.execute("Select * from inventory")
        data = cur.fetchall()
        cart = int(cart)
        c = con.cursor()
        c.execute("UPDATE customer_balance SET total_cart = ? ",(cart,) )
        c.execute("SELECT total_cart from customer_balance")
        customer_total_cart = c.fetchall();
        for row in customer_total_cart:
            print("Total cart amount",row['total_cart'])
        
        print(type(data))
        for row in data:
            if row['itemID'] == int(pr_id):
                previous_qut = row['QTY']
        
                pr_id = int(pr_id)
                print("Previous quantity", previous_qut)
                print("Cart value",int(cart))
                if previous_qut >= int(cart):
                    new_qut = previous_qut-int(cart)
                    print("before New quantity", new_qut )
                    print("cond id",pr_id)
                    cur.execute("UPDATE inventory SET QTY = ? WHERE itemID = ?",(new_qut, pr_id) )
                    if row['cart'] != 0:
                        print(row['cart'])
                        cart = row['cart']+cart
                        cur.execute("UPDATE inventory SET cart = ? WHERE itemID = ?",(cart, pr_id) )
                    else:
                        cur.execute("UPDATE inventory SET cart = ? WHERE itemID = ?",(cart, pr_id) )


                    print("New quantity", new_qut )
        cur.execute("select * from inventory")

   
        rows = cur.fetchall();
        for row in rows:
            print(row['cart'])

        print("Try mode")
        cur.execute("select * from inventory")
        cart_total = cur.fetchall();
        t = 0
        dlt = 0
        for row in cart_total:
            t = t+row['cart']
        
        con.commit()
        msg = "Product Deleted"
        
        return redirect(url_for('Product')+"?msg="+str(t))
        con.close()

@app.route('/restock')
def restock():
    insert_data()
    con = sql.connect("my_database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from inventory")
    rows = cur.fetchall();
    return  render_template('Product.html',rows = rows)



if __name__ == '__main__':
    app.run(debug=True)
