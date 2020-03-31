from bs4 import BeautifulSoup as bs
from utils import logger
import traceback

class ZhihuParseService:

    def parse_topstory_hotlist(self, content):
        data = []
        if content is None:
            return data
        try:
            soup = bs(content, 'lxml')
            table_list = soup.find_all('section')
            return table_list
        except Exception as err:
            logger.error('==== parse_betfair_xml err %s [%s]====', err, traceback.format_exc())
        return

zhihu_parse_svc = ZhihuParseService()
