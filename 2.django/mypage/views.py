from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views import generic
from .models import books, loan

class LoanModelView(TemplateView):
    template_name = 'mypage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['loan', 'books']
        return context

class BookListView(ListView):
    print('---BookListView---')
    model = books
    print('---모델 : ',model)
    queryset = books.objects.all().order_by('-loanCnt')[:50]
    template_name = 'mypage/books.html' 
    
class LoanListView(LoginRequiredMixin, ListView):
    print('---LoanListView---')
    model = loan
    print('---모델 : ',model)
    template_name = 'mypage/loan_list.html'

    def get_queryset(self):
        return loan.objects.filter(id_id = self.request.user.username)
        
class LoanDetailView(DetailView):
    model = loan
    def get_object(self):
        return get_object_or_404(loan, pk=self.request.session['loan.id_id'])
  
    # model.objects.all().prefetch_related('books')
