from django.urls import path
# from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'mypage'
urlpatterns = [
    path('', views.LoanModelView.as_view(), name = 'index'),
    path('books/', views.BookListView.as_view(), name='books_list'),
    path('loan/', views.LoanListView.as_view(), name='loan_list'),
    path('loan/', views.LoanDetailView.as_view(), name='loan_detail'),

    # path('books/encore<int:num><int:num>/', views.LoanDetailView.as_view(), name='loan_detail'),
    # path('books/unknown<int:num><int:num><int:num>/', views.LoanDetailView.as_view(), name='loan_detail'),
    # path('books/master<int:num><int:num>/', views.LoanDetailView.as_view(), name='loan_detail'),
]