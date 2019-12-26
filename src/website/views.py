from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'website/pages/index.html'
