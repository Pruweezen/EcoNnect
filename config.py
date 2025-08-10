import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or (
        f"mysql+pymysql://{os.getenv('DB_USER','econnect_user')}:"
        f"{os.getenv('DB_PASSWORD','12345678')}@{os.getenv('DB_HOST','localhost')}:"
        f"{os.getenv('DB_PORT','3306')}/{os.getenv('DB_NAME','econnnect_db')}"
    )
