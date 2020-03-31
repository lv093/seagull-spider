from requests.adapters import HTTPAdapter
import requests
from utils import logger

class ZhihuGrabService:

    domain = 'https://www.zhihu.com/'
    domain_key = "d1b4327d3ddfec0245f122c0331c2f5a"

    def grab_topstory_hotlist(self):
        url = self.domain + "hot"
        s = requests.Session()
        s.mount('https://', HTTPAdapter(max_retries=1))

        try:
            r = s.get(url, timeout=(20, 20))
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
        return

zhihu_grab_svc = ZhihuGrabService()

