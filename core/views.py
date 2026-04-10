from django.views.generic import TemplateView
from .models import Services, Member, Features


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Services.objects.order_by('?').all()
        context['member'] = Member.objects.order_by('?').all()
        context['features'] = list(Features.objects.order_by('?')[:6])
        return context


'''
class NotFoundView(TemplateView):
    template_name = '404.html'
'''
