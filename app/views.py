from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from app.models import Book, Transaction

# Create your views here.


def home(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


def borrow_book(request, id):
    book = Book.objects.get(id=id)
    if book.in_stock == True:
        book.in_stock = False
        book.save()
        messages.success(request, f"Borrowed {book.title} by {book.author}")
        book_transaction = Transaction.objects.create(
            date_time=datetime.now(), action="CHECKOUT", book=book
        )
        book_transaction.save()
        return redirect("home")
    elif book.in_stock == False:
        messages.error(request, f"{book.title} by {book.author} is unavailable")
        return redirect("home")


def return_book(request, id):
    book = Book.objects.get(id=id)
    if book.in_stock == False:
        book.in_stock = True
        book.save()
        messages.success(request, f"Returned {book.title} by {book.author}")
        book_transaction = Transaction.objects.create(
            date_time=datetime.now(), action="CHECKIN", book=book
        )
        book_transaction.save()
        return redirect("home")
    elif book.in_stock == True:
        messages.error(request, f"{book.title} by {book.author} is already here")
        return redirect("home")

