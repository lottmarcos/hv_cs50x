import os
import datetime

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    #Create a table for index
    table = db.execute("SELECT symbol, SUM(shares) FROM transactions WHERE user_id=:user_id GROUP BY symbol HAVING SUM(shares) > 0", user_id=session["user_id"])

    #Storig data
    symbols = []
    all_total = 0

    for row in table:
        stock = lookup(row['symbol'])
        sum_value = (stock["price"] * row["SUM(shares)"])
        symbols.append({"symbol": stock["symbol"], "name": stock["name"], "shares": row["SUM(shares)"], "price": usd(stock["price"]), "total": usd(sum_value)})
        all_total += stock["price"] * row["SUM(shares)"]

    rows = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])
    cash = rows[0]["cash"]
    all_total += cash

    return render_template("index.html", symbols=symbols, cash=usd(cash), all_total=usd(all_total))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "GET":
        return render_template("buy.html")

    else:
        #Handle the shares
        shares = float(request.form.get("shares"))
        if shares < 0:
            return apology("share is not allowed")

        #handle the symbols
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must have a symbol")

        stock = lookup(symbol.upper())
        if stock == None:
            return apology("symbol does not exist")

        #Make the transaction
        value = shares * stock["price"]
        user_id = session["user_id"]

        db_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_cash = db_cash[0]["cash"]

        if user_cash < value:
            return apology("not enough money")

        update_cash = user_cash - value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", update_cash, user_id)
        date = datetime.datetime.now()
        db.execute("INSERT INTO transactions(user_id, symbol, shares, price, date) VALUES(?, ?, ?, ?, ?)", user_id, stock["symbol"], shares, stock["price"], date)

        #Display a message confirming that the transaction went great
        flash("Bought!")

        return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    transactions = db.execute("SELECT symbol, shares, price, date FROM transactions WHERE user_id = ?", session["user_id"])
    for i in range(len(transactions)):
        transactions[i]["price"] = usd(transactions[i]["price"])
    return render_template("history.html", transactions=transactions)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "GET":
        return render_template("quote.html")

    else:
        #Handle the symbols
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must have a symbol")

        #Handle the stocks and returns
        stock = lookup(symbol.upper())
        if stock == None:
            return apology("symbol does not exist", 400)

        else:
            return render_template("quoted.html", stock = {'name': stock['name'], 'symbol': stock['symbol'], 'price': usd(stock['price'])})

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "GET":
        return render_template("register.html")

    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        #Check users inputs
        if not username:
            return apology("username can not be blank")
        if not password:
            return apology("password can not be blank")
        if not confirmation:
            return apology("must give confirmation")
        if confirmation != password:
            return apology("confirmation does not match")

        #Encrypt the user password
        hash_password = generate_password_hash(password)

        #Stores the users data
        try:
            user = db.execute("INSERT INTO users(username, hash) VALUES (?, ?)", username, hash_password)
        except:
            return apology("user already exists")

        #Set the user entrance to the website
        session["user_id"] = user
        return redirect("/")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "GET":
        user_id = session["user_id"]
        user_symbols = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", user_id)
        return render_template("sell.html", symbols = [row["symbol"] for row in user_symbols])

    else:
        #Ensure stock was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        #Ensure shares was submitted
        elif not request.form.get("shares"):
            return apology("must provide shares", 403)

        #Ensure shares is greater than 0
        elif int(request.form.get("shares")) < 0:
            return apology("must provide a valid number of shares", 403)

        #Ensure shock exists
        if not request.form.get("symbol"):
            return apology("must provide an existing symbol", 403)


        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)

        rows = db.execute("SELECT symbol, SUM(shares) FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", session["user_id"])

        # Value of transaction
        shares = int(request.form.get("shares"))
        for row in rows:
            if row["symbol"] == symbol:
                if shares > row["SUM(shares)"]:
                    return apology("you're doing something wrong", 400)

        transaction = shares * stock['price']

        # Check if user has enough cash for transaction
        user_cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = user_cash[0]["cash"]

        # Subtract user_cash by value of transaction
        updt_cash = cash + transaction

        # Update how much left in his account (cash) after the transaction
        db.execute("UPDATE users SET cash = ? WHERE id = ?", updt_cash, session["user_id"]);
        # Update de transactions table
        date = datetime.datetime.now()
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)", session["user_id"], stock['symbol'],  -1 * shares, stock['price'], date)
        flash("Sold!")
        return redirect("/")

def error_checker(e):
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(error_checker)