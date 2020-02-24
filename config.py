import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "TmsDxTm53ViWecv9k6sCNuwS"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("SQLALCHEMY_DATABASE_URI")
        or "postgresql://casting:pass@localhost:5432/casting"
    )
    TESTING = os.environ.get("TESTING") or False
    DEBUG = os.environ.get("DEBUG") or False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://casting:pass@localhost:5432/casting"
    )


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://casting:pass@localhost:5432/casting_test"
    )


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("SQLALCHEMY_DATABASE_URI")
        or "postgresql://casting:pass@localhost:5432/casting"
    )


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
