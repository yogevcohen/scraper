from app import app
from app import HandlerScraperManager
from app.constant import consts

scrape_manager = HandlerScraperManager.ScraperManager()


@app.route('/')
def index():
    return '<p> "/handles/<handle_name>" - for getting a new link </p>' \
           '<p> "/getAllHandles/<handle_name>" - [post] gett all handles</p>'


@app.route('/handles/<handle_name>')
def get_handle_profile(handle_name):
    try:
        link = scrape_manager.scrape(consts.twitter_request_type, handle_name)
        return link
    except Exception as e:
        return 'Failed to get {} profile link'.format(handle_name)


@app.route('/getAllHandles', methods = ['POST'])
def get_all_profile_links():
    try:
        return '\n'.join(scrape_manager.export_all().values())
    except Exception as e:
        return 'Failed to get all profile link'
