class Config(object):
    DEBUG = True

class ProductionConfig(Config):
    DATABASE_NAME = "blzfcfay"
    DATABASE_USER = "blzfcfay"
    DATABASE_HOST = "horton.elephantsql.com"
    DATABASE_PASSWORD = "XWq1VkHmZBzOS1yP5RiLLAANYEEUsK20 "
    DEBUG = False


class TestConfig(Config):
        DATABASE_NAME = "ljaxkuji"
        DATABASE_USER = "ljaxkuji"
        DATABASE_HOST = "horton.elephantsql.com"
        DATABASE_PASSWORD = "7LSqRwlNZqVAbSFpnnr8GHf4b1Gu83ac"
        DEBUG = True
