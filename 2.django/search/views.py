from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views import generic
from .models import books, loan

class LoanModelView(TemplateView):
    template_name = 'search/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['loan', 'books']
        return context

# 각 table들의 모든 정보 제공하는 view + template
class BookListView(ListView):
    print('---BookListView---')
    model = books
    print('---모델 : ',model)
    queryset = books.objects.all().order_by('-loanCnt')[:50]
    template_name = 'search/books.html' #pages/templates/pages/books.html

class LoanListView(ListView):
    print('---LoanListView---')
    model = loan
    print('---모델 : ',model)
    template_name = 'search/loan.html'

# 조건 검색인 경우 사용하는 generic view
class LoanDetailView(DetailView):
    model = loan
    # model.objects.all().prefetch_related('books')

# class Top30(ListView):
    # model = books
    # queryset = books.objects.all().order_by('-loanCnt')[:30]
    # template_name = 'search/books_top30.html'