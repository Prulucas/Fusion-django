from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Services, Member, Features
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Services.objects.order_by('?').all()
        context['member'] = Member.objects.order_by('?').all()
        context['features'] = list(Features.objects.order_by('?')[:6])
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao tentar enviar mensagem!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


'''
class NotFoundView(TemplateView):
    template_name = '404.html'
'''
