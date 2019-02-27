import json
from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views import generic
from .models import loan, recommendations, members

class LoanListView(LoginRequiredMixin, ListView):
    model = loan
    template_name = 'mypage/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LoanListView, self).get_context_data(*args, **kwargs)
        context['top_rates'] = loan.objects.filter(id_id = self.request.user.username).order_by('-rate')[:5]
        context['read_books'] = loan.objects.filter(id_id = self.request.user.username)
        context['num_of_read_books'] = loan.objects.filter(id_id = self.request.user.username).count()
        raw_rates = loan.objects.filter(id_id = self.request.user.username).values_list('bName', 'rate')
        rNames = []
        rRates = []
        for key, value in raw_rates:
            rNames.append(key)
            rRates.append(float(value))
        context['bName_list'] = rNames
        context['rate_list'] = rRates
        context['avg_rate'] = loan.objects.filter(id_id = self.request.user.username).aggregate(Avg('rate'))
        context['rec_list'] = recommendations.objects.filter(id_id = self.request.user.username)
        context['profile_pics'] = members.objects.filter(id = self.request.user.username)
        return context