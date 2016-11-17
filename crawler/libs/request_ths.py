__author__ = 'exiaohao@gmail.com'

import requests
import importlib


class THSRequestLib:
    REQU_DAILY_LINE = 'ths_daily_line'
    REQU_LIVE_PRICE = 'ths_live_price'
    def __init__(self, request_type, stock_id):
        self.stock_id = stock_id

        module_path = "crawler.lib.parser.{}".format(request_type)
        self.module = importlib.import_module(module_path)

    def _do_request(self):
        if self.module.__request_type__ == 'GET':
            result = requests.get(self.module.__data_source__.format(stock_id=self.stock_id), headers=self.module.__headers__)
        elif self.module.__request_type__ == 'POST':
            result = request.post()
        else:
            raise Exception

        if result.status == 200:
            pass
        else:
            raise Exception

    def data(self):
        return getattr(self.module, 'Parser')(self.stock_id)
        
