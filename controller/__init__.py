from .common.proxy import proxy

DEFAULT_BLUEPRINT = (
    ('/common/proxy', proxy),
)


# Functions that encapsulate the configuration blueprint
def init_blueprint(app):
    print("init controller, blueprint")
    # loop read tuple blueprints
    for prefix, blueprint in DEFAULT_BLUEPRINT:
        print(prefix)
        print(blueprint)
        app.register_blueprint(blueprint, url_prefix=prefix)
