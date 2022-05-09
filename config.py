import os


DATABASE_URL = os.environ['DATABASE_URL']

class Config:


   '''
   General configuration parent class
   '''
   DATABASE_URL = os.environ['DATABASE_URL']
   SECRET_KEY=os.environ.get('SECRET_KEY')
#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Mbuguack@localhost/pitches'
   UPLOADED_PHOTOS_DEST ='app/static/photos'
   #simple mde configuration
   # SIMPLEMDE_JS_IIFE = True
   # SIMPLEMDE_USE_CDN = True

   #mail cconfiguration


   MAIL_SERVER= 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS=True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD= os.environ.get("MAIL_PASSWORD")


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
   DATABASE_URL = os.environ['DATABASE_URL']

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
