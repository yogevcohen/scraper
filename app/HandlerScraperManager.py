from app.scrape.Factory import ScrapeFactory
from app.FSCache import FSCache
from app.constant import consts

#   HandleScraperManager
#   Role:
#       This class handles scraping of various resources (profile images / comments / posts)
#       from various location (twitter, facebook, etc..).
#
#   Responsible:
#       gets the scrape request and returns the scraped data from the scrape location (twitter, facebook, etc..).
class ScraperManager:
    scrape_factory = None
    handlers_cache = None

    def __init__(self):
        print("ScraperManager ctor")
        self.scrape_factory = ScrapeFactory()
        self.handlers_cache = FSCache('{}_{}'.format(consts.twitter_request_type,consts.product_type_profile_picture))
        return

    def get_all_scraped_values(self):
        return self.handlers_cache()

    def scrape(self, type, handle_name):
        try:
            # 1. check cache
            cached_link  = self.handlers_cache.get_value(handle_name)
            if cached_link:
                return cached_link

            # NO cache 2. gets the scraper
            scraper = self.scrape_factory.get_scraper(type)
            response = scraper.get_page(handle_name)

            #check valid response
            if not response:
                raise Exception('Failed to get valid response')

            page = response.text
            # 3. scrape whatever you want - profile.
            link = scraper.scrape_profile_image_link(page)
            if not link:
                return 'Failed to scrape page - no link was found, check scraper. (page was modified)'

            #TODO: scrape some more info

            # 4. modify cache
            self.handlers_cache.set_value(handle_name, link)
            # 5. return url
            return link
        except Exception as e:
            print(e)
            raise e

    def export_all(self):
        return self.handlers_cache.get_all()
