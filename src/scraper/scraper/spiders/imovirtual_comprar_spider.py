import scrapy
from scraper.scraper.items import ScraperItem
from scraper.scraper.settings import URLS_IMOVIRTUAL
from scraper.scraper.selectors import IMOVIRTUAL_SELECTORS, OLX_SELECTORS

from scraper.scraper.settings import USER_AGENT, HTTPCACHE_ENABLED 
from scraper.scraper.settings import ITEM_PIPELINES, ITEM_PIPELINES_OLX 


class ImovirtualSpider(scrapy.Spider):
    
    name = "Imovirtual"
    
    start_urls = URLS_IMOVIRTUAL
    
    custom_settings = {
        'USER_AGENT': USER_AGENT,
        'HTTPCACHE_ENABLED':HTTPCACHE_ENABLED,
        'DOWNLOAD_DELAY': 2,
        'ITEM_PIPELINES': ITEM_PIPELINES,
    }

    house = ScraperItem()

    ad_type = []
    
    def parse(self, response):
        # process each house link
        self.ad_type = response.url.split('/')
        
        urls = response.css('.offer-item-details').xpath('header/h3/a/@href').extract() 
        for url in urls:
            #url = response.urljoin(url)
            
            yield scrapy.Request(
                    url, callback=self.parse_housepage)   

        # process next page
        # next_page_url = response.xpath('//a[text()="Next"]/@href').extract_first()
        # absolute_next_page_url = response.urljoin(next_page_url)
        # request = scrapy.Request(absolute_next_page_url)
        # yield request
    
    def parse_housepage(self, response):
        

        self.house['Alugar'] = self.ad_type[-3]
        self.house['Tipo'] = self.ad_type[-2]
        

        self.house['Titulo'] = response.xpath(
                        IMOVIRTUAL_SELECTORS['TITILE_SELECTOR']
                        ).extract() 
        
        self.house['Preco'] = response.xpath(
                        IMOVIRTUAL_SELECTORS['PRICE_SELECTOR']
                        ).extract()[0].replace('€', '').replace(' ', '')
        
        self.house['PrecoArea'] = response.xpath(
                            IMOVIRTUAL_SELECTORS['PRICE_AREA_SELECTOR']
                            ).extract()[0] 

        self.house['Localizacao'] = response.xpath(
                            IMOVIRTUAL_SELECTORS['LOCALIZATION_SELECTOR']
                            ).extract()[0]

        propriedades_dict = dict()
        keys = [k.split(':')[0] for k in response.css('.css-2fnk9o').xpath('ul/li/text()').extract()]     
        values = response.css('.css-2fnk9o').xpath('ul/li//strong//text()').extract() 
        for k, v in zip(keys,values):
            propriedades_dict[k] = v

        self.house['Propriedades'] = propriedades_dict
        self.house['Caracteristicas'] = response.css('.css-1bpegon').xpath('ul/li/text()').extract()
        
        try:
            self.house['Imobiliaria'] = response.xpath(
                            IMOVIRTUAL_SELECTORS['REAL_STATE_SELECTOR_1']
                            ).extract()[0]
        except IndexError:
            self.house['Imobiliaria'] = response.xpath(
                            IMOVIRTUAL_SELECTORS['REAL_STATE_SELECTOR_2']
                            ).extract()[0]
            
        self.house['Descricao'] = " ".join(response.xpath(
                            IMOVIRTUAL_SELECTORS['DESCRIPTION_SELECTOR']
                            ).extract())    
        yield self.house
