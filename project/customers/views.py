import os
from flask import render_template, request, redirect, Blueprint
from project import db
from project.customers.models import Customers
from project.loans.models import Loans

"""
in this file we are defining the customers blue print setting & wrote all the end points that related to customers
"""

customers = Blueprint('customers', __name__, template_folder='templates')

#display customers:
@customers.route('/customers/', methods = ['GET'])
@customers.route('/customers/<id>')
def all_customers(id = -1):
    if int(id) == -1:
        return render_template('all_customers.html', customers = Customers.query.all())
    if int(id) > -1: 
        customer = Customers.query.get(int(id))
        return render_template('selected_customer.html', customer = customer)

#search customer
@customers.route('/search_customer', methods = ['POST'])
def search_customer():
    name = request.form['name']
    customer = Customers.query.filter(Customers.customer_name == name).first()
    if customer is None: 
        return redirect('/customers/')
    return redirect(f'/customers/{customer.customer_id}')

#add Customer 
@customers.route("/add_customer/", methods=['POST', 'GET'])
def add_customer():
    if request.method == "POST":
        customer_name = request.form.get("customer_name")
        city = request.form.get("city")
        age = request.form.get("age")
        customer_image = f'{request.form.get("customer_image")}.jpeg'

        customers_lst= os.listdir("project/static/customers")
        
        if customer_image not in customers_lst:
            customer_image = 'no_image.jpeg'

        newCustomer= Customers(customer_name, city, age, customer_image)
        db.session.add (newCustomer)
        db.session.commit()
        return render_template ('add_customer.html', customer_add=True)
    return render_template ('add_customer.html')

#delete customer
@customers.route("/delete_customer/<ind>", methods=['DELETE', 'GET'])
def del_customer(ind=-1):
        customer=Customers.query.get(int(ind))
        if customer:
            loans = Loans.query.filter_by(returned= False)
            for loan in loans:
                if loan.customer_id == customer.customer_id:
                    return render_template ('all_customers.html', customers = Customers.query.all(), active_loan=True)
            db.session.delete(customer)
            db.session.commit()
        return render_template('delete_customer.html', customer=customer)