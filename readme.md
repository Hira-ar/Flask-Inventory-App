
# Flask Inventory App

## Application Workflow

<p align="justify"> A simple sales management system app in Flask (a Python-based framework for web-based application development). Flask has been used for the backend, and HTML, CSS, and JavaScript have been used for frontend development. SQLite database is used for inventory data storage.</p>
<p align="justify"> I wrote a script "connect.py" that reads data from the Excel file and stores that data in the database.</p>

### Database Tables

1. **inventory**: 
   - Stores `itemId`, `itemName`, `cost` (per item cost), `quantity` (changes as user buys something), `cart` (purchase items quantity), `total_cost` (if the customer adds more than one quantity of the same item), `baseQTY` (original quantity that remains unchanged).

2. **customer_balance**: 
   - Stores `customerID`, `c_balance` (customer's original balance), `remaining_balance` (updated balance left after the customer buys something), `purchase_amount` (total cost of all purchased items), `total_cart` (total quantity of items bought).

### How to Execute the Code?

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hira-ar/Flask-Inventory-App
   cd Flask-Inventory-App
2. **Create and activate a virtual environment:**
	``` bash
	python -m venv venv
	.\venv\Scripts\activate
3. **Install the dependencies:**
	```bash
	  pip install -r requirements.txt
4. **Run the following command to store data in the database (only once):**
	```bash
	  python connect.py
5. **Run the application:**
	```bash
	  python app.py
<p align="justify">
It will show something like below image. You need to copy that address http://127.0.0.1:5000/ in your browser. It will run your application in browser.</p>

![image](https://github.com/Hira-ar/Flask-Inventory-App/assets/94753183/ef93c1aa-1d71-462f-b9d6-6ee1e384d2ad)

6.  "templates" folder have all html files that will run automatically
    on the go.

# **Application working**
>
> Once your app will open in browser it will look like this.

![image](https://github.com/Hira-ar/Flask-Inventory-App/assets/94753183/6a695bb8-cbe5-4945-8814-8cab71648bfc)

  - **Restock:** By clicking "restock", your database will be reset to its original base values. But you need to click again to **Product** to get back to your products page after restock. 
- **Product:** It is your home page where you can made purchase, items will be added to cart.
- **Cart:** To go back from cart page you need to click **product**.

1.  Keep an inventory of stock items and their cost
    -  All items and their cost are displayed and store in database as
        well
2.  Allow the customer to view the current quantity and cost of each
    item
    -  Customer can view all items current quantity and cost of each
        item
3.  Allow the customer to see their current balance
4.  Allow the customer to purchase an item if it is both in stock and
    they have enough money to do so
    -   Customer can enter quantity and click add to cart to add that
        item in cart and can proceed to cart page where he can checkout
        if the item in cart or have enough balance.
5.  Inform the customer if they do not have enough money to purchase an item
    -  If item quantity is not in stock customer will not be able to add
        that quantity in cart.

       ![image](https://github.com/Hira-ar/Flask-Inventory-App/assets/94753183/ac2b4665-18ac-4bb2-bb38-84ad855b3cc9)

    - If the customer has lower balance he will not be able to checkout

        ![image](https://github.com/Hira-ar/Flask-Inventory-App/assets/94753183/267ba140-502e-4f52-8a34-5568b2919260)



6.  Inform the customer if an item is out of stock

   ![image](https://github.com/Hira-ar/Flask-Inventory-App/assets/94753183/64270108-2b27-452f-bcf8-ef50b88c1aba)

    All items in database will be updated.

For inquiries or support,  please contact [iamhira94@gmail.com].

