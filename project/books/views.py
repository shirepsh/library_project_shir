import os
from flask import render_template, request, redirect, Blueprint
from project import db
from project.books.models import Books
from project.loans.models import Loans

"""
in this file we are defining the books blue print setting & wrote all the end points that related to books
"""
books = Blueprint('books', __name__, template_folder='templates', static_folder='static')

#display books:
@books.route('/books/', methods = ['GET'])
@books.route('/books/<id>')
def all_books(id = -1):
    if int(id) == -1:
        return render_template('all_books.html', books = Books.query.all())
    if int(id) > -1: 
        book = Books.query.get(int(id))
        return render_template('selected_book.html', book = book)

#search for a book
@books.route('/search_book', methods = ['POST'])
def search_book():
    
    name = request.form['name']
    print(name)
    book = Books.query.filter(Books.book_name == name).first()
    if book is None: 
        print(book)
        return redirect('/books/')
    return redirect(f'/books/{book.book_id}')

#add book 
@books.route("/add_book/", methods=['POST', 'GET'])
def add_book():
    if request.method == "POST":
        book_name = request.form.get("book_name")
        author = request.form.get("author")
        year_published = request.form.get("year_published")
        book_type = request.form.get("book_type")
        book_image = f'{request.form.get("book_image")}.jpeg'

        books_lst= os.listdir("project/static/books")
    
        if book_image not in books_lst:
            book_image = 'no_image.jpeg'

        newBook= Books(book_name, author, year_published, book_type, book_image)
        db.session.add (newBook)
        db.session.commit()
        return render_template('add_book.html', book_add=True)
    return render_template('add_book.html')

#delete book
@books.route("/delete_book/<ind>", methods=['DELETE', 'GET'])
def del_book(ind=-1):
        book=Books.query.get(int(ind))
        if book:
            loans = Loans.query.filter_by(returned= False)
            for loan in loans:
                if loan.book_id == book.book_id:
                    return render_template ('all_books.html', books = Books.query.all(), active_loan=True)
            db.session.delete(book)
            db.session.commit()
        return render_template('delete_book.html', book=book)