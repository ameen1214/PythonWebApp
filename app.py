from flask import Flask, render_template, flash, redirect
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'a long string value'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///pyGym.sqlite'

from models import db

db.init_app(app) #Add this line Before migrate line
migrate = Migrate(app, db)

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/register')
def index():  # put application's code here
    return render_template('register.html')

@app.route('/login')
def index():  # put application's code here
    return render_template('login.html')

@app.route('/products')
def index():  # put application's code here
    return render_template('newproducts.html')

@app.route('/memberships')
def index():  # put application's code here
    return render_template('purchasemembership.html')


@app.route('/cart')
def index():  # put application's code here
    return render_template('cart.html')


if __name__ == '__main__':
    app.run()
