from django.views.generic import TemplateView

from scraper.scraper.spiders.imovirtual_comprar_spider import ImovirtualSpider
from scraper.scraper.spiders.olx_splider import OlxlSpider
from scrapy.crawler import CrawlerProcess
from scraper.scraper.settings import USER_AGENT, HTTPCACHE_ENABLED 
from scraper.scraper.settings import ITEM_PIPELINES, ITEM_PIPELINES_OLX 



class IndexView(TemplateView):
    #$print(settings['USER_AGENT'])
    #print('O'*50)
    process = CrawlerProcess()
    process.crawl(ImovirtualSpider)
    process.crawl(OlxlSpider)
    process.start()

    template_name = 'website/pages/index.html'
