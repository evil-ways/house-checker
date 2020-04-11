import scrapy
from scraper.scraper.items import ScraperItemOLX
from scraper.scraper.settings import URLS_IMOVIRTUAL
from scraper.scraper.selectors import IMOVIRTUAL_SELECTORS, OLX_SELECTORS

from scraper.scraper.settings import USER_AGENT, HTTPCACHE_ENABLED 
from scraper.scraper.settings import ITEM_PIPELINES, ITEM_PIPELINES_OLX 

class OlxlSpider(scrapy.Spider):
    name = "OLX"

    start_urls = ["https://www.olx.pt/imoveis/"]

    custom_settings = {
        'USER_AGENT': USER_AGENT,
        'HTTPCACHE_ENABLED':HTTPCACHE_ENABLED,
        'DOWNLOAD_DELAY': 2,
        'ITEM_PIPELINES': ITEM_PIPELINES_OLX,
    }

    def parse(self, response):
        # process each house link
        

        urls = response.css(OLX_SELECTORS['URL_SELECTOR']).extract()   
        urls = [url for url in urls if url.split('/')[2] != 'www.imovirtual.com']

        for url in urls:
            #url = response.urljoin(url)
        
            yield scrapy.Request(
                    url, callback=self.parse_housepage) 
             
            #yield {'url': url}
        # process next page
        # next_page_url = response.xpath('//a[text()="Next"]/@href').extract_first()
        # absolute_next_page_url = response.urljoin(next_page_url)
        # request = scrapy.Request(absolute_next_page_url)
        # yield request
    
    def parse_housepage(self, response):
        #house = HousescraperItem()
        
        house = ScraperItemOLX()

        house['Titulo'] = response.css(
                        OLX_SELECTORS['TITLE_SELECTOR'][0]
                        ).css(
                            OLX_SELECTORS['TITLE_SELECTOR'][1]
                        ).extract()[0].strip() 
        
        house['Preco'] = response.css(
                        OLX_SELECTORS['PRICE_SELECTOR']
                        ).extract()[0]
        
        house['Localizacao'] = response.css(
                            OLX_SELECTORS['LOCALIZATION_SELECTOR'][0]
                            ).xpath(
                                OLX_SELECTORS['LOCALIZATION_SELECTOR'][1]
                            ).extract()[0] 

        #house['PrecoArea'] = response.xpath('/html/body/div/article/header/div[2]/div[2]/div/text()').extract()[0] 
        

        propriedades_dict = dict()
        keys = response.css('[class="details fixed marginbott20 margintop5 full"]').xpath('tr/td/table/tr/th/text()').extract()   
        values = [value.strip() for value in response.css('[class="details fixed marginbott20 margintop5 full"]').xpath('tr/td/table/tr/td/strong/a/text()').extract()]
        for k, v in zip(keys,values):
            propriedades_dict[k] = v

        house['Propriedades'] = propriedades_dict
        #house['Caracteristicas'] = response.css('.css-1bpegon').xpath('ul/li/text()').extract()
        #house['Imobiliaria'] = response.xpath('/html/body/div/article/div[3]/div[2]/div[3]/ul/li[2]/strong/text()').extract()[0]
        house['Descricao'] =  response.css('[id="textContent"]::text').extract()[0].strip()

        
        yield house