
from django.urls import include,path
from . import views
from . import api
app_name='book'
urlpatterns = [
    
    path('',views.bookList,name='bookList'),
    path('add',views.addBook,name='addBook'),
    path('editBook/<str:slug>',views.editBook,name='editBook'),
    path('<str:slug>',views.bookDetails,name='book_details'),
    path('api/list',api.bookListApi,name='bookListApi'),
]