from service.news.zhihu.zhihu_grab_service import zhihu_grab_svc
from service.news.zhihu.zhihu_parse_service import zhihu_parse_svc

class ZhihuScheduleService:

    @classmethod
    def schedule_topstory_hotlist(self):
        xml = zhihu_grab_svc.grab_topstory_hotlist()
        data = zhihu_parse_svc.parse_topstory_hotlist(xml)
        return data

zhihu_sc_svc = ZhihuScheduleService()