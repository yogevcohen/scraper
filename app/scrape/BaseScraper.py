import requests


#   BaseScraper
#   Role:
#       defines basic functionality of all scrapers
#
#   Responsible:
#       To get the HTML from any source for scraping.
class BaseScraper:
    URL = None

    def __init__(self,url):
        print('BaseScraper')
        self.URL=url
        return

    def get_page(self, handle):
        link = self.URL.format(handle)
        page = requests.get(link, verify=False, timeout=5)
        return page
