from .app import Config

app_config = {}

# config:app.py/Config class and config.py
def init_config(app):
    print("init config")
    app.config.from_object(Config)
    app.config.from_pyfile("config.py")
    app.config.from_pyfile("env.py", silent=True)
    global app_config
    app_config = app.config
