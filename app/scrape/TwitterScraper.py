from bs4 import BeautifulSoup
from app.scrape.BaseScraper import BaseScraper


#   TwitterHandleScraper
#   Role:
#       Scrape the html for the twitter handle (profile picture).
#
#   Responsible:
#       To get the HTML from twitter and to return the profile image link, posts and etc..
class TwitterScraper(BaseScraper):

    def __init__(self):
        super().__init__('https://twitter.com/{}')
        print('ScrapeHandlerFactory Ctor')
        return

    def scrape_profile_image_link(self, handle_page):
        soup = BeautifulSoup(handle_page)
        profile_image = soup.find('img', class_='ProfileAvatar-image')
        if profile_image and profile_image['src']:
            print('link: {}'.format(profile_image['src']))
            return profile_image["src"]
        return None

    def scrape_posts(self, handle_page):
        raise Exception('Not implemented yet')
