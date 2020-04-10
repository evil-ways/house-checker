# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field



class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Titulo = Field()
    Preco = Field()
    PrecoArea = Field()
    Localizacao = Field()
    Propriedades = Field()
    Caracteristicas = Field()
    Imobiliaria = Field()
    Descricao = Field()
    Tipo = Field()
    Alugar = Field()