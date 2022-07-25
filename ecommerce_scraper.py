import requests
from bs4 import BeautifulSoup


def get_product_links(url):
    base_url = 'https://www.thewhiskyexchange.com'
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    links  = sp.select('a.core')
    return [base_url + link.attrs['href'] for link in links]

def product_data(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    product = {
        'title':sp.select_one('h1.product-main__name').text.strip().replace('\n', ' '),
        'price':float(sp.select_one('p.product-action__price').text.replace('£', '')),
        'stock':sp.select_one('p.product-action__stock-flag').text.strip().replace('\n', ' '),
        'desc':sp.select_one('div.product-main__description p').text.strip().replace('\n', ' '),
    }
    return product 

def main():
    for x in range(1,17):
        url = 'https://www.thewhiskyexchange.com/c/304/blended-scotch-whisky?pg={}'.format(x)
        links = get_product_links(url)
        for link in links:
            product = product_data(link)
            return product

main()