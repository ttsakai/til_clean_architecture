from app.flask_app import create_app
from app.flask_config import DevConfig

app = create_app(DevConfig)
