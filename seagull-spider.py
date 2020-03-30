from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    from config import init_config
    init_config(app)

    from model import init_db
    init_db(app)

    from controller import init_blueprint
    init_blueprint(app)

    # if False and app.config.get('CRON_STATE') is True:
    #     from cron import init_cron
    #     init_cron(app)

    from utils import init_util
    init_util(app)

    # from utils.kafka import KafkaClient
    # KafkaClient.init_kafka()
    #
    from utils.redis import init_redis
    init_redis(app)

    return app


# def server_defer(signum, frame):
#     from utils.kafka import KafkaClient
#     KafkaClient.stop_kafka()
#     os._exit(0)


if __name__ == '__main__':
    # for sig in [signal.SIGINT, signal.SIGHUP, signal.SIGTERM]:#, signal.SIGKILL]:
    # # signal.signal(signal.SIGINT, server_defer)
    # # signal.signal(signal.SIGTERM, server_defer)
    #     signal.signal(sig, server_defer)

    app = create_app()
    print(app)
    host = app.config.get('APP_HOST')
    port = app.config.get('APP_PORT')
    app.run(host, port)
