from service.news.zhihu.zhihu_grab_service import zhihu_grab_svc

class ZhihuScheduleService:

    @classmethod
    def schedule_topstory_hotlist(self):
        xml = zhihu_grab_svc.grab_topstory_hotlist()
        return xml

zhihu_sc_svc = ZhihuScheduleService()