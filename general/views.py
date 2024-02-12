from django.views.generic import TemplateView
from hr.models import Company


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.first()
        context['custom_company_logo'] = context['company'].logo if context['company'] else None
        return context
