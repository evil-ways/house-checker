from django.core.management.base import BaseCommand
from scraper.spiders import ImovirtualSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
    help = "Free the Spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(ImovirtualSpider)
        process.start()