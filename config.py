# base setting
ENV = 'Dev'
APP_HOST = '0.0.0.0'
APP_PORT = 5000

RD_WEIDANCING_OPEN = True
RD_WEIDANCING_HOST = '127.0.0.1'
RD_WEIDANCING_PORT = 6379
RD_WEIDANCING_MAX_POOL = 100
RD_WEIDANCING_PWD = ''
RD_WEIDANCING_DB = '3'

# database
DB_WEIDANCING_HOST = '127.0.0.1'
DB_WEIDANCING_PORT = '3306'
DB_WEIDANCING_USER = 'root'
DB_WEIDANCING_PWD = 'root@123456'
DB_WEIDANCING_DB = 'weidancing'

PROXY_HOST_PORT = 'http://106.75.79.132:31280'

SCHEDULER_API_ENABLED = True

# kafka
KAFKA_HOST = 'localhost:9092'


# logs
LOG_PATH = './logs'
LOG_FILENAME = 'seagull-news'
LOG_LEVEL = 10

SQLALCHEMY_ECHO = False