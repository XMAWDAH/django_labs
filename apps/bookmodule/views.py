from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Address,Student
from django.db.models import Q
from django.db.models import Count, Sum,Max,Min,Avg
from django.shortcuts import  redirect, get_object_or_404
#from .forms import BookForm,AddressForm,StudentForm,StudentForm2,SignUpForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Book


def index(request):
 return render(request, "bookmodule/index.html")

def list_books(request):
 return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')

def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')

def links(request):
 return render(request, 'bookmodule/links.html')

def text(request):
 return render(request, 'bookmodule/text_fromating.html')

def listing(request):
 return render(request, 'bookmodule/listing.html')

def tables(request):
 return render(request, 'bookmodule/table.html')

def search(request):
 if request.method == "POST":
    string = request.POST.get('keyword').lower()
    isTitle = request.POST.get('option1')
    isAuthor = request.POST.get('option2')
    books = __getBooksList()
    newBooks = []
    for item in books:
       contained = False
       if isTitle and string in item['title'].lower(): contained = True
       if not contained and isAuthor and string in item['author'].lower():contained = True
       if contained: newBooks.append(item)
    return render(request, 'bookmodule/list_books.html', {'books':newBooks})
 return render(request, 'bookmodule/base.html')

def __getBooksList(): 
      return Book.objects.all()

def viewbook(request, bookId):
    targetBook = get_object_or_404(Book, id=bookId)
    return render(request, 'bookmodule/show.html', {'book': targetBook})


#lab7

def __insertion_db():
    book1 = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 2)
    book1.save()
    book2 = Book(title = 'Reversing: Secrets of Reverse Engineering', author = 'E. Eilam', edition = 1)
    book2.save()
    book3 = Book(title = 'The Hundred-Page Machine Learning Book', author = 'Andriy Burkov', edition = 1)
    book3.save()
    book4 = Book(title="Clean Code: A Handbook of Agile Software Craftsmanship", author="Robert C. Martin", price=80.0, edition=2)
    book4.save()
    book5 = Book(title="The Pragmatic Programmer: Your Journey to Mastery", author="Andrew Hunt and David Thomas", price=90.0, edition=3)
    book5.save()
    book6 = Book(title="Artificial Intelligence: A Guide to Intelligent Systems", author="Michael Negnevitsky", price=110.0, edition=4)
    book6.save()
    book7 = Book(title="Python Crash Course: A Hands-On Project-Based Introduction to Programming", author="Eric Matthes", price=70.0, edition=1)
    book7.save()
    book8 = Book(title="Refactoring: Improving the Design of Existing Code", author="Martin Fowler", price=100.0, edition=2)
    book8.save()
    address = Address.objects.create(city='Al-Qassim', street='omarbin')
    student = Student.objects.create(name='STAR', age=23, address=address)
    student.save()

def createBook(request):
    mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)
    mybook.save()
    return HttpResponse("Book created successfully")

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lookup_query(request): 
   mybooks=books=Book.objects.filter(author__isnull =  False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10] 
   if len(mybooks)>=1: 
      return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 
   else: 
      return render(request, 'bookmodule/index.html') 


def lab8_task1(request):
   mybooks = Book.objects.filter(Q(price__lte = 50))
   return render(request, 'bookmodule/lab8/task1.html',{'books':mybooks})

def lab8_task2(request):
   mybooks = Book.objects.filter(Q(edition__gt = 2) & (Q(title__icontains='qu')|Q(author__icontains='qu')))
   return render(request, 'bookmodule/lab8/task2.html',{'books':mybooks})

def lab8_task3(request):
    mybooks = Book.objects.filter(~Q(edition__gt = 2) & (~Q(title__icontains='qu')|~Q(author__icontains='qu')))
    return render(request, 'bookmodule/lab8/task3.html',{'books':mybooks})

def lab8_task4(request):
   mybooks = Book.objects.all().order_by('title')
   return render(request, 'bookmodule/lab8/task4.html',{'books':mybooks})

def lab8_task5(request):
    mybooks = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8/task5.html', {'stats': mybooks})
 

def lab8_task6(request):
    city_counts = Address.objects.annotate(student_count=Count('student')).values_list('city', 'student_count')
    city_counts_dict = dict(city_counts)
    return render(request, 'bookmodule/lab8/task6.html', {'city_counts': city_counts_dict})

def lab9_task1(request):
    mybooks = Book.objects.all()
    return render(request, 'bookmodule/lab9/task1.html', {'books': mybooks})

def lab9_task2(request):
        if request.method == "POST":
            title = request.POST.get('title')
            author = request.POST.get('author')
            price = float(request.POST.get('price'))
            edition = int(request.POST.get('edition'))

            Book.objects.create(
                title=title,
                author=author,
                price=price,
                edition=edition
            )

            return redirect('list_books')
        return render(request, 'bookmodule/lab9/task2.html')

def lab9_task3(request, id):
    mybooks = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        mybooks.title = request.POST.get('title')
        mybooks.author = request.POST.get('author')
        mybooks.price = float(request.POST.get('price'))
        mybooks.edition = int(request.POST.get('edition'))
        mybooks.save()
        return redirect('list_books')
    return render(request, 'bookmodule/lab9/task3.html', {'book': mybooks})

def lab9_task4(request, id):
    mybooks = get_object_or_404(Book, id=id)
    mybooks.delete()
    return redirect('list_books')

def list_books_form(request):
    mybooks = Book.objects.all()
    return render(request, 'books/listbooks_form.html', {'books': mybooks})

from .forms import BookForm

def add_book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'books/addbook_form.html', {'form': form})

def edit_book_form(request, id):

    mybooks = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=mybooks)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=mybooks)
    return render(request, 'bookmodule/editbook_form.html', {'form': form, 'book': mybooks})

def delete_book_form(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books')




#-----Lab4----
"""
def index(request):
 return HttpResponse("Hello, world!")

def index(request):
 name = request.GET.get("name") or "world!" #add this line
 return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name

def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))
 
def index(request):
 name = request.GET.get("name") or "world!"
 return render(request, "bookmodule/index.html" , {"name": name}) 

def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)
"""

