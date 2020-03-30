from flask_redis import FlaskRedis

redis_store = FlaskRedis()


def init_redis(app):
    if app.config.get('RD_WEIDANCING_OPEN', False) is False:
        return
        # app.config['REDIS_URL'] = "redis://:@localhost:6379/0"
    max_connections = app.config.get('RD_WEIDANCING_MAX_POOL', 10)

    app.config['REDIS_URL'] = get_rd_uri(
        app.config.get('RD_WEIDANCING_HOST', 'localhost'),
        app.config.get('RD_WEIDANCING_PORT', '6379'),
        app.config.get('RD_WEIDANCING_PWD', ''),
        app.config.get('RD_WEIDANCING_DB', '0'),
    )
    print("init-redis-url:", app.config['REDIS_URL'])

    redis_store.init_app(app, max_connections=max_connections, socket_timeout=2, retry_on_timeout=0.2)


def get_rd_uri(host, port, pwd, db):
    uri = "redis://:{pwd}@{host}:{port}/{db}"
    return uri.format(pwd=pwd, host=host, port=port, db=db)
