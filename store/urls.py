from django.urls import path
from .views import detail
from .views import contact 

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('detail/<int:pk>/', detail, name= 'detail'),
 ]

