IMOVIRTUAL_SELECTORS = {
    'TITILE_SELECTOR'       : '/html/body/div/article/header/div[1]/div/div/h1/text()',
    'PRICE_SELECTOR'        : '/html/body/div/article/header/div[2]/div[1]/div[2]/text()',
    'PRICE_AREA_SELECTOR'   : '/html/body/div/article/header/div[2]/div[2]/div/text()',
    'LOCALIZATION_SELECTOR' : '/html/body/div/article/header/div[1]/div/div/div/a/text()',
    'REAL_STATE_SELECTOR_1' : '/html/body/div/article/div[3]/div[2]/div[3]/ul/li[2]/strong/text()',
    'REAL_STATE_SELECTOR_2' : '/html/body/div/article/div[3]/div[2]/div[4]/ul/li[2]/strong/text()',
    'DESCRIPTION_SELECTOR'  : '/html/body/div/article/div[3]/div[1]/section[2]/div[1]/text()',
}

OLX_SELECTORS = {
    'URL_SELECTOR' : '[class="marginright5 link linkWithHash detailsLink"]::attr(href)',
    'TITLE_SELECTOR' : ['[class="offer-titlebox"]', 'h1::text'],
    'PRICE_SELECTOR' : '[class="xxxx-large not-arranged"]::text',
    'LOCALIZATION_SELECTOR' : ['[class="show-map-link"]', 'strong/text()'],
    
}