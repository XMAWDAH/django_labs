from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links/', views.links, name="books.links"),
 path('html5/text/formating', views.text, name="text.links"), 
 path('html5/listing', views.listing, name="listing.links"),
 path('html5/tables', views.tables, name="tables.links"),
 path('search/', views.search, name="search.links"),
 path('<int:bookId>', views.viewbook), 

 
]
