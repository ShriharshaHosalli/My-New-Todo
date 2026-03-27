import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DATABASE = os.getenv("DATABASE", "database.db")
    DEBUG = False