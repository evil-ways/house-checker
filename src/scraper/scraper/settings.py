# -*- coding: utf-8 -*-

# Scrapy settings for scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import sys


# # DJANGO INTEGRATION
sys.path.append(os.path.dirname(os.path.abspath('.')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'houseChecker.settings.base'

# This is required only if Django Version > 1.8
import django
django.setup()


BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scraper.middlewares.ScraperSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scraper.middlewares.ScraperDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scraper.scraper.pipelines.ScraperPipeline': 300,
}

ITEM_PIPELINES_OLX = {
    'scraper.scraper.pipelines.ScraperPipelineOLX': 300,
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


URLS_IMOVIRTUAL = [
        "https://www.imovirtual.com/comprar/apartamento/",
        "https://www.imovirtual.com/arrendar/apartamento/",
        "https://www.imovirtual.com/ferias/apartamento/",

        "https://www.imovirtual.com/comprar/moradia/",
        "https://www.imovirtual.com/arrendar/moradia/",
        "https://www.imovirtual.com/ferias/moradia/",

        "https://www.imovirtual.com/arrendar/quarto/",

        "https://www.imovirtual.com/comprar/terreno/",
        "https://www.imovirtual.com/arrendar/terreno/",

        "https://www.imovirtual.com/comprar/loja/",
        "https://www.imovirtual.com/arrendar/loja/",

        "https://www.imovirtual.com/comprar/armazem/",
        "https://www.imovirtual.com/arrendar/armazem/",

        "https://www.imovirtual.com/comprar/garagem/",
        "https://www.imovirtual.com/arrendar/garagem/",

        "https://www.imovirtual.com/comprar/escritorio/",
        "https://www.imovirtual.com/arrendar/escritorio/",

        "https://www.imovirtual.com/comprar/predio/",
        "https://www.imovirtual.com/arrendar/predio/",

        "https://www.imovirtual.com/comprar/quintaeherdade/",
        "https://www.imovirtual.com/arrendar/quintaeherdade/",

        "https://www.imovirtual.com/comprar/trespasse/",

    ]

URLS_OLX = []
