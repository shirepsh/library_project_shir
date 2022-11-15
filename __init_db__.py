from project import db, app
from project.books.models import Books
from project.customers.models import Customers
from project.loans.models import Loans
from datetime import date


book1 = Books(book_name= "Peter pan", author="Sir James Matthew Barrie", year_published=1953, book_type="1 - loan time up to 10 days", book_image="peter_pan.jpeg")
book2 = Books(book_name= "Da Vinci Code", author="Dan Brown", year_published=2003, book_type="2 - loan time up to 5 days", book_image="no_image.jpeg")
book3 = Books(book_name= "Harry Potter and the Philosopher's Stone", author="Joanne Rowling", year_published=1997, book_type="1 - loan time up to 10 days", book_image="harry_potter.jpeg")
book4 = Books(book_name= "Rosie project", author="Graeme Simsion", year_published=2013, book_type="3 - loan time up to 2 days", book_image="rosie_project.jpeg")

customer1= Customers(customer_name="roee meshulam", city="tel aviv", age=26, customer_image="roee_meshulam.jpeg")
customer2= Customers(customer_name="alon levi", city="holon", age=11, customer_image="no_image.jpeg")
customer3= Customers(customer_name="talia saglam", city="hadera", age=22, customer_image="talia_saglam.jpeg")
customer4= Customers(customer_name="nava eliya", city="natania", age=22, customer_image="nava_eliya.jpeg")


loan1 = Loans(customer_id= 1, book_id =2 , loan_date=date(2022, 10, 10), return_date=date(2022, 10, 18))
loan2 = Loans(customer_id= 2, book_id =3 , loan_date=date(2022, 10, 20), return_date=date(2022, 10, 28))
loan3 = Loans(customer_id= 3, book_id =4 , loan_date=date(2022, 10, 2 ), return_date=date(2022, 10, 10))
loan4 =Loans(customer_id= 4, book_id=1, loan_date=date(2022, 11, 1), return_date=date(2022, 10, 18))


with app.app_context():

    db.session.add_all([book1, book2,book3, book4])
    db.session.add_all([customer1, customer2 ,customer3 , customer4])
    db.session.add_all([loan1, loan2,loan3, loan4])

    db.session.commit()

