import json
import requests
import numpy as np

from bs4 import BeautifulSoup

class Scraper:
    '''
    This class implements an easy way to scrape the main home market sites in Portugal
    Website already suppoted:
        -- olx
        -- custojusto

    Attributes
    ----------
    site : str
        the site to be scraped
    houses : str
        url of houses to be scraped

    Methods
    -------
    crawl_index(number_pages)
        Scrape the Site until the page = number_pages
        Save the url of scraped houses in house atribute

    crawl_houses(already_scraped)
        Scrape all houses in atribute houses except houses that are in already_scraped list
    '''
    def __init__(self, site):

        if site == 'olx':
            self.site = 'olx'
            self.URL = "https://www.olx.pt/imoveis/?page={}"
        elif site == 'custojusto':
            self.site = 'custojusto'
            self.URL = "https://www.custojusto.pt/portugal/imobiliario?o={}"
        self.houses = []

    def crawl_index(self, number_pages):
        i = 1
        while i <= number_pages:
            page = requests.get(self.URL .format(i))
            soup = BeautifulSoup(page.text, 'html.parser')
            if self.site == 'olx':
                links = soup.find_all(class_="lheight22 margintop5")
                for link in links:
                    self.houses.append(link.find('a', href=True)['href'])
            elif self.site == 'custojusto':
                links = soup.find_all('div', class_="container_related")
                
                for link in links:
                    try:
                        self.houses.append(link.find('a').get('href'))
                    except:
                        continue
            i +=1
    def crawl_houses(self, already_scraped):
        try:
            if len(self.houses) <= 0:
                raise ValueError
            house_atributes = list()
            for house in self.houses:
                if house not in already_scraped:
                    if self.site == 'olx':
                        atributes = scrap_olx(house)
                        house_atributes.append(atributes)
                    elif self.site == 'custojusto':
                        atributes = scrap_custojusto(house)
                        house_atributes.append(atributes)

            return json.dumps(house_atributes)
        except ValueError:
            print("Don't have houses to scrape.\n Please use 'crawl_index'")

def scrap_olx(house):
    atributes = dict()

    page = requests.get(house)
    soup = BeautifulSoup(page.text, 'html.parser')

    try:
        atributes['Title'] = soup.find('h1', class_='css-18igut2').text
    except:
        atributes['Title'] = np.nan

    try:
        atributes['Price'] =  soup.find('div', class_='css-1vr19r7').text
    except:
        atributes['Price'] = np.nan

    try:
        atributes['Price Area'] = soup.find('div', class_='css-18q4l99').text
    except:
        atributes['Price Area'] = np.nan
    try:
        atributes['Local'] = soup.find('a', class_='css-edldse', href=True).text.split('}')[-1]
    except:
        atributes['Local'] = np.nan

    try:
        proprieties = soup.find('div', class_='css-2fnk9o').find_all('li')
        for propriety in proprieties:
            prob = propriety.text.split(':')
            atributes[prob[0]] = prob[1]
    except:
        atributes['Proprieties'] = np.nan

    try:
        atributes['Description'] = soup.find('section', class_='section-description').find('div').text
    except:
        atributes['Description'] = np.nan
    try:
        features = soup.find('section', class_='section-features').find_all('li')
        atributes['Features']  = [feature.text for feature in features]
    except:
        atributes['Features'] = np.nan

    return atributes

def scrap_custojusto(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    atributes = dict()
    try:
        atributes['Title'] = soup.find('h1', class_='words').text
    except:
        atributes['Title'] = np.nan

    try:
        atributes['Date'] = soup.find('div', class_='col-xs-6 pull-left').text
    except:
        atributes['Date'] = np.nan

    try:
        atributes['Price'] = str(soup.find('span', class_="real-price").text).replace('\n', '')
    except:
        atributes['Price'] = np.nan

    try:
        atributes['Price_type'] = soup.find('small', class_="hidden-xs").text
    except:
        atributes['Price_type'] = np.nan
    try:
        atributes['Description'] = soup.find('p', class_='lead words').text
    except:
        atributes['Description'] = np.nan


    atributes_list = soup.find('ul', class_='list-group gbody')
    soup_atributes = BeautifulSoup(str(atributes_list), 'html.parser')
    
    for tag in soup_atributes.find_all("li"):
        value = tag.find('span').text
        key = str(tag.text).replace(value, '')
        if key == 'Cert. Energética':
            key = 'CE1'
        elif key == 'Cert. nergética':
            key = 'CE2'
        elif key == 'ert. Energética':
            key = 'CE3'
        elif key == 'Área útil':
            key = "Area"
        atributes[key] = value

    try:
        atributes['host_name'] = str(soup.find('h3', class_='user words').text).replace('\n', '')
    except:
        atributes['host_name'] = np.nan

    
    try:
        host_since_aux = str(soup.find('span', class_='since').text).replace('\n', ' ').split('     ')
        atributes['host_since'] =  host_since_aux[0].split('Anunciante desde')[1]
        atributes['host_number_ads'] = re.sub("[^0-9]", "", host_since_aux[1])
    except:
        atributes['host_since'] = np.nan
        atributes['host_number_ads'] = np.nan
    
    atributes['URL'] = url

    return atributes
