from pymongo import MongoClient
from crawler.libs.request_ths import THSRequestLib
from crawler.exceptions import RequestException

ths = THSRequestLib(THSRequestLib.REQU_DAILY_LINE)

client = MongoClient('127.0.0.1', 17017)
db = client['stock']
daily = db['daily']

for stock_id in range(600000, 6039999):
    try:
        result = ths.data(str(stock_id))
        daily.insert({'data':result, 'stock_id': stock_id})
    except RequestException as ex:
        print(ex)
