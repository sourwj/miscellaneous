from django.urls import path
# from django.conf.urls import url
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.LoanModelView.as_view(), name = 'index'),
    path('books/', views.BookListView.as_view(), name='books_list'),
    path('loan/', views.LoanListView.as_view(), name='loan_list'),
    path('books/<int:pk>/', views.LoanDetailView.as_view(), name='loan_detail'),
]