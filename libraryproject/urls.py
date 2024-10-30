from django.contrib import admin
from django.urls import include, path

urlpatterns = [
 path('admin/', admin.site.urls),
 path('books/', include("apps.bookmodule.urls")), #include urls.py of bookmodule app
 path('users/', include("apps.usermodule.urls")) #include urls.py of usermodule app
]
