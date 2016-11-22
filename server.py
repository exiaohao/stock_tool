from crawler.libs.request_ths import THSRequestLib
from crawler.exceptions import RequestException

ths = THSRequestLib(THSRequestLib.REQU_DAILY_LINE)

try:
    ths.data('010976')
except RequestException as ex:
    pass