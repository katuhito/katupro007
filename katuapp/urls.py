from unicodedata import name
from django.urls import path
from . import views

app = 'katuapp'

urlpatterns = [
    path('', views.index, name='index'),
    # path('page/<int:page_id>/', views.page, name='page'),
    path('article/<int:pk>/', views.article, name='article'),
    path('article/new/', views.new, name='new'),
]