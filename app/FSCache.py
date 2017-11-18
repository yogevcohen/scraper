import json
import os.path
from app.constant import consts


#   FSCacheManager
#   Role:
#       uses FS to Cache key value
#
#   Responsible:
#       loading, saving and init the cache
class FSCache:
    cache_file_name = None
    def __init__(self, type):
        self.cache_file_name = '{}{}_cache.json'.format(consts.cache_location, type)
        self.file_create()
        return

    def get_value(self, key):
        cache = self.get_all()
        value = cache.get(key)
        return value

    def set_value(self, key, value):
        data = {key:value}
        all = self.get_all()
        all.update(data)


        with open(self.cache_file_name, 'w') as f:
            json.dump(all, f)
        return

    def get_all(self):
        data = {}
        with open(self.cache_file_name, 'r+') as f:
            try:
                data = json.load(f)
                return data
            except Exception as e:
                print(e)
                raise e
        return data;

    def file_create(self):
        if os.path.exists(self.cache_file_name) == False:
            with open(self.cache_file_name, 'w+') as f:
                json.dump({}, f)
                return
