from requests.adapters import HTTPAdapter
import requests
from utils import logger

class ZhihuGrabService:

    domain = 'https://www.zhihu.com/'
    domain_key = "d1b4327d3ddfec0245f122c0331c2f5a"

    def grab_topstory_hotlist(self):
        url = self.domain + "hot"
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=1))
        cookie = '_zap=0c26bae5-a78a-41d5-b348-e199cfe90457; _xsrf=d30b9157-9253-4626-994f-896dcb256c19; d_c0="ACCbOBLz4xCPTvL3w5QR8PNpLL9FOf95Tog=|1582955338"; _ga=GA1.2.1217546277.1582955344; capsion_ticket="2|1:0|10:1583137586|14:capsion_ticket|44:MDI1OTUzODdmNjM2NGQ3ZGJkODM3ZjFhYjkzZmUyYjU=|6ad2020bb78ab3a9e75effabb7c56277769eb9cb703e32c3bd5613e396ab983a"; z_c0="2|1:0|10:1583137609|4:z_c0|92:Mi4xekc2NkFBQUFBQUFBSUpzNEV2UGpFQ1lBQUFCZ0FsVk5TUkZLWHdCX2s5U0UxbFN1ZEVJanhQeUIwSF9KSDl0eGdR|757dbcd716998ab5010003c1503e32f62247eebe52aefbd15358223fbbc10115"; q_c1=1037c3a197fe4a60be2c36c8c5edd55b|1583492067000|1583492067000; tshl=; _gid=GA1.2.999655570.1585540646; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1585540645,1585541915,1585561916,1585581326; tst=h; _gat_gtag_UA_149949619_1=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1585623109; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1585623133|1585619257'
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
            "Cookie": cookie
        }

        try:
            r = session.get(url, timeout=(20, 20), headers=headers)
            print(r)
            if r.status_code == 200 or r.status_code == "200":
                logger.info("request and red time is [%s]" % r.elapsed)
                return r.text
            else:
                logger.error("grep_live_index is not 200 [%s]" % url)
                return None

        except requests.exceptions.RequestException as err:
            logger.error("grep_live_index_status_code err:[%s]" % err)
            return None

zhihu_grab_svc = ZhihuGrabService()

