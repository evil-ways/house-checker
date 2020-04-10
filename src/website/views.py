from django.views.generic import TemplateView

from scraper.scraper.spiders.imovirtual_comprar_spider import ImovirtualSpider
from scrapy.crawler import CrawlerProcess
from scraper.scraper.settings import USER_AGENT, HTTPCACHE_ENABLED 



class IndexView(TemplateView):
    #$print(settings['USER_AGENT'])
    #print('O'*50)
    process = CrawlerProcess({
        'USER_AGENT':USER_AGENT,
        'HTTPCACHE_ENABLED':HTTPCACHE_ENABLED
        })
    process.crawl(ImovirtualSpider)
    process.start()

    template_name = 'website/pages/index.html'
