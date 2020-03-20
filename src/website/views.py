from django.views.generic import TemplateView

from website.tasks import test_task


class IndexView(TemplateView):
    template_name = 'website/pages/index.html'

    def get(self, request, *args, **kwargs):
        test_task.delay()
        return super(IndexView, self).get(request, args, kwargs)
