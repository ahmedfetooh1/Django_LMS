from django.urls import path 
from . import views 

urlpatterns =[
    path('',views.index,name='index'),
    path('books',views.books,name='books'),
    path('<int:id>',views.update,name='update'),
    path('<int:id>',views.delete,name = 'delete'),
    
]