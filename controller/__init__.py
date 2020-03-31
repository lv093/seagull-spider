from .common.proxy import proxy
from .news.zhihu import zhihu

DEFAULT_BLUEPRINT = (
    ('/common/proxy', proxy),
    ('/news/zhihu', zhihu)
)


# Functions that encapsulate the configuration blueprint
def init_blueprint(app):
    print("init controller, blueprint")
    # loop read tuple blueprints
    for prefix, blueprint in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
