from app import app
from instance.config import app_config
from app.auth.views import register

if __name__ =='__main__':
    app.config.from_object(app_config['development'])
    app.run()