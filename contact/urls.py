from django.urls.conf import path
from . import views

app_name='contact'
urlpatterns = [
    path('',views.sendMessage,name='sendMessage'),
    
    
    ]