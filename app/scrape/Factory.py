from app.scrape.TwitterScraper import TwitterScraper
from app.constant import consts


#   ScrapeHandlerFactory
#   Role:
#       Factory
#
#   Responsible:
#       get a scrape request type and create the correct scarper.
#
class ScrapeFactory:
    def __init__(self):
        print("ScrapeHandlerFactory Ctor")
        return

    def get_scraper(self, scrape_type):
        if scrape_type == consts.twitter_request_type:
            return TwitterScraper()
        return
