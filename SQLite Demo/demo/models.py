from email.policy import default
from enum import unique
from unicodedata import category
from sqlalchemy.sql.expression import false
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Customer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    complaints = db.relationship("Complaint", backref = "customer", lazy = "dynamic")
    # todo add authentication

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String(100))
    salary = db.Column(db.Float)
    complaints = db.relationship("Complaint", backref = "employee")

class Shops(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    products = db.relationship('Products', backref = 'shop')

class Products(db.Model):
    name = db.Column(db.String(128))
    id = db.Column(db.Integer, primary_key = True, unique = True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))
    category = db.Column(db.String(128))
    maker = db.Column(db.String(128))
    price = db.Column(db.Float)
    # todo add price history

class Order(db.Model):
    # todo too lazy to deal with orders for now
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id')) # ? needs a foreign key, so it knows which custoiemr the order belongs to
    customer = db.relationship('Customer', backref = 'orders')
    order_date = db.Column(db.DateTime(timezone = False), default = func.now())
    order_status = db.Column(db.String(128))

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    complaint_date = db.Column(db.DateTime(timezone = False), default = func.now())
    complaint_closed = db.Column(db.Boolean, default = False)
    complaint_closed_date = db.Column(db.DateTime(timezone = False), default = None)
