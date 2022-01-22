import json
import random
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import *
from . import db
from datetime import datetime, timedelta
views = Blueprint("views", __name__)

@views.route("/", methods = ["GET", "POST"])
def home():
    # list all customers
    customers = Customer.query.all()

    # from all customers, find the first that made complaints
    for customer in customers:
        if customer.complaints:
            complainer = customer # should be jovian
            break

    # get the first complaint of complainer
    complaint = complainer.complaints.first() #? complainer.complaints is a list of all complaints from jovian, first returns the first one

    # get the employee who made the complaint
    employee = complaint.employee 
    
    string = f"{complainer.name} has {complainer.complaints.count()} complaints. the first complaint was made by {employee.name}"
    return string

@views.route("/creation", methods = ["GET", "POST"])
def creation():
    create_shop()
    create_employee()
    create_customer()
    return redirect(url_for("views.home"))

def create_customer():
    # create 2 customers named jovian and timothy
    jovian = Customer(name = "Jovian", id = 1)
    timothy = Customer(name = "Timothy", id = 2)
    db.session.add(jovian)
    db.session.add(timothy)
    # commit the changes
    db.session.commit()
    create_complaint(jovian)

def create_shop():
    # create one shop called mcdonalds
    id = random.randint(1, 100)
    mcdonalds = Shops(name = "McDonalds", id = id)
    db.session.add(mcdonalds)
    db.session.commit()
    create_products(mcdonalds)

def create_products(shop):
    # create big mac
    shop_id = shop.id
    big_mac = Products(
        name = "Big Mac",
        id = random.randint(1, 100),
        shop_id = shop_id, # this is the foreign key
        category = "Food",
        maker = "McDonalds",
        price = 10.00
    )
    db.session.add(big_mac)
    db.session.commit()

def create_employee():
    eliezer = Employee(
        name = "Eliezer",
        id = 1,
        salary = 100000.00
    )

    josh = Employee(
        name = "Josh",
        id = 2,
        salary = 100000.00
    )

    db.session.add(eliezer)
    db.session.add(josh)
    db.session.commit()

def create_complaint(complainer):
    # choose a random employee
    employee = Employee.query.all()
    employee = random.choice(employee)
    # create a complaint
    complaint = Complaint(
        id = random.randint(1, 100),
        customer_id = complainer.id,
        employee_id = employee.id,
    )

    db.session.add(complaint)
    db.session.commit()