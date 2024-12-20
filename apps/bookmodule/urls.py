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
 path('simple/query', views.simple_query, name="simple_query"),
 path('complex/query', views.lookup_query, name="lookup_query"),
 path('lab8/task1',views.lab8_task1,name="Lab8_Task1"),
 path('lab8/task2',views.lab8_task2,name="Lab8_Task2"),
 path('lab8/task3',views.lab8_task3,name="Lab8_Task3"),
 path('lab8/task4',views.lab8_task4,name="Lab8_Task4"),
 path('lab8/task5',views.lab8_task5,name="Lab8_Task5"),
 path('lab8/task6', views.lab8_task6, name = "Lab8_task6"),
 path('lab9/task1/', views.lab9_task1, name='list_books'),
 path('lab9/task2/', views.lab9_task2, name='add_book'),
 path('lab9/task3/<int:id>/', views.lab9_task3, name='edit_book'),
 path('lab9/task4/<int:id>/', views.lab9_task4, name='delete_book'),
 path('lab9_part2/editbook/<int:id>', views.edit_book_form, name='edit_book_form'),
 path('lab9_part2/deletebook/<int:id>', views.delete_book_form, name='delete_book_form'),

 path('lab10/studentlist/',views.student_list,name="student_list"),
 path('lab10/add/',views.student_add,name="student_add"),
 path('lab10/update<bID>',views.student_update,name="student_update"),
 path('lab10/delete<bID>', views.student_delete, name='student_delete'),
 path('lab10/addStudent2', views.addStudent2, name= "addStudent2"),
 path('lab10/listStudent2', views.student_list2, name= "listStudent2"),
 path('lab10/deleteStudent2/<bID>', views.deleteStudent2, name= "deleteStudent2"),
 path('lab10/editStudent2/<bID>', views.editStudent2, name= "editStudent2"),
 path('lab10/upload_image', views.upload_image, name= "upload_image"),
 path('lab10/image_list', views.image_list, name= "image_list"),
]
