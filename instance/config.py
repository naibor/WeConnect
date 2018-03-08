import os
 
class Config (object):
    """parent configaration class"""
    DEBUG =False
    CSRF_ENABLE =True #protection from unwanted requests
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '23WEASFDwsa') 
    

class DevelopmentConfig(Config):
    # configuration for the development 
    DEBUG =True

class TestingConfg(Config):
    # configuration for testing ,with a seprate test database
    DEBUG =True

class StagingConfig(Config):
    # configurations for staging
    DEBUG =True

class ProductionConfig(Config):
    # configuration for production
    DEBUG =True
    TESTING = False

# app_config dictionary is used for exporting the environment
app_config ={
    'development':DevelopmentConfig,
    'testing':TestingConfg,
    'staging':StagingConfig,
    'production':ProductionConfig,
}
