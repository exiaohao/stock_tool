import collections

Identity = collections.namedtuple('Identity', ['module', 'code', 'error_msg'])


class BaseException(Exception):
    def __init__(self, identity):
        super().__init__(identity)
        self.identity = Identity(*identity)


class CrawlerException(BaseException):
    BAD_THS_DAILY_DATA = 'ths', 1001, '错误的同花顺日线信息'


class RequestException(BaseException):
    BAD_STATUS_CODE = 'request', 400, '非正常返回'
    ILLEGAL_REQUEST = 'illgeal request', 403, '非法的请求'
