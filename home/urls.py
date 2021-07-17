from django.urls.conf import path
from . import views

app_name='home'
urlpatterns = [
    path('',views.homePage,name='homepage'),
    
    
    ]