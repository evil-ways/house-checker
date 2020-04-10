import scrapy
from scraper.scraper.items import ScraperItem
from scraper.scraper.settings import USER_AGENT

#from config import URL
URL = "https://www.imovirtual.com/comprar/apartamento/"


class ImovirtualSpider(scrapy.Spider):
    name = "Imovirtual_Comprar_Apartamento"
    
    #allowed_domains = ['https://www.imovirtual.com/']
    start_urls = [URL]
    
    def parse(self, response):
        # process each house link
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
        house = ScraperItem()
        #house = dict()
        
        house['Titulo'] = response.xpath('/html/body/div/article/header/div[1]/div/div/h1/text()').extract() 
        house['Preco'] = response.xpath('/html/body/div/article/header/div[2]/div[1]/div[2]/text()').extract()[0].replace('€', '').replace(' ', '')
        house['Alugar'] = 'Nao'
        house['Tipo'] = 'apartamento'
        house['PrecoArea'] = response.xpath('/html/body/div/article/header/div[2]/div[2]/div/text()').extract()[0] 
        house['Localizacao'] = response.xpath('/html/body/div/article/header/div[1]/div/div/div/a/text()').extract()[0]

        propriedades_dict = dict()
        keys = [k.split(':')[0] for k in response.css('.css-2fnk9o').xpath('ul/li/text()').extract()]     
        values = response.css('.css-2fnk9o').xpath('ul/li//strong//text()').extract() 
        for k, v in zip(keys,values):
            propriedades_dict[k] = v

        house['Propriedades'] = propriedades_dict
        house['Caracteristicas'] = response.css('.css-1bpegon').xpath('ul/li/text()').extract()
        
        try:
            house['Imobiliaria'] = response.xpath('/html/body/div/article/div[3]/div[2]/div[3]/ul/li[2]/strong/text()').extract()[0]
        except IndexError:
            house['Imobiliaria'] = response.xpath('/html/body/div/article/div[3]/div[2]/div[4]/ul/li[2]/strong/text()').extract()[0]
            
        house['Descricao'] = " ".join(response.xpath('/html/body/div/article/div[3]/div[1]/section[2]/div[1]/text()').extract())    
        yield house