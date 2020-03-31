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
            for table in table_list:
                content_arr = table.find_all('a')
                title = content_arr[0].find_all('h2')[0].text.encode('utf-8')
                subtitle = content_arr[0].find_all('p')[0].text.encode('utf-8')
                url = content_arr[0]['href']
                story = {
                    'title': title,
                    'subtitle': subtitle,
                    'url': url
                }
                data.append(story)

            return data
        except Exception as err:
            logger.error('==== parse_betfair_xml err %s [%s]====', err, traceback.format_exc())
        return data

zhihu_parse_svc = ZhihuParseService()
