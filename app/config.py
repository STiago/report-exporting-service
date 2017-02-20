class Config(object):
    DEBUG = True

class ProductionConfig(Config):
    DATABASE_NAME = ""
    DATABASE_USER = ""
    DATABASE_HOST = ""
    DATABASE_PASSWORD = ""
    DEBUG = False


class TestConfig(Config):
        DATABASE_NAME = "ljaxkuji"
        DATABASE_USER = "ljaxkuji"
        DATABASE_HOST = "horton.elephantsql.com"
        DATABASE_PASSWORD = "7LSqRwlNZqVAbSFpnnr8GHf4b1Gu83ac"
        DEBUG = True
