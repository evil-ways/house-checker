from django.views.generic import TemplateView

from website.tasks import test_task

import logging

LOGGER = logging.getLogger()

class IndexView(TemplateView):
    template_name = 'website/pages/index.html'

    def get(self, request, *args, **kwargs):
        test_task.delay()
        LOGGER.error('batataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaas')
        return super(IndexView, self).get(request, args, kwargs)
