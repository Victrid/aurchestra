import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_conn = os.getenv('AURCHESTRA_DB_CONNECTION', "sqlite:///test_local.db")

engine = create_engine(db_conn)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)