import os

class Config:
    '''
    General configuration parent class
    '''
    # MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'

    # MOVIE_API_KEY=os.environ.get('MOVIE_API_KEY') 

    # SECRET_KEY=os.environ.get('SECRET_KEY') 

    #simple mde configuration
    # SIMPLEMDE_JS_IIFE = True
    # SIMPLEMDE_USE_CDN = True



    # UPLOADED_PHOTOS_DEST ='app/static/photos'

    # #mail cconfiguration
    # MAIL_SERVER= 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS=True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD= os.environ.get("MAIL_PASSWORD")

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Mbuguack@localhost/watchlist_test'

    pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Mbuguack@localhost/watchlist'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass


    


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
} 