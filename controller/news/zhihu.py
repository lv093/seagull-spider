from flask import Blueprint, request
from service.news.zhihu.zhihu_schedule_service import zhihu_sc_svc

zhihu = Blueprint("zhihu", __name__)

@zhihu.route('/grab_topstory_hotlist')
def grab_topstory_hotlist():
    data = zhihu_sc_svc.schedule_topstory_hotlist()
    return data