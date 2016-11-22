__author__ = 'exiaohao@gmail.com'
__data_source__ = 'http://d.10jqka.com.cn/v2/line/hs_{stock_id}/01/last.js'
__request_method__ = 'GET'
__headers__ = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
}

import json
import logging
from ..exceptions import CrawlerException
from ..libs.utils import try_int, try_float


class Parser:
    STRUCTURE = (
        'date',
        'opening_price',
        'max_price',
        'min_price',
        'closing_price',
        'trade_volume',
        'trade_amount',
    )

    def __init__(self, raw_data):
        try:
            self.data = json.loads(raw_data[38:-1])
        except:
            raise CrawlerException(CrawlerException.BAD_THS_DAILY_DATA)

    def result(self):
        """
        返回数据列
        :return:
        """
        try:
            data_collections = self.data.get('data').split(';')
        except CrawlerException:
            raise CrawlerException(CrawlerException.BAD_THS_DAILY_DATA)

        day_data = {}
        for item in data_collections:
            day_split = item.split(',')
            day_data.update({day_split[0]:{field: try_float(day_split[i]) for i, field in enumerate(self.STRUCTURE)}})

        return day_data
