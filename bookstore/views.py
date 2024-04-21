from django.shortcuts import render
from .models import Book
from django.db.models import Count
# Create your views here.

def book_li(request):
    books = Book.objects.all()

    # book_filter = Book.objects.filter(title="aaa")
    # print("book_filter",book_filter)

    # first_book = Book.objects.first()
    # print("firstbook", first_book.author)

    # last_book = Book.objects.last()
    # print("last_book", last_book.author)

    # get_va = Book.objects.get(title="aaa")
    # print("getva", get_va.author)

    # exclude_opt = Book.objects.exclude(title="aaa")
    # print("exclude_opt", exclude_opt)

    # count_opt = Book.objects.count()
    # print("count_opt", count_opt)

    # order_by = Book.objects.order_by('title')
    # print("order_by", order_by)

    # val = Book.objects.values('title')
    # print("val", val)

    # val_li = Book.objects.values('title', 'author')
    # print("val_li", val_li)

    # dist = Book.objects.values('title').distinct()
    # print("dist", dist)

    # upda = Book.objects.filter(title="aaa").update(title="vygjhj")
    # print("update", upda)

    # # dele = Book.objects.filter(title="bookname").delete()
    # # print("dele", dele)

    # book_countby_author = Book.objects.values('author').annotate(book_count=Count('id'))
    # print("annotate", book_countby_author)
    return render(request,'book.html', {'books':books})

def set_session(request):
    request.session['author'] = 'vvvvvvb'
    response = render(request,'se.html')
    response.set_cookie('accepttoken','12345')
    return response

def get_session(request):
    author = request.session.get('author','aaa')
    title = request.COOKIES.get('accepttoken', '12345')
    return render(request,'se.html', {'author':author, 'title':title})
