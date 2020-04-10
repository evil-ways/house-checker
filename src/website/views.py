from django.views.generic import TemplateView

from scraper.scraper.spiders.imovirtual_comprar_spider import ImovirtualSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings



class IndexView(TemplateView):
    process = CrawlerProcess(get_project_settings())
    process.crawl(ImovirtualSpider)
    process.start()

    template_name = 'website/pages/index.html'
