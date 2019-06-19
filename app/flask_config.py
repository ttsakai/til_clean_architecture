class Config:
    """Base Configuration"""

class ProdConfig(Config):
    """Production Configuration"""
    ENV = "production"
    DEBUG = False

class DevConfig(Config):
    """Development Configuration"""
    ENV = "development"
    DEBUG = 1

class TestConfig(Config):
    """Test Configuration"""
    ENV = "test"
    TESTING = True
    DEBUG = True

