from flask_sqlalchemy import SQLAlchemy
from apscheduler.jobstores.memory import MemoryJobStore
db = SQLAlchemy()


def init_db(app):
    print("init db")

    weidancing = get_db_uri(
        app.config['DB_WEIDANCING_HOST'],
        app.config['DB_WEIDANCING_PORT'],
        app.config['DB_WEIDANCING_USER'],
        app.config['DB_WEIDANCING_PWD'],
        app.config['DB_WEIDANCING_DB'],
    )
    print("init db, weidancing, " + weidancing)

    app.config['SQLALCHEMY_DATABASE_URI'] = weidancing
    app.config['SQLALCHEMY_BINDS'] = {
        'weidancing': weidancing,
    }

    app.config['SCHEDULER_JOBSTORES'] = {
        'default': MemoryJobStore()
    }

    if 'DB_SD_BASKETBALL_SOURCE_POOL_SIZE' in app.config.keys():
        app.config['SQLALCHEMY_POOL_SIZE'] = app.config['DB_SD_BASKETBALL_SOURCE_POOL_SIZE']
    else:
        app.config['SQLALCHEMY_POOL_SIZE'] = 300
        app.config['SQLALCHEMY_MAX_OVERFLOW'] = 600
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 10
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)


def get_db_uri(host, port, user, pwd, db):
    uri = "mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}?charset=utf8"
    return uri.format(host=host, port=port, user=user, pwd=pwd, db=db)
