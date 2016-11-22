__author__ = 'exiaohao@gmail.com'

import requests
import importlib

from ..exceptions import RequestException


class THSRequestLib:
    REQU_DAILY_LINE = 'ths_daily_line'
    REQU_LIVE_PRICE = 'ths_live_price'

    def __init__(self, request_type):
        module_path = "crawler.parser.{}".format(request_type)
        self.module = importlib.import_module(module_path)

    def _do_request(self, stock_id):
        if self.module.__request_method__ == 'GET':
            result = requests.get(self.module.__data_source__.format(stock_id=stock_id),
                                  headers=self.module.__headers__)
        elif self.module.__request_method__ == 'POST':
            result = requests.post()
        else:
            raise RequestException(RequestException.ILLEGAL_REQUEST)

        if result.status_code == 200:
            return result.text
        else:
            raise RequestException(RequestException.BAD_STATUS_CODE)

    def data(self, stock_id):
        result = self._do_request(stock_id)
        module = getattr(self.module, 'Parser')(result)
        return module.result()
